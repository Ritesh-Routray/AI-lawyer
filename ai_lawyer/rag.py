"""Retrieval over primary legal texts (BNS, BNSS, Constitution, Consumer Protection Act, Code on Wages, ...).

Pipeline
  1. chunk   - PDFs -> one chunk per Section / Article (split if long), with page number and margin title
  2. index   - BM25 (pure Python, always available) + dense embeddings (local sentence-transformers model,
               used if installed) saved to corpus/index/
  3. search  - hybrid score (reciprocal-rank fusion of BM25 + dense), optional cross-encoder rerank,
               filtered to the Acts relevant to the problem type
  4. cite    - each hit becomes a KB-style entry ("src_<act>_<section>") so the existing citation
               validator and citation receipts work unchanged: the model may cite a section only if
               we retrieved and showed it the official text of that section.
"""
from __future__ import annotations

import json
import math
import os
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
RAW, INDEX = CORPUS / "raw", CORPUS / "index"
EMBED_MODEL = os.getenv("RAG_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
RERANK_MODEL = os.getenv("RAG_RERANK_MODEL", "cross-encoder/ms-marco-MiniLM-L-6-v2")
MAX_CHARS = 2200

# "21. ...", and amended/inserted provisions printed with a footnote marker: "1[39A. ...", "*[21A. ..."
HEADING = re.compile(r"^\s*(?:\d{0,2}\*?\[)?(\d{1,3}[A-Z]{0,2})\.\s+(\S.*)$")
NOISE = re.compile(r"^\s*(THE CONSTITUTION OF INDIA|\(Part [^)]*\)|Page\s*\d+\s*of\s*\d+|\d{1,3}|AS PASSED BY.*|"
                   r"Bill No\..*|ON\s+\d\d\.\d\d\.\d{4}|THE GAZETTE OF INDIA.*|SEC\.\s*1\].*)\s*$")


def load_sources() -> list[dict]:
    return yaml.safe_load((CORPUS / "sources.yaml").read_text(encoding="utf-8"))


# ------------------------------------------------------------------ chunking
def _num_value(n: str) -> float:
    m = re.match(r"(\d+)([A-Z]*)", n)
    return int(m.group(1)) + (0.01 * (ord(m.group(2)[0]) - 64) if m.group(2) else 0)


def _pdf_lines(path: Path) -> list[tuple[int, str]]:
    import pymupdf
    doc = pymupdf.open(path)
    out = []
    for pno, page in enumerate(doc, start=1):
        for line in page.get_text().splitlines():
            line = line.replace("—", "-").replace("�", "-").strip()
            if line:
                out.append((pno, line))
    return out


def chunk_source(src: dict, files: list[Path], url_for: dict[str, str]) -> list[dict]:
    """Split an Act (or the Constitution's Parts) into section-level chunks.

    A line starting "<n>. " is treated as a new section only if n continues the running
    sequence (n in [last, last+6]); this skips the table of contents, footnotes and numbered lists.
    """
    chunks, last = [], 0.0
    for f in files:
        lines = _pdf_lines(f)
        if src["unit"] == "Section":   # skip the "arrangement of sections" table of contents
            start = next((i for i, (_, l) in enumerate(lines) if re.search(r"be it enacted", l, re.I)), 0)
            lines = lines[start:]
        if src["unit"] == "Article" and "__S" in f.stem:   # Schedules: fixed windows
            chunks += _window_chunks(src, f, lines, url_for[f.name])
            continue
        cur = None
        for i, (pno, line) in enumerate(lines):
            m = HEADING.match(line)
            if m:
                v = _num_value(m.group(1))
                if last < v <= last + 6 or (last == 0 and v <= 2):
                    if cur:
                        chunks.append(cur)
                    prev = lines[i - 1][1] if i else ""
                    title = prev if (len(prev) < 90 and not prev.endswith((".", ";", ":", ",")) and not HEADING.match(prev)) else ""
                    cur = {"source_id": src["id"], "act": src["title"], "unit": src["unit"], "number": m.group(1),
                           "title": title, "page": pno, "file": f.name, "url": url_for[f.name], "text": line}
                    last = v
                    continue
            if cur and not NOISE.match(line):
                cur["text"] += "\n" + line
        if cur:
            chunks.append(cur)
    # split overly long sections into parts (same citation number)
    out = []
    for c in chunks:
        t = c["text"]
        parts = [t[i:i + MAX_CHARS] for i in range(0, len(t), MAX_CHARS)] or [t]
        for k, p in enumerate(parts):
            out.append({**c, "text": p, "part": k + 1, "id": f"src_{c['source_id']}_{c['number']}".lower()
                        + (f"_p{k + 1}" if k else "")})
    return out


def _window_chunks(src, f, lines, url) -> list[dict]:
    sched = f.stem.split("__")[1].replace("S", "Schedule ")
    text, page0, out = "", None, []
    for pno, line in lines:
        if NOISE.match(line):
            continue
        page0 = page0 or pno
        text += line + "\n"
        if len(text) > 1500:
            out.append((page0, text))
            text, page0 = "", None
    if text.strip():
        out.append((page0 or 1, text))
    return [{"source_id": src["id"], "act": src["title"], "unit": "Schedule", "number": sched, "title": "",
             "page": p, "file": f.name, "url": url, "text": t, "part": k + 1,
             "id": f"src_{src['id']}_{sched.replace(' ', '').lower()}_p{k + 1}"} for k, (p, t) in enumerate(out)]


# ------------------------------------------------------------------ BM25
STOP = set("the a an of to and or in on for by with is are be as at that this which shall any such from it its "
           "may under has have not no if he his her their them they who whom whose was were been being than".split())


def tokens(s: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1]


class BM25:
    def __init__(self, docs: list[str], k1=1.4, b=0.75):
        self.toks = [tokens(d) for d in docs]
        self.k1, self.b = k1, b
        self.avg = sum(map(len, self.toks)) / max(len(self.toks), 1)
        df = Counter(w for t in self.toks for w in set(t))
        n = len(self.toks)
        self.idf = {w: math.log(1 + (n - c + 0.5) / (c + 0.5)) for w, c in df.items()}
        self.tf = [Counter(t) for t in self.toks]

    def scores(self, q: str) -> list[float]:
        qt = tokens(q)
        out = []
        for tf, t in zip(self.tf, self.toks):
            s, L = 0.0, len(t)
            for w in qt:
                if w in tf:
                    f = tf[w]
                    s += self.idf[w] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * L / self.avg))
            out.append(s)
        return out


# ------------------------------------------------------------------ index
def build_index(embed: bool = True) -> dict:
    manifest = json.loads((RAW / "manifest.json").read_text(encoding="utf-8"))
    url_for = {k: v["url"] for k, v in manifest.items()}
    chunks = []
    for src in load_sources():
        files = sorted([RAW / k for k, v in manifest.items() if v["source_id"] == src["id"]],
                       key=lambda p: (("__S" in p.stem), int(re.sub(r"\D", "", p.stem.split("__")[-1]) or 0)))
        files = [f for f in files if f.exists()]
        if files:
            got = chunk_source(src, files, url_for)
            print(f"{src['id']:14s} {len(files):2d} file(s) -> {len(got):4d} chunks")
            chunks += got
    INDEX.mkdir(parents=True, exist_ok=True)
    (INDEX / "chunks.json").write_text(json.dumps(chunks, ensure_ascii=False), encoding="utf-8")
    info = {"chunks": len(chunks), "embed_model": None}
    if embed:
        try:
            import numpy as np
            model = _embedder()
            vecs = model.encode([_embed_text(c) for c in chunks], batch_size=64, normalize_embeddings=True,
                                show_progress_bar=True)
            np.save(INDEX / "embeddings.npy", vecs.astype("float32"))
            info["embed_model"] = EMBED_MODEL
        except Exception as e:  # sentence-transformers missing or model not available offline
            print(f"dense embeddings skipped ({e}); BM25 only")
    (INDEX / "info.json").write_text(json.dumps(info), encoding="utf-8")
    return info


def _embed_text(c: dict) -> str:
    return f"{c['act']} {c['unit']} {c['number']}. {c['title']}\n{c['text'][:1200]}"


def _prep_ml_imports():
    """Text models only: skip TensorFlow, and a torchvision build that doesn't match torch
    (common on Windows) must not break `transformers` imports."""
    import sys
    os.environ.setdefault("USE_TF", "0")
    os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
    try:
        import torchvision  # noqa: F401
    except Exception:
        sys.modules["torchvision"] = None


@lru_cache(maxsize=1)
def _embedder():
    _prep_ml_imports()
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(EMBED_MODEL)


@lru_cache(maxsize=1)
def _reranker():
    _prep_ml_imports()
    from sentence_transformers import CrossEncoder
    return CrossEncoder(RERANK_MODEL)


class Retriever:
    def __init__(self):
        self.chunks = json.loads((INDEX / "chunks.json").read_text(encoding="utf-8"))
        self.bm25 = BM25([f"{c['act']} {c['title']} {c['text']}" for c in self.chunks])
        self.vecs = None
        info = json.loads((INDEX / "info.json").read_text(encoding="utf-8"))
        if info.get("embed_model") and (INDEX / "embeddings.npy").exists() and os.getenv("RAG_DENSE", "1") == "1":
            try:
                import numpy as np
                self.vecs = np.load(INDEX / "embeddings.npy")
                _embedder()                       # fail early if the model can't load
            except Exception:
                self.vecs = None
        self.sources = {s["id"]: s for s in load_sources()}

    @property
    def mode(self) -> str:
        return "hybrid (BM25 + dense)" if self.vecs is not None else "BM25"

    def search(self, query: str, problem_type: str | None = None, k: int = 6, pool: int = 40,
               rerank: bool = True) -> list[dict]:
        allowed = {sid for sid, s in self.sources.items()
                   if problem_type is None or problem_type in s.get("problem_types", [])}
        idx = [i for i, c in enumerate(self.chunks) if c["source_id"] in allowed]
        if not idx:
            return []
        bm = self.bm25.scores(query)
        ranked_bm = sorted(idx, key=lambda i: -bm[i])[:pool]
        fused = Counter({i: 1 / (60 + r) for r, i in enumerate(ranked_bm)})
        if self.vecs is not None:
            import numpy as np
            q = _embedder().encode([query], normalize_embeddings=True)[0]
            sims = self.vecs[idx] @ q
            for r, j in enumerate(np.argsort(-sims)[:pool]):
                fused[idx[j]] += 1 / (60 + r)
        cand = [i for i, _ in fused.most_common(pool)]
        if rerank and os.getenv("RAG_RERANK", "1") == "1":
            try:
                scores = _reranker().predict([(query, _embed_text(self.chunks[i])) for i in cand])
                cand = [i for _, i in sorted(zip(scores, cand), key=lambda x: -x[0])]
            except Exception:
                pass
        out, seen = [], set()
        for i in cand:
            c = self.chunks[i]
            key = (c["source_id"], c["number"])
            if key in seen:          # one chunk per section is enough
                continue
            seen.add(key)
            out.append(c)
            if len(out) >= k:
                break
        return out


@lru_cache(maxsize=1)
def get_retriever() -> Retriever | None:
    if not (INDEX / "chunks.json").exists():
        return None
    return Retriever()


def as_kb_entries(hits: list[dict], sources: dict | None = None) -> list[dict]:
    """Turn retrieved chunks into KB-style entries the validator and citation receipts understand."""
    sources = sources or {s["id"]: s for s in load_sources()}
    out = []
    for h in hits:
        s = sources.get(h["source_id"], {})
        out.append({
            "id": h["id"], "kind": "law", "problem_types": s.get("problem_types", []),
            "act": h["act"], "act_aliases": s.get("aliases", []),
            "sections": [h["number"]] if h["unit"] != "Schedule" else [],
            "unit": h["unit"],
            "title": h["title"] or f"{h['unit']} {h['number']}",
            "plain": h["text"][:900],
            "source_url": f"{h['url']}#page={h['page']}",
            "status": "primary", "checked_on": f"official text, p.{h['page']}",
        })
    return out
