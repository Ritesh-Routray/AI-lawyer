# con02_upi_failed  (gemini:gemini-3.5-flash-lite)

## Input

Bhai maine 8 October 2026 ko UPI se 15000 bheje, paise account se kat gaye par receiver ko nahi mile. Bank ko complaint ki, 3 hafte ho gaye koi jawab nahi. Kya karun?

## Reply shown to user

Aapka 15,000 rupaye ka UPI transaction fail hone ke baad bhi account se debit ho gaya hai aur bank ne abhi tak koi response nahi diya hai. Yeh banking service mein deficiency maani ja sakti hai [KB:cpa_consumer_def]. Aapke paas transaction record hai jo ki ek accha proof hai. Sabse pehle aapko bank se contact karke complaint number ya ticket reference lena chahiye. Agar bank 30 din ke andar action na le, toh aap RBI Ombudsman portal (cms.rbi.org.in) par free mein complaint darj kar sakte hain [KB:rbi_ios_2026]. Kya aapne apne UPI app (jaise Google Pay ya PhonePe) par bhi iski koi complaint ya ticket raise kiya hai?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "failed UPI transaction refund not processed",
 "user_language": "Hinglish",
 "state": null,
 "city": null,
 "summary": "The user transferred 15000 via UPI on 8 October 2026, but the amount was debited without reaching the receiver. Although the bank was notified, no response has been received after 3 weeks.",
 "user_goal": "Get a refund of the failed UPI transaction amount from the bank.",
 "user_role": "consumer",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "timeline": [
  {
   "date": "2026-10-08",
   "event": "Transferred 15000 via UPI which was debited but not received by the payee",
   "proof": "bank statement / UPI transaction screenshot"
  },
  {
   "date": null,
   "event": "Raised a complaint with the bank",
   "proof": "complaint number"
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
 "evidence_have": [
  "bank transaction record"
 ],
 "evidence_missing": [
  "complaint number or copy",
  "bank response or ticket reference"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Aap kaunse state mein rehte hain?",
  "Kya aapke paas bank complaint number ya complaint ki copy hai?",
  "Kya aapne UPI app (jaise Google Pay, PhonePe, Paytm) par bhi ticket raise kiya tha?"
 ]
}

```

## Calculation (code)

- Amount paid: Rs 15,000

- Refund due: Rs 15,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Consumer Protection Act, 2019 Section 88 (OFFENCES AND PENALTIES) p.33

- Consumer Protection Act, 2019 Section 69  p.28

- Consumer Protection Act, 2019 Section 35  p.18

- Consumer Protection Act, 2019 Section 4  p.10

- Consumer Protection Act, 2019 Section 34  p.17

- Consumer Protection Act, 2019 Section 47  p.23

- Consumer Protection Act, 2019 Section 20  p.14

- Constitution of India Article 365 (234) p.5

## Where you stand



## Options

1. **Bank aur UPI App se follow-up karein** (1-2 days, free): Apne bank aur UPI app (jaise Google Pay, PhonePe, Paytm) par dobara contact karke complaint number ya ticket reference lein.

2. **RBI Ombudsman [KB:rbi_ios_2026] par complaint karein** (1 week, free): Agar bank 30 din ke andar jawab na de ya refund na kare, toh cms.rbi.org.in par online complaint darj karein [KB:rbi_ios_2026].

3. **National Consumer Helpline [KB:forum_nch] (NCH)** (1-2 weeks, free): NCH helpline 1915 par call karein ya consumerhelpline.gov.in par apni shikayat darj karein [KB:forum_nch].

## What I don't know

- Kya bank ki taraf se koi internal technical error ki wajah se delay hua hai.

- Kya aapne UPI app par bhi alag se ticket raise kiya tha ya nahi.

## Needs lawyer: False - Yeh ek simple failed UPI transaction ka mamla hai jise aap khud bank, NCH, ya RBI Ombudsman [KB:rbi_ios_2026] ke zariye solve kar sakte hain. Iske liye abhi lawyer ki zaroorat nahi hai.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cpa_consumer_def",
  "cpa_limitation",
  "forum_nch",
  "rbi_ios_2026"
 ],
 "support_check": "not auto-checked (non-English reply; cross-encoder is English-only)"
}

```