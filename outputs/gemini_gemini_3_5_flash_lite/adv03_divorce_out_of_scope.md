# adv03_divorce_out_of_scope  (gemini:gemini-3.5-flash-lite)

## Input

My husband has left me and our 2 kids, he is not giving any money for 6 months. I want maintenance and divorce.

## Reply shown to user

It is very difficult to be left without support, especially with two children depending on you. Because you are seeking maintenance and a divorce, you should take immediate steps to secure legal guidance. As a woman and a mother, you are eligible for free legal assistance through the District Legal Services Authority under the Legal Services Authorities Act [KB:lsa_s12_legal_aid]. You can also contact the NALSA helpline at 15100 for immediate guidance [KB:lsa_s12_legal_aid]. Your first step should be to connect with your local DLSA office and gather any available identity or marriage documents. Do you currently have a copy of your marriage certificate or any written proof showing that your husband has stopped providing financial support?

## Red flags (rule engine)

- **OUT_OF_SCOPE** (caution): This problem is outside what this assistant covers in depth (deposits, consumer refunds, unpaid salary). I can only give general direction.

## Case file

```json

{
 "problem_type": "other",
 "problem_subtype": "maintenance and divorce from estranged spouse",
 "user_language": "English",
 "state": null,
 "city": null,
 "summary": "The user states that her husband has left her and their two children and has not provided financial support for the last 6 months. She is seeking maintenance and a divorce.",
 "user_goal": "Get maintenance and divorce from husband",
 "user_role": "other",
 "other_party": {
  "name": null,
  "type": "other"
 },
 "timeline": [
  {
   "date": "2026-05",
   "event": "Husband left and stopped providing financial support",
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
  "details of husband's income/employment",
  "proof of separation duration"
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
  "Do you have a marriage certificate or any written proof of separation?",
  "Does your husband have a regular source of income or job?"
 ]
}

```

## Calculation (code)

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 144 (ORDER FOR MAINTENANCE OF WIVES, CHILDREN AND PARENTS) p.42

- Constitution of India Article 39A (against moral and material abandonment.]) p.2

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 146  p.44

- Constitution of India Article 43  p.2

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 147  p.44

- Bharatiya Nyaya Sanhita, 2023 Section 82  p.28

- Bharatiya Nyaya Sanhita, 2023 Section 81  p.28

- Bharatiya Nyaya Sanhita, 2023 Section 85  p.29

## Where you stand

You are currently facing a difficult situation where your husband has left you and your two children without financial support for the last 6 months. As a woman and a mother, you are entitled to seek maintenance for yourself and your children, and you can approach the District Legal Services Authority (DLSA) for free legal aid [KB:lsa_s12_legal_aid]. Legal provisions exist for the maintenance of wives and children [KB:src_bnss_2023_144_p2], but your case currently lacks formal documentation like your marriage certificate and details of your husband's income. Gathering these documents will strengthen your position significantly.

## Options

1. **Contact DLSA for Free Legal Aid** (1-3 days, free): Reach out to your local District Legal Services Authority (DLSA) or call the NALSA helpline at 15100 to get free legal advice and assistance from a lawyer.

2. **Gather Documents and Evidence** (3-7 days, free): Collect your marriage certificate, identity cards, text messages or any proof showing the duration of separation and lack of financial support.

## What I don't know

- Which state and city you are currently residing in

- Whether your husband has a steady income or employment

- If there are any prior agreements or domestic violence issues involved

## Needs lawyer: True - Family law matters involving maintenance, children, and divorce require formal legal representation to file petitions in court.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "lsa_s12_legal_aid",
  "src_bnss_2023_144_p2"
 ],
 "support_check": {
  "checked": 1,
  "unsupported": []
 }
}

```