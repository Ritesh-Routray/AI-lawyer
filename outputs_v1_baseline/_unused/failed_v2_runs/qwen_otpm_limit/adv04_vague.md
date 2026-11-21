# adv04_vague  (groq:qwen/qwen3.8-27b)

## Input

company ne paisa nahi diya

## Reply shown to user

Namaste! Aapki company ne salary nahi di, jo ki Code on Wages ke against hai [KB:cow_s17]. Pehle aap company ko ek clear written message (email/WhatsApp) bhejein jismein batayein ki kitne mahine ka paisa baaki hai aur total amount kitna hai. Unse 7 din ke andar payment karne ko kahein. Agar wo nahi dete, toh aap Labour Commissioner office mein complaint file kar sakte hain [KB:cow_s45]. Kripya mujhe batayein: Aap kis state mein hain aur total unpaid amount kitna hai? Isse main aapko sahi office ka address aur next steps bata paunga.

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid salary",
 "user_language": "Hinglish",
 "state": null,
 "city": null,
 "summary": "The user states that their company has not paid them money. No specific details regarding the amount, duration, or nature of the dues were provided.",
 "user_goal": "To recover unpaid money from the company.",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [
  {
   "date": null,
   "event": "Company failed to pay dues",
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
  "Offer letter or employment contract",
  "Payslips",
  "Bank statements showing missing credits",
  "Exit settlement letter (if applicable)"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Aap kis state aur city mein rehte hain?",
  "Kitne mahine ka paisa baaki hai aur total amount kitna hai?",
  "Kya aapke paas offer letter, payslips ya bank statement jaisa koi written proof hai?"
 ]
}

```

## Calculation (code)

## Where you stand

Aapki company ne aapka paisa nahi diya hai, jo ki galat hai. Code on Wages ke hisaab se salary agle mahine ke 7 tareekh se pehle deni hoti hai [KB:cow_s17]. Agar aapki naukri khatam ho chuki hai, toh final dues 2 working days mein deni chahiye thi [KB:cow_s17]. Abhi aapke paas specific amount ya months ke baare mein koi detail nahi hai, isliye hum exact claim calculate nahi kar sakte. Aapke paas written proof (jaise payslips ya bank statement) hona chahiye taaki aapki baat strong ho.

## Options

1. **Written Demand to Employer** (1-2 din, Free): Company ke HR ya manager ko ek clear written message (email/WhatsApp) bhejein jismein aap batayein ki kitne mahine ka paisa baaki hai aur total amount kitna hai. Unse 7 din ke andar payment karne ko kahein.

2. **File Complaint with Labour Department** (2-4 weeks for resolution, Free / Low (filing fees may apply)): Agar company ne 7 din mein paisa nahi diya, toh aap apne state ke Labour Commissioner office mein complaint file kar sakte hain. Yeh claim 3 saal ke andar file kiya ja sakta hai [KB:cow_s45].

3. **Seek Free Legal Aid** (Immediate advice, Free): Agar aap SC/ST hain, industrial workman hain, ya income limit ke neeche hain, toh aap District Legal Services Authority (DLSA) se free lawyer le sakte hain. NALSA helpline 15100 par call karke bhi free advice mil sakti hai [KB:lsa_s12_legal_aid].

## What I don't know

- Aap kis state aur city mein rehte hain (kyunki local labour office ka address uspar depend karta hai).

- Total unpaid amount kitna hai aur kitne mahine ke liye baaki hai.

- Kya aapke paas koi written proof (contract/payslip) hai ya nahi.

## Needs lawyer: False - Abhi ke liye aap khud written demand bhej sakte hain aur Labour Department mein complaint file kar sakte hain. Lawyer tab zaroori hoga agar company ne court case file kiya ho, ya amount bahut bada ho, ya aapko free legal aid ke liye qualify karna ho.

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