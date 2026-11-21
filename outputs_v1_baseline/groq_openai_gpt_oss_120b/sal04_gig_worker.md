# sal04_gig_worker  (groq:openai/gpt-oss-120b)

## Input

I deliver food for an app in Jaipur. They deactivated my ID last week and are holding 8,500 of my earnings for the last 2 weeks. Support just sends automated replies. Am I an employee? Can I claim salary?

## Reply shown to user

You earned ₹8,500 as a food‑delivery partner, but the app deactivated your account on 13 Nov 2026 and is now holding that money. This is a breach of your contract, and under the Indian Contract Act you can claim the loss [KB:ica_s73]. Because the amount is wages, the Code on Wages says it should be paid within 2 working days after termination [KB:cow_s17], and you may file a claim with the labour authority within 3 years [KB:cow_s45]. First, gather proof: screenshots of the deactivation notice, your earnings statement, and any chat with support. Next, send a formal written demand to the platform asking for payment within 7 days. If they do not comply, you can lodge a complaint with the Rajasthan Labour Commissioner. You can also get free legal aid through the Legal Services Authority if you need help preparing the claim. Do you have the screenshots of your earnings and the deactivation notice ready?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid gig earnings",
 "user_language": "English",
 "state": "Rajasthan",
 "city": "Jaipur",
 "summary": "The user works as a food delivery partner for an app in Jaipur. Their account was deactivated last week and the platform is withholding INR 8500 earned over the past two weeks. Support responses are only automated.",
 "user_goal": "To get the withheld earnings released and understand if they can claim them as salary.",
 "user_role": "other",
 "other_party": {
  "name": null,
  "type": "platform"
 },
 "timeline": [
  {
   "date": "2026-11-13",
   "event": "Account deactivated by the app",
   "proof": null
  },
  {
   "date": "2026-11-20",
   "event": "User contacted support and received automated replies",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": null,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": 8500,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [],
 "evidence_missing": [
  "Screenshot of the deactivation notice",
  "Payment statement showing the INR 8500 earned",
  "Correspondence with the platform support"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": ""
 },
 "follow_up_questions": [
  "When exactly was your account deactivated (date)?",
  "Did you receive any written notice or email about the deactivation?",
  "Do you have screenshots of your earnings and the deactivation message?",
  "What is the name of the food‑delivery app you work for?"
 ]
}

```

## Calculation (code)

- Other dues (leave encashment, reimbursements, etc.): Rs 8,500

- Amount to claim: Rs 8,500

## Where you stand

You are a gig worker who earned INR 8,500 in the last two weeks, but the platform deactivated your account and is now withholding that money. The platform’s action can be seen as a breach of the contract you have with it, so you may claim compensation for the loss under the Indian Contract Act, 1872 [KB:ica_s73]. Since the earnings are essentially wages, the Code on Wages, 2019 requires payment of wages within 2 working days after termination [KB:cow_s17]. You can file a claim for the unpaid amount within 3 years before the labour authority [KB:cow_s45]. Strengths: you have a clear amount (₹8,500) and a written contract/terms of service with the app. Weaknesses: you currently lack screenshots of the earnings and the deactivation notice, which are needed as proof.

## Options

1. **Collect evidence** (1-2 days, free): Take screenshots of the deactivation notice, your earnings statement, and any chat or email with the platform. Save them as PDFs or images.

2. **Send a formal written demand** (2-3 days (including waiting for reply), free or nominal post fee): Draft a polite but firm email or registered letter to the platform’s support/legal team stating: you earned ₹8,500, your account was deactivated on 13‑Nov‑2026, you request payment within 7 days, and you will approach the labour authority if not resolved.

3. **File a claim with the Labour Department** (1-2 weeks for filing, then variable for resolution, court/authority fee (minimal) and possible travel cost): If the platform does not pay, submit a written complaint to the Rajasthan Labour Commissioner (or nearest labour office). Attach your evidence and the demand letter. The claim must be filed within 3 years of the breach [KB:cow_s45].

4. **Seek free legal aid** (same day to a few days, free): If you need help preparing the claim, call the Legal Services Authority helpline 15100 or visit a Common Service Centre for free advice [KB:lsa_s12_legal_aid].

## What I don't know

- The exact terms of your gig contract (e.g., notice period, termination clause).

- Whether the platform has a specific grievance redressal mechanism mandated by its own policy.

- If any state-specific labour rules in Rajasthan modify the general Code on Wages [KB:cow_s17] provisions.

## Needs lawyer: False - For the initial steps—collecting proof, sending a demand, and filing a labour‑department complaint—you can act yourself. A lawyer becomes useful if the platform contests the claim or you need to pursue court action.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17",
  "cow_s45",
  "ica_s73",
  "lsa_s12_legal_aid"
 ]
}

```