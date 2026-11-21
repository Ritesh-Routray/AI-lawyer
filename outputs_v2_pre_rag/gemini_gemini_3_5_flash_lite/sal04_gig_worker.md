# sal04_gig_worker  (gemini:gemini-3.5-flash-lite)

## Input

I deliver food for an app in Jaipur. They deactivated my ID last week and are holding 8,500 of my earnings for the last 2 weeks. Support just sends automated replies. Am I an employee? Can I claim salary?

## Reply shown to user

Hello! Having your delivery ID deactivated and your earnings of Rs 8,500 withheld is very stressful, but the law protects your right to receive wages for work already done. Under the Code on Wages, final dues must be cleared promptly when an engagement ends, and you have up to 3 years to file a formal claim [KB:cow_s17, KB:cow_s45]. To get started, you should immediately gather proof by taking screenshots of your app dashboard showing the withheld amount and downloading bank statements showing past payouts. Next, send a written demand to the platform. If they do not respond, you can file a complaint at the Labour Commissioner office in Jaipur [KB:cow_s45]. Do you currently have screenshots of the withheld Rs 8,500 on your app dashboard?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "delivery app withheld earnings after ID deactivation",
 "user_language": "English",
 "state": "Rajasthan",
 "city": "Jaipur",
 "summary": "The user works as a food delivery executive for an app in Jaipur. Their ID was deactivated last week and the platform is withholding 8,500 rupees of earnings for the last two weeks with only automated support replies.",
 "user_goal": "Get back the withheld earnings and understand their status and rights",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "platform"
 },
 "timeline": [
  {
   "date": "2026-11-13",
   "event": "ID deactivated and last 2 weeks earnings withheld",
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
  "delivery partner agreement or contract",
  "payment history or bank statements showing previous payouts",
  "screenshots of app dashboard showing withheld amount and support chats"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Do you have a copy of your delivery partner agreement or contract with the app?",
  "Do you have screenshots showing the withheld amount of 8,500 rupees in your app dashboard?",
  "Do you have bank statements showing your previous payouts from this app?"
 ]
}

```

## Calculation (code)

- Other dues (leave encashment, reimbursements, etc.): Rs 8,500

- Amount to claim: Rs 8,500

## Where you stand



## Options

1. **Gather Evidence and Screenshots** (1-2 hours, free): Take clear screenshots of your app dashboard showing the blocked earnings of Rs 8,500 and download your bank statements showing past payments from the company.

2. **Send a Written Demand** (1 day, low): Send a formal written request via email or registered post to the platform's support or grievance officer demanding your withheld earnings within 7 days.

3. **File a Labour Department Complaint** (1-3 weeks, free / low): If the company fails to pay, file a formal claim for unpaid wages before the Labour Commissioner office in Jaipur under the Code on Wages [KB:cow_s45].

## What I don't know

- Whether your delivery partner agreement contains a mandatory private arbitration clause instead of standard labour court routes.

- The exact reason provided internally by the platform for your ID deactivation.

## Needs lawyer: False - No court case or police involvement exists yet, and you can initiate a formal wage claim or grievance yourself through the Labour Department.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17",
  "cow_s45"
 ]
}

```