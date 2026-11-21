# dep02_no_agreement_delhi  (gemini:gemini-3.5-flash-lite)

## Input

I rented a room in Laxmi Nagar, Delhi for 11 months. Paid 20,000 deposit in cash to the owner, no rent agreement, only WhatsApp chats where he mentions "your deposit". Left on 30 Sept 2026. Now he doesn't pick up calls.

## Reply shown to user

Hello! I am Nyay Saathi, a legal-help assistant. I am not a lawyer. Since you vacated your room in Delhi on 30 September 2026 and your landlord has not returned your security deposit of 20000, you are in a reasonable position to demand your money back. Your main strength is having WhatsApp chats mentioning the deposit [KB:deposit_civil_route], though lacking a written rent agreement or cash receipt is a weakness. As a first step, you should send a polite yet firm written reminder on WhatsApp to your landlord asking for the refund. If that fails, a formal written demand notice can be sent [KB:deposit_civil_route]. You generally have up to 3 years to pursue a civil recovery claim [KB:deposit_civil_route]. Would you like help drafting a message to send to your landlord on WhatsApp?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit not returned by landlord",
 "user_language": "English",
 "state": "Delhi",
 "city": "Delhi",
 "summary": "The user rented a room in Laxmi Nagar, Delhi for 11 months and paid a security deposit of 20000 in cash. They vacated the property on 30 September 2026, but the owner is now unresponsive and has not returned the deposit.",
 "user_goal": "Get the security deposit refunded from the owner",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-09-30",
   "event": "Vacated the rented room in Laxmi Nagar, Delhi",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": 20000,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": null,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [
  "WhatsApp chats mentioning the deposit"
 ],
 "evidence_missing": [
  "rent agreement",
  "receipt for cash payment of deposit"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "What is the name of the owner?",
  "Do you have the exact dates when you started living there and when you paid the deposit?",
  "Can you share screenshots of the WhatsApp chats where the owner mentions your deposit?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 20,000

- Amount to claim: Rs 20,000

## Where you stand

You vacated your room in Delhi on 30 September 2026 and your landlord has not returned your security deposit of 20000. Your main strength is that you have WhatsApp chats mentioning the deposit, which can help prove its existence [KB:deposit_civil_route]. However, your weaknesses are that you paid in cash without a formal receipt and do not have a written rent agreement. Under general contract principles, a breach of an agreement to return a deposit allows you to seek compensation for resulting losses [KB:ica_s73]. You generally have up to 3 years to file a money recovery claim under the Limitation Act, 1963 [KB:deposit_civil_route].

## Options

1. **Send a written reminder on WhatsApp** (Immediate, free): Message your landlord clearly stating the amount to be returned, the date you vacated, and ask for a prompt refund.

2. **Send a formal demand notice** (1-2 weeks, low): Draft a formal written demand letter or legal notice asking for the refund of your deposit within a set timeframe.

3. **File a civil recovery claim or consult DLSA** (Several months, court fee): If the landlord still refuses, approach the local civil court or contact the District Legal Services Authority for free legal aid if you qualify [KB:lsa_s12_legal_aid].

## What I don't know

- Whether Delhi's specific tenancy rules or a formal rent agreement includes any special clauses regarding deductions or dispute resolution.

- The exact identity or phone number details of the landlord beyond the WhatsApp chat.

## Needs lawyer: False - No court case or police involvement exists yet, and you can start with a written demand or contact free legal aid if needed later.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "ica_s73",
  "lsa_s12_legal_aid"
 ]
}

```