# con02_upi_failed  (groq:qwen/qwen3.8-27b)

## Input

Bhai maine 8 October 2026 ko UPI se 15000 bheje, paise account se kat gaye par receiver ko nahi mile. Bank ko complaint ki, 3 hafte ho gaye koi jawab nahi. Kya karun?

## Reply shown to user

Aapka case strong hai kyunki aapne 15,000 INR UPI se bheja tha jo debit hua lekin receiver ko nahi mila, aur aapne bank mein complaint bhi kar di hai. Pehle bank se written follow-up karein aur unse complaint ka ticket number maangein. Agar 30 din se zyada ho gaya hai, toh RBI Ombudsman [KB:rbi_ios_2026] par free complaint file karein. Aapke paas 2 saal ka time limit hai consumer complaint file karne ke liye. Kya aapke paas UTR number ya bank complaint ticket number hai?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "failed UPI transaction refund pending",
 "user_language": "Hinglish",
 "state": null,
 "city": null,
 "summary": "The user sent 15000 INR via UPI on 2026-10-08, which was debited from their account but not credited to the receiver. They filed a complaint with their bank three weeks ago but have not received a response or refund.",
 "user_goal": "Get the 15000 INR refunded or resolved by the bank.",
 "user_role": "consumer",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "timeline": [
  {
   "date": "2026-10-08",
   "event": "Sent 15000 INR via UPI; amount debited from user's account but not received by beneficiary.",
   "proof": null
  },
  {
   "date": "2026-10-29",
   "event": "Filed a complaint with the bank regarding the failed transaction.",
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
  "order_value": 15000,
  "amount_refunded": null
 },
 "evidence_have": [],
 "evidence_missing": [
  "UPI transaction reference number (UTR/VPA)",
  "Bank complaint ticket number or email acknowledgment",
  "Bank statement showing the debit entry"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Aapka bank kaunsa hai aur aap kis state/city mein rehte hain?",
  "Kya aapke paas UPI transaction ka reference number (UTR) ya bank complaint ka ticket number hai?",
  "Bank ne koi written acknowledgment (email/SMS) complaint ke baare mein diya tha?"
 ]
}

```

## Calculation (code)

- Amount paid: Rs 15,000

- Refund due: Rs 15,000

## Where you stand

Aapka case strong hai kyunki aapne 15,000 INR UPI se bheja tha jo debit hua lekin receiver ko nahi mila, aur aapne bank mein complaint bhi kar di hai. Aap ek consumer hain aur bank ki taraf se refund na milna ek deficiency in service ho sakta hai [KB:cpa_consumer_def]. Abhi tak koi red flag nahi hai, lekin aapke paas UTR number, bank complaint ticket, aur bank statement jaise important proofs missing hain. Aapke paas 2 saal ka time limit hai consumer complaint file karne ke liye [KB:cpa_limitation], isliye abhi bhi time hai. Pehle RBI Ombudsman ya National Consumer Helpline jaise free options try karna chahiye [KB:rbi_ios_2026] [KB:forum_nch].

## Options

1. **Bank se written follow-up** (1-2 din, free): Bank ke customer care ko call karein aur complaint ka status puchein. Unse email ya SMS mein written acknowledgment maangein. Agar 30 din se zyada ho gaya hai, toh RBI Ombudsman [KB:rbi_ios_2026] ke liye ready hain.

2. **National Consumer Helpline [KB:forum_nch] (NCH) par complaint** (1-2 hafte, free): 1915 par call karein ya consumerhelpline.gov.in par online complaint file karein. NCH bank ko forward karega aur aksar refund bina case ke mil jata hai. Yeh free hai.

3. **RBI Ombudsman [KB:rbi_ios_2026] par complaint** (2-4 hafte, free): Agar bank ne 30 din mein reply nahi diya ya reject kiya, toh cms.rbi.org.in par free complaint file karein. Yeh 1 saal ke andar karna hai bank ke reply ke baad.

4. **District Consumer Commission par complaint** (1-3 mahine, free (filing fee nil)): Agar upar wale steps fail ho jayein, toh e-Jagriti [KB:forum_ejagriti] portal par online complaint file karein. Rs 5 lakh tak ki complaints ke liye court fee nil hai, aur aap khud file kar sakte hain.

## What I don't know

- Aapka bank kaunsa hai aur kis state/city mein aap rehte hain.

- Kya aapke paas UTR number ya bank complaint ticket number hai.

- Bank ne koi written acknowledgment diya tha ya nahi.

## Needs lawyer: False - Abhi ke liye lawyer zaroori nahi hai kyunki aap pehle bank, NCH, ya RBI Ombudsman [KB:rbi_ios_2026] jaise free steps try kar sakte hain. Agar in steps se result na mile ya case complex ho jaye, tab lawyer ki zaroorat ho sakti hai.

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
 ]
}

```