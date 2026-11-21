"""The 'stays with you' layer - all pure code, no LLM:

  deadlines()     time limits and due dates worked out from the case dates, each tied to a KB source
  cost_benefit()  what each route costs (money, time, lawyer?) and an honest rule-of-thumb verdict
  help_near_you() verified national channels + map searches for the local offices
  next_step()     claim tracker: from what the person logged so far, what to do next and by when

Every legal fact here points at a KB entry id (kb/laws.yaml) so the UI can show its citation receipt.
"""
from __future__ import annotations

import re
from datetime import date, timedelta
from urllib.parse import quote_plus

from .escalation import _parse_date

# ---------------------------------------------------------------- deadlines

LIMITS = {   # problem_type -> (years, KB id, wording)
    "consumer": (2, "cpa_limitation", "Last day to file a consumer complaint (2 years)"),
    "salary": (3, "cow_s45", "Last day to file a wage claim (3 years)"),
    "deposit": (3, "deposit_civil_route", "Last day to file a money-recovery suit (3 years, usual rule)"),
}
LEFT_JOB = re.compile(r"resign|quit|left (the )?(job|company)|last (working )?day|relieved|terminat|fired|"
                      r"dismiss|laid off|istifa|इस्तीफ|naukri chhod|job chhod", re.I)


def _add_years(d: date, n: int) -> date:
    try:
        return d.replace(year=d.year + n)
    except ValueError:          # 29 Feb
        return d.replace(year=d.year + n, day=28)


def _working_days_after(d: date, n: int) -> date:
    while n:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def _status(days_left: int) -> str:
    return "passed" if days_left < 0 else "urgent" if days_left <= 30 else "soon" if days_left <= 90 else "ok"


def deadlines(case: dict, tracker: list[dict] | None = None, today: date | None = None) -> list[dict]:
    """Each item: label, date, days_left, status, start, basis, kb (source id), kind."""
    today = today or date.today()
    out = []
    pt = case.get("problem_type")
    events = [(d, e) for e in case.get("timeline") or [] if (d := _parse_date(e.get("date")))]

    if pt in LIMITS and events:
        years, kb_id, label = LIMITS[pt]
        start = min(d for d, _ in events)        # earliest date = conservative (the real start may be later)
        end = _add_years(start, years)
        out.append({"kind": "limit", "label": label, "date": end, "start": start, "kb": kb_id,
                    "basis": f"Counted from your earliest date ({start.isoformat()}), to be safe. The exact start "
                             "is when your claim arose; a lawyer can confirm it."})

    if pt == "salary":
        for d, e in events:
            if LEFT_JOB.search(str(e.get("event") or "")):
                due = _working_days_after(d, 2)
                out.append({"kind": "overdue", "label": "Employer had to pay your final wages by", "date": due,
                            "start": d, "kb": "cow_s17",
                            "basis": f"2 working days after you left ({d.isoformat()})."})
                break

    dm = case.get("deadline_mentioned") or {}
    if (d := _parse_date(dm.get("date"))):
        out.append({"kind": "reply", "label": f"Deadline you mentioned: {dm.get('what') or 'reply / action'}",
                    "date": d, "start": None, "kb": None, "basis": "From your own message or the notice."})

    for t in tracker or []:
        d = _parse_date(t.get("date"))
        if not d:
            continue
        if t["kind"] == "sent_notice":
            out.append({"kind": "followup", "label": "The 15 days in your legal notice end", "date": d + timedelta(days=15),
                        "start": d, "kb": None, "basis": f"You sent the notice on {d.isoformat()}."})
        if t["kind"] == "complained_grievance":
            out.append({"kind": "followup", "label": "Grievance officer must resolve your complaint by",
                        "date": d + timedelta(days=30), "start": d, "kb": "ecom_grievance_officer",
                        "basis": f"One month from your complaint on {d.isoformat()}."})
        if t["kind"] == "sent_message":
            out.append({"kind": "followup", "label": "Reasonable time for a reply to your message ends",
                        "date": d + timedelta(days=7), "start": d, "kb": None,
                        "basis": "Rule of thumb: give them 7 days, then send a formal notice."})

    for x in out:
        x["days_left"] = (x["date"] - today).days
        x["status"] = "overdue" if x["kind"] == "overdue" and x["days_left"] < 0 else _status(x["days_left"])
        if x.get("start"):
            span = max((x["date"] - x["start"]).days, 1)
            x["elapsed"] = min(max((today - x["start"]).days / span, 0), 1)
        else:
            x["elapsed"] = None
    return sorted(out, key=lambda x: x["date"])


# ---------------------------------------------------------------- cost / benefit

ROUTES = {
    "consumer": [
        {"route": "Written complaint to the company's grievance officer", "money": "Free", "time": "Up to 1 month",
         "lawyer": "No", "kb": "ecom_grievance_officer"},
        {"route": "National Consumer Helpline (1915)", "money": "Free", "time": "Usually weeks",
         "lawyer": "No", "kb": "forum_nch"},
        {"route": "District Consumer Commission (online on e-Jagriti)", "money": "Nil up to Rs 5 lakh",
         "time": "Target 3–5 months; often longer", "lawyer": "Not required", "kb": "cpa_s38_timeline"},
    ],
    "salary": [
        {"route": "Written demand to HR / employer", "money": "Free", "time": "1–2 weeks", "lawyer": "No", "kb": None},
        {"route": "Wage claim before the authority (Labour Department)", "money": "Usually no fee; ask the office",
         "time": "Target 3 months", "lawyer": "Not required", "kb": "cow_s45_compensation"},
    ],
    "deposit": [
        {"route": "Written demand (WhatsApp / email)", "money": "Free", "time": "1 week", "lawyer": "No", "kb": None},
        {"route": "Legal notice", "money": "Free if you send it; a lawyer charges a fee", "time": "15 days",
         "lawyer": "Optional", "kb": None},
        {"route": "Rent Authority (only where your state adopted the Model Tenancy Act)", "money": "Varies by state",
         "time": "Varies", "lawyer": "Optional", "kb": "mta_s11_deposit"},
        {"route": "Civil money-recovery suit", "money": "Court fee depends on state and amount", "time": "Months to years",
         "lawyer": "Advisable (free via DLSA if eligible)", "kb": "deposit_civil_route"},
    ],
}


def cost_benefit(case: dict, calc: dict) -> dict:
    pt, total = case.get("problem_type"), calc.get("total")
    routes = ROUTES.get(pt, [])
    if total is None:
        verdict = "Tell me the amounts involved and I'll say whether a formal case is worth your time."
    elif pt == "consumer":
        verdict = ("Worth pursuing. Filing is free at this amount and you don't need a lawyer. Start with the "
                   "grievance officer and the helpline; go to the Commission only if they fail."
                   if total <= 500_000 else
                   "Worth pursuing, but above Rs 5 lakh a filing fee applies - have a lawyer look at it.")
    elif pt == "salary":
        verdict = ("Worth pursuing. You don't need a lawyer, and the authority can order compensation of up to "
                   "10 times the unpaid amount on top of the wages.")
    elif pt == "deposit":
        verdict = ("Push hard with the written demand and a legal notice. For this amount a court case may cost "
                   "more time than it recovers - use free legal aid (15100) if you go further."
                   if total < 25_000 else
                   "Worth a legal notice. Most landlords pay at that stage; a suit is the last resort.")
    else:
        verdict = "This isn't a money claim I can weigh up. Talk to free legal aid (15100) first."
    return {"routes": routes, "verdict": verdict, "total": total,
            "note": "Rule of thumb, not a prediction. Time and costs vary by state and by case."}


# ---------------------------------------------------------------- help near you

def _maps(q: str) -> str:
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(q)


def help_near_you(case: dict, flags: list[dict]) -> list[dict]:
    where = case.get("city") or case.get("state") or ""
    pt = case.get("problem_type")
    out = [{"name": "Free legal aid (NALSA / your DLSA)", "how": "Call 15100", "url": "https://nalsa.gov.in",
            "kb": "lsa_s12_legal_aid", "what": "A free lawyer if you are eligible, and free advice for anyone."},
           {"name": f"District Legal Services Authority{' near ' + where if where else ''}", "how": "Open map",
            "url": _maps(f"District Legal Services Authority {where}".strip()), "kb": None,
            "what": "Usually at the district court complex. Walk in with your documents."}]
    if pt == "consumer":
        out += [{"name": "National Consumer Helpline", "how": "Call 1915", "url": "https://consumerhelpline.gov.in",
                 "kb": "forum_nch", "what": "They take up your complaint with the company, free."},
                {"name": "e-Jagriti (file a consumer complaint online)", "how": "Website", "url": "https://e-jagriti.gov.in",
                 "kb": "forum_ejagriti", "what": "File with the District Commission from home."}]
        if re.search(r"upi|bank|wallet|card|debit|transaction", str(case.get("problem_subtype") or "") +
                     str(case.get("summary") or ""), re.I):
            out.append({"name": "RBI complaint portal (Integrated Ombudsman)", "how": "Website",
                        "url": "https://cms.rbi.org.in", "kb": "rbi_ios_2026",
                        "what": "If the bank doesn't fix it within 30 days or rejects it."})
    if pt == "salary":
        out.append({"name": f"Labour Commissioner office{' near ' + where if where else ''}", "how": "Open map",
                    "url": _maps(f"Labour Commissioner office {where}".strip()), "kb": "cow_s45",
                    "what": "Where wage claims are filed."})
    if pt in ("deposit", "notice"):
        out.append({"name": f"Civil court / Rent Authority{' in ' + where if where else ''}", "how": "Open map",
                    "url": _maps(f"civil court {where}".strip()), "kb": None,
                    "what": "Only if a written demand and a notice have failed."})
    codes = {f["code"] for f in flags}
    if codes & {"CRIMINAL", "DOMESTIC"}:
        out.insert(0, {"name": "Emergency", "how": "Call 112", "url": "tel:112", "kb": None,
                       "what": "If you are in danger right now."})
    if "DOMESTIC" in codes:
        out.insert(1, {"name": "Women's helpline", "how": "Call 181", "url": "tel:181", "kb": None,
                       "what": "Support and protection officers."})
    return out


# ---------------------------------------------------------------- claim tracker

EVENT_KINDS = {
    "sent_message": "I sent a polite message / email",
    "complained_grievance": "I complained to the grievance officer / HR in writing",
    "complained_helpline": "I complained to a helpline (NCH 1915, bank, etc.)",
    "sent_notice": "I sent a legal notice",
    "filed_case": "I filed a complaint / case",
    "paid_part": "They paid part of it",
    "paid_full": "They paid everything",
    "refused": "They refused / said no",
    "replied_other": "They replied, but nothing concrete",
}
RUNG = {"sent_message": 1, "complained_grievance": 2, "complained_helpline": 2, "sent_notice": 3, "filed_case": 4}
LADDER = [(1, "Polite message"), (2, "Grievance / helpline"), (3, "Legal notice"), (4, "Formal complaint"), (5, "Resolved")]
FILE_DOC = {"consumer": "consumer_complaint", "salary": "labour_complaint"}
FILE_WHERE = {"consumer": "the District Consumer Commission (online on e-Jagriti)",
              "salary": "the wage authority (Labour Department)",
              "deposit": "the Rent Authority (if your state has one) or the civil court - free legal aid can help"}


def next_step(case: dict, calc: dict, events: list[dict], today: date | None = None) -> dict:
    today = today or date.today()
    pt = case.get("problem_type")
    total = calc.get("total")
    paid = sum(float(e.get("amount") or 0) for e in events if e["kind"] == "paid_part")
    remaining = None if total is None else max(total - paid, 0)
    rung = max((RUNG.get(e["kind"], 0) for e in events), default=0)
    done = any(e["kind"] == "paid_full" for e in events) or (remaining == 0 and paid > 0)
    last_formal = max((e for e in events if e["kind"] in RUNG), key=lambda e: (RUNG[e["kind"]], e.get("date") or ""),
                      default=None)
    since = (today - (_parse_date(last_formal.get("date")) or today)).days if last_formal else None
    refused = any(e["kind"] == "refused" and (e.get("date") or "") >= (last_formal or {}).get("date", "")
                  for e in events) if last_formal else any(e["kind"] == "refused" for e in events)

    def res(head, detail, doc=None, wait_until=None, stage=rung):
        return {"headline": head, "detail": detail, "doc": doc, "wait_until": wait_until, "stage": stage,
                "remaining": remaining, "paid": paid}

    if done:
        return res("You've been paid. Case closed.", "Keep the payment proof and all messages for at least 3 years.",
                   stage=5)
    left = f"Still owed: Rs {remaining:,.0f}. " if remaining is not None and paid else ""
    if rung == 0:
        return res("Send a polite written message first", left + "Writing creates proof and gives them a fair chance. "
                   "Give them 7 days.", doc="whatsapp_message")
    if rung == 1:
        if since is not None and since < 7 and not refused:
            return res("Wait for their reply", left + f"Give them until {(today + timedelta(days=7 - since)).isoformat()}. "
                       "If they don't pay, the next step is a legal notice.", wait_until=today + timedelta(days=7 - since))
        if pt == "consumer":
            return res("Complain to the grievance officer and the National Consumer Helpline",
                       left + "Both are free. The grievance officer must resolve it within a month. "
                       "Log it here when you've done it.", doc=None)
        return res("Send a legal notice", left + "They didn't pay after your message. A formal notice with a 15-day "
                   "deadline is the usual next step.", doc="legal_notice")
    if rung == 2:
        wait = 30 if any(e["kind"] == "complained_grievance" for e in events) else 15
        if since is not None and since < wait and not refused:
            return res("Give the complaint time to work", left + f"Wait until {(today + timedelta(days=wait - since)).isoformat()} "
                       "before escalating.", wait_until=today + timedelta(days=wait - since))
        return res("Send a legal notice", left + "The complaint didn't fix it. A formal notice is the step before a "
                   "case.", doc="legal_notice")
    if rung == 3:
        if since is not None and since < 15 and not refused:
            return res("Wait for the notice period to end", left + f"Your notice gave them 15 days: until "
                       f"{(today + timedelta(days=15 - since)).isoformat()}.", wait_until=today + timedelta(days=15 - since))
        return res("File a formal complaint", left + f"The notice period is over. File with {FILE_WHERE.get(pt, 'the right forum - ask legal aid (15100)')}.",
                   doc=FILE_DOC.get(pt))
    return res("Follow your case", left + "Keep every notice from the forum, attend each hearing (online where "
               "allowed), and log any payment here. Free legal aid (15100) can represent you.", stage=4)
