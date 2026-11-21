# adv04_vague  (gemini:gemini-3.5-flash-lite)

## Input

company ne paisa nahi diya

## Reply shown to user

Aapka company ki taraf se salary rokna galat hai aur Code on Wages ke mutabik aapko apne dues milne chahiye [KB:cow_s17]. Aap 3 saal ke andar Labour Department mein iska claim file kar sakte hain [KB:cow_s45]. Kyunki abhi hamare paas aapke offers, payslips ya exact amount ki details nahi hain, pehla kadam yeh hoga ki aap HR ya employer ko WhatsApp ya email par ek written reminder bhejein taki baat record par aaye. Aapka kitna paisa ya kitne mahine ka salary baaki hai?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid salary",
 "user_language": "Hinglish",
 "state": null,
 "city": null,
 "summary": "The user states that their company has not paid their money/salary.",
 "user_goal": "Get their pending salary or dues from the company",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [],
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
  "offer letter",
  "payslips",
  "bank statements"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Aapka kitna paisa ya kitne mahine ka salary baaki hai?",
  "Aap kaunse state me rehte hain?",
  "Kya aapke paas offer letter ya koi written proof hai?"
 ]
}

```

## Calculation (code)

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Code on Wages, 2019 Section 59  p.29

- Code on Wages, 2019 Section 17  p.12

- Code on Wages, 2019 Section 45  p.23

- Code on Wages, 2019 Section 43 (PAYMENT OF DUES, CLAIMS AND AUDIT) p.22

- Code on Wages, 2019 Section 18  p.12

- Code on Wages, 2019 Section 48  p.24

- Code on Wages, 2019 Section 27  p.17

- Code on Wages, 2019 Section 44  p.22

## Where you stand



## Options

1. **Written Demand Message bhejiye** (1 din, free): Apne employer ya HR ko WhatsApp ya email par ek written message bhejiye jismein apne pending salary aur amount ka clear zikr karein.

2. **Labour Commissioner Office mein Complaint** (1-3 mahine, low): Agar employer response na de, toh local Labour Department ya authority ke paas unpaid wages ke liye application file karein.

## What I don't know

- Aapka kitna paisa ya kitne mahine ka salary baaki hai.

- Aap kaunse state ya city mein kaam kar rahe hain.

- Kya aapke paas employment ka koi written proof jaise offer letter ya ID card hai.

## Needs lawyer: False - Abhi koi court case ya criminal angle nahi hai, aur aap khud ek written demand ya labour department mein complaint file kar sakte hain. Lawyer ki zaroorat tab padegi jab case labour authority mein aage badhega.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17",
  "cow_s45",
  "src_cow_2019_59"
 ],
 "support_check": "not auto-checked (non-English reply; cross-encoder is English-only)"
}

```