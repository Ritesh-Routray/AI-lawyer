"""Visual layer for the Streamlit app: the watermelon theme (CSS) and small HTML building blocks.

Palette - rind to flesh:
  rind      #1E3A2D  deep green (sidebar, headings accents)
  rind-2    #2F5D46  mid green (links, "you're fine" states)
  pith      #E4EDDC  pale green (soft success surfaces)
  cream     #FBF7F2  page background
  flesh     #C8374F  watermelon red (primary action, key numbers)
  blush     #FBE6E8  pale flesh (soft alert surfaces)
  seed      #2A2321  text
"""
from __future__ import annotations

from datetime import date
from html import escape

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap');

:root{
  --rind:#1E3A2D; --rind-2:#2F5D46; --pith:#E4EDDC; --cream:#FBF7F2; --paper:#FFFDFA;
  --flesh:#C8374F; --flesh-2:#E0566C; --blush:#FBE6E8; --seed:#2A2321; --muted:#7A6E66; --line:#E6DBD0;
  --amber:#B7791F; --amber-bg:#FBF1DE;
}
html, body, .stMarkdown, button, input, textarea { font-family:'Inter', sans-serif; }
h1, h2, h3, .serif { font-family:'Fraunces', Georgia, serif !important; font-weight:500 !important; letter-spacing:-0.01em; }
.block-container{ padding-top:2.2rem; max-width:1080px; }
#MainMenu, footer, [data-testid="stDecoration"]{ visibility:hidden; height:0; }

/* --- signature: the rind stripe --- */
.rind{ height:6px; border-radius:6px; margin:0 0 1.4rem 0;
  background:linear-gradient(90deg,var(--rind) 0 22%, #6E9A6A 22% 30%, var(--pith) 30% 36%, var(--flesh-2) 36% 100%); }

/* --- hero --- */
.hero{ display:flex; justify-content:space-between; align-items:flex-end; gap:2rem; margin-bottom:.6rem; }
.eyebrow{ font-size:.72rem; letter-spacing:.16em; text-transform:uppercase; color:var(--rind-2); font-weight:600; }
.hero .display{ font-family:'Fraunces',Georgia,serif; font-weight:400; font-size:2.35rem; line-height:1.1; margin:.4rem 0 .6rem; color:var(--seed); letter-spacing:-0.015em; }
.hero .display em{ font-style:italic; color:var(--flesh); }
.hero p{ color:var(--muted); max-width:560px; margin:0; font-size:1rem; line-height:1.55; }
.hero .facts{ display:flex; gap:1.6rem; white-space:nowrap; }
.hero .facts div{ text-align:right; }
.hero .facts b{ display:block; font-family:'Fraunces',serif; font-weight:500; font-size:1.5rem; color:var(--seed); }
.hero .facts span{ font-size:.72rem; color:var(--muted); text-transform:uppercase; letter-spacing:.08em; }
@media (max-width:760px){ .hero{ flex-direction:column; align-items:flex-start; } .hero .facts div{ text-align:left; } }

.hero.compact{ align-items:center; margin-bottom:.5rem; }
.summary{ font-size:1rem; line-height:1.6; color:var(--seed); margin-bottom:.9rem; }
h3{ font-size:1.45rem !important; margin-top:1.2rem !important; }

/* --- tabs: quiet underline, no pills --- */
.stTabs [data-baseweb="tab-list"]{ gap:1.6rem; border-bottom:1px solid var(--line); }
.stTabs [data-baseweb="tab"]{ padding:.6rem 0; font-weight:500; color:var(--muted); background:transparent; }
.stTabs [aria-selected="true"]{ color:var(--seed); }
.stTabs [data-baseweb="tab-highlight"]{ background:var(--flesh); height:2px; }

/* --- buttons --- */
.stButton>button, .stDownloadButton>button{ border-radius:999px; font-weight:500; border:1px solid var(--line);
  background:var(--paper); color:var(--seed); transition:all .15s ease; }
.stButton>button:hover, .stDownloadButton>button:hover{ border-color:var(--flesh); color:var(--flesh); }
.stButton>button[kind="primary"]{ background:var(--flesh); border-color:var(--flesh); color:#fff; }
.stButton>button[kind="primary"]:hover{ background:#B02F45; color:#fff; }

/* --- sidebar (deep rind) --- */
[data-testid="stSidebar"] .stButton>button{ background:transparent; border:1px solid #3D6352; color:#EFE7DC;
  justify-content:flex-start; border-radius:.5rem; }
[data-testid="stSidebar"] .stButton>button:hover{ border-color:#F08A9B; color:#fff; background:#284A3A; }
[data-testid="stSidebar"] .side-brand{ font-family:'Fraunces',serif; font-size:1.45rem; color:#FBF7F2; line-height:1.1; }
[data-testid="stSidebar"] .side-brand small{ display:block; font-family:'Inter',sans-serif; font-size:.78rem;
  color:#B9C9BC; margin-top:.35rem; letter-spacing:0; line-height:1.45; }
[data-testid="stSidebar"] .side-label{ font-size:.68rem; letter-spacing:.14em; text-transform:uppercase; color:#9FB5A6;
  margin:1.2rem 0 .45rem; font-weight:600; }
[data-testid="stSidebar"] .side-note{ font-size:.78rem; color:#B9C9BC; line-height:1.5; }
[data-testid="stSidebar"] .side-note b{ color:#FBF7F2; }
[data-testid="stSidebar"] hr{ border-color:#35574A; }
[data-testid="stSidebar"] [data-testid="stExpander"]{ background:transparent; border-color:#3D6352; }
[data-testid="stSidebar"] [data-testid="stExpander"] summary{ color:#EFE7DC; font-weight:400; font-size:.88rem; }

/* --- chat --- */
[data-testid="stChatMessage"]{ background:transparent; padding:.9rem 0; border-bottom:1px solid var(--line); border-radius:0; }
[data-testid="stChatMessageAvatarUser"]{ background:var(--pith); color:var(--rind); }
[data-testid="stChatMessageAvatarAssistant"]{ background:var(--flesh); color:#fff; }
[data-testid="stChatInput"]{ border-radius:14px; }

/* --- cards --- */
.card{ background:var(--paper); border:1px solid var(--line); border-radius:14px; padding:1.1rem 1.25rem; margin-bottom:1rem; }
.card h4{ font-family:'Fraunces',serif; font-weight:500; margin:0 0 .5rem; font-size:1.05rem; color:var(--seed); }
.label{ font-size:.7rem; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); font-weight:600; margin-bottom:.35rem; }
.kv{ display:grid; grid-template-columns:110px 1fr; gap:.35rem .8rem; font-size:.92rem; }
.kv dt{ color:var(--muted); } .kv dd{ margin:0; color:var(--seed); }

/* claim figure */
.claim{ background:var(--rind); color:#FBF7F2; border-radius:14px; padding:1.2rem 1.3rem; margin-bottom:1rem; position:relative; overflow:hidden; }
.claim:after{ content:""; position:absolute; left:0; right:0; bottom:0; height:5px; background:var(--flesh-2); }
.claim .label{ color:#A9C0B0; }
.claim .amt{ font-family:'Fraunces',serif; font-size:2.3rem; line-height:1.1; margin:.2rem 0 .6rem; }
.claim ul{ margin:0; padding-left:1rem; font-size:.86rem; color:#DCE5DD; }
.claim .note{ font-size:.78rem; color:#A9C0B0; margin-top:.6rem; }

/* flags */
.flag{ border-left:3px solid var(--flesh); background:var(--blush); border-radius:0 10px 10px 0; padding:.75rem 1rem; margin:.5rem 0; font-size:.92rem; }
.flag b{ display:block; font-size:.7rem; letter-spacing:.12em; text-transform:uppercase; color:var(--flesh); margin-bottom:.2rem; }
.flag.caution{ border-color:var(--amber); background:var(--amber-bg); } .flag.caution b{ color:var(--amber); }
.flag.ok{ border-color:var(--rind-2); background:var(--pith); } .flag.ok b{ color:var(--rind-2); }

/* option steps */
.steps{ counter-reset:step; }
.step{ display:grid; grid-template-columns:2.2rem 1fr; gap:.9rem; padding:1rem 0; border-bottom:1px solid var(--line); }
.step .n{ width:2.2rem; height:2.2rem; border-radius:50%; border:1px solid var(--flesh); color:var(--flesh);
  display:flex; align-items:center; justify-content:center; font-family:'Fraunces',serif; font-size:1.05rem; }
.step:first-child .n{ background:var(--flesh); color:#fff; }
.step h4{ margin:0 0 .25rem; font-family:'Fraunces',serif; font-weight:500; font-size:1.08rem; }
.step .meta{ font-size:.78rem; color:var(--muted); margin-bottom:.45rem; }
.step .meta span{ margin-right:1rem; }
.step p{ margin:0 0 .4rem; line-height:1.55; font-size:.94rem; }
.step .needs{ font-size:.82rem; color:var(--muted); }

/* citation chips */
.cite{ display:inline-flex; align-items:center; gap:.35rem; font-size:.72rem; line-height:1; vertical-align:2px;
  padding:.22rem .5rem; margin:0 .15rem; border-radius:999px; border:1px solid var(--line); background:var(--paper);
  color:var(--seed); text-decoration:none !important; white-space:nowrap; }
.cite i{ width:.45rem; height:.45rem; border-radius:50%; display:inline-block; background:var(--muted); }
.cite.primary i{ background:var(--rind-2); } .cite.verified i{ background:var(--rind-2); }
.cite.secondary i{ background:var(--amber); } .cite.unverified i{ background:var(--flesh); }
.cite:hover{ border-color:var(--rind-2); }

/* timeline */
.tl{ position:relative; margin:.4rem 0 0 .3rem; padding-left:1.2rem; border-left:2px solid var(--pith); }
.tl div{ position:relative; padding:.25rem 0 .7rem; font-size:.9rem; }
.tl div:before{ content:""; position:absolute; left:-1.55rem; top:.5rem; width:.6rem; height:.6rem; border-radius:50%;
  background:var(--cream); border:2px solid var(--flesh); }
.tl time{ display:block; font-size:.74rem; color:var(--muted); letter-spacing:.04em; }
.tl small{ color:var(--rind-2); }

/* proof chips */
.chips span{ display:inline-block; font-size:.8rem; padding:.25rem .6rem; border-radius:999px; margin:0 .3rem .35rem 0; }
.chips.have span{ background:var(--pith); color:var(--rind); }
.chips.miss span{ background:var(--blush); color:#8E2236; }

/* deadline countdown */
.dl{ display:grid; grid-template-columns:5.2rem 1fr; gap:1rem; align-items:center; padding:.85rem 0; border-bottom:1px solid var(--line); }
.dl .days{ font-family:'Fraunces',serif; font-size:1.9rem; line-height:1; color:var(--seed); text-align:right; }
.dl .days small{ display:block; font-family:'Inter',sans-serif; font-size:.68rem; color:var(--muted); letter-spacing:.08em; text-transform:uppercase; margin-top:.2rem; }
.dl.urgent .days, .dl.overdue .days, .dl.passed .days{ color:var(--flesh); }
.dl .what{ font-size:.95rem; color:var(--seed); } .dl .what b{ font-weight:600; }
.dl .basis{ font-size:.78rem; color:var(--muted); margin-top:.15rem; }
.bar{ height:5px; border-radius:5px; background:var(--pith); margin-top:.45rem; overflow:hidden; }
.bar i{ display:block; height:100%; background:var(--rind-2); border-radius:5px; }
.dl.soon .bar i{ background:var(--amber); } .dl.urgent .bar i, .dl.passed .bar i, .dl.overdue .bar i{ background:var(--flesh); }

/* tracker ladder */
.ladder{ display:flex; gap:.35rem; margin:.4rem 0 1rem; }
.ladder div{ flex:1; text-align:center; font-size:.72rem; color:var(--muted); padding-top:.55rem; border-top:4px solid var(--line); }
.ladder div.done{ border-color:var(--rind-2); color:var(--rind); }
.ladder div.now{ border-color:var(--flesh); color:var(--flesh); font-weight:600; }
.next{ background:var(--paper); border:1px solid var(--line); border-left:4px solid var(--flesh); border-radius:12px; padding:1rem 1.2rem; }
.next .serif{ font-size:1.25rem; margin:.15rem 0 .35rem; }
.log{ font-size:.86rem; } .log div{ padding:.35rem 0; border-bottom:1px dashed var(--line); }
.log time{ color:var(--muted); margin-right:.6rem; font-size:.78rem; }

/* routes table */
.routes{ width:100%; border-collapse:collapse; font-size:.86rem; margin:.3rem 0 .6rem; }
.routes th{ text-align:left; font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); font-weight:600;
  border-bottom:1px solid var(--line); padding:.4rem .5rem .4rem 0; }
.routes td{ padding:.6rem .5rem .6rem 0; border-bottom:1px solid var(--line); vertical-align:top; }
.routes td:first-child{ color:var(--seed); font-weight:500; }
.verdict{ font-family:'Fraunces',serif; font-size:1.12rem; line-height:1.45; color:var(--seed); margin:.2rem 0 .4rem; }

/* help cards */
.helps{ display:grid; grid-template-columns:repeat(auto-fill,minmax(230px,1fr)); gap:.7rem; }
.help{ background:var(--paper); border:1px solid var(--line); border-radius:12px; padding:.85rem 1rem; text-decoration:none !important; color:var(--seed) !important; display:block; }
.help:hover{ border-color:var(--rind-2); }
.help b{ display:block; font-weight:600; font-size:.9rem; margin-bottom:.2rem; }
.help span{ font-size:.8rem; color:var(--muted); display:block; }
.help em{ font-style:normal; font-size:.78rem; color:var(--flesh); font-weight:600; display:block; margin-top:.45rem; }

/* trace (show your work) */
.trace{ counter-reset:t; }
.trace div{ position:relative; padding:.5rem 0 .6rem 2.3rem; border-left:1px solid var(--line); margin-left:.8rem; font-size:.88rem; }
.trace div:before{ counter-increment:t; content:counter(t); position:absolute; left:-.8rem; top:.45rem; width:1.6rem; height:1.6rem;
  border-radius:50%; background:var(--cream); border:1px solid var(--rind-2); color:var(--rind-2); font-size:.75rem;
  display:flex; align-items:center; justify-content:center; font-weight:600; }
.trace div.cut:before{ border-color:var(--flesh); color:var(--flesh); }
.trace b{ color:var(--seed); } .trace span{ color:var(--muted); }
.trace s{ color:var(--flesh); }

/* law check (notice) */
.law{ border:1px solid var(--line); border-radius:10px; padding:.6rem .85rem; margin:.4rem 0; font-size:.86rem; background:var(--paper); }
.law b{ font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; margin-right:.5rem; }
.law.found b{ color:var(--rind-2); } .law.old b, .law.missing b{ color:var(--flesh); } .law.unknown b{ color:var(--muted); }
.bignum{ font-family:'Fraunces',serif; font-size:2.6rem; line-height:1; color:var(--flesh); }

/* empty state */
.empty{ text-align:center; padding:3.5rem 1rem; color:var(--muted); }
.empty .serif{ font-size:1.35rem; color:var(--seed); margin-bottom:.3rem; }

/* expanders, dataframes, metrics */
[data-testid="stExpander"]{ border:1px solid var(--line); border-radius:12px; background:var(--paper); }
[data-testid="stExpander"] summary{ font-weight:500; }
[data-testid="stMetricValue"]{ font-family:'Fraunces',serif; color:var(--flesh); }
.small-muted{ font-size:.8rem; color:var(--muted); }
</style>
"""


def e(x) -> str:
    return escape(str(x if x is not None else ""))


def hero(n_sections: int | None, compact: bool = False) -> str:
    if compact:   # once a conversation is going, the big headline just pushes the work down
        return ('<div class="hero compact"><div class="eyebrow">Nyay Saathi &nbsp;·&nbsp; न्याय साथी</div>'
                '<div class="small-muted">Not legal advice · Free legal aid 15100</div></div><div class="rind"></div>')
    lib = f"<div><b>{n_sections:,}</b><span>sections of law</span></div>" if n_sections else ""
    return f"""
<div class="hero">
  <div>
    <div class="eyebrow">Nyay Saathi &nbsp;·&nbsp; न्याय साथी</div>
    <div class="display">Tell me what happened.<br><em>I'll help you stand your ground.</em></div>
    <p>Speak or type in your own language. I'll put your case in order, show you where you stand
       under Indian law, draft the letters, and tell you honestly when you need a real lawyer.</p>
  </div>
  <div class="facts">{lib}<div><b>12</b><span>languages</span></div><div><b>₹0</b><span>to use</span></div></div>
</div>
<div class="rind"></div>"""


def empty(title: str, sub: str = "") -> str:
    return f'<div class="empty"><div class="serif">{e(title)}</div><div>{e(sub)}</div></div>'


FLAG_LABEL = {"refuse": "I can't help with this", "lawyer": "Talk to a lawyer", "caution": "Be careful"}


def flag(sev: str, code: str, message: str) -> str:
    cls = {"refuse": "", "lawyer": "", "caution": "caution", "ok": "ok"}.get(sev, "")
    head = FLAG_LABEL.get(sev) or code
    return f'<div class="flag {cls}"><b>{e(head)} · {e(code.replace("_", " ").lower())}</b>{e(message)}</div>'


def note(kind: str, head: str, body: str) -> str:
    return f'<div class="flag {kind}"><b>{e(head)}</b>{e(body)}</div>'


def claim_card(calc: dict) -> str:
    amt = f"₹{calc['total']:,.0f}" if calc.get("total") is not None else "—"
    lines = "".join(f"<li>{e(l)}</li>" for l in calc.get("lines", []))
    notes = "".join(f'<div class="note">{e(n)}</div>' for n in calc.get("notes", []))
    return (f'<div class="claim"><div class="label">Amount to claim</div><div class="amt">{amt}</div>'
            f'<ul>{lines}</ul>{notes}<div class="note">Worked out by code from your numbers, not by the AI.</div></div>')


def chips(items, kind: str) -> str:
    return f'<div class="chips {kind}">' + "".join(f"<span>{e(i)}</span>" for i in items) + "</div>"


def timeline(rows: list[dict]) -> str:
    out = []
    for r in rows:
        when = r.get("date") or r.get("when") or ""
        what = r.get("event") or r.get("what") or ""
        src = r.get("proof") if r.get("from") == "evidence" else ""
        src_html = f" <small>· from {e(src)}</small>" if src else ""
        out.append(f"<div><time>{e(when)}</time>{e(what)}{src_html}</div>")
    return '<div class="tl">' + "".join(out) + "</div>"


def kv(pairs: list[tuple[str, str]]) -> str:
    return '<dl class="kv">' + "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in pairs) + "</dl>"


# ---------------------------------------------------------------- companion views

def deadline_rows(items: list[dict], cite) -> str:
    """cite: function(kb_id) -> citation chip html ('' if none)."""
    if not items:
        return '<div class="small-muted">No dates yet. Tell me when things happened and I\'ll work out your deadlines.</div>'
    out = []
    for d in items:
        n = d["days_left"]
        big = f"{abs(n)}" if n else "Today"
        small = ("days ago" if n < 0 else "days left") if n else ""
        if d["kind"] == "overdue" and n < 0:
            small = "days late"
        bar = f'<div class="bar"><i style="width:{d["elapsed"] * 100:.0f}%"></i></div>' if d.get("elapsed") is not None else ""
        chip = cite(d["kb"]) if d.get("kb") else ""
        out.append(f'<div class="dl {d["status"]}"><div class="days">{big}<small>{small}</small></div><div>'
                   f'<div class="what">{e(d["label"])}: <b>{d["date"].strftime("%d %b %Y")}</b>{chip}</div>'
                   f'<div class="basis">{e(d["basis"])}</div>{bar}</div></div>')
    return "".join(out)


def routes_table(cb: dict, cite) -> str:
    rows = "".join(f'<tr><td>{e(r["route"])}{cite(r["kb"]) if r.get("kb") else ""}</td><td>{e(r["money"])}</td>'
                   f'<td>{e(r["time"])}</td><td>{e(r["lawyer"])}</td></tr>' for r in cb["routes"])
    table = (f'<table class="routes"><tr><th>Route</th><th>Cost</th><th>Time</th><th>Lawyer?</th></tr>{rows}</table>'
             if rows else "")
    return f'<div class="verdict">{e(cb["verdict"])}</div>{table}<div class="small-muted">{e(cb["note"])}</div>'


def help_cards(items: list[dict]) -> str:
    return '<div class="helps">' + "".join(
        f'<a class="help" href="{e(h["url"])}" target="_blank"><b>{e(h["name"])}</b><span>{e(h["what"])}</span>'
        f'<em>{e(h["how"])} ↗</em></a>' for h in items) + "</div>"


def ladder(stage: int, labels) -> str:
    """stage = highest rung completed (5 = resolved)."""
    return '<div class="ladder">' + "".join(
        f'<div class="{"done" if n <= stage else "now" if n == stage + 1 else ""}">{e(t)}</div>'
        for n, t in labels) + "</div>"


def next_card(nx: dict) -> str:
    return (f'<div class="next"><div class="label">Your next step</div><div class="serif">{e(nx["headline"])}</div>'
            f'<div style="font-size:.92rem">{e(nx["detail"])}</div></div>')


def log_list(events: list[dict], kinds: dict) -> str:
    if not events:
        return '<div class="small-muted">Nothing logged yet.</div>'
    return '<div class="log">' + "".join(
        f'<div><time>{e(x.get("date"))}</time>{e(kinds.get(x["kind"], x["kind"]))}'
        + (f' · Rs {float(x["amount"]):,.0f}' if x.get("amount") else "") + (f' · <i>{e(x["note"])}</i>' if x.get("note") else "")
        + "</div>" for x in sorted(events, key=lambda x: x.get("date") or "")) + "</div>"


def trace(result: dict) -> str:
    case, g, ret = result["case"], result["guardrail_report"], result.get("retrieval") or {}
    flags = result["flags"]
    steps = []
    n_pii = len(result.get("pii_mapping_keys") or [])
    steps.append(("", f"<b>Privacy.</b> <span>{n_pii} personal detail(s) masked before anything was sent to the AI model.</span>"))
    steps.append(("", f"<b>Understood your story.</b> <span>Type: {e(case.get('problem_type'))} · "
                      f"{e(case.get('problem_subtype'))} · language: {e(case.get('user_language'))}.</span>"))
    steps.append(("", "<b>Safety rules (code, not AI).</b> <span>"
                      + (", ".join(e(f["code"].replace("_", " ").lower()) for f in flags) or "nothing flagged") + ".</span>"))
    total = result["calculation"].get("total")
    steps.append(("", f"<b>Calculator (code).</b> <span>{'Rs ' + format(total, ',.0f') if total is not None else 'not enough numbers'}.</span>"))
    acts = sorted({h["act"] for h in ret.get("hits", [])})
    steps.append(("", f"<b>Searched the law.</b> <span>{len(ret.get('hits', []))} sections from "
                      f"{e(', '.join(acts) or 'curated notes only')}.</span>"))
    steps.append(("", f"<b>The AI model wrote an answer.</b> <span>{e(result.get('model'))}, allowed to cite only "
                      f"{len(result.get('kb_ids_given') or [])} checked sources.</span>"))
    removed = []
    for it in g.get("items") or []:
        for k in ("unverified_sections", "unverified_acts", "old_criminal_codes", "case_law", "bad_kb_tags"):
            removed += [f"<s>{e(x)}</s>" for x in it.get(k) or []]
    steps.append(("cut" if removed else "", "<b>Fact-checker (code).</b> <span>"
                  + (f"Removed {len(removed)}: " + ", ".join(removed) if removed else "Nothing needed removing.") + "</span>"))
    sc = g.get("support_check")
    if isinstance(sc, dict):
        un = sc.get("unsupported") or []
        steps.append(("cut" if un else "", f"<b>Citation support check.</b> <span>{sc.get('checked', 0)} checked"
                      + (f"; dropped {len(un)} that didn't match the section: " + ", ".join(e(u['id']) for u in un) if un else "; all matched")
                      + ".</span>"))
    elif sc:
        steps.append(("", f"<b>Citation support check.</b> <span>{e(sc)}.</span>"))
    steps.append(("", f"<b>Final answer.</b> <span>Cites {len(g.get('kb_cited') or [])} source(s); "
                      f"needs a lawyer: {'yes' if result['assessment'].get('needs_lawyer') else 'not yet'}.</span>"))
    return '<div class="trace">' + "".join(f'<div class="{c}">{t}</div>' for c, t in steps) + "</div>"


SPEECH_LANG = {"devanagari": "hi-IN", "tamil": "ta-IN", "bengali": "bn-IN", "telugu": "te-IN", "kannada": "kn-IN",
               "gujarati": "gu-IN", "gurmukhi": "pa-IN", "malayalam": "ml-IN", "latin": "en-IN"}


def speak_button(text: str, lang: str) -> str:
    """Read the reply aloud with the browser's own voices (free, offline-capable, nothing sent anywhere)."""
    import json as _json
    import re as _re
    clean = _re.sub(r"<[^>]+>", "", text)
    clean = _re.sub(r"[*_#`]|\[KB:[^\]]+\]", "", clean)
    return f"""
<div style="font-family:Inter,sans-serif">
<button id="b" style="border:1px solid #E6DBD0;background:#FFFDFA;color:#2A2321;border-radius:999px;padding:.35rem .9rem;
 font-size:.82rem;cursor:pointer">▶ Listen</button>
<span id="s" style="font-size:.75rem;color:#7A6E66;margin-left:.5rem"></span></div>
<script>
const t={_json.dumps(clean)}, lang={_json.dumps(lang)}, b=document.getElementById('b'), s=document.getElementById('s');
b.onclick=()=>{{
  const sy=window.speechSynthesis; if(!sy){{s.textContent='Your browser cannot read aloud.';return;}}
  if(sy.speaking){{sy.cancel(); b.textContent='▶ Listen'; return;}}
  const u=new SpeechSynthesisUtterance(t); u.lang=lang; u.rate=0.95;
  const v=sy.getVoices().find(v=>v.lang===lang)||sy.getVoices().find(v=>v.lang.startsWith(lang.slice(0,2)));
  if(v) u.voice=v; else if(lang!=='en-IN') s.textContent='No '+lang+' voice installed; using the default voice.';
  u.onend=()=>b.textContent='▶ Listen'; b.textContent='■ Stop'; sy.speak(u);
}};
</script>"""


def case_page(result: dict, dls: list[dict], events: list[dict], nx: dict | None, kinds: dict) -> str:
    """A standalone, shareable case page. Personal details stay masked (it never calls restore())."""
    case, calc, a = result["case"], result["calculation"], result["assessment"]
    import re as _re
    strip = lambda s: _re.sub(r"\s*\[KB:[^\]]+\]", "", str(s or ""))
    other = case.get("other_party") or {}
    tl = "".join(f"<tr><td>{e(t.get('date') or '?')}</td><td>{e(strip(t.get('event')))}</td><td>{e(t.get('proof') or '')}</td></tr>"
                 for t in case.get("timeline") or [])
    opts = "".join(f"<li><b>{e(strip(o.get('title')))}</b> — {e(strip(o.get('what_to_do')))}</li>" for o in a.get("options") or [])
    dl = "".join(f"<li>{e(d['label'])}: <b>{d['date'].strftime('%d %b %Y')}</b> ({d['days_left']} days)</li>" for d in dls)
    log = "".join(f"<li>{e(x.get('date'))} — {e(kinds.get(x['kind'], x['kind']))}</li>" for x in events)
    total = f"Rs {calc['total']:,.0f}" if calc.get("total") is not None else "not calculated"
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Case file · Nyay Saathi</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>body{{font-family:Inter,sans-serif;background:#FBF7F2;color:#2A2321;max-width:760px;margin:0 auto;padding:32px 20px;line-height:1.55}}
h1,h2{{font-family:Fraunces,Georgia,serif;font-weight:500}} h1{{font-size:2rem;margin:.2rem 0}} h2{{font-size:1.2rem;margin-top:1.8rem}}
.rind{{height:6px;border-radius:6px;background:linear-gradient(90deg,#1E3A2D 0 22%,#6E9A6A 22% 30%,#E4EDDC 30% 36%,#E0566C 36% 100%);margin:1rem 0}}
.eyebrow{{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:#2F5D46;font-weight:600}}
table{{width:100%;border-collapse:collapse;font-size:.9rem}} td{{border-bottom:1px solid #E6DBD0;padding:.45rem .4rem .45rem 0;vertical-align:top}}
.amt{{font-family:Fraunces,serif;font-size:2rem;color:#C8374F}} .muted{{color:#7A6E66;font-size:.82rem}}
@media print{{body{{background:#fff}}}}</style></head><body>
<div class="eyebrow">Nyay Saathi · case file</div><h1>{e(case.get('problem_subtype') or case.get('problem_type'))}</h1>
<div class="muted">Prepared {date.today().strftime('%d %b %Y')}. Personal details are masked. Not legal advice.</div><div class="rind"></div>
<p>{e(case.get('summary'))}</p>
<p class="muted">State: {e(case.get('state') or 'not given')} · Other side: {e(other.get('type') or '?')}</p>
<h2>Amount claimed</h2><div class="amt">{total}</div><ul>{''.join(f'<li>{e(l)}</li>' for l in calc.get('lines', []))}</ul>
<h2>Timeline</h2><table>{tl or '<tr><td>No dates given</td></tr>'}</table>
<h2>Deadlines</h2><ul>{dl or '<li>None worked out yet</li>'}</ul>
<h2>Options</h2><ol>{opts}</ol>
{f'<h2>What has happened so far</h2><ul>{log}</ul>' if log else ''}
{f'<h2>Next step</h2><p><b>{e(nx["headline"])}</b><br>{e(nx["detail"])}</p>' if nx else ''}
<h2>Proof</h2><p>Have: {e(', '.join(case.get('evidence_have') or []) or 'none listed')}<br>Missing: {e(', '.join(case.get('evidence_missing') or []) or 'none listed')}</p>
<div class="rind"></div><p class="muted">Made with Nyay Saathi, an AI legal-help assistant. Check every fact with a lawyer. Free legal aid: 15100 (NALSA).</p>
</body></html>"""
