"""Chunk the downloaded legal PDFs and build the retrieval index.

    python scripts/fetch_corpus.py   # 1. download (once)
    python scripts/build_index.py    # 2. chunk + index  (add --no-embed for BM25 only)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ai_lawyer import rag  # noqa: E402

if __name__ == "__main__":
    print(rag.build_index(embed="--no-embed" not in sys.argv))
