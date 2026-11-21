"""Evidence locker: screenshots / exported WhatsApp chats -> dated facts -> merged timeline."""
from __future__ import annotations

import os
from datetime import date

from .core import prompt
from .llm import LLM
from .redact import redact

# Vision needs a multimodal model. Override with EVIDENCE_MODEL if the chat model can't see images.
VISION_DEFAULTS = {"groq": "gemini:gemini-3.5-flash-lite", "gemini": None, "openai": None,
                   "anthropic": None, "openrouter": None}


def vision_llm(chat_llm: LLM) -> LLM:
    spec = os.getenv("EVIDENCE_MODEL") or VISION_DEFAULTS.get(chat_llm.provider)
    return LLM(spec) if spec else chat_llm


def read_evidence(filename: str, data: bytes, llm: LLM, pii_mapping: dict, today: date | None = None) -> dict:
    today = today or date.today()
    sys = prompt("evidence", today=today.isoformat())
    name = filename.lower()
    if name.endswith((".txt", ".csv")):            # e.g. WhatsApp "Export chat" .txt
        text, _ = redact(data.decode("utf-8", errors="ignore")[-12000:], pii_mapping)
        content = f"Evidence file '{filename}' (text):\n{text}"
        msgs = [{"role": "system", "content": sys}, {"role": "user", "content": content}]
        out = llm.chat_json(msgs, tag="evidence_text")
    else:
        mime = "image/png" if name.endswith(".png") else "image/jpeg" if name.endswith((".jpg", ".jpeg")) else "image/webp"
        vlm = vision_llm(llm)
        msgs = [{"role": "system", "content": sys},
                {"role": "user", "content": [{"type": "text", "text": f"Evidence file: {filename}"},
                                             LLM.image_part(data, mime)]}]
        out = vlm.chat_json(msgs, tag="evidence_image")
    out["source"] = filename
    return out


def merge_timeline(case: dict, evidence: list[dict]) -> list[dict]:
    """Story events + evidence facts, sorted by date. Each row says where it came from."""
    rows = [{"date": e.get("date"), "event": e.get("event"), "proof": e.get("proof"), "from": "your story"}
            for e in case.get("timeline") or []]
    for ev in evidence:
        for f in ev.get("facts") or []:
            amt = f" (Rs {f['amount']:,.0f})" if isinstance(f.get("amount"), (int, float)) else ""
            rows.append({"date": f.get("date"), "event": f"{f.get('event')}{amt}", "proof": ev["source"],
                         "from": "evidence", "quote": f.get("quote")})
    return sorted(rows, key=lambda r: (r["date"] is None, str(r["date"] or "")))
