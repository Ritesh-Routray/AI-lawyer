"""'Got a notice?' - read a notice someone RECEIVED (photo, PDF, text), explain it, and check the laws it cites.

The law check is pure code against the official-text library: a notice that cites a section which does
not exist, or cites the IPC/CrPC for recent events, is a real red flag the person should know about.
"""
from __future__ import annotations

import json
import re
from datetime import date

from . import escalation, guardrails, kb
from .core import prompt
from .evidence import vision_llm
from .llm import LLM
from .rag import INDEX
from .redact import redact

ACT_KEYS = {   # how acts are written in notices -> source_id in the library
    "bns_2023": r"bharatiya nyaya sanhita|\bBNS\b",
    "bnss_2023": r"bharatiya nagarik suraksha sanhita|\bBNSS\b",
    "constitution": r"constitution",
    "cow_2019": r"code on wages",
    "cpa_2019": r"consumer protection act",
    "mta_2021": r"model tenancy act",
}
_CHUNKS: list[dict] | None = None


def _chunks() -> list[dict]:
    global _CHUNKS
    if _CHUNKS is None:
        p = INDEX / "chunks.json"
        _CHUNKS = json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
    return _CHUNKS


def pdf_text(data: bytes) -> str:
    import fitz  # PyMuPDF
    with fitz.open(stream=data, filetype="pdf") as doc:
        return "\n".join(page.get_text() for page in doc)[:15000]


def check_law(ref: str) -> dict:
    """One law reference as written in the notice -> what our library says about it."""
    if guardrails.OLD_CODES.search(ref):
        return {"ref": ref, "verdict": "old",
                "note": "The IPC and CrPC were replaced by the BNS and BNSS from 1 July 2024. A notice about "
                        "events after that date should not rely on them. Ask a lawyer about this."}
    src = next((s for s, pat in ACT_KEYS.items() if re.search(pat, ref, re.I)), None)
    m = guardrails.SECTION.search(ref)
    if not src:
        return {"ref": ref, "verdict": "unknown", "note": "This law isn't in my library, so I can't check it."}
    if not m:
        return {"ref": ref, "verdict": "unknown", "note": "No section number given, so there is nothing specific to check."}
    num = re.sub(r"\(.*", "", m.group(1)).strip().upper()
    hit = next((c for c in _chunks() if c["source_id"] == src and str(c["number"]).upper() == num), None)
    if not hit:
        return {"ref": ref, "verdict": "missing",
                "note": f"I couldn't find section {num} in the official text of this law. It may be a mistake; "
                        "ask a lawyer before you reply."}
    return {"ref": ref, "verdict": "found", "act": hit["act"], "unit": hit["unit"], "number": hit["number"],
            "title": hit.get("title"), "page": hit["page"], "url": f"{hit['url']}#page={hit['page']}",
            "excerpt": hit["text"][:600], "note": "Found in the official text. Read what it actually says."}


def read_notice(llm: LLM, pii_mapping: dict, language: str, *, filename: str | None = None,
                data: bytes | None = None, text: str | None = None, context: str = "",
                today: date | None = None) -> dict:
    today = today or date.today()
    sys = prompt("notice", today=today.isoformat(), language=language, context=context or "(nothing yet)")
    name = (filename or "").lower()
    if data is not None and name.endswith(".pdf"):
        text = pdf_text(data)
    elif data is not None and name.endswith((".txt", ".md")):
        text = data.decode("utf-8", errors="ignore")[:15000]

    if text is not None:
        masked, mapping = redact(text, pii_mapping)
        out = llm.chat_json([{"role": "system", "content": sys},
                             {"role": "user", "content": f"The notice:\n\"\"\"\n{masked}\n\"\"\""}],
                            tag="notice_text", max_tokens=2000)
        raw_text = text
    else:
        mime = "image/png" if name.endswith(".png") else "image/webp" if name.endswith(".webp") else "image/jpeg"
        out = vision_llm(llm).chat_json(
            [{"role": "system", "content": sys},
             {"role": "user", "content": [{"type": "text", "text": "Photo of the notice:"}, LLM.image_part(data, mime)]}],
            tag="notice_image", max_tokens=2000)
        mapping, raw_text = pii_mapping, json.dumps(out, ensure_ascii=False)

    # The model must not add law of its own: strip any section/Act it wrote outside laws_named_in_notice
    named = [str(x) for x in out.get("laws_named_in_notice") or []]
    laws = [check_law(r) for r in named]
    allowed = kb.retrieve("notice") + [{"id": f"notice_{i}", "act": l["act"], "sections": [str(l["number"])]}
                                       for i, l in enumerate(laws) if l["verdict"] == "found"]
    clean, report = guardrails.validate_obj({k: v for k, v in out.items() if k != "laws_named_in_notice"}, allowed)
    clean["laws_named_in_notice"] = named

    # Rules decide escalation and the countdown, not the model
    pseudo_case = {"problem_type": "notice", "deadline_mentioned": {"date": out.get("reply_deadline"), "what": "reply"},
                   "risk_signals": ["court summons"] if out.get("is_court_document") else []}
    trigger = raw_text + (" my client advocate" if out.get("sender_is_lawyer") else "")
    flags = [f for f in escalation.check(trigger, pseudo_case, today) if f["code"] != "OUT_OF_SCOPE"]
    days_left = None
    if (d := escalation._parse_date(out.get("reply_deadline"))):
        days_left = (d - today).days
    return {"reading": clean, "laws": laws, "flags": flags, "days_left": days_left,
            "guardrail_report": report, "_pii_mapping": mapping}


def as_story(n: dict) -> str:
    """Turn a read notice into a message for the main pipeline ('use this as my case')."""
    r = n["reading"]
    bits = [f"I received a notice from {r.get('sender') or 'someone'}"]
    if r.get("notice_date"):
        bits.append(f"dated {r['notice_date']}")
    s = " ".join(bits) + f". It says: {r.get('what_they_claim') or ''}"
    if r.get("amount_demanded"):
        s += f" They demand Rs {r['amount_demanded']:,.0f}."
    if r.get("reply_deadline") or r.get("deadline_text"):
        s += f" Deadline: {r.get('reply_deadline') or r.get('deadline_text')}."
    return s + " What should I do?"
