# sal02_fnf_delay  (groq:qwen/qwen3.8-27b)

## Input

I resigned from an IT company in Gurgaon, last working day 15 Sept 2026. My full and final settlement of about 1,10,000 (last month salary + leave encashment) is still not paid. HR says F&F takes 90 days as per policy.

## Reply shown to user

Your employer's 90-day policy is likely not valid. Under the Code on Wages, 2019, your final dues must be paid within 2 working days of your resignation [KB:cow_s17]. Since your last working day was 15 September 2026, the delay is significant. 

First, send a firm email to HR citing this law and demanding immediate payment. Ask them to confirm your last working day and the exact amount in writing. Keep a copy of this email. If they still delay, you can file a claim with the Labour Commissioner in Haryana, which is a free or low-cost option [KB:cow_s45]. You can also call the NALSA helpline at 15100 for free advice [KB:lsa_s12_legal_aid]. 

Do you have a relieving letter or any written confirmation of your last working day?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "delayed full and final settlement",
 "user_language": "English",
 "state": "Haryana",
 "city": "Gurgaon",
 "summary": "The user resigned from an IT company in Gurgaon with a last working day of 15 September 2026. The full and final settlement of approximately 1,10,000 INR has not been paid. HR has stated that the process takes 90 days according to company policy.",
 "user_goal": "To receive the pending full and final settlement amount.",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [
  {
   "date": "2026-09-15",
   "event": "Last working day at the IT company",
   "proof": null
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
  "Resignation letter",
  "Relieving letter",
  "Offer letter or employment contract",
  "Payslips for the last few months",
  "Communication with HR regarding the delay"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": "HR claims 90 days for F&F settlement"
 },
 "follow_up_questions": [
  "Do you have a relieving letter or any written confirmation of your last working day?",
  "Have you sent any written follow-up emails to HR regarding the delay?",
  "Do you have your offer letter or employment contract that mentions the F&F timeline?"
 ]
}

```

## Calculation (code)

- Other dues (leave encashment, reimbursements, etc.): Rs 110,000

- Amount to claim: Rs 110,000

## Where you stand

You are in a strong position because the law is clear that your final dues must be paid quickly after you resign. Under the Code on Wages, 2019, wages due upon resignation must be paid within 2 working days [KB:cow_s17]. Your employer's claim of a 90-day policy is likely invalid against this statutory deadline. Your main weakness is the lack of documented proof, such as a relieving letter or written communication with HR, which you need to gather immediately to support any formal claim.

## Options

1. **Send a formal written demand** (1-2 days, Free): Send an email to HR and your manager stating that the 90-day policy violates the Code on Wages, 2019, which requires payment within 2 working days of resignation [KB:cow_s17]. Request immediate payment and ask for a written confirmation of your last working day and the exact amount due.

2. **File a complaint with the Labour Commissioner** (2-4 weeks for filing, Low (government fees)): If the company does not pay after your written demand, file a claim for unpaid wages before the Labour Commissioner in Haryana. This is a government authority that handles such disputes. You must file this within 3 years of the due date [KB:cow_s45].

3. **Seek free legal aid** (Immediate, Free): If you face difficulties or the amount is significant, contact the District Legal Services Authority (DLSA) in Gurgaon or call the NALSA helpline at 15100 for free legal advice and representation [KB:lsa_s12_legal_aid].

## What I don't know

- Whether your specific employment contract has any valid clauses that might alter the standard statutory timeline (though statutory minimums usually override company policy).

- The exact breakdown of the Rs 1,10,000 (e.g., how much is salary vs. leave encashment vs. bonus), which may affect the specific legal route.

## Needs lawyer: False - The first steps (written demand and checking documents) can be done by you. A lawyer is not needed yet unless the company refuses to pay after your formal demand or if you decide to file a formal legal notice/case, at which point free legal aid or a private lawyer can assist.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17",
  "cow_s45",
  "lsa_s12_legal_aid"
 ]
}

```