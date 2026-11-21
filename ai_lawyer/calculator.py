"""Claim amounts are computed in code, never by the LLM. The LLM only extracts the inputs."""
from __future__ import annotations


def _num(x) -> float | None:
    try:
        return float(x) if x not in (None, "") else None
    except (TypeError, ValueError):
        return None


def rs(x: float) -> str:
    return f"Rs {x:,.0f}"


def compute(case: dict) -> dict:
    a = case.get("amounts") or {}
    pt = case.get("problem_type")
    lines, notes, total = [], [], None

    if pt == "deposit":
        dep, ded, rent = _num(a.get("deposit_paid")), _num(a.get("deductions_claimed")), _num(a.get("monthly_rent"))
        if dep is not None:
            total = dep
            lines.append(f"Deposit paid: {rs(dep)}")
            if ded:
                lines.append(f"Less deductions the landlord claims: - {rs(ded)}")
                total = dep - ded
                notes.append("Deductions are only valid for unpaid rent/bills or damage beyond normal wear "
                             "and tear. Ask the landlord for bills/photos for each deduction; if they can't "
                             f"show any, claim the full {rs(dep)}.")
            lines.append(f"Amount to claim: {rs(total)}")
            if rent and dep > 2 * rent:
                notes.append(f"Your deposit ({rs(dep)}) is more than 2 months' rent ({rs(2 * rent)}). The Model "
                             "Tenancy Act caps it at 2 months, but only in states that adopted it.")
    elif pt == "salary":
        sal, months, other = _num(a.get("monthly_salary")), _num(a.get("months_unpaid")), _num(a.get("other_dues"))
        if sal is not None and months:
            total = sal * months
            lines.append(f"Monthly salary {rs(sal)} x {months:g} unpaid month(s) = {rs(total)}")
        if other:
            total = (total or 0) + other
            lines.append(f"Other dues (leave encashment, reimbursements, etc.): {rs(other)}")
        if total is not None:
            lines.append(f"Amount to claim: {rs(total)}")
            notes.append("Check your offer letter/payslips for the exact gross vs in-hand salary. Gratuity, if "
                         "any, has separate rules - ask a lawyer.")
    elif pt == "consumer":
        paid, refunded = _num(a.get("order_value")), _num(a.get("amount_refunded"))
        if paid is not None:
            total = paid - (refunded or 0)
            lines.append(f"Amount paid: {rs(paid)}")
            if refunded:
                lines.append(f"Already refunded: - {rs(refunded)}")
            lines.append(f"Refund due: {rs(total)}")
            notes.append("A Consumer Commission can also award compensation and litigation costs - we don't "
                         "estimate that figure; it depends on the case.")

    if total is None:
        notes.append("Not enough numbers to calculate. Tell me the amounts involved.")
    notes.append("Interest on delayed money may be claimable; the rate is for a lawyer/court to decide, so we "
                 "don't add it here.")
    return {"lines": lines, "total": total, "notes": notes}
