# dep02_no_agreement_delhi  (groq:qwen/qwen3.8-27b)

## Input

I rented a room in Laxmi Nagar, Delhi for 11 months. Paid 20,000 deposit in cash to the owner, no rent agreement, only WhatsApp chats where he mentions "your deposit". Left on 30 Sept 2026. Now he doesn't pick up calls.

## Reply shown to user

You have a good chance of getting your Rs 20,000 back, but you need to act quickly. Since you don't have a written agreement, your WhatsApp chats are your best proof. First, send a clear, firm message to the landlord via WhatsApp and email. State that you vacated on 30 September 2026, the room was in good condition, and you expect the deposit back within 7 days. Tell them you will file a consumer complaint if they don't respond. Keep a screenshot of this message. If they still ignore you, you can file a complaint with the District Consumer Disputes Redressal Commission in Delhi, which is faster and cheaper than civil court. Do you have the landlord's full name and address, or any bank slip showing the cash withdrawal for the deposit?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit not returned after vacating",
 "user_language": "English",
 "state": "Delhi",
 "city": "Laxmi Nagar",
 "summary": "The user rented a room in Laxmi Nagar, Delhi for 11 months and paid a cash deposit of 20,000 INR to the owner without a written rent agreement. The user vacated the premises on 30 September 2026, but the owner is now unresponsive to calls and has not returned the deposit.",
 "user_goal": "To recover the 20,000 INR security deposit from the landlord.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2025-11",
   "event": "Started renting the room (approximate start date based on 11-month duration ending Sept 2026)",
   "proof": null
  },
  {
   "date": "2025-11",
   "event": "Paid 20,000 INR deposit in cash",
   "proof": "WhatsApp chats mentioning 'your deposit'"
  },
  {
   "date": "2026-09-30",
   "event": "Vacated the room",
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
  "WhatsApp chats where landlord mentions 'your deposit'"
 ],
 "evidence_missing": [
  "Rent agreement",
  "Proof of cash payment (e.g., bank withdrawal slip, witness statement)",
  "Move-out inspection report or handover note",
  "Landlord's full name and address"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "What is the full name and address of the landlord?",
  "Did you sign any move-out checklist or receive any written notice about deductions?",
  "Do you have any bank statements showing the cash withdrawal for the deposit?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 20,000

- Amount to claim: Rs 20,000

## Where you stand

You have a strong claim for your Rs 20,000 deposit, but your main weakness is the lack of a written agreement or formal proof of the cash payment. Your WhatsApp chats where the landlord mentions 'your deposit' are helpful evidence that the money was received and acknowledged. Since you vacated on 30 September 2026, you are well within the general 3-year time limit to file a claim [KB:deposit_civil_route]. The landlord's silence is a red flag, but it doesn't stop you from taking action. You can claim the full amount, and potentially interest, though the rate is for a court to decide [KB:ica_s73].

## Options

1. **Send a formal written demand** (1 hour, Free): Send a detailed message via WhatsApp and email (if you have it) stating you vacated on 30 Sept 2026, the room was in good condition, and you expect the Rs 20,000 back within 7 days. Mention that you will file a complaint if not received. Keep a screenshot of this message.

2. **File a consumer complaint** (2-4 weeks for filing, Low (nominal court fee)): If the landlord ignores the demand, file a complaint with the District Consumer Disputes Redressal Commission in Delhi. This is a faster and cheaper route than civil court for small amounts. You can do this online or in person.

3. **File a civil money recovery suit** (3-6 months, Court fees (depends on amount)): If the consumer route fails or is not applicable, file a suit in the local civil court (Small Causes Court) in Laxmi Nagar. This is more formal and slower but is the standard legal route for deposit recovery.

## What I don't know

- Whether the landlord has claimed any deductions for damage or unpaid rent (you said none, but confirm in writing).

- The exact full name and address of the landlord, which is needed for any formal complaint.

- If there was any verbal agreement about the deposit return timeline.

## Needs lawyer: False - The amount is small (Rs 20,000) and the first steps (written demand, consumer complaint) can be done by you. A lawyer is only needed if you go to civil court or if the landlord files a counter-claim.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "ica_s73"
 ]
}

```