# sal02_fnf_delay  (gemini:gemini-3.5-flash-lite)

## Input

I resigned from an IT company in Gurgaon, last working day 15 Sept 2026. My full and final settlement of about 1,10,000 (last month salary + leave encashment) is still not paid. HR says F&F takes 90 days as per policy.

## Reply shown to user

You have a strong legal basis to claim your pending full and final settlement of Rs 110,000. Although HR is citing a 90-day company policy, the law requires wages to be paid within two working days of resignation [KB:src_cow_2019_17]. Your first step is to send a formal written email to HR demanding your dues and pointing out this delay. If they still fail to pay, you can approach the Labour Department in Gurgaon to file a formal claim within 3 years [KB:cow_s45]. Do you currently have a copy of your employment agreement or company policy stating the 90-day F&F clause?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "delayed full and final settlement after resignation",
 "user_language": "English",
 "state": "Haryana",
 "city": "Gurgaon",
 "summary": "The user resigned from an IT company in Gurgaon with their last working day on 15 September 2026. The full and final settlement of approximately 110000, including the last month's salary and leave encashment, remains unpaid, and HR is citing a 90-day company policy.",
 "user_goal": "Get the pending full and final settlement paid by the employer",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [
  {
   "date": "2026-09-15",
   "event": "Last working day at the IT company",
   "proof": "Resignation acceptance or relieving letter"
  }
 ],
 "amounts": {
  "deposit_paid": null,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": 110000,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [],
 "evidence_missing": [
  "offer letter",
  "resignation email",
  "relieving letter",
  "payslips",
  "employment agreement showing F&F timeline"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": "HR stated F&F takes 90 days as per company policy"
 },
 "follow_up_questions": [
  "Do you have a copy of your employment agreement or company policy stating the 90-day F&F clause?",
  "Do you have your relieving letter and written communication with HR regarding the pending dues?",
  "Did you sign any settlement papers or get an official F&F calculation statement from the company?"
 ]
}

```

## Calculation (code)

- Other dues (leave encashment, reimbursements, etc.): Rs 110,000

- Amount to claim: Rs 110,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Constitution of India Article 311  p.2

- Code on Wages, 2019 Section 17  p.12

- Code on Wages, 2019 Section 45  p.23

- Code on Wages, 2019 Section 18  p.12

- Code on Wages, 2019 Section 48  p.24

- Constitution of India Article 68  p.8

- Constitution of India Article 62  p.5

- Code on Wages, 2019 Section 28  p.17

## Where you stand

As an employee who has resigned, you have a strong legal right to receive your full and final settlement. Under the law, when an employee resigns, wages due must be paid within two working days [KB:src_cow_2019_17], making the company's 90-day policy legally questionable. Your strength is the clear timeline of your exit, while your weakness is the lack of written proof gathered so far, such as payslips and your employment agreement. You can formally claim unpaid wages before the government-appointed authority within 3 years [KB:cow_s45].

## Options

1. **Send a formal written demand email** (1-2 days, free): Write an email to HR and management demanding your pending full and final settlement of Rs 110,000 immediately, citing that delayed payments cause financial loss.

2. **File a complaint with the Labour Department** (1-3 months, low): If HR does not respond or refuses to pay, approach the local Labour Commissioner office in Gurgaon to file a formal claim for unpaid wages.

## What I don't know

- Whether your signed employment contract explicitly includes a valid 90-day F&F clause agreed upon by you

- Exact breakup of the Rs 110,000 pending amount into salary, leave encashment, or other components

## Needs lawyer: False - A lawyer is not needed at this initial stage since you can first send a written demand or approach the Labour Department yourself. A lawyer would only be necessary if the company initiates legal proceedings against you or refuses completely after a formal labour complaint.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s45",
  "src_cow_2019_17"
 ],
 "support_check": {
  "checked": 2,
  "unsupported": []
 }
}

```