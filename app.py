"""Nyay Saathi - Streamlit UI.  Run:  streamlit run app.py"""
from __future__ import annotations

import json
import os
import re
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from ai_lawyer import companion, docs, evidence, guardrails, kb, rag, roleplay, ui
from ai_lawyer import notice as notice_mod
from ai_lawyer.core import script_of
from ai_lawyer.core import analyze
from ai_lawyer.llm import DEFAULT_MODEL, LLM
from ai_lawyer.redact import restore

ROOT = Path(__file__).parent
STATES = ["Not sure", "Andhra Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa", "Gujarat", "Haryana",
          "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Odisha", "Punjab",
          "Rajasthan", "Tamil Nadu", "Telangana", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Other"]
EXAMPLES = {
    "Deposit (Hinglish)": "Maine Bangalore mein 2 saal flat rent pe liya tha, rent 18000 tha aur 60000 deposit diya tha "
                          "bank transfer se. March 2026 mein flat khali kar diya, keys bhi de di. Ab landlord bol raha hai "
                          "painting aur cleaning ke 25000 katenge aur baaki bhi abhi nahi de raha, 6 mahine ho gaye. "
                          "Agreement mere paas hai.",
    "Refund (English)": "I ordered a phone worth Rs 32,999 on an e-commerce site on 2 Sept 2026. It was delivered with "
                        "a cracked screen, I returned it on 5 Sept and they picked it up, but the refund still hasn't "
                        "come. Customer care keeps saying 7-10 days. I have the order invoice and pickup receipt.",
    "Salary (Hindi)": "मैं पुणे में एक स्टार्टअप में काम करता था, सैलरी 35000 महीना थी। अगस्त से अक्टूबर 2026 तक की "
                      "सैलरी नहीं मिली। 31 अक्टूबर को मैंने इस्तीफा दे दिया। HR कहता है पैसे नहीं हैं, बाद में देंगे। "
                      "मेरे पास ऑफर लेटर और पुरानी सैलरी स्लिप हैं।",
}

st.set_page_config(page_title="Nyay Saathi · legal help", page_icon="⚖️", layout="wide")
st.markdown(ui.CSS, unsafe_allow_html=True)

ss = st.session_state
SAVE_KEYS = ("chat", "result", "evidence", "drafts", "rp", "pii", "tracker", "notice")
for k, v in {"chat": [], "result": None, "evidence": [], "drafts": {}, "rp": [], "rp_fb": None, "pii": {},
             "tracker": [], "notice": None}.items():
    ss.setdefault(k, v)

# ---------------- sidebar ----------------
with st.sidebar:
    st.markdown('<div class="side-brand">Nyay Saathi<small>Help with deposits, refunds, unpaid salary and '
                'notices. Not a lawyer, and it will tell you when you need one.</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="side-label">Settings</div>', unsafe_allow_html=True)
    model = st.text_input("Model (provider:model)", value=DEFAULT_MODEL,
                          help="e.g. groq:openai/gpt-oss-120b, gemini:gemini-3.5-flash-lite, openai:gpt-4.1-mini, "
                               "anthropic:claude-sonnet-5-5, ollama:llama3.1")
    state = st.selectbox("Your state", STATES, help="Rent and labour rules differ by state.")
    st.markdown('<div class="side-label">Try an example</div>', unsafe_allow_html=True)
    for name, text in EXAMPLES.items():
        if st.button(name, use_container_width=True):
            ss.pending = text
    st.markdown('<div class="side-label">Session</div>', unsafe_allow_html=True)
    if st.button("Start a new case", use_container_width=True):
        for k in ("chat", "evidence", "rp", "tracker"):
            ss[k] = []
        ss.result, ss.rp_fb, ss.drafts, ss.pii, ss.notice = None, None, {}, {}, None
        st.rerun()
    if ss.chat or ss.notice:
        st.download_button("Save this case (.json)", json.dumps({k: ss[k] for k in SAVE_KEYS}, default=str,
                                                                 ensure_ascii=False).encode("utf-8"),
                           file_name=f"nyay_saathi_case_{date.today().isoformat()}.json", use_container_width=True,
                           help="Private file with everything, including your personal details. Keep it to yourself; "
                                "upload it later to carry on where you left off.")
    with st.expander("Carry on a saved case"):
        resume = st.file_uploader("Saved case file", type=["json"], label_visibility="collapsed")
    if resume is not None and ss.get("resumed") != resume.file_id:
        try:
            data = json.loads(resume.getvalue().decode("utf-8"))
            for k in SAVE_KEYS:
                if k in data:
                    ss[k] = data[k]
            ss.resumed = resume.file_id
            st.rerun()
        except Exception as e:
            st.error(f"Couldn't open that file: {e}")
    st.markdown('<div class="side-label">Privacy &amp; help</div><div class="side-note">Phone, Aadhaar, PAN, bank, UPI '
                'and email are masked before anything reaches the AI model.<br><br>Free legal aid <b>15100</b> (NALSA)'
                '<br>Emergency <b>112</b></div>', unsafe_allow_html=True)


def get_llm() -> LLM | None:
    try:
        return LLM(model)
    except Exception as e:
        st.error(f"Model setup problem: {e}")
        return None


def banner(flags):
    if flags:
        st.markdown("".join(ui.flag(f["severity"], f["code"], f["message"]) for f in flags), unsafe_allow_html=True)


def md_inline(text: str) -> str:
    """Tiny markdown -> HTML for text placed inside our own HTML blocks."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text or "")
    return text.replace("\n", "<br>")


def nothing_yet():
    st.markdown(ui.empty("Nothing here yet", "Tell me your problem in the Talk tab, and this page fills in."),
                unsafe_allow_html=True)


@st.cache_resource(show_spinner="Loading the law library (first time only)...")
def law_library():
    """Load the search index + embedding models once per server, not per chat turn."""
    r = rag.get_retriever()
    if r is not None and r.vecs is not None:
        r.search("warm up", "consumer", k=1)     # loads embedder + reranker now, not on first question
    return r


HERO = st.empty()
HERO.markdown(ui.hero(None, compact=bool(ss.chat)), unsafe_allow_html=True)   # shows at once, before the slow model load
LIB = law_library()
with st.sidebar:
    if LIB:
        n_src = len({c["source_id"] for c in LIB.chunks})
        st.markdown(f'<div class="side-label">Law library</div><div class="side-note"><b>{len(LIB.chunks):,}</b> sections '
                    f'from {n_src} official texts: BNS, BNSS, the Constitution, Consumer Protection Act, Code on Wages, '
                    f'Model Tenancy Act.<br><span style="opacity:.7">{LIB.mode}</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="side-label">Law library</div><div class="side-note">Not built. Run '
                    '<code>python scripts/build_index.py</code>. Using curated notes only.</div>', unsafe_allow_html=True)

KB = kb.load_kb()


def kb_for_render() -> dict:
    """Curated KB + the official-text sections retrieved for this case."""
    extra = {e["id"]: e for e in (ss.result or {}).get("_rag_entries", [])}
    return {**KB, **extra}


HERO.markdown(ui.hero(len(LIB.chunks) if LIB else None, compact=bool(ss.chat)), unsafe_allow_html=True)

tabs = st.tabs(["Talk", "Case file", "Your options", "Next steps", "Documents", "Got a notice?", "Practise", "Models"])


def cite(kb_id: str | None) -> str:
    return guardrails.render_citations(f"[KB:{kb_id}]", kb_for_render()) if kb_id else ""


def speech_lang() -> str:
    story = " ".join(m["content"] for m in ss.chat if m["role"] == "user")
    sc = script_of(story)
    lang = ((ss.result or {}).get("case") or {}).get("user_language", "").lower()
    if sc == "latin" and ("hinglish" in lang or "hindi" in lang):
        return "hi-IN"
    return ui.SPEECH_LANG.get(sc, "en-IN")

# ---------------- Talk ----------------
with tabs[0]:
    for i, m in enumerate(ss.chat):
        with st.chat_message(m["role"]):
            st.markdown(m["content"], unsafe_allow_html=True)
            if m["role"] == "assistant" and i == len(ss.chat) - 1:
                components.html(ui.speak_button(m["content"], speech_lang()), height=44)

    EMPTY = st.empty()
    if not ss.chat:
        EMPTY.markdown(ui.empty("Start with your story", "Who owes you what, since when, and what proof you have. Any language is fine."), unsafe_allow_html=True)
    audio = st.audio_input("Or speak instead of typing")
    if audio is not None and ss.get("last_audio") != audio.file_id:
        llm = get_llm()
        if llm:
            with st.spinner("Listening..."):
                try:
                    ss.pending = llm.transcribe(audio.getvalue(), "voice.wav")
                    ss.last_audio = audio.file_id
                except Exception as e:
                    st.error(str(e))

    typed = st.chat_input("Describe your problem, or answer my questions...")
    msg = typed or ss.pop("pending", None)
    if msg:
        EMPTY.empty()
        HERO.markdown(ui.hero(None, compact=True), unsafe_allow_html=True)
        ss.chat.append({"role": "user", "content": msg})
        with st.chat_message("user"):
            st.markdown(msg)
        llm = get_llm()
        if llm:
            with st.spinner("Reading your story and checking the law..."):
                story = "\n".join(m["content"] for m in ss.chat if m["role"] == "user")
                try:
                    ss.result = analyze(story, llm, state_hint=None if state == "Not sure" else state,
                                        pii_mapping=ss.pii)
                    ss.pii = ss.result["_pii_mapping"]
                    a, case = ss.result["assessment"], ss.result["case"]
                    reply = guardrails.render_citations(a.get("reply", ""), kb_for_render())
                    qs = case.get("follow_up_questions") or []
                    if qs and not any(f["severity"] == "refuse" for f in ss.result["flags"]):
                        reply += "\n\n**A few things that would make your case stronger:**\n" + "\n".join(f"- {q}" for q in qs[:4])
                    removed = ss.result["guardrail_report"].get("removed_count", 0)
                    if removed:
                        reply += f"\n\n<span class='small-muted'>The fact-checker removed {removed} legal reference(s) it could not verify.</span>"
                    ss.chat.append({"role": "assistant", "content": reply})
                except Exception as e:
                    ss.chat.append({"role": "assistant", "content": f"Sorry, something went wrong: {e}"})
        st.rerun()

    if ss.result:
        banner(ss.result["flags"])

# ---------------- Case file ----------------
with tabs[1]:
    if not ss.result:
        nothing_yet()
    else:
        case, calc = ss.result["case"], ss.result["calculation"]
        c1, c2 = st.columns([3, 2], gap="large")
        with c1:
            other = case.get("other_party") or {}
            st.markdown(
                '<div class="card"><div class="label">Your case</div>'
                f'<div class="summary">{ui.e(case.get("summary"))}</div>'
                + ui.kv([("Problem", f"{case.get('problem_type')} · {case.get('problem_subtype') or ''}"),
                         ("State", case.get("state") or "not given"),
                         ("Other side", f"{other.get('name') or 'unknown'} ({other.get('type') or '?'})")])
                + "</div>", unsafe_allow_html=True)
            rows = evidence.merge_timeline(case, ss.evidence)
            if rows:
                st.markdown('<div class="card"><div class="label">What happened, in order</div>'
                            + ui.timeline(rows) + "</div>", unsafe_allow_html=True)
            have, missing = case.get("evidence_have") or [], case.get("evidence_missing") or []
            proof = '<div class="card"><div class="label">Proof you have</div>'
            proof += ui.chips(have, "have") if have else '<div class="small-muted">None mentioned yet.</div>'
            if missing:
                proof += '<div class="label" style="margin-top:.8rem">Proof that would help</div>' + ui.chips(missing, "miss")
            tips = ss.result["assessment"].get("proof_tips") or []
            if tips:
                proof += ('<div class="label" style="margin-top:.8rem">How to get it</div><ul style="margin:0;padding-left:1.1rem;'
                          'font-size:.9rem">' + "".join(f"<li>{md_inline(ui.e(t))}</li>" for t in tips) + "</ul>")
            st.markdown(proof + "</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(ui.claim_card(calc), unsafe_allow_html=True)
            st.markdown('<div class="label" style="margin-top:.6rem">Evidence locker</div>'
                        '<div class="small-muted" style="margin-bottom:.5rem">Screenshots of WhatsApp, UPI or bank receipts, '
                        'the agreement or invoice, or an exported WhatsApp chat (.txt). I pull out dates and amounts and '
                        'add them to your timeline.</div>', unsafe_allow_html=True)
            files = st.file_uploader("Add evidence", type=["png", "jpg", "jpeg", "webp", "txt"],
                                     accept_multiple_files=True, label_visibility="collapsed")
            if files and st.button("Read my evidence", type="primary"):
                llm = get_llm()
                done = {e["source"] for e in ss.evidence}
                for f in files:
                    if f.name in done or not llm:
                        continue
                    with st.spinner(f"Reading {f.name}..."):
                        try:
                            ss.evidence.append(evidence.read_evidence(f.name, f.getvalue(), llm, ss.pii))
                        except Exception as e:
                            st.error(f"{f.name}: {e}")
                st.rerun()
            for ev in ss.evidence:
                with st.expander(f"{ev['source']} · {ev.get('doc_type', '')}"):
                    st.markdown(f"**Proves:** {ev.get('what_it_proves')}  \n**Doesn't prove:** {ev.get('weaknesses')}")
                    st.json(ev.get("facts"))

# ---------------- Options ----------------
with tabs[2]:
    if not ss.result:
        nothing_yet()
    else:
        a, K = ss.result["assessment"], kb_for_render()
        banner(ss.result["flags"])
        if (a.get("where_you_stand") or "").strip():
            st.markdown("### Where you stand")
            st.markdown(guardrails.render_citations(a["where_you_stand"], K), unsafe_allow_html=True)

        st.markdown("### Your options, gentlest first")
        steps = []
        for o in a.get("options") or []:
            body = md_inline(guardrails.render_citations(o.get("what_to_do", ""), K))
            refs = "".join(guardrails.render_citations(f"[KB:{r}]", K) for r in (o.get("kb_refs") or []) if r in K)
            needs = f'<div class="needs">You\'ll need: {ui.e(", ".join(o["needs"]))}</div>' if o.get("needs") else ""
            steps.append(f'<div class="step"><div class="n">{ui.e(o.get("step"))}</div><div>'
                         f'<h4>{ui.e(guardrails.KB_TAG.sub("", o.get("title") or "").strip())}</h4>'
                         f'<div class="meta"><span>Time · {ui.e(o.get("time"))}</span><span>Cost · {ui.e(o.get("cost"))}</span></div>'
                         f'<p>{body}</p>{needs}<div style="margin-top:.35rem">{refs}</div></div></div>')
        st.markdown('<div class="steps">' + "".join(steps) + "</div>", unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown("### Do you need a lawyer?")
            if a.get("needs_lawyer"):
                st.markdown(ui.note("", "Yes, get one", a.get("needs_lawyer_reason", "")), unsafe_allow_html=True)
            else:
                st.markdown(ui.note("ok", "Not yet", a.get("needs_lawyer_reason", "")), unsafe_allow_html=True)
        with c2:
            if a.get("what_i_dont_know"):
                st.markdown("### What I don't know")
                st.markdown("\n".join(f"- {guardrails.render_citations(x, K)}" for x in a["what_i_dont_know"]),
                            unsafe_allow_html=True)

        g = ss.result["guardrail_report"]
        ret = ss.result.get("retrieval") or {}
        cited = set(g.get("kb_cited", []))
        if ret.get("hits"):
            st.markdown("### The law, in its own words")
            st.markdown(f'<div class="small-muted" style="margin-bottom:.6rem">Sections found in the official texts for your '
                        f'case. The ones marked ★ were used above. Open the PDF to read the full text.</div>',
                        unsafe_allow_html=True)
            for h in ret["hits"]:
                star = "★  " if h["id"] in cited else ""
                cont = " (continued)" if re.search(r"_p[2-9]$", h["id"]) else ""
                label = f"{star}{h['act']} · {h['unit']} {h['number']}{cont}" + (f" — {h['title']}" if h["title"] else "")
                with st.expander(label):
                    st.text(h["excerpt"])
                    st.markdown(f"[Open the official PDF at page {h['page']} ↗]({h['url']}#page={h['page']})")
        st.markdown("### How I got this answer")
        st.markdown('<div class="small-muted" style="margin-bottom:.5rem">Every step, including what the code '
                    'checked and removed after the AI wrote its answer.</div>' + ui.trace(ss.result),
                    unsafe_allow_html=True)
        with st.expander(f"Raw fact-check report · {g.get('removed_count', 0)} reference(s) removed · "
                         f"{len(g.get('kb_cited', []))} source(s) cited"):
            st.json(g)

# ---------------- Next steps: deadlines, tracker, cost/benefit, help ----------------
with tabs[3]:
    if not ss.result:
        nothing_yet()
    else:
        case, calc = ss.result["case"], ss.result["calculation"]
        nx = companion.next_step(case, calc, ss.tracker)
        st.markdown(ui.ladder(nx["stage"], companion.LADDER) + ui.next_card(nx), unsafe_allow_html=True)
        refused = any(f["severity"] == "refuse" for f in ss.result["flags"])
        if nx.get("doc") and not refused:
            if st.button("Draft it for me", type="primary", help=docs.DOC_TYPES[nx["doc"]][0]):
                llm = get_llm()
                if llm:
                    with st.spinner("Drafting..."):
                        ss.drafts[nx["doc"]] = docs.draft(case, calc, nx["doc"], llm, ss.result.get("_rag_entries"))
                    ss.doc_choice = nx["doc"]
                    st.success("Your draft is ready in the Documents tab.")

        c1, c2 = st.columns([3, 2], gap="large")
        with c1:
            st.markdown("### Your deadlines")
            st.markdown(ui.deadline_rows(companion.deadlines(case, ss.tracker), cite), unsafe_allow_html=True)
        with c2:
            st.markdown("### Log what happened")
            with st.form("log", clear_on_submit=True, border=False):
                kind = st.selectbox("What happened?", list(companion.EVENT_KINDS),
                                    format_func=companion.EVENT_KINDS.get)
                when = st.date_input("When?", value=date.today(), max_value=date.today(), format="DD/MM/YYYY")
                amt = st.number_input("Amount received (only if they paid)", min_value=0, step=500, value=0)
                note = st.text_input("Note (optional)", placeholder="e.g. replied on WhatsApp, said next week")
                if st.form_submit_button("Add to my case"):
                    ss.tracker.append({"kind": kind, "date": when.isoformat(), "amount": amt or None, "note": note})
                    st.rerun()
            st.markdown(ui.log_list(ss.tracker, companion.EVENT_KINDS), unsafe_allow_html=True)
            if ss.tracker and st.button("Undo last entry"):
                ss.tracker.pop()
                st.rerun()

        st.markdown("### Is it worth it?")
        st.markdown(ui.routes_table(companion.cost_benefit(case, calc), cite), unsafe_allow_html=True)
        st.markdown("### Where to get help")
        st.markdown(ui.help_cards(companion.help_near_you(case, ss.result["flags"])), unsafe_allow_html=True)

# ---------------- Documents ----------------
with tabs[4]:
    if not ss.result:
        nothing_yet()
    else:
        case = ss.result["case"]
        pt = case.get("problem_type")
        options = ["whatsapp_message", "legal_notice"] + {"consumer": ["consumer_complaint"],
                                                           "salary": ["labour_complaint"]}.get(pt, [])
        if any(f["severity"] == "refuse" for f in ss.result["flags"]):
            st.markdown(ui.note("", "Not available", "I can't draft documents for this request."), unsafe_allow_html=True)
        else:
            pick = ss.get("doc_choice")
            dt = st.radio("What do you need?", options, format_func=lambda k: docs.DOC_TYPES[k][0], horizontal=True,
                          index=options.index(pick) if pick in options else 0)
            if st.button("Draft it", type="primary"):
                llm = get_llm()
                if llm:
                    with st.spinner("Drafting..."):
                        ss.drafts[dt] = docs.draft(case, ss.result["calculation"], dt, llm, ss.result.get("_rag_entries"))
            if dt in ss.drafts:
                d = ss.drafts[dt]["draft"]
                if d.get("explain_in_user_language"):
                    st.markdown(ui.note("ok", "What this letter does", d["explain_in_user_language"]), unsafe_allow_html=True)
                st.text_area("Your draft — edit anything before you send it",
                             restore(guardrails.KB_TAG.sub("", d.get("body", "")), ss.pii), height=380)
                if d.get("placeholders_to_fill"):
                    st.markdown(ui.note("caution", "Fill these in", ", ".join(d["placeholders_to_fill"])), unsafe_allow_html=True)
                st.download_button("Download as Word (.docx)", docs.to_docx(d, ss.pii), file_name=f"{dt}.docx")
                rep = ss.drafts[dt]["guardrail_report"]
                st.markdown(f'<div class="small-muted">Fact-check: {rep.get("removed_count", 0)} reference(s) removed.</div>',
                            unsafe_allow_html=True)
        st.markdown('<div class="rind" style="margin-top:1.6rem"></div>', unsafe_allow_html=True)
        st.markdown("### Take it further")
        c1, c2, c3 = st.columns(3)
        c1.download_button("Case brief for a lawyer (.docx)", docs.case_brief_docx(ss.result), file_name="case_brief.docx",
                           help="One page a legal-aid lawyer can read in two minutes.", use_container_width=True)
        c2.download_button("Deadline reminders (.ics)", docs.reminders_ics(case), file_name="reminders.ics",
                           help="Adds follow-up dates to your phone calendar.", use_container_width=True)
        dls = companion.deadlines(case, ss.tracker)
        nx = companion.next_step(case, ss.result["calculation"], ss.tracker)
        c3.download_button("Shareable case page (.html)",
                           ui.case_page(ss.result, dls, ss.tracker, nx, companion.EVENT_KINDS).encode("utf-8"),
                           file_name="case_file.html", use_container_width=True,
                           help="A clean page to send to family or a legal-aid lawyer. Phone, Aadhaar, bank and other "
                                "personal details stay masked. Open it and use Print → Save as PDF if you need a PDF.")

# ---------------- Got a notice? ----------------
LANGS = ["English", "Hindi", "Hinglish (Roman letters)", "Tamil", "Bengali", "Marathi", "Telugu", "Kannada",
         "Gujarati", "Punjabi", "Malayalam"]
with tabs[5]:
    st.markdown('<div class="small-muted" style="margin-bottom:.7rem">Got a legal notice, a notice to vacate, a demand '
                'letter or a summons? Upload a photo or PDF, or paste the text. I\'ll explain it in plain words, '
                'count down to the reply deadline, and check every law it cites against the official texts.</div>',
                unsafe_allow_html=True)
    c1, c2 = st.columns([3, 2], gap="large")
    with c1:
        up = st.file_uploader("Photo or PDF of the notice", type=["png", "jpg", "jpeg", "webp", "pdf", "txt"])
        pasted = st.text_area("…or paste its text", height=120)
    with c2:
        guess = ((ss.result or {}).get("case") or {}).get("user_language", "English")
        default = next((i for i, l in enumerate(LANGS) if l.split()[0].lower() in guess.lower()), 0)
        nlang = st.selectbox("Explain it to me in", LANGS, index=default)
        ctx = st.text_area("Your side, in a line or two (optional)", height=100,
                           placeholder="e.g. I paid rent till March and handed over the keys")
        go = st.button("Read my notice", type="primary", disabled=not (up or pasted.strip()))
    if go:
        llm = get_llm()
        if llm:
            with st.spinner("Reading the notice and checking its laws..."):
                try:
                    if up is not None:
                        ss.notice = notice_mod.read_notice(llm, ss.pii, nlang, filename=up.name, data=up.getvalue(),
                                                           context=ctx)
                    else:
                        ss.notice = notice_mod.read_notice(llm, ss.pii, nlang, text=pasted, context=ctx)
                    ss.pii = ss.notice.pop("_pii_mapping", ss.pii)
                except Exception as e:
                    st.error(f"Couldn't read it: {e}")
    if ss.notice:
        n, r = ss.notice, ss.notice["reading"]
        st.markdown('<div class="rind" style="margin-top:1rem"></div>', unsafe_allow_html=True)
        banner(n["flags"])
        a1, a2 = st.columns([1, 3], gap="large")
        with a1:
            if n["days_left"] is not None:
                st.markdown(f'<div class="label">Reply deadline</div><div class="bignum">{abs(n["days_left"])}</div>'
                            f'<div class="small-muted">{"days left" if n["days_left"] >= 0 else "days ago"} · '
                            f'{ui.e(r.get("reply_deadline"))}</div>', unsafe_allow_html=True)
            elif r.get("deadline_text"):
                st.markdown(f'<div class="label">Deadline in the notice</div><div class="verdict">{ui.e(r["deadline_text"])}</div>'
                            '<div class="small-muted">Counted from the day you received it. Write that date down.</div>',
                            unsafe_allow_html=True)
            if r.get("amount_demanded"):
                st.markdown(f'<div class="label" style="margin-top:1rem">They demand</div>'
                            f'<div class="bignum" style="font-size:1.8rem">₹{float(r["amount_demanded"]):,.0f}</div>',
                            unsafe_allow_html=True)
        with a2:
            st.markdown(f'<div class="label">From {ui.e(r.get("sender"))}'
                        f'{" · a lawyer" if r.get("sender_is_lawyer") else ""}'
                        f'{" · COURT DOCUMENT" if r.get("is_court_document") else ""}</div>'
                        f'<div class="verdict">{ui.e(r.get("plain_explanation"))}</div>', unsafe_allow_html=True)
            if r.get("what_if_ignored"):
                st.markdown(ui.note("caution", "If you ignore it", r["what_if_ignored"]), unsafe_allow_html=True)
        b1, b2 = st.columns(2, gap="large")
        with b1:
            if r.get("points_to_check"):
                st.markdown("### Check these")
                st.markdown("\n".join(f"- {x}" for x in r["points_to_check"]))
        with b2:
            if r.get("do_not"):
                st.markdown("### Don't")
                st.markdown("\n".join(f"- {x}" for x in r["do_not"]))
        if n["laws"]:
            st.markdown("### The laws it cites, checked")
            for l in n["laws"]:
                head = {"found": "In the official text", "old": "Old law", "missing": "Not found",
                        "unknown": "Can't check"}[l["verdict"]]
                link = (f' · <a href="{ui.e(l["url"])}" target="_blank">{ui.e(l["act"])} {ui.e(l["unit"])} {ui.e(l["number"])}'
                        f'{": " + ui.e(l["title"]) if l.get("title") else ""} ↗</a>') if l["verdict"] == "found" else ""
                st.markdown(f'<div class="law {l["verdict"]}"><b>{head}</b>{ui.e(l["ref"])}{link}'
                            f'<div class="small-muted">{ui.e(l["note"])}</div></div>', unsafe_allow_html=True)
        st.markdown("### What next")
        d1, d2 = st.columns(2)
        if d1.button("Draft a reply to this notice", use_container_width=True):
            llm = get_llm()
            if llm:
                ncase = {"problem_type": "notice", "user_language": nlang,
                         "summary": f"Notice from {r.get('sender')}: {r.get('what_they_claim')} Person's side: {ctx or 'not given'}",
                         "other_party": {"name": r.get("sender"), "type": r.get("doc_kind")},
                         "timeline": [{"date": r.get("notice_date"), "event": "Notice received", "proof": "the notice"}],
                         "reply_points": r.get("reply_points"), "amounts": {}}
                with st.spinner("Drafting your reply..."):
                    ss.drafts["notice_reply"] = docs.draft(ncase, {"total": None, "lines": [], "notes": []}, "notice_reply", llm)
        if d2.button("Use this notice as my case", use_container_width=True,
                     help="Sends a summary to the Talk tab so you get the full case file, options and deadlines."):
            ss.pending = notice_mod.as_story(n) + (f" My side: {ctx}" if ctx else "")
            st.rerun()
        if "notice_reply" in ss.drafts:
            d = ss.drafts["notice_reply"]["draft"]
            if d.get("explain_in_user_language"):
                st.markdown(ui.note("ok", "What this reply does", d["explain_in_user_language"]), unsafe_allow_html=True)
            st.text_area("Your reply — edit before sending, and have a lawyer check it",
                         restore(guardrails.KB_TAG.sub("", d.get("body", "")), ss.pii), height=340)
            st.download_button("Download reply (.docx)", docs.to_docx(d, ss.pii), file_name="notice_reply.docx")

# ---------------- Practise ----------------
with tabs[6]:
    if not ss.result:
        nothing_yet()
    else:
        who, _ = roleplay.opponent(ss.result["case"])
        st.markdown(f'<div class="small-muted" style="margin-bottom:.8rem">I\'ll play <b>{ui.e(who)}</b>. Ask for your money '
                    f'calmly and firmly, then press “Score me”.</div>', unsafe_allow_html=True)
        for m in ss.rp:
            with st.chat_message("user" if m["role"] == "user" else "assistant"):
                st.write(m["content"])
        said = st.text_input("You say", key=f"rp_in_{len(ss.rp)}", placeholder="e.g. I vacated on 31 March and returned the keys…")
        c1, c2, _ = st.columns([1, 1, 4])
        if c1.button("Send", type="primary") and said:
            llm = get_llm()
            if llm:
                ss.rp.append({"role": "user", "content": said})
                ss.rp.append({"role": "assistant", "content": roleplay.reply(ss.result["case"], ss.rp, llm)})
                st.rerun()
        if c2.button("Score me") and ss.rp:
            llm = get_llm()
            if llm:
                ss.rp_fb = roleplay.feedback(ss.result["case"], ss.rp, llm)
        if ss.rp_fb:
            fb = ss.rp_fb
            cols = st.columns(4)
            for col, key, label in zip(cols, ["used_facts", "cited_proof", "stayed_calm", "clear_next_step"],
                                       ["Facts", "Proof", "Calm", "Next step"]):
                col.metric(label, f"{(fb.get(key) or {}).get('score', '?')}/2")
                col.caption((fb.get(key) or {}).get("comment", ""))
            st.markdown(ui.note("ok", "Your best line", fb.get("best_line", "")) +
                        ui.note("caution", "Try this next time", fb.get("tip", "")), unsafe_allow_html=True)

# ---------------- Models ----------------
with tabs[7]:
    st.markdown('<div class="small-muted" style="margin-bottom:.6rem">The same 18 test cases run on different models. '
                'Fewer invented references is better. Produced by <code>python run_eval.py</code>.</div>',
                unsafe_allow_html=True)
    lb = ROOT / "outputs" / "leaderboard.csv"
    if lb.exists():
        st.dataframe(pd.read_csv(lb), hide_index=True, use_container_width=True)
    else:
        st.markdown(ui.empty("No leaderboard yet", "Run python run_eval.py --models groq:openai/gpt-oss-120b,"
                             "gemini:gemini-3.5-flash-lite"), unsafe_allow_html=True)
