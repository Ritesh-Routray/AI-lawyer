# adv04_vague  (gemini:gemini-3.5-flash-lite)

## Input

company ne paisa nahi diya

## Reply shown to user

Namaste! Main Nyay Saathi hoon. Main koi lawyer nahi hoon, par aapki madad kar sakta hoon. Aapki unpaid salary ke mamle mein, Code on Wages, 2019 [KB:cow_s17] ke mutabik resigned ya removed hone par wages 2 working days ke andar milni chahiye [KB:cow_s17], aur aap 3 saal ke andar Labour Authority ke paas claim kar sakte hain [KB:cow_s45]. Lekin abhi hamare paas yeh pakka karne ke liye zaroori proofs jaise offer letter aur payslips nahi hain. Pehla step yeh hoga ki aap employer ko written mein reminder bhejein aur apne bank statements check karein. Kya aap bata sakte hain ki aapko kitne mahine ka salary nahi mila hai aur total amount kitna hai?

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
 "user_goal": "Get the unpaid money from the company",
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
  "bank statement showing salary history"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Aapko kitne mahine ka salary nahi mila hai aur total amount kitna hai?",
  "Aap kaunse state aur city mein kaam karte hain?",
  "Kya aapke paas offer letter, payslips ya koi written agreement hai?"
 ]
}

```

## Calculation (code)

## Where you stand

Aapka case unpaid salary ka hai. Code on Wages, 2019 [KB:cow_s17] ke mutabik wages time par milni chahiye, aur resign ya remove hone par 2 working days ke andar settlement hona chahiye [KB:cow_s17]. Aap 3 saal ke andar Labour Authority ke paas claim file kar sakte hain [KB:cow_s45]. Magar abhi aapke paas offer letter, payslips ya bank statement jaise proofs nahi hain, jo ki case strong karne ke liye zaroori hain.

## Options

1. **Employer ko written reminder bhejein** (1-2 din, free): Company HR ya manager ko email ya WhatsApp par apni unpaid salary ke liye written request bhejein aur total amount mention karein.

2. **Labour Commissioner office ya helpline se baat karein** (1-2 hafte, low): Agar employer response na de, toh state Labour Department ya Inspector-cum-Facilitator ke paas complaint file karne ki taiyaari karein [KB:cow_s45].

## What I don't know

- Exact unpaid amount kitna hai aur kitne mahine ki salary baki hai.

- Aap kaunse state aur city mein kaam karte hain, jisse local jurisdiction pata chale.

## Needs lawyer: False - Abhi koi court case ya criminal matter nahi hai. Pehle aapko employer ko written demand bhejni chahiye aur proofs ikatthe karne chahiye. Lawyer ki zaroorat tab padegi jab Labour Authority mein formal case file karna ho.

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