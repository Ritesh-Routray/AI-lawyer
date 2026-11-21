"""Deterministic red-flag rules. These run in code and always override the LLM.

severity:
  refuse  - we will not help with this (e.g. forging documents)
  lawyer  - get a real lawyer / legal aid now; AI help is limited to explaining
  caution - AI can help, but a lawyer should check before acting
"""
from __future__ import annotations

import re
from datetime import date, datetime

LEGAL_AID = ("Free legal aid: call NALSA helpline 15100 or visit your District Legal Services "
             "Authority (DLSA) at the district court.")

RULES = [
    ("UNETHICAL", "refuse",
     r"back\s?-?dat|forg(e|ery|ed)|fake (receipt|bill|agreement|document|evidence|witness)|"
     r"jhooth[ae]? (saboot|gawah)|nakli (receipt|bill|agreement)|fabricat",
     "I can't help create, change or backdate documents or evidence. That can itself be a crime and "
     "would hurt your case. I can help you use the genuine proof you have."),
    ("CRIMINAL", "lawyer",
     r"\b(police|fir|arrest(ed)?|giraftar|thana|jail|bail|chargesheet|threat(en)?(ed|ing)?|dhamki|"
     r"assault|beat(en|ing)? me|maar(a|pit)|stalk|blackmail|extort)\b",
     "This involves police or possible criminal matters. Talk to a lawyer before you act or say anything."),
    ("DOMESTIC", "lawyer",
     r"domestic violence|dowry|dahej|in-?laws? (beat|harass)|husband (beats|hits)|wife (beats|hits)",
     "Domestic violence and dowry matters need a lawyer or protection officer. If you are in danger call 112. "
     "Women's helpline: 181."),
    ("COURT", "lawyer",
     r"\b(summons|warrant|decree|court (notice|case|date|hearing)|hearing (date|on)|tareekh|"
     r"case (filed|darj) against|ex-?parte)\b",
     "A court process has started. Court deadlines are strict - get a lawyer now, even if only to file a reply."),
    ("PROPERTY_TITLE", "lawyer",
     r"\b(ownership|title deed|registry dispute|inheritance|succession|partition|illegal possession|"
     r"encroach|kabza)\b",
     "Property ownership disputes are complex and state-specific. This assistant does not cover them."),
    ("MINOR", "lawyer", r"\b(minor|child labour|under ?18|nabalig)\b",
     "Cases involving children need a lawyer or Childline (1098)."),
]


def _amounts(case: dict) -> list[float]:
    vals = []
    for v in (case.get("amounts") or {}).values():
        try:
            vals.append(float(v))
        except (TypeError, ValueError):
            pass
    return vals


def _parse_date(s) -> date | None:
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(str(s)[: len(fmt) + 2].strip(), fmt).date()
        except ValueError:
            continue
    return None


def check(raw_text: str, case: dict, today: date | None = None) -> list[dict]:
    today = today or date.today()
    text = raw_text.lower()
    flags = []
    for code, sev, pattern, msg in RULES:
        if re.search(pattern, text, flags=re.I):
            flags.append({"code": code, "severity": sev, "message": msg})

    # signals the LLM pulled out of the story (catches other languages / paraphrase)
    for sig in case.get("risk_signals") or []:
        s = str(sig).lower()
        for code, sev, pattern, msg in RULES:
            if code not in {f["code"] for f in flags} and re.search(pattern, s, flags=re.I):
                flags.append({"code": code, "severity": sev, "message": msg})

    # Other side already has a lawyer and threatens proceedings -> reply should be lawyer-checked.
    # (Added after eval: the model under-escalated a lawyer's eviction notice.)
    if case.get("problem_type") == "notice" and re.search(
            r"proceedings|evict|vacate|legal action|recovery|suit|my client|advocate|vakil|notice period", text):
        flags.append({"code": "LAWYER_NOTICE", "severity": "lawyer",
                      "message": "You've received a formal notice that threatens legal proceedings. Reply in "
                                 "writing within the time it gives, and have a lawyer (free via DLSA / 15100) "
                                 "check your reply - what you write now can be used later."})

    amts = _amounts(case)
    if amts and max(amts) > 1_000_000:
        flags.append({"code": "HIGH_VALUE", "severity": "caution",
                      "message": f"The amount involved (Rs {max(amts):,.0f}) is high. Have a lawyer review "
                                 "the notice before sending."})

    # limitation (time-bar) check from the earliest dated event
    dates = [d for d in (_parse_date(e.get("date")) for e in case.get("timeline") or []) if d]
    if dates:
        age_years = (today - min(dates)).days / 365.25
        pt = case.get("problem_type")
        limit = {"consumer": 2, "salary": 3, "deposit": 3}.get(pt)
        if limit and age_years > limit - 0.25:
            flags.append({"code": "TIME_LIMIT", "severity": "lawyer",
                          "message": f"The problem started about {age_years:.1f} years ago. The usual time limit for "
                                     f"this kind of claim is around {limit} years - it may be expired or about to "
                                     "expire. See a lawyer quickly."})

    dl = _parse_date((case.get("deadline_mentioned") or {}).get("date"))
    if dl and 0 <= (dl - today).days <= 15:
        flags.append({"code": "URGENT_DEADLINE", "severity": "lawyer",
                      "message": f"There is a deadline on {dl.isoformat()} - within 15 days. Get a lawyer now."})

    if case.get("problem_type") == "other":
        flags.append({"code": "OUT_OF_SCOPE", "severity": "caution",
                      "message": "This problem is outside what this assistant covers in depth (deposits, "
                                 "consumer refunds, unpaid salary). I can only give general direction."})
    return flags


def top_severity(flags: list[dict]) -> str | None:
    order = {"refuse": 3, "lawyer": 2, "caution": 1}
    return max((f["severity"] for f in flags), key=lambda s: order[s], default=None)
