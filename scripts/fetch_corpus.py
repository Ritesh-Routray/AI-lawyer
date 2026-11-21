"""Download the primary legal texts listed in corpus/sources.yaml into corpus/raw/.

Writes corpus/raw/manifest.json with URL, size, SHA-256 and download date for every file,
so anyone can check that the text we retrieve from is the text the government published.

    python scripts/fetch_corpus.py            # download missing files
    python scripts/fetch_corpus.py --force    # re-download everything
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import date
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "corpus" / "raw"
H = {"User-Agent": "Mozilla/5.0 (legal-help research prototype)"}


def files_for(src: dict) -> list[tuple[str, str]]:
    if "urls" in src:
        return [(f"{src['id']}{'' if i == 0 else f'_{i}'}.pdf", u) for i, u in enumerate(src["urls"])]
    return [(f"{src['id']}__{n}.pdf", src["urls_pattern"].format(name=n)) for n in src["names"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    sources = yaml.safe_load((ROOT / "corpus" / "sources.yaml").read_text(encoding="utf-8"))
    mpath = RAW / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {}
    for src in sources:
        for fname, url in files_for(src):
            out = RAW / fname
            if out.exists() and not args.force:
                continue
            for attempt in range(3):
                try:
                    r = requests.get(url, headers=H, timeout=(20, 180))
                    r.raise_for_status()
                    if not r.content.startswith(b"%PDF"):
                        raise ValueError(f"not a PDF (content-type {r.headers.get('content-type')})")
                    out.write_bytes(r.content)
                    manifest[fname] = {"source_id": src["id"], "url": url, "bytes": len(r.content),
                                       "sha256": hashlib.sha256(r.content).hexdigest(),
                                       "downloaded": date.today().isoformat()}
                    print(f"ok   {fname:28s} {len(r.content) / 1e6:6.2f} MB")
                    break
                except Exception as e:
                    print(f"fail {fname} (attempt {attempt + 1}): {e}", file=sys.stderr)
                    time.sleep(3)
    mpath.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print(f"{len(manifest)} files in manifest")


if __name__ == "__main__":
    main()
