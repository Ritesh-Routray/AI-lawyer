"""Post-generation citation validator: the anti-hallucination layer that does not trust the model.

1. [KB:id] tags that aren't among the entries we gave the model -> removed.
2. Any section/article reference, Act name, IPC/CrPC mention or case-law citation in the
   text must be backed by one of the KB entries given to the model. If not -> replaced
   with a visible "[unverified legal reference removed]" marker and logged.
3. Case law is never allowed (policy): precedent is where models invent the most.
"""
from __future__ import annotations

import re

REMOVED = "[unverified legal reference removed]"

KB_TAG = re.compile(r"\[KB:([a-z0-9_]+)\]")
SECTION = re.compile(
    r"\b(?:Section|Sections|Sec\.?|S\.|Article|Art\.|Rule|Order|Regulation|धारा|अनुच्छेद|नियम)\s*"
    r"(\d+[A-Z]?(?:\s*\(\s*\w+\s*\))*)", re.I)
ACT = re.compile(
    r"\b((?:The\s+)?(?:[A-Z][\w()'.-]*\s+){1,9}(?:Act|Rules|Code|Sanhita|Adhiniyam|Scheme|Regulations)"
    r"(?:,?\s*(?:of\s+)?\d{4})?)")
OLD_CODES = re.compile(r"\b(?:I\.?P\.?C\.?|Cr\.?P\.?C\.?|Indian Penal Code|Code of Criminal Procedure)\b")
CASE_LAW = re.compile(
    r"(?:\b[A-Z][\w.&]*(?:\s+[A-Z][\w.&]*){0,5}\s+(?:v\.|vs\.?|versus)\s+[A-Z][\w.&]*(?:\s+[A-Z][\w.&]*){0,5})"
    r"|\(\d{4}\)\s*\d+\s*SCC\s*\d+|\bAIR\s*\d{4}\s*[A-Z]+\s*\d+|\b\d{4}\s*SCC\s*OnLine\b[^.;]*")
GENERIC_WORDS = {"the act", "this act", "an act", "the code", "the rules", "these rules"}
# "Code"/"Rules"/"Scheme" words that are not laws
NOT_LAW = re.compile(r"\b(IFSC|PIN|Pin|Postal|Zip|ZIP|Promo|Coupon|QR|Access|Dress|Source|Discount|Reference|"
                     r"Ground|House|Society|Company|Office|HR|Leave|Refund|Return|Cancellation|Privacy)\s+"
                     r"(Code|Rules|Policy|Scheme)\b")


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _norm_sec(s: str) -> str:
    return re.sub(r"\s+", "", s).lower()


def validate(text: str, allowed: list[dict]) -> tuple[str, dict]:
    allowed_ids = {e["id"] for e in allowed}
    act_keys = set()
    sections = set()
    for e in allowed:
        for name in map(str, [e["act"], *e.get("act_aliases", [])]):
            act_keys.add(_norm(re.sub(r",?\s*\d{4}$", "", name)))
            act_keys.add(_norm(name))
        for s in e.get("sections", []):
            sections.add(_norm_sec(s))
            sections.add(_norm_sec(re.sub(r"\(.*", "", s)))
    report = {"bad_kb_tags": [], "unverified_sections": [], "unverified_acts": [],
              "old_criminal_codes": [], "case_law": [], "kb_cited": []}
    # "[KB:a, KB:b]" -> "[KB:a] [KB:b]" (models sometimes merge tags)
    text = re.sub(r"\[((?:KB:[a-z0-9_]+\s*,\s*)+KB:[a-z0-9_]+)\]",
                  lambda m: " ".join(f"[{p.strip()}]" for p in m.group(1).split(",")), text)

    # 1. KB tags
    def kb_sub(m):
        if m.group(1) in allowed_ids:
            report["kb_cited"].append(m.group(1))
            return m.group(0)
        report["bad_kb_tags"].append(m.group(1))
        return ""
    text = KB_TAG.sub(kb_sub, text)

    # 2. case law: always removed
    def case_sub(m):
        report["case_law"].append(m.group(0).strip())
        return REMOVED
    text = CASE_LAW.sub(case_sub, text)

    # 3. repealed / criminal codes
    def old_sub(m):
        report["old_criminal_codes"].append(m.group(0))
        return REMOVED
    text = OLD_CODES.sub(old_sub, text)

    # 4. section numbers must exist in a supplied entry - and, if an Act is named right after the
    #    number ("Section 17 of the Code on Wages"), in an entry for THAT Act
    act_sections = []   # (act name keys, section set) per entry
    for e in allowed:
        keys = {_norm(re.sub(r",?\s*\d{4}$", "", str(n))) for n in [e["act"], *e.get("act_aliases", [])]}
        secs = {_norm_sec(s) for s in e.get("sections", [])} | {_norm_sec(re.sub(r"\(.*", "", s)) for s in e.get("sections", [])}
        act_sections.append(({k for k in keys if len(k) > 2}, secs))

    def sec_sub(m):
        nums = {_norm_sec(m.group(1)), _norm_sec(re.sub(r"\(.*", "", m.group(1)))}
        if not nums & sections:
            report["unverified_sections"].append(m.group(0))
            return REMOVED
        after = _norm(m.string[m.end(): m.end() + 70])
        named = [secs for keys, secs in act_sections if any(after.startswith(("of" + k, "ofthe" + k, k)) for k in keys)]
        if named and not any(nums & secs for secs in named):   # right number, wrong Act
            report["unverified_sections"].append(m.group(0) + " (wrong Act)")
            return REMOVED
        tail = m.string[m.end(): m.end() + 80]
        if not named and re.match(r"\s*(?:\(\w+\)\s*)*of\s+(?:the\s+)?(?=[A-Z])[^.;\n]{0,70}?"
                                  r"\b(Act|Code|Sanhita|Adhiniyam|Rules|Constitution)\b", tail):
            report["unverified_sections"].append(m.group(0) + " (Act not in sources)")
            return REMOVED
        return m.group(0)
    text = SECTION.sub(sec_sub, text)

    # 5. Act / Rules / Code names must match a supplied KB entry
    def act_sub(m):
        name = m.group(1).strip()
        if name.lower() in GENERIC_WORDS or NOT_LAW.search(name):
            return m.group(0)
        key = _norm(re.sub(r",?\s*(?:of\s+)?\d{4}$", "", name))
        key_full = _norm(name)
        if any(k and (k in key_full or key in k) for k in act_keys if len(k) > 4) or key in act_keys:
            return m.group(0)
        # names like "Code on Wages": the regex stops at "Code", so also look at the words that follow it
        ahead = _norm(m.string[m.start(1): m.end(1) + 30])
        if any(k in ahead for k in act_keys if len(k) > 8):
            return m.group(0)
        report["unverified_acts"].append(name)
        return REMOVED
    text = ACT.sub(act_sub, text)

    report["removed_count"] = (len(report["bad_kb_tags"]) + len(report["unverified_sections"]) +
                               len(report["unverified_acts"]) + len(report["old_criminal_codes"]) +
                               len(report["case_law"]))
    report["kb_cited"] = sorted(set(report["kb_cited"]))
    return text, report


def validate_obj(obj, allowed: list[dict], report: dict | None = None):
    """Recursively validate every string inside a JSON-like object."""
    report = report if report is not None else {"removed_count": 0, "items": [], "kb_cited": set()}
    if isinstance(obj, str):
        clean, r = validate(obj, allowed)
        if r["removed_count"]:
            report["removed_count"] += r["removed_count"]
            report["items"].append({k: v for k, v in r.items() if v and k not in ("removed_count", "kb_cited")})
        report["kb_cited"].update(r["kb_cited"])
        return clean, report
    if isinstance(obj, list):
        out = []
        for x in obj:
            c, report = validate_obj(x, allowed, report)
            out.append(c)
        return out, report
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            c, report = validate_obj(v, allowed, report)
            out[k] = c
        return out, report
    return obj, report


SUPPORT_THRESHOLD = -5.0   # cross-encoder score; calibrated: supported claims scored +0.4..+6.9, misattached ones ~-11


def check_support(obj, entries: list[dict], scorer, report: dict | None = None):
    """For citations of OFFICIAL TEXT: does the sentence carrying the tag match what that section says?
    A tag on a sentence the section doesn't support is removed (the sentence stays) and logged.
    English only - the cross-encoder is English, and correct Hinglish claims score low (measured)."""
    report = report if report is not None else {"checked": 0, "unsupported": []}
    # heading + text: continuation chunks (part 2 of a long section) lack the opening words without it
    texts = {e["id"]: f"{e.get('title', '')}. {e['plain']}" for e in entries if e.get("status") == "primary"}
    if isinstance(obj, str):
        out = []
        for sent in re.split(r"(?<=[.!?])\s+", obj):
            for tid in set(KB_TAG.findall(sent)) & set(texts):
                claim = KB_TAG.sub("", sent).strip()
                score = float(scorer(claim, texts[tid]))
                report["checked"] += 1
                if score < SUPPORT_THRESHOLD:
                    sent = sent.replace(f"[KB:{tid}]", "")
                    report["unsupported"].append({"id": tid, "claim": claim[:200], "score": round(score, 2)})
            out.append(sent)
        return " ".join(out), report
    if isinstance(obj, list):
        res = []
        for x in obj:
            c, report = check_support(x, entries, scorer, report)
            res.append(c)
        return res, report
    if isinstance(obj, dict):
        res = {}
        for k, v in obj.items():
            res[k], report = check_support(v, entries, scorer, report) if k not in ("kb_refs",) else (v, report)
        return res, report
    return obj, report


def auto_tag(text: str, entries: list[dict]) -> str:
    """If a valid KB law is named but not tagged, add its tag after the first mention (deterministic)."""
    by_id = {e["id"]: e for e in entries}
    acts_done = {by_id[i]["act"] for i in KB_TAG.findall(text) if i in by_id}  # one receipt per Act is enough
    for e in entries:
        if e.get("kind") in ("trap", "guidance") or e["act"] in acts_done:
            continue
        acts_done.add(e["act"])
        names = sorted({str(n) for n in [e["act"], *e.get("act_aliases", [])] if len(str(n)) > 6}, key=len, reverse=True)
        for n in names:
            m = re.search(re.escape(n) + r"(?:,?\s*\d{4})?", text, flags=re.I)
            if m:
                text = text[:m.end()] + f" [KB:{e['id']}]" + text[m.end():]
                break
    return text


def auto_tag_obj(obj, entries):
    if isinstance(obj, str):
        return auto_tag(obj, entries)
    if isinstance(obj, list):
        return [auto_tag_obj(x, entries) for x in obj]
    if isinstance(obj, dict):
        return {k: auto_tag_obj(v, entries) for k, v in obj.items()}
    return obj


def render_citations(text: str, kb: dict[str, dict]) -> str:
    """Turn [KB:id] tags into human-readable citation receipts (markdown)."""
    from html import escape
    seen = set()

    def sub(m):
        e = kb.get(m.group(1))
        if not e or m.group(1) in seen:      # one chip per source per passage
            return ""
        seen.add(m.group(1))
        status = e.get("status", "")
        badge = {"primary": "official text", "verified": "verified", "secondary": "check source",
                 "unverified": "please verify"}.get(status, "")
        unit = "Art." if e.get("unit") == "Article" else "s."
        sec = f" {unit}{e['sections'][0]}" if e.get("sections") else ""
        when = e["checked_on"] if status == "primary" else f"checked {e['checked_on']}"
        act = re.sub(r",\s*\d{4}$", "", str(e["act"]))
        tip = escape(f"{e['act']}{sec} · {badge} · {when}", quote=True)
        return (f' <a class="cite {status}" href="{escape(e["source_url"], quote=True)}" target="_blank" title="{tip}">'
                f'<i></i>{escape(act)}{escape(sec)}</a>')
    return KB_TAG.sub(sub, text)
