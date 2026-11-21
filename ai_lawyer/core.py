"""The main pipeline: story -> case file -> rules -> calculation -> grounded assessment -> validator."""
from __future__ import annotations

import json
import os
import re
from datetime import date
from pathlib import Path

from . import calculator, escalation, guardrails, kb, rag
from .llm import LLM
from .redact import redact

PROMPTS = Path(__file__).resolve().parent.parent / "prompts"

SCRIPTS = {"devanagari": r"[ऀ-ॿ]", "tamil": r"[஀-௿]", "bengali": r"[ঀ-৿]",
           "telugu": r"[ఀ-౿]", "kannada": r"[ಀ-೿]", "gujarati": r"[઀-૿]",
           "gurmukhi": r"[਀-੿]", "malayalam": r"[ഀ-ൿ]"}

CITATION_REQUEST = re.compile(r"\b(judgments?|case ?laws?|citations?|precedents?|supreme court|high court|"
                              r"IPC|section numbers?|which section|kaunsi dhara|dhara)\b|धारा|फैसला", re.I)
HONESTY_NOTE = ("**About the judgment / section you asked for:** I don't give court-case citations or legal "
                "sections that I can't verify - AI tools often invent them, and a wrong citation can hurt your case. "
                "I only quote the provisions in my checked list below. A lawyer (free via NALSA 15100) can find "
                "the right judgments if you go to court. (Also: the IPC was replaced by the Bharatiya Nyaya Sanhita "
                "from 1 July 2024, and a deposit dispute is usually a civil matter, not a criminal one.)")


def script_of(text: str) -> str:
    counts = {k: len(re.findall(p, text)) for k, p in SCRIPTS.items()}
    best = max(counts, key=counts.get)
    return best if counts[best] > 20 else "latin"


def prompt(name: str, **vars) -> str:
    text = (PROMPTS / f"{name}.md").read_text(encoding="utf-8")
    for k, v in vars.items():
        text = text.replace("{{" + k + "}}", v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, indent=1))
    return text


def intake(story_masked: str, llm: LLM, today: date) -> dict:
    case = llm.chat_json([
        {"role": "system", "content": prompt("intake", today=today.isoformat(),
                                             script="Latin/Roman letters" if script_of(story_masked) == "latin"
                                             else script_of(story_masked).title())},
        {"role": "user", "content": story_masked},
    ], tag="intake")
    case.setdefault("problem_type", "other")
    case.setdefault("amounts", {})
    case.setdefault("timeline", [])
    case.setdefault("user_language", "English")
    return case


def assess(case: dict, flags: list[dict], calc: dict, entries: list[dict], llm: LLM) -> dict:
    lang = case.get("user_language") or "English"
    trap_text = "\n".join(f"- {t['title']}: {t['plain'].strip()}" for t in kb.traps(case.get("problem_type", "other")))
    sys = prompt("assess", language=lang, traps=trap_text, case=case, kb=kb.format_for_prompt(entries),
                 flags=flags or "none", calc=calc)
    return llm.chat_json([{"role": "system", "content": sys},
                          {"role": "user", "content": "Assess this case and reply in the JSON format."}],
                         tag="assess", max_tokens=2200)


def rag_query(case: dict) -> str:
    """English query built from the case file (the intake step already translated the story)."""
    return " ".join(str(x) for x in (case.get("problem_subtype"), case.get("summary"), case.get("user_goal")) if x)


# Every case of a type needs these answered (forum, time limit, core right), whatever words the story uses.
ANCHOR_QUERIES = {
    "consumer": ["complaint filed District Commission jurisdiction where to file",
                 "complaint within two years cause of action limitation",
                 "deficiency in service unfair trade practice definition"],
    "salary": ["time limit for payment of wages resignation removal",
               "claims of unpaid wages authority application"],
    "deposit": ["security deposit refund on vacating premises",
                "Rent Authority application landlord tenant dispute"],
    "notice": ["notice to vacate eviction recovery of possession tenant",
               "legal aid free legal services"],
    "other": ["legal aid free legal services equal justice"],
}


def retrieve_law(case: dict, k: int = 6) -> tuple[list[dict], str]:
    """Multi-query retrieval: the case's own query first, then problem-type anchor queries (round-robin)."""
    if os.getenv("RAG", "1") != "1":
        return [], "off"
    try:
        r = rag.get_retriever()
    except Exception as e:  # index missing/corrupt: degrade to curated KB only
        return [], f"unavailable ({type(e).__name__})"
    if r is None:
        return [], "no index (run scripts/build_index.py)"
    pt = case.get("problem_type")
    lists = [r.search(rag_query(case), pt, k=k)] + [r.search(q, pt, k=2) for q in ANCHOR_QUERIES.get(pt, [])]
    out, seen = [], set()
    for rank in range(k):
        for lst in lists:
            if rank < len(lst) and lst[rank]["id"] not in seen and len(out) < k + 2:
                seen.add(lst[rank]["id"])
                out.append(lst[rank])
    return out, r.mode + " + anchor queries"


def support_check(assessment: dict, entries: list[dict], case: dict):
    """Returns (assessment, report) when the check ran, else a short status string."""
    if not any(e.get("status") == "primary" for e in entries):
        return "no official text cited"
    if (case.get("user_language") or "").strip().lower() != "english":
        return "not auto-checked (non-English reply; cross-encoder is English-only)"
    try:
        ce = rag._reranker()
    except Exception as e:
        return f"unavailable ({type(e).__name__})"
    return guardrails.check_support(assessment, entries, lambda claim, text: ce.predict([(claim, text[:1500])])[0])


def refusal(flags: list[dict], lang: str) -> dict:
    msg = next(f["message"] for f in flags if f["severity"] == "refuse")
    return {"where_you_stand": msg, "options": [], "proof_tips": [], "what_i_dont_know": [],
            "needs_lawyer": True, "needs_lawyer_reason": msg,
            "reply": msg + " " + escalation.LEGAL_AID}


def analyze(story: str, llm: LLM, state_hint: str | None = None, today: date | None = None,
            pii_mapping: dict | None = None) -> dict:
    """Run the full pipeline on the conversation so far (all user messages joined)."""
    today = today or date.today()
    masked, mapping = redact(story, pii_mapping)
    case = intake(masked, llm, today)
    if state_hint and not case.get("state"):
        case["state"] = state_hint

    # The reply must match how the person WRITES, not just the language (Hinglish != Hindi in Devanagari)
    script = script_of(story)
    lang = case.get("user_language") or "English"
    if script == "latin" and lang.lower() != "english":
        if "roman" not in lang.lower() and "hinglish" not in lang.lower():
            case["user_language"] = f"{lang} written in Roman (English) letters, the way the person wrote"
    elif script != "latin":
        case["user_language"] = f"{lang} written in {script.title()} script (not Roman letters), the way the person wrote"
    flags = escalation.check(story, case, today)          # rules see raw text locally
    calc = calculator.compute(case)
    entries = kb.retrieve(case.get("problem_type", "other"))
    hits, rag_mode = retrieve_law(case)
    entries = entries + rag.as_kb_entries(hits)       # retrieved official text = additional citable sources

    raw_assessment = None
    if escalation.top_severity(flags) == "refuse":
        assessment, guard = refusal(flags, case.get("user_language", "English")), {"removed_count": 0, "items": [], "kb_cited": []}
    else:
        raw_assessment = assess(case, flags, calc, entries, llm)
        assessment, guard = guardrails.validate_obj(raw_assessment, entries)
        assessment = guardrails.auto_tag_obj(assessment, entries)   # untagged-but-valid law names get receipts
        guard["support_check"] = support_check(assessment, entries, case)
        if isinstance(guard["support_check"], tuple):
            assessment, guard["support_check"] = guard["support_check"]
        guard["kb_cited"] = sorted(guard["kb_cited"])
        if escalation.top_severity(flags) == "lawyer":
            assessment["needs_lawyer"] = True       # rules override the model
        if CITATION_REQUEST.search(story):         # honesty note is guaranteed by code, not left to the model
            assessment["reply"] = HONESTY_NOTE + "\n\n" + assessment.get("reply", "")

    return {
        "model": llm.spec,
        "masked_story": masked,
        "pii_mapping_keys": sorted(mapping),
        "case": case,
        "flags": flags,
        "calculation": calc,
        "kb_ids_given": [e["id"] for e in entries],
        "retrieval": {"mode": rag_mode, "query": rag_query(case),
                      "hits": [{k: h[k] for k in ("id", "act", "unit", "number", "title", "page", "url")}
                               | {"excerpt": h["text"][:700]} for h in hits]},
        "_rag_entries": [e for e in entries if e["id"].startswith("src_")],
        "assessment": assessment,
        "assessment_raw": raw_assessment,
        "guardrail_report": guard,
        "_pii_mapping": mapping,   # stays local; never sent to the LLM
    }
