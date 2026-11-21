"""Practice mode: the AI plays the other side; then scores the user's arguments."""
from __future__ import annotations

from .core import prompt
from .llm import LLM

OPPONENTS = {
    "deposit": ("the landlord", "'the walls need painting', 'you broke the geyser', 'you didn't give one month notice', "
                "'I'll pay when the new tenant comes', 'agreement says deposit is non-refundable'"),
    "consumer": ("the company's customer-care agent", "'refund is under process, wait 7-10 days', 'policy doesn't allow refunds', "
                 "'please raise a new ticket', 'the product was used/damaged by you', 'seller is responsible, not us'"),
    "salary": ("your employer / HR manager", "'company is facing cash crunch', 'you didn't serve notice period', "
               "'full and final takes 45-90 days', 'you have to return the laptop first', 'your performance was poor'"),
}


def opponent(case: dict) -> tuple[str, str]:
    return OPPONENTS.get(case.get("problem_type"), ("the other party", "'that's not my problem', 'wait for some time'"))


def reply(case: dict, history: list[dict], llm: LLM) -> str:
    who, defences = opponent(case)
    sys = prompt("roleplay", opponent=who, summary=case.get("summary", ""), defences=defences,
                 language=case.get("user_language") or "English")
    return llm.chat([{"role": "system", "content": sys}, *history], temperature=0.7, tag="roleplay", max_tokens=200)


def feedback(case: dict, history: list[dict], llm: LLM) -> dict:
    who, _ = opponent(case)
    transcript = "\n".join(f"{'PERSON' if m['role'] == 'user' else 'OTHER SIDE'}: {m['content']}" for m in history)
    sys = prompt("roleplay_feedback", opponent=who, summary=case.get("summary", ""), transcript=transcript,
                 language=case.get("user_language") or "English")
    return llm.chat_json([{"role": "system", "content": sys}, {"role": "user", "content": "Score it."}], tag="roleplay_feedback")
