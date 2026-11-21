"""Load and retrieve entries from the curated legal knowledge base (kb/*.yaml)."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import yaml

KB_DIR = Path(__file__).resolve().parent.parent / "kb"


@lru_cache(maxsize=1)
def load_kb() -> dict[str, dict]:
    entries: dict[str, dict] = {}
    for f in sorted(KB_DIR.glob("*.yaml")):
        for e in yaml.safe_load(f.read_text(encoding="utf-8")) or []:
            e.setdefault("kind", "law")
            e.setdefault("sections", [])
            e.setdefault("act_aliases", [])
            entries[e["id"]] = e
    return entries


def retrieve(problem_type: str) -> list[dict]:
    """Entries relevant to a problem type (traps excluded; they go into the prompt as rules).

    The KB is small (tens of entries), so filtering by problem type is exact and
    predictable. Swap in embedding search when it grows to hundreds.
    """
    pt = problem_type if problem_type in {"deposit", "consumer", "salary", "notice"} else "other"
    return [e for e in load_kb().values() if e["kind"] != "trap" and pt in e["problem_types"]]


def traps(problem_type: str) -> list[dict]:
    return [e for e in load_kb().values() if e["kind"] == "trap"
            and (problem_type in e["problem_types"] or "other" in e["problem_types"])]


def format_for_prompt(entries: list[dict]) -> str:
    curated = [e for e in entries if e.get("status") != "primary"]
    official = [e for e in entries if e.get("status") == "primary"]
    lines = ["--- Curated plain-language notes (checked by us) ---"]
    for e in curated:
        secs = ", ".join(e["sections"]) or "-"
        lines.append(f"[KB:{e['id']}] {e['act']} | sections: {secs} | {e['title']}\n    {e['plain'].strip()}")
    if official:
        lines.append("\n--- OFFICIAL TEXT retrieved from the Act itself (most authoritative; quote short phrases "
                     "when useful; it may not be relevant - ignore what doesn't fit the case) ---")
        for e in official:
            unit = e.get("unit", "Section")
            num = e["sections"][0] if e["sections"] else ""
            lines.append(f"[KB:{e['id']}] {e['act']}, {unit} {num} ({e['title']})\n\"\"\"{e['plain'].strip()}\"\"\"")
    return "\n".join(lines)
