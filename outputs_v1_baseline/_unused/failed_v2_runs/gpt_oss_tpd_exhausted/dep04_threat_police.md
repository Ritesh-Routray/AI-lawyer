# dep04_threat_police  (groq:openai/gpt-oss-120b)

## Input

Landlord in Noida is refusing to return my 40000 deposit and when I went to ask, his son pushed me and threatened to beat me up if I come again. Should I go to the police? I also want my money.

## Reply shown to user

You have a clear right to get back the Rs 40,000 you paid as security deposit, and the threat by the landlord’s son adds a criminal angle. Since you lack a written agreement or receipt, start by gathering any proof of payment (bank statement, WhatsApp confirmation) and send a short written demand to the landlord asking for the money back within 7 days. At the same time, because you were threatened and pushed, you should file a police complaint and obtain an FIR. After that, if the landlord still does not pay, you can file a civil money recovery suit in the Small Causes Court of Noida. Would you like a template for the written demand or guidance on filing the police FIR?

## Red flags (rule engine)

- **CRIMINAL** (lawyer): This involves police or possible criminal matters. Talk to a lawyer before you act or say anything.

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit not returned",
 "user_language": "English",
 "state": "Uttar Pradesh",
 "city": "Noida",
 "summary": "The tenant paid a security deposit of 40000 rupees to a landlord in Noida. The landlord is refusing to return the deposit, and the landlord's son threatened and pushed the tenant when they asked for it.",
 "user_goal": "Recover the 40000 rupee deposit and consider police action for the threat",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": null,
   "event": "Paid security deposit of 40000 rupees to landlord",
   "proof": null
  },
  {
   "date": null,
   "event": "Asked for deposit return; landlord's son threatened and pushed the tenant",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": 40000,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": null,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [],
 "evidence_missing": [
  "rent agreement",
  "deposit receipt or bank transfer proof",
  "any written communication with landlord about deposit"
 ],
 "risk_signals": [
  "threat of violence",
  "physical assault"
 ],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "When did you pay the 40000 rupee deposit?",
  "Do you have a written rent agreement or any receipt for the deposit?",
  "Did you receive any written communication (SMS/email) from the landlord regarding the deposit?",
  "Are there any witnesses who saw the son threaten or push you?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 40,000

- Amount to claim: Rs 40,000

## Where you stand

You paid a Rs 40,000 security deposit to your landlord in Noida and now the landlord is refusing to return it. You have no written agreement or receipt, and the landlord's son threatened and pushed you when you asked for the money. Without a written contract, proving the deposit amount and the terms of return will be harder, but the fact that you paid money and were threatened gives you a reasonable claim for the full deposit under contract principles [KB:ica_s73]. The threat of violence also means you should involve the police before taking any further step.

## Options

1. **Send a polite written demand** (1‑2 days, free): Draft a short letter or email to the landlord stating the amount paid, request return within 7 days, and mention you will approach legal help if not received. Keep a copy for your records.

2. **File a police complaint for assault** (1‑3 days, free): Visit the nearest police station, give a written statement about the threat and push, attach any evidence (photos, witness names). Obtain a FIR copy.

3. **File a civil money recovery suit** (2‑4 weeks for filing, months for resolution, court fee (low) + possible lawyer fee): Prepare a plaint for Rs 40,000, attach any proof of payment and the police FIR, and file it in the Small Causes Court of Noida. Pay the court fee and serve the landlord.

## What I don't know

- Exact date of the deposit payment

- Whether a formal rent agreement exists

- If the Model Tenancy Act [KB:mta_s11_deposit] has been adopted in Uttar Pradesh

## Needs lawyer: True - A criminal aspect (threat and assault) is present, and you may need legal advice before speaking to police or filing a suit. A lawyer can also help draft a proper legal notice and represent you in court.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "ica_s73"
 ]
}

```