# con02_upi_failed  (gemini:gemini-3.5-flash-lite)

## Input

Bhai maine 8 October 2026 ko UPI se 15000 bheje, paise account se kat gaye par receiver ko nahi mile. Bank ko complaint ki, 3 hafte ho gaye koi jawab nahi. Kya karun?

## Reply shown to user

Namaste! Aapka Rs 15,000 ka failed UPI transaction ka mamla kaafi clear hai. Bank dwara 3 hafte tak jawab na dena deficiency in service kehlata hai [KB:cpa_consumer_def]. Abhi sabse pehle aapko National Consumer Helpline (1915 ya consumerhelpline.gov.in) par free mein complaint karni chahiye [KB:forum_nch]. Agar wahan se baat na bane, toh RBI Ombudsman (cms.rbi.org.in) par complain kar sakte hain kyunki banking transactions ke liye yeh bahut bada zariya hai [KB:rbi_ios_2026]. Isme kisi lawyer ki zaroorat nahi hai aur koi court fee bhi nahi lagti [KB:cpa_fee_nil_5lakh]. Kya aapke paas abhi wo UPI transaction ID ya screenshot aur bank statement available hai?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "failed UPI transaction refund not processed",
 "user_language": "Hinglish",
 "state": null,
 "city": null,
 "summary": "The user transferred 15000 rupees via UPI on 8 October 2026, but the amount was debited from their account and not credited to the receiver. They filed a complaint with the bank three weeks ago, but have received no response yet.",
 "user_goal": "Get the failed UPI transaction amount refunded by the bank",
 "user_role": "consumer",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "timeline": [
  {
   "date": "2026-10-08",
   "event": "Transferred 15000 via UPI, money debited from account but not received by receiver",
   "proof": "bank statement / UPI transaction screenshot"
  }
 ],
 "amounts": {
  "deposit_paid": null,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": null,
  "order_value": 15000,
  "amount_refunded": null
 },
 "evidence_have": [],
 "evidence_missing": [
  "bank statement showing debit",
  "UPI transaction reference ID / screenshot",
  "copy of bank complaint"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Aap kaunse state mein rehte hain?",
  "Kya aapke paas bank complaint number ya acknowledgment hai?",
  "Kya UPI transaction ID ya screenshot available hai?"
 ]
}

```

## Calculation (code)

- Amount paid: Rs 15,000

- Refund due: Rs 15,000

## Where you stand

Aapka Rs 15,000 ka failed UPI transaction ka case kaafi strong hai kyunki aapke paas bank account statement se debit ka proof mil sakta hai [KB:cpa_consumer_def]. Bank ko 3 haftay pehle complaint bhejne ke baad bhi reply na dena deficiency in service maana jaata hai [KB:cpa_consumer_def]. Yeh achhi baat hai ki aapke paas time hai aur aap Consumer Protection Act ke antargat complain kar sakte hain [KB:cpa_limitation]. Lekin abhi aapke paas transaction reference ID / screenshot aur bank complaint ki copy missing hai, jise aapko jald se jald ikattha karna hoga.

## Options

1. **Bank aur National Consumer Helpline [KB:forum_nch] par follow-up** (1-2 din, free): Apne bank se complaint acknowledgment number maangein aur National Consumer Helpline [KB:forum_nch] (1915 ya consumerhelpline.gov.in) par complaint darj karein.

2. **RBI Ombudsman [KB:rbi_ios_2026] par complaint** (1-3 mahine, free): Agar bank 30 din ke andar jawab nahi deta ya reject karta hai, toh RBI ke online portal (cms.rbi.org.in) par free mein complaint file karein.

3. **District Consumer Commission mein shikayat** (3-6 mahine, free / nil court fee): Agar wahan bhi solution na mile, toh e-Jagriti portal par online consumer complaint darj karein [KB:forum_ejagriti]. Rs 5 lakh tak ke case ke liye koi court fee nahi hai [KB:cpa_fee_nil_5lakh].

## What I don't know

- Exact UPI transaction reference ID aur bank complaint ka acknowledgment number kya hai.

- Kya bank ne aapki pehli complaint par koi internal status update diya hai ya nahi.

## Needs lawyer: False - Yeh ek simple failed UPI transaction ka refund case hai jise aap khud National Consumer Helpline [KB:forum_nch] aur RBI Ombudsman [KB:rbi_ios_2026] ke zariye bina kisi lawyer ke solve kar sakte hain.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cpa_consumer_def",
  "cpa_fee_nil_5lakh",
  "cpa_limitation",
  "forum_ejagriti",
  "forum_nch",
  "rbi_ios_2026"
 ]
}

```