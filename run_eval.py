"""Run every test case on one or more models; save RAW outputs + metrics + a model leaderboard.

    python run_eval.py --models groq:openai/gpt-oss-120b,gemini:gemini-3.5-flash-lite
    python run_eval.py --cases dep01,con01            # subset
    python run_eval.py --story "my landlord..."       # one-off new input (interview mode)
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

import yaml

from ai_lawyer import docs, escalation
from ai_lawyer.core import analyze, script_of
from ai_lawyer.llm import DEFAULT_MODEL, LLM

ROOT = Path(__file__).parent
OUT = ROOT / "outputs"
TODAY = date(2026, 11, 20)  # fixed so runs are reproducible

# USD per 1M tokens (input, output), for the cost column. 0 = free tier. Edit as prices change.
PRICES = {"groq:openai/gpt-oss-120b": (0.15, 0.60), "groq:qwen/qwen3.8-27b": (0.29, 0.59), "gemini:gemini-3.5-flash-lite": (0.10, 0.40),
          "openai:gpt-4.1-mini": (0.40, 1.60)}
USD_INR = 88


def score(case_def: dict, res: dict) -> dict:
    exp, case, a = case_def["expected"], res["case"], res["assessment"]
    sev = escalation.top_severity(res["flags"])
    escalated = bool(a.get("needs_lawyer")) or sev in ("lawyer", "refuse")
    m = {
        "type_ok": exp["problem_type"] == "any" or case.get("problem_type") == exp["problem_type"],
        "escalate_expected": exp["escalate"], "escalated": escalated,
        "escalate_ok": escalated == exp["escalate"],
        "refuse_ok": (sev == "refuse") == bool(exp.get("refuse", False)),
        "lang_ok": script_of(a.get("reply", "")) == exp["script"],
        "invented_refs_removed": res["guardrail_report"].get("removed_count", 0),
        "kb_citations": len(res["guardrail_report"].get("kb_cited", [])),
        "rag_hits": len((res.get("retrieval") or {}).get("hits", [])),
        "official_text_citations": sum(1 for i in res["guardrail_report"].get("kb_cited", []) if i.startswith("src_")),
        "unsupported_citations_dropped": len((res["guardrail_report"].get("support_check") or {}).get("unsupported", []))
        if isinstance(res["guardrail_report"].get("support_check"), dict) else 0,
    }
    want = exp.get("amounts") or {}
    got = case.get("amounts") or {}
    hits = sum(1 for k, v in want.items() if _close(got.get(k), v))
    m["amounts_ok"] = f"{hits}/{len(want)}" if want else "-"
    m["amounts_frac"] = hits / len(want) if want else None
    return m


def _close(a, b) -> bool:
    try:
        return abs(float(a) - float(b)) < 1
    except (TypeError, ValueError):
        return False


def slug(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", s).strip("_")


def run_model(spec: str, cases: list[dict]) -> list[dict]:
    llm = LLM(spec)
    mdir = OUT / slug(spec)
    mdir.mkdir(parents=True, exist_ok=True)
    rows = []
    for c in cases:
        print(f"[{spec}] {c['id']} ...", flush=True)
        before = (llm.usage.prompt_tokens, llm.usage.completion_tokens)
        t0 = time.time()
        try:
            res = analyze(c["story"].strip(), llm, today=TODAY)
            if c.get("draft") and escalation.top_severity(res["flags"]) != "refuse":
                res["draft"] = docs.draft(res["case"], res["calculation"], c["draft"], llm, res.get("_rag_entries"))
            err = None
        except Exception as e:  # keep going; record the failure honestly
            res, err = None, f"{type(e).__name__}: {e}"
        secs = time.time() - t0
        pt, ct = llm.usage.prompt_tokens - before[0], llm.usage.completion_tokens - before[1]
        row = {"model": spec, "case": c["id"], "secs": round(secs, 1), "prompt_tokens": pt, "completion_tokens": ct,
               "error": err}
        if res:
            res.pop("_pii_mapping", None)
            res.pop("_rag_entries", None)
            row.update(score(c, res))
            if res.get("draft"):
                row["invented_refs_removed"] += res["draft"]["guardrail_report"].get("removed_count", 0)
            (mdir / f"{c['id']}.json").write_text(json.dumps({"input": c, "output": res, "metrics": row},
                                                             ensure_ascii=False, indent=2), encoding="utf-8")
            (mdir / f"{c['id']}.md").write_text(render_md(c, res), encoding="utf-8")
        else:
            (mdir / f"{c['id']}.error.txt").write_text(err, encoding="utf-8")
        rows.append(row)
    return rows


def render_md(c: dict, res: dict) -> str:
    a, case = res["assessment"], res["case"]
    out = [f"# {c['id']}  ({res['model']})", "## Input", c["story"].strip(), "## Reply shown to user", a.get("reply", ""),
           "## Red flags (rule engine)", *(f"- **{f['code']}** ({f['severity']}): {f['message']}" for f in res["flags"]),
           "## Case file", "```json", json.dumps(case, ensure_ascii=False, indent=1), "```",
           "## Calculation (code)", *(f"- {l}" for l in res["calculation"]["lines"]),
           "## Retrieved official text (" + str((res.get("retrieval") or {}).get("mode")) + ")",
           *(f"- {h['act']} {h['unit']} {h['number']} {('(' + h['title'] + ')') if h['title'] else ''} p.{h['page']}"
             for h in (res.get("retrieval") or {}).get("hits", [])),
           "## Where you stand", a.get("where_you_stand", ""), "## Options"]
    for o in a.get("options") or []:
        out.append(f"{o.get('step')}. **{o.get('title')}** ({o.get('time')}, {o.get('cost')}): {o.get('what_to_do')}")
    out += ["## What I don't know", *(f"- {x}" for x in a.get("what_i_dont_know") or []),
            f"## Needs lawyer: {a.get('needs_lawyer')} - {a.get('needs_lawyer_reason', '')}",
            "## Guardrail report", "```json", json.dumps(res["guardrail_report"], ensure_ascii=False, indent=1), "```"]
    if res.get("draft"):
        d = res["draft"]["draft"]
        out += [f"## Draft: {d.get('title')}", "```", d.get("body", ""), "```",
                "Explanation for user: " + d.get("explain_in_user_language", ""),
                "Draft guardrail: " + json.dumps(res["draft"]["guardrail_report"], ensure_ascii=False)]
    return "\n\n".join(out)


def leaderboard(rows: list[dict]) -> list[dict]:
    board = []
    for spec in dict.fromkeys(r["model"] for r in rows):
        rs = [r for r in rows if r["model"] == spec]
        ok = [r for r in rs if not r["error"]]
        n = len(ok) or 1
        pin, pout = PRICES.get(spec, (0, 0))
        tok_in = sum(r["prompt_tokens"] for r in rs) / max(len(rs), 1)
        tok_out = sum(r["completion_tokens"] for r in rs) / max(len(rs), 1)
        amt = [r["amounts_frac"] for r in ok if r.get("amounts_frac") is not None]
        board.append({
            "model": spec, "cases_run": f"{len(ok)}/{len(rs)}",
            "type_accuracy": f"{sum(r['type_ok'] for r in ok) / n:.0%}",
            "escalation_accuracy": f"{sum(r['escalate_ok'] for r in ok) / n:.0%}",
            "escalation_recall": _recall(ok),
            "refusal_correct": f"{sum(r['refuse_ok'] for r in ok) / n:.0%}",
            "reply_language_match": f"{sum(r['lang_ok'] for r in ok) / n:.0%}",
            "amount_extraction": f"{sum(amt) / len(amt):.0%}" if amt else "-",
            "invented_refs_caught": sum(r["invented_refs_removed"] for r in ok),
            "cases_with_invented_refs": sum(1 for r in ok if r["invented_refs_removed"]),
            "cases_citing_official_text": sum(1 for r in ok if (r.get("official_text_citations") or 0) > 0),
            "unsupported_citations_dropped": sum(int(r.get("unsupported_citations_dropped") or 0) for r in ok),
            "avg_secs": round(sum(r["secs"] for r in rs) / max(len(rs), 1), 1),
            "avg_tokens": int(tok_in + tok_out),
            "inr_per_case_paid_tier": round((tok_in * pin + tok_out * pout) / 1e6 * USD_INR, 2),
        })
    return board


def _recall(rows):
    pos = [r for r in rows if r["escalate_expected"]]
    return f"{sum(r['escalated'] for r in pos) / len(pos):.0%}" if pos else "-"


def _typed(r: dict) -> dict:
    out = {}
    for k, v in r.items():
        if v in ("True", "False"):
            out[k] = v == "True"
        elif v == "":
            out[k] = None
        else:
            try:
                out[k] = float(v) if "." in v else int(v)
            except ValueError:
                out[k] = v
    return out


def write_csv(path: Path, rows: list[dict]):
    if not rows:
        return
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default=DEFAULT_MODEL)
    ap.add_argument("--cases", default="", help="comma-separated id prefixes")
    ap.add_argument("--story", default="", help="run a single new story and print the result")
    args = ap.parse_args()

    if args.story:
        res = analyze(args.story, LLM(args.models.split(",")[0]))
        res.pop("_pii_mapping", None)
        res.pop("_rag_entries", None)
        print(render_md({"id": "adhoc", "story": args.story}, res))
        return

    cases = yaml.safe_load((ROOT / "tests/cases/cases.yaml").read_text(encoding="utf-8"))
    if args.cases:
        pre = args.cases.split(",")
        cases = [c for c in cases if any(c["id"].startswith(p) for p in pre)]
    OUT.mkdir(exist_ok=True)
    for spec in args.models.split(","):
        try:
            rows = run_model(spec.strip(), cases)
            mfile = OUT / slug(spec.strip()) / "metrics.csv"
            if args.cases and mfile.exists():   # partial rerun: replace only the rerun cases
                with mfile.open(encoding="utf-8") as fh:
                    old = [_typed(r) for r in csv.DictReader(fh)]
                new_ids = {r["case"] for r in rows}
                rows = [r if r["case"] not in new_ids else next(n for n in rows if n["case"] == r["case"]) for r in old] \
                    + [r for r in rows if r["case"] not in {o["case"] for o in old}]
            write_csv(mfile, rows)
        except Exception as e:
            print(f"!! {spec}: {e}", file=sys.stderr)
    # leaderboard over every model run so far (lets models run in separate processes)
    all_rows = []
    for f in sorted(OUT.glob("*/metrics.csv")):
        with f.open(encoding="utf-8") as fh:
            all_rows += [_typed(r) for r in csv.DictReader(fh)]
    write_csv(OUT / "metrics.csv", all_rows)
    board = leaderboard(all_rows)
    write_csv(OUT / "leaderboard.csv", board)
    for b in board:
        print(json.dumps(b))


if __name__ == "__main__":
    main()
