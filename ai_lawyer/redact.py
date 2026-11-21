"""Mask personal identifiers before any text leaves the machine for an LLM API.

The mapping stays local, so final documents (notice, case brief) can put the real
values back. Order matters: more specific patterns run first.
"""
from __future__ import annotations

import re

PATTERNS: list[tuple[str, re.Pattern]] = [
    ("EMAIL", re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")),
    ("UPI", re.compile(r"\b[\w.-]{2,}@(?:ok\w+|ybl|paytm|upi|ibl|axl|apl|icici|sbi|hdfcbank|axisbank)\b", re.I)),
    ("AADHAAR", re.compile(r"\b[2-9]\d{3}[\s-]?\d{4}[\s-]?\d{4}\b")),
    ("PAN", re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b")),
    ("IFSC", re.compile(r"\b[A-Z]{4}0[A-Z0-9]{6}\b")),
    ("PHONE", re.compile(r"(?<!\d)(?:\+91[\s-]?|0)?[6-9]\d{4}[\s-]?\d{5}(?!\d)")),
    ("ACCOUNT", re.compile(r"(?<![\d,.])\d{9,18}(?![\d,.])")),
]


def redact(text: str, mapping: dict[str, str] | None = None) -> tuple[str, dict[str, str]]:
    mapping = dict(mapping or {})
    reverse = {v: k for k, v in mapping.items()}
    for label, pat in PATTERNS:
        def _sub(m: re.Match) -> str:
            val = m.group(0)
            if val in reverse:
                return reverse[val]
            n = sum(1 for k in mapping if k.startswith(f"[{label}_")) + 1
            token = f"[{label}_{n}]"
            mapping[token] = val
            reverse[val] = token
            return token
        text = pat.sub(_sub, text)
    return text, mapping


def restore(text: str, mapping: dict[str, str]) -> str:
    for token, val in mapping.items():
        text = text.replace(token, val)
    # tokens the model made up as placeholders (no real value behind them) -> readable blanks
    nice = {"PHONE": "[your phone]", "EMAIL": "[your email]", "UPI": "[your UPI ID]", "AADHAAR": "[Aadhaar]",
            "PAN": "[PAN]", "IFSC": "[IFSC]", "ACCOUNT": "[bank account no.]"}
    return re.sub(r"\[(PHONE|EMAIL|UPI|AADHAAR|PAN|IFSC|ACCOUNT)_\d+\]", lambda m: nice[m.group(1)], text)
