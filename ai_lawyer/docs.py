"""Document outputs: drafted letters (LLM + validator), lawyer hand-off brief and calendar reminders (pure code)."""
from __future__ import annotations

import io
import uuid
from datetime import date, datetime, timedelta

from docx import Document
from docx.shared import Pt

from . import guardrails, kb
from .core import prompt
from .escalation import _parse_date
from .llm import LLM
from .redact import restore

DOC_TYPES = {
    "whatsapp_message": ("Polite WhatsApp / email message (first step)",
                         "A short, polite but clear message (max 120 words) the person sends themselves, stating "
                         "the amount due and asking for payment by a specific date 7 days from today. No legal "
                         "references needed.", False),
    "legal_notice": ("Legal notice / formal demand letter",
                     "A formal demand notice: date, From, To, Subject, numbered paragraphs of facts, the legal "
                     "basis (only KB laws), a clear demand to pay the calculated amount within 15 days, and the "
                     "lawful next steps if not paid. End with name/signature placeholders.", True),
    "consumer_complaint": ("Consumer complaint draft (District Commission)",
                           "A draft complaint for the District Consumer Disputes Redressal Commission: parties, "
                           "facts in numbered paragraphs, deficiency in service / unfair trade practice, attempts "
                           "to resolve (grievance officer, NCH), relief sought (refund of the calculated amount + "
                           "compensation and costs as the Commission thinks fit), list of documents, verification "
                           "placeholder.", True),
    "notice_reply": ("Reply to the notice you received",
                     "A formal written reply to a notice the person received: refer to the notice by date and "
                     "sender, respond point by point using only the facts given, clearly dispute what the person "
                     "disputes without admitting anything else, state the person's own claim if any, and reserve "
                     "all rights. Calm and factual. End with name/signature/date placeholders and a line that "
                     "the reply is sent without prejudice.", True),
    "labour_complaint": ("Unpaid wages claim application",
                         "An application to the authority under the Code on Wages / Labour Commissioner office for "
                         "unpaid wages: employee details, employer details, employment period, wages due month by "
                         "month (use the calculation), attempts made, relief sought, list of documents.", True),
}


def draft(case: dict, calc: dict, doc_type: str, llm: LLM, extra_entries: list[dict] | None = None) -> dict:
    """extra_entries: official-text sections retrieved for this case (analyze()['_rag_entries'])."""
    name, guidance, formal = DOC_TYPES[doc_type]
    lang = case.get("user_language") or "English"
    entries = kb.retrieve(case.get("problem_type", "other")) + list(extra_entries or [])
    language_rule = ("Write the document body in formal English (that is what offices and courts expect)."
                     if formal else f"Write the message body in {lang}.")
    sys = prompt("draft", doc_type=name, doc_guidance=guidance, language=lang, language_rule=language_rule,
                 case=case, calc=calc, kb=kb.format_for_prompt(entries))
    raw = llm.chat_json([{"role": "system", "content": sys},
                         {"role": "user", "content": "Draft it now."}], tag=f"draft:{doc_type}", max_tokens=2500)
    clean, report = guardrails.validate_obj(raw, entries)
    report["kb_cited"] = sorted(report["kb_cited"])
    return {"doc_type": doc_type, "draft": clean, "draft_raw": raw, "guardrail_report": report}


def _strip_tags(text: str) -> str:
    return guardrails.KB_TAG.sub("", text)


def to_docx(d: dict, mapping: dict) -> bytes:
    doc = Document()
    doc.styles["Normal"].font.size = Pt(11)
    doc.add_heading(restore(d.get("title", "Draft"), mapping), level=1)
    for para in restore(_strip_tags(d.get("body", "")), mapping).split("\n"):
        doc.add_paragraph(para)
    if d.get("attach_checklist"):
        doc.add_heading("Attach / keep ready", level=2)
        for item in d["attach_checklist"]:
            doc.add_paragraph(item, style="List Bullet")
    p = doc.add_paragraph()
    p.add_run("Draft prepared with an AI assistant (Nyay Saathi). Check every fact and fill all [placeholders] "
              "before sending. This is not legal advice; for court matters consult a lawyer or DLSA (15100).").italic = True
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


def case_brief_docx(result: dict) -> bytes:
    """One-page hand-off for a legal-aid lawyer. Pure code - no LLM, no new claims."""
    case, calc, a = result["case"], result["calculation"], result["assessment"]
    m = result.get("_pii_mapping", {})
    doc = Document()
    doc.styles["Normal"].font.size = Pt(10)
    doc.add_heading("Case brief for lawyer / legal aid", level=1)
    doc.add_paragraph(f"Prepared {date.today().isoformat()} with Nyay Saathi from the client's own account. Unverified by a lawyer.")
    doc.add_heading("Summary", level=2)
    doc.add_paragraph(restore(case.get("summary") or "", m))
    other = case.get("other_party") or {}
    doc.add_paragraph(f"Type: {case.get('problem_type')} - {case.get('problem_subtype')} | State: {case.get('state') or 'unknown'} "
                      f"| Other party: {other.get('name') or '?'} ({other.get('type') or '?'})")
    doc.add_heading("Timeline", level=2)
    t = doc.add_table(rows=1, cols=3)
    t.style = "Light Grid Accent 1"
    for i, h in enumerate(("Date", "Event", "Proof")):
        t.rows[0].cells[i].text = h
    for e in case.get("timeline") or []:
        r = t.add_row().cells
        r[0].text, r[1].text, r[2].text = str(e.get("date") or "?"), restore(str(e.get("event") or ""), m), str(e.get("proof") or "-")
    doc.add_heading("Amount claimed (computed)", level=2)
    for line in calc["lines"] or ["Not computed"]:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("Evidence", level=2)
    doc.add_paragraph("Have: " + ("; ".join(case.get("evidence_have") or []) or "none listed"))
    doc.add_paragraph("Missing: " + ("; ".join(case.get("evidence_missing") or []) or "none listed"))
    if result["flags"]:
        doc.add_heading("Red flags", level=2)
        for f in result["flags"]:
            doc.add_paragraph(f"{f['code']} ({f['severity']}): {f['message']}", style="List Bullet")
    doc.add_heading("Questions for the lawyer", level=2)
    for q in (a.get("what_i_dont_know") or []) + ["Which law applies in my state, and is my claim within time?"]:
        doc.add_paragraph(_strip_tags(q), style="List Bullet")
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


def reminders_ics(case: dict, today: date | None = None) -> bytes:
    """Calendar reminders. Dates are simple rules of thumb and labelled as such."""
    today = today or date.today()
    events = [
        (today + timedelta(days=7), "Nyay Saathi: did they reply to your message? If not, send the legal notice."),
        (today + timedelta(days=22), "Nyay Saathi: 15-day notice period over (if notice sent ~day 7). Next: file complaint."),
    ]
    dates = [d for d in (_parse_date(e.get("date")) for e in case.get("timeline") or []) if d]
    limit = {"consumer": 2, "salary": 3, "deposit": 3}.get(case.get("problem_type"))
    if dates and limit:
        last = min(dates).replace(year=min(dates).year + limit) - timedelta(days=30)
        events.append((last, f"Nyay Saathi: approx. 1 month before the usual {limit}-year time limit. "
                             "Confirm the exact deadline with a lawyer."))
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//NyaySaathi//EN"]
    for d, title in events:
        if d < today:
            continue
        lines += ["BEGIN:VEVENT", f"UID:{uuid.uuid4()}", f"DTSTAMP:{stamp}",
                  f"DTSTART;VALUE=DATE:{d.strftime('%Y%m%d')}", f"SUMMARY:{title}", "END:VEVENT"]
    lines.append("END:VCALENDAR")
    return "\r\n".join(lines).encode()
