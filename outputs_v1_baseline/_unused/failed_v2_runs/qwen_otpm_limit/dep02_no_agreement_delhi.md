# dep02_no_agreement_delhi  (groq:qwen/qwen3.8-27b)

## Input

I rented a room in Laxmi Nagar, Delhi for 11 months. Paid 20,000 deposit in cash to the owner, no rent agreement, only WhatsApp chats where he mentions "your deposit". Left on 30 Sept 2026. Now he doesn't pick up calls.

## Reply shown to user

You have a good chance of getting your Rs 20,000 back, but you need to act quickly because you don't have a written agreement. Your WhatsApp chats are your best proof right now. First, send a final, polite but firm message to the landlord on WhatsApp. Tell him you vacated on 30 September 2026 and ask for the deposit back within 7 days. Tell him that if you don't hear back, you will file a complaint with the Consumer Commission. Save this message. If he still ignores you, you can file a complaint with the District Consumer Disputes Redressal Commission in Delhi, which is a cheaper and faster option than civil court. You can also call the NALSA helpline at 15100 to see if you qualify for a free lawyer. Do you have the landlord's full name or any other contact details besides the phone number?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit not returned after vacating",
 "user_language": "English",
 "state": "Delhi",
 "city": "Laxmi Nagar",
 "summary": "The user rented a room in Laxmi Nagar, Delhi for 11 months and paid a cash deposit of 20,000 INR to the owner without a written rent agreement. The user vacated the premises on 30 September 2026, but the owner is now unresponsive to calls regarding the return of the deposit.",
 "user_goal": "Recover the 20,000 INR security deposit from the landlord.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2025-12",
   "event": "Rental period began (approximate, 11 months prior to departure)",
   "proof": null
  },
  {
   "date": "2025-12",
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
  "Rent agreement (user stated none exists)",
  "Proof of cash payment (e.g., bank withdrawal slip, receipt, or witness)",
  "Move-out inspection report or condition of room at departure",
  "Landlord's full name and contact details"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Do you have the landlord's full name or any other contact details besides the phone number?",
  "Did you send a final message on WhatsApp asking for the refund, and what was his last response?",
  "Was the room handed over in good condition, and do you have photos of the room when you left?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 20,000

- Amount to claim: Rs 20,000

## Where you stand

You have a strong moral claim to your Rs 20,000 deposit, but your legal position is weakened by the lack of a written rent agreement and proof of cash payment. Your main strength is the WhatsApp chat where the landlord mentions 'your deposit,' which helps prove the money was given. The biggest weakness is that you cannot easily prove the exact amount or that the room was returned in good condition without photos or a receipt. Since the landlord is unresponsive, you need to create a paper trail immediately to show you tried to resolve this amicably before taking formal steps.

## Options

1. **Send a final written demand** (10 minutes, free): Send a clear WhatsApp message and an email (if you have it) stating: 'I vacated on 30 Sept 2026. Please return my Rs 20,000 deposit by [date 7 days from now]. If not, I will file a complaint.' Keep this message saved.

2. **File a consumer complaint** (1-2 weeks for filing, Low (court fees based on claim value)): If the landlord ignores the demand, file a complaint with the District Consumer Disputes Redressal Commission in Delhi. This is a low-cost forum for service/contract disputes. You can file this yourself or with help from a legal aid center.

3. **Seek free legal aid** (Varies by DLSA workload, free): Contact the District Legal Services Authority (DLSA) in Delhi or call the NALSA helpline at 15100. If you meet the income criteria, they can provide a free lawyer to send a legal notice or file a civil suit.

4. **File a civil money recovery suit** (Months to years, Court fees + lawyer fees): If other methods fail, file a suit in the civil court for recovery of Rs 20,000. This is the most formal and time-consuming route. A specific legal provision may apply regarding the exact limitation period, so a lawyer can confirm the deadline.

## What I don't know

- The exact limitation period for this specific type of deposit claim in Delhi without a written contract.

- Whether the landlord has any valid claim for deductions (like unpaid rent or damage) that you are unaware of.

- The landlord's full legal name and address, which is needed for any formal filing.

## Needs lawyer: False - The amount is small (Rs 20,000) and there is no immediate court summons or criminal angle. You can start with a written demand and potentially file a consumer complaint yourself. A lawyer becomes necessary if the landlord files a counter-claim, if you decide to go to civil court, or if you qualify for free legal aid and want professional representation.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": []
}

```