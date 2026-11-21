# dep02_no_agreement_delhi  (gemini:gemini-3.5-flash)

## Input

I rented a room in Laxmi Nagar, Delhi for 11 months. Paid 20,000 deposit in cash to the owner, no rent agreement, only WhatsApp chats where he mentions "your deposit". Left on 30 Sept 2026. Now he doesn't pick up calls.

## Reply shown to user

I am Nyay Saathi, an legal-help assistant (not a lawyer). You have a solid position to claim your Rs 20,000 deposit back [KB:ica_s73]. Even without a formal rent agreement, your WhatsApp chat acknowledging the deposit is usable evidence.

Since the landlord is ignoring your calls, your best first step is to send a formal written text or WhatsApp message stating your bank details and giving a strict 7-day deadline for repayment [KB:deposit_civil_route]. If they fail to respond, the next step would be a legal notice. If you qualify for free legal assistance, you can also contact the Legal Services Authority helpline at 15100 [KB:lsa_s12_legal_aid].

Do you have the landlord's full name and physical postal address in Delhi to send a formal demand letter?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "deposit withheld without rent agreement",
 "user_language": "English",
 "state": "Delhi",
 "city": "Delhi",
 "summary": "The user rented a room in Laxmi Nagar, Delhi, and paid a security deposit of 20,000 in cash to the landlord without a formal rent agreement. The tenancy ended on September 30, 2026. The landlord is now uncontactable and refusing to answer calls regarding the deposit refund.",
 "user_goal": "Recover the security deposit of 20,000 rupees from the landlord.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-09-30",
   "event": "Tenant vacated the property in Laxmi Nagar, Delhi",
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
  "WhatsApp chat messages acknowledging deposit receipt"
 ],
 "evidence_missing": [
  "rent agreement",
  "bank statement or cash receipt for deposit payment",
  "vacating receipt or key handover proof"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "What is the name of the landlord?",
  "Do you have screenshot exports of the WhatsApp chats clearly showing the landlord's phone number?",
  "Do you have any proof of monthly rent payments made to him (e.g., UPI transfers, bank receipts, or messages)?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 20,000

- Amount to claim: Rs 20,000

## Where you stand

You have a clear right to get your Rs 20,000 security deposit back [KB:ica_s73]. Although you do not have a written rent agreement or cash receipt, your WhatsApp messages acknowledging the deposit serve as valid evidence. The law allows up to 3 years from the vacating date to file a recovery claim in civil court [KB:deposit_civil_route]. However, since the landlord is avoiding your calls, you need to formalize your demand in writing before taking formal steps.

## Options

1. **Send a formal written message** (1-2 days, Free): Send a clear, polite written message on WhatsApp and via email (if available) stating your vacating date, deposit amount of Rs 20,000, bank transfer details, and a 7-day deadline to refund the money.

2. **Send a Legal Notice** (1-2 weeks, Low (Lawyer typing/drafting charges)): If the landlord ignores the message, send a formal legal notice through an advocate or draft a written final notice demanding Rs 20,000 within 15 days [KB:deposit_civil_route].

3. **File a Civil Recovery Suit** (Several months, Court fee as applicable): File a civil suit for money recovery in the local civil court / small causes court [KB:deposit_civil_route]. If eligible, you can seek assistance from the District Legal Services Authority (DLSA) [KB:lsa_s12_legal_aid].

## What I don't know

- Whether the landlord maintains that any damage or unpaid utility bills justify withholding part of the deposit.

- The landlord's full permanent address for sending legal notices.

## Needs lawyer: False - This is a basic deposit recovery claim. You can first send a formal written notice yourself before hiring a lawyer or going to court.

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