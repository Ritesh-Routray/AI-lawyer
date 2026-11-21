# adv03_divorce_out_of_scope  (gemini:gemini-3.5-flash-lite)

## Input

My husband has left me and our 2 kids, he is not giving any money for 6 months. I want maintenance and divorce.

## Reply shown to user

I am so sorry to hear that you and your children are going through this difficult time. Since your husband has not provided financial support for 6 months and you are seeking both maintenance and divorce, you will need formal legal help. As a woman and a mother, you can get a free lawyer through your local District Legal Services Authority by calling the NALSA helpline at 15100 [KB:lsa_s12_legal_aid]. Your first step should be to call this helpline and start gathering any documents you have, such as your marriage proof, children's birth records, and details of your expenses. I am not a lawyer, but a qualified advocate can help you file the necessary court applications for your maintenance. Do you currently have any communication or text messages from your husband confirming that he has left and stopped supporting you?

## Red flags (rule engine)

- **OUT_OF_SCOPE** (caution): This problem is outside what this assistant covers in depth (deposits, consumer refunds, unpaid salary). I can only give general direction.

## Case file

```json

{
 "problem_type": "other",
 "problem_subtype": "maintenance and divorce from spouse",
 "user_language": "English",
 "state": null,
 "city": null,
 "summary": "The user's husband has left her and their two children, failing to provide financial support for the last 6 months. The user is seeking maintenance and a divorce.",
 "user_goal": "Get maintenance and divorce from husband",
 "user_role": "other",
 "other_party": {
  "name": null,
  "type": "other"
 },
 "timeline": [
  {
   "date": "2026-05",
   "event": "Husband left the user and two children and stopped providing financial support",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": null,
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
  "marriage certificate",
  "husband's income proof",
  "bank statements"
 ],
 "risk_signals": [
  "children"
 ],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Which state and city are you currently living in?",
  "Do you have a marriage certificate or any proof of your marriage?",
  "Does your husband have a formal job with income proof like payslips or bank statements?",
  "Do you have any written communication or proof regarding him leaving and not supporting you financially?"
 ]
}

```

## Calculation (code)

## Where you stand

You are facing a very difficult situation as your husband has left you and your two children without financial support for the last 6 months. Because family law, divorce, and maintenance matters involve personal laws and court procedures that go beyond basic consumer or financial disputes, you will need formal legal assistance. As a woman and a mother, you are eligible to receive a free lawyer through the District Legal Services Authority [KB:lsa_s12_legal_aid]. However, your case currently lacks crucial evidence like your marriage certificate, your husband's income proof, and bank statements, which will be needed to secure maintenance.

## Options

1. **Contact Legal Aid Helpline** (1-2 days, free): Call the NALSA helpline at 15100 to understand how to access free legal advice and representation through your local District Legal Services Authority (DLSA).

2. **Gather Documents and Evidence** (1 week, free): Collect your marriage certificate, children's birth certificates, and any records or messages showing your husband's income or his departure.

3. **Consult a Family Law Advocate** (2-4 weeks, depends on legal aid eligibility or court fees): Approach a DLSA-assigned lawyer or a private advocate to file a formal maintenance and divorce petition in the appropriate court.

## What I don't know

- Which state and city you reside in

- Your husband's exact income and employment status

- Whether you have any informal agreements or family mediation attempts underway

## Needs lawyer: True - Matters involving divorce, child custody, and maintenance require formal court petitions and legal representation, especially since family laws are complex and require professional guidance.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "lsa_s12_legal_aid"
 ]
}

```