"""Model-agnostic LLM adapter.

Every provider below speaks the OpenAI chat-completions format, so one client
covers all of them. Swap the model with a single string, e.g.

    MODEL="groq:openai/gpt-oss-120b"
    MODEL="gemini:gemini-3.5-flash-lite"
    MODEL="openai:gpt-4.1-mini"
    MODEL="anthropic:claude-sonnet-5-5"
    MODEL="ollama:llama3.1"
    MODEL="custom:<model>"   # + CUSTOM_BASE_URL / CUSTOM_API_KEY (e.g. an API Kuku provides)
"""
from __future__ import annotations

import base64
import json
import os
import re
import time
from dataclasses import dataclass, field

from openai import OpenAI


def _load_dotenv():
    """Minimal .env loader (no extra dependency). Real env vars win."""
    from pathlib import Path
    f = Path(__file__).resolve().parent.parent / ".env"
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                if v.strip() and not os.getenv(k.strip()):
                    os.environ[k.strip()] = v.strip()


_load_dotenv()

PROVIDERS = {
    "groq": {"base_url": "https://api.groq.com/openai/v1", "key": "GROQ_API_KEY",
             "stt_model": "whisper-large-v3"},
    "gemini": {"base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "key": "GEMINI_API_KEY",
               "stt_model": None},
    "openai": {"base_url": None, "key": "OPENAI_API_KEY", "stt_model": "whisper-1"},
    "anthropic": {"base_url": "https://api.anthropic.com/v1/", "key": "ANTHROPIC_API_KEY", "stt_model": None},
    "openrouter": {"base_url": "https://openrouter.ai/api/v1", "key": "OPENROUTER_API_KEY", "stt_model": None},
    "ollama": {"base_url": "http://localhost:11434/v1", "key": None, "stt_model": None},
    "custom": {"base_url": os.getenv("CUSTOM_BASE_URL"), "key": "CUSTOM_API_KEY", "stt_model": None},
}

DEFAULT_MODEL = os.getenv("MODEL", "gemini:gemini-3.5-flash-lite")


@dataclass
class Usage:
    calls: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    seconds: float = 0.0
    log: list = field(default_factory=list)

    def add(self, resp, secs: float, tag: str):
        self.calls += 1
        self.seconds += secs
        u = getattr(resp, "usage", None)
        if u:
            self.prompt_tokens += u.prompt_tokens or 0
            self.completion_tokens += u.completion_tokens or 0
        self.log.append({"step": tag, "secs": round(secs, 2)})


class LLM:
    def __init__(self, model: str | None = None):
        spec = model or DEFAULT_MODEL
        if ":" not in spec:
            raise ValueError(f"Model must look like 'provider:model', got {spec!r}")
        self.provider, self.model = spec.split(":", 1)
        if self.provider not in PROVIDERS:
            raise ValueError(f"Unknown provider {self.provider!r}. Options: {list(PROVIDERS)}")
        cfg = PROVIDERS[self.provider]
        key = os.getenv(cfg["key"]) if cfg["key"] else "ollama"
        if not key:
            raise RuntimeError(f"Set {cfg['key']} to use provider '{self.provider}'.")
        base_url = cfg["base_url"] if self.provider != "custom" else os.getenv("CUSTOM_BASE_URL")
        self.client = OpenAI(api_key=key, base_url=base_url, max_retries=3, timeout=120)
        self.spec = spec
        self.usage = Usage()

    # ---- text ---------------------------------------------------------
    def chat(self, messages: list[dict], temperature: float = 0.2, tag: str = "chat", max_tokens: int = 2500) -> str:
        t0 = time.time()
        resp = self._create(messages=messages, temperature=temperature, max_tokens=max_tokens)
        self.usage.add(resp, time.time() - t0, tag)
        return resp.choices[0].message.content or ""

    def chat_json(self, messages: list[dict], temperature: float = 0.1, tag: str = "json", max_tokens: int = 3000) -> dict:
        """Ask for JSON; tolerate providers that ignore response_format."""
        t0 = time.time()
        try:
            resp = self._create(messages=messages, temperature=temperature, max_tokens=max_tokens,
                                response_format={"type": "json_object"})
        except Exception:  # provider without JSON mode
            resp = self._create(messages=messages, temperature=temperature, max_tokens=max_tokens)
        self.usage.add(resp, time.time() - t0, tag)
        text = resp.choices[0].message.content or ""
        try:
            return parse_json(text)
        except json.JSONDecodeError as e:  # one repair attempt: show the model its broken output
            t0 = time.time()
            fix = messages + [{"role": "assistant", "content": text[-6000:]},
                              {"role": "user", "content": f"That was not valid JSON ({e}). Return the complete "
                                                          "answer again as ONE valid JSON object only."}]
            resp = self._create(messages=fix, temperature=0, max_tokens=max_tokens)
            self.usage.add(resp, time.time() - t0, tag + ":json_repair")
            return parse_json(resp.choices[0].message.content or "")

    def _create(self, **kw):
        # Reasoning models think before answering; extraction/drafting doesn't need deep thought.
        effort = os.getenv("REASONING_EFFORT", "low")
        if effort and (self.provider == "gemini" or "gpt-oss" in self.model) and "reasoning_effort" not in kw:
            kw["reasoning_effort"] = effort
        cap = int(os.getenv("MAX_OUTPUT_TOKENS", "0") or 0)   # some free tiers cap output tokens/minute
        if cap and kw.get("max_tokens", 0) > cap:
            kw["max_tokens"] = cap
        for attempt in range(4):
            try:
                return self.client.chat.completions.create(model=self.model, **kw)
            except Exception as e:  # free tiers rate-limit often: back off and retry
                msg = str(e).lower()
                if "request too large" in msg:   # exceeds the free tier's per-request token cap: retrying won't help
                    raise
                if any(s in msg for s in ("rate", "429", "quota", "connection", "timed out", "503", "502")) and attempt < 3:
                    time.sleep(8 * (attempt + 1))
                    continue
                raise

    # ---- vision -------------------------------------------------------
    @staticmethod
    def image_part(data: bytes, mime: str = "image/png") -> dict:
        b64 = base64.b64encode(data).decode()
        return {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}}

    # ---- speech-to-text ----------------------------------------------
    def transcribe(self, audio: bytes, filename: str = "audio.wav") -> str:
        """Use this provider's Whisper if it has one, else any configured one."""
        order = [self.provider] + [p for p in ("groq", "openai") if p != self.provider]
        for p in order:
            cfg = PROVIDERS[p]
            if cfg["stt_model"] and cfg["key"] and os.getenv(cfg["key"]):
                client = OpenAI(api_key=os.getenv(cfg["key"]), base_url=cfg["base_url"])
                r = client.audio.transcriptions.create(model=cfg["stt_model"], file=(filename, audio))
                return r.text
        raise RuntimeError("Voice needs GROQ_API_KEY (free) or OPENAI_API_KEY for Whisper.")


def parse_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.M).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, flags=re.S)
        if m:
            return json.loads(m.group(0))
        raise
