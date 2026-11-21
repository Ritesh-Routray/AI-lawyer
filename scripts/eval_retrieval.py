"""Retrieval benchmark (no LLM): hit@1 / hit@3 / hit@5 / MRR for BM25-only vs hybrid vs hybrid+rerank.

    python scripts/eval_retrieval.py      -> prints a table, writes outputs/retrieval_eval.csv
"""
import csv
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import yaml  # noqa: E402

from ai_lawyer import rag  # noqa: E402

cases = yaml.safe_load((ROOT / "tests" / "retrieval_cases.yaml").read_text(encoding="utf-8"))
r = rag.get_retriever()
dense_vecs = r.vecs
configs = {"bm25": dict(dense=False, rerank=False), "hybrid": dict(dense=True, rerank=False),
           "hybrid+rerank": dict(dense=True, rerank=True)}
rows, per_case = [], []
for name, cfg in configs.items():
    if cfg["dense"] and dense_vecs is None:
        continue
    r.vecs = dense_vecs if cfg["dense"] else None
    h1 = h3 = h5 = mrr = 0
    for c in cases:
        hits = r.search(c["q"], c["pt"], k=5, rerank=cfg["rerank"])
        got = [f"{h['source_id']}:{h['number']}" for h in hits]
        rank = next((i + 1 for i, g in enumerate(got) if g in c["expected"]), None)
        h1 += rank == 1
        h3 += bool(rank and rank <= 3)
        h5 += bool(rank)
        mrr += 1 / rank if rank else 0
        per_case.append({"config": name, "query": c["q"], "expected": "|".join(c["expected"]), "rank": rank or "-",
                         "top5": " ".join(got)})
    n = len(cases)
    rows.append({"config": name, "queries": n, "hit@1": f"{h1 / n:.0%}", "hit@3": f"{h3 / n:.0%}",
                 "hit@5": f"{h5 / n:.0%}", "MRR": f"{mrr / n:.2f}"})

for row in rows:
    print(row)
out = ROOT / "outputs" / "retrieval_eval.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
with (ROOT / "outputs" / "retrieval_eval_cases.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(per_case[0]))
    w.writeheader()
    w.writerows(per_case)
