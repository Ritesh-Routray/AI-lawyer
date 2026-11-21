# con02_upi_failed  (groq:openai/gpt-oss-120b)

## Input

Bhai maine 8 October 2026 ko UPI se 15000 bheje, paise account se kat gaye par receiver ko nahi mile. Bank ko complaint ki, 3 hafte ho gaye koi jawab nahi. Kya karun?

## Reply shown to user

Aapka paisa UPI se deduct ho gaya lekin receiver ko nahi mila, isliye service mein deficiency hai [KB:cpa_consumer_def]. Aapke paas transaction receipt aur bank statement hai – ye strong proof hain, lekin bank ka complaint reference ya receiver ka confirmation abhi missing hai. Sabse pehle, bank ke grievance officer ko likhit complaint bhejein aur 48 ghante ke acknowledgement ka demand karein [KB:ecom_grievance_officer]. Agar 30 din mein koi reply nahi milta, to RBI Ombudsman portal par free complaint file karein [KB:rbi_ios_2026]. Saath hi, National Consumer Helpline (1915) se bhi madad le sakte hain, wo bank ko pressure mein la sakte hain [KB:forum_nch]. Agar in steps se solution nahi milta, to aap e‑Jagriti portal se District Consumer Commission me nil filing fee ke saath complaint file kar sakte hain [KB:cpa_fee_nil_5lakh]. Kya aapke paas bank se koi acknowledgement ya reference number hai?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "UPI transfer not received",
 "user_language": "Hinglish",
 "state": null,
 "city": null,
 "summary": "The user sent a UPI payment of 15000 on 8 October 2026, the amount was deducted from their account but the receiver did not get it. They lodged a complaint with the bank, but after three weeks there has been no response.",
 "user_goal": "Get the transferred amount credited to the receiver or refunded to the sender.",
 "user_role": "consumer",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "timeline": [
  {
   "date": "2026-10-08",
   "event": "Sent 15000 via UPI; amount deducted from sender's account",
   "proof": "bank statement or UPI transaction receipt"
  },
  {
   "date": "2026-10-29",
   "event": "No response from bank after filing complaint",
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
 "evidence_have": [
  "UPI transaction receipt",
  "bank statement showing deduction"
 ],
 "evidence_missing": [
  "complaint reference number or acknowledgment from bank",
  "any communication from the receiver confirming non-receipt"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": ""
 },
 "follow_up_questions": [
  "Aap kis state aur city mein rehte hain?",
  "Bank ko complaint karte waqt aapko koi reference number ya complaint ID mili thi?",
  "Kya aapke paas transaction ka screenshot ya UPI receipt hai?",
  "Receiver ne aapko koi reply ya confirmation diya hai?"
 ]
}

```

## Calculation (code)

## Where you stand

Aap ek consumer hain kyunki aapne UPI ke through service (payment) li. Bank ne aapka paisa deduct kar diya lekin receiver ko nahi mila, isliye service mein deficiency hai [KB:cpa_consumer_def]. Aapke paas transaction receipt aur bank statement hai – ye strong proof hain. Lekin aapke paas bank ka complaint reference ya receiver ka non‑receipt confirmation nahi hai, jo aapke case ko thoda weak bana sakta hai. Abhi tak 2‑year limitation period ka koi issue nahi hai [KB:cpa_limitation].

## Options

1. **RBI Ombudsman [KB:rbi_ios_2026] ko complain karein** (2-3 weeks, free): Bank ki grievance ko likhit roop mein (email/letter) bhejein, complaint reference ya acknowledgement ka screenshot lein. 30 din ke andar reply na milne par RBI Ombudsman [KB:rbi_ios_2026] portal (cms.rbi.org.in) par free complaint file karein. Attach transaction receipt, bank statement, aur bank se milne wali koi bhi communication.

2. **Bank ke grievance officer ko likhit complaint** (1-2 weeks, free): Bank ki website ya app par grievance officer ka contact dhundein (usually 48‑hour acknowledgement hota hai). Apni UPI receipt aur statement attach karte hue ek formal email/letter bhejein, reference number maangein. 1 month ke andar response ka demand karein.

3. **National Consumer Helpline [KB:forum_nch] (NCH) se madad lein** (a few days, free): 1915 par call karein ya consumerhelpline.gov.in par online complaint file karein. Unko sabhi documents (receipt, statement, bank ke saath ki hui baatein) bhejein. NCH aapke liye bank ko pressure mein la sakta hai aur refund ya credit ki request ko aage badha sakta hai.

4. **District Consumer Commission me complaint file karein** (1-2 months (including hearing), nil filing fee): e‑Jagriti portal (e‑Jagriti) par login karke consumer complaint file karein. Value Rs 15,000 hone ki wajah se District Commission me jaayega, filing fee nil hai [KB:cpa_fee_nil_5lakh]. Sabhi documents (receipt, bank statement, grievance officer ka response ya uska na hona) upload karein.

## What I don't know

- Bank ka exact grievance officer ka contact detail

- Receiver ka exact response ya proof ki unhone paise receive nahi kiye

## Needs lawyer: False - Abhi tak aapke paas simple pre‑litigation steps hain (bank grievance, RBI Ombudsman [KB:rbi_ios_2026], NCH). Lawyer ki zaroorat tab hogi jab in sabka koi fayda na ho ya aapko District Commission me formal hearing attend karni pade.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cpa_consumer_def",
  "cpa_fee_nil_5lakh",
  "cpa_limitation",
  "ecom_grievance_officer",
  "forum_nch",
  "rbi_ios_2026"
 ]
}

```