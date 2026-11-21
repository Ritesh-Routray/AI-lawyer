# dep02_no_agreement_delhi  (gemini:gemini-3.5-flash-lite)

## Input

I rented a room in Laxmi Nagar, Delhi for 11 months. Paid 20,000 deposit in cash to the owner, no rent agreement, only WhatsApp chats where he mentions "your deposit". Left on 30 Sept 2026. Now he doesn't pick up calls.

## Reply shown to user

You are in a fair position to recover your Rs 20,000 security deposit since you have WhatsApp chats mentioning the amount, even though you lack a formal rent agreement or cash receipt. Landlords are generally expected to refund deposits upon handing over vacant possession [KB:src_mta_2021_11]. Your first step should be to send a clear written reminder on WhatsApp and keep screenshots of the conversation. If the owner continues to ignore you, you can send a formal demand notice or seek free legal guidance from the District Legal Services Authority [KB:lsa_s12_legal_aid] [KB:deposit_civil_route]. Do you currently have screenshots of the WhatsApp chats where the landlord acknowledges your deposit?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "landlord not returning security deposit",
 "user_language": "English",
 "state": "Delhi",
 "city": "Delhi",
 "summary": "The user rented a room in Laxmi Nagar, Delhi, and paid a security deposit of 20000 in cash without a formal rent agreement. After vacating the room on 30 September 2026, the owner is ignoring phone calls and has not returned the deposit.",
 "user_goal": "Get back the security deposit from the landlord",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-09-30",
   "event": "Vacated the rented room",
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
  "receipt for cash payment"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "What is the name or phone number of the owner?",
  "Do you have screenshots of the WhatsApp chats where he mentions your deposit?",
  "Did you send any written reminder or notice to the owner after moving out?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 20,000

- Amount to claim: Rs 20,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Model Tenancy Act, 2021 Section 11  p.11

- Model Tenancy Act, 2021 Section 10  p.11

- Model Tenancy Act, 2021 Section 15  p.13

- Model Tenancy Act, 2021 Section 14  p.12

- Model Tenancy Act, 2021 Section 24  p.18

- Model Tenancy Act, 2021 Section 8 (RENT) p.11

- Model Tenancy Act, 2021 Section 23  p.18

## Where you stand



## Options

1. **Send a written reminder on WhatsApp** (1 day, free): Send a clear, polite message on WhatsApp reminding the owner about the Rs 20,000 deposit and asking for a date to return it. Keep screenshots of this chat.

2. **Send a formal written demand notice** (3-5 days, low): Draft a formal demand letter asking for the return of your security deposit within a specific timeframe, mentioning your WhatsApp proof.

3. **Consult DLSA for free legal aid** (1-2 weeks, free): If the owner still refuses, approach the District Legal Services Authority (DLSA) for guidance or free legal assistance.

## What I don't know

- Whether Delhi has formally adopted the Model Tenancy Act [KB:mta_s11_deposit] provisions for your specific locality.

- If the landlord has any valid claims for deductions that you are unaware of.

## Needs lawyer: False - A lawyer is not needed right now because you can first try sending a written demand or approaching DLSA; a lawyer would only become necessary if you decide to file a formal civil recovery suit.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "lsa_s12_legal_aid",
  "src_mta_2021_11"
 ],
 "support_check": {
  "checked": 2,
  "unsupported": [
   {
    "id": "src_mta_2021_11",
    "claim": "You vacated your room in Delhi on 30 September 2026 and your landlord is ignoring calls regarding your Rs 20,000 security deposit .",
    "score": -5.31
   }
  ]
 }
}

```