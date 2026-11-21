# not02_court_summons  (groq:openai/gpt-oss-120b)

## Input

Mujhe court se summons aaya hai, bank ne loan recovery ka case kiya hai, hearing 28 November 2026 ko hai. Kya karun?

## Reply shown to user

Aapko bank ke loan recovery case ka court summons mila hai aur hearing 28 Nov ko hai. Sabse pehle, summons ki copy aur loan agreement ya koi bhi bank ki notice ikattha karein. Yeh saboot aapke defence ke liye bahut important hain. Phir, NALSA helpline 15100 par call karke free legal aid ke liye apply karein ya apne najdeeki District Legal Services Authority se lawyer lein. Lawyer aapke paas maujood saboot dekhkar court me likhit reply file karega ya settlement ki koshish karega. Kya aapke paas loan agreement ya bank ki koi written communication hai?

## Red flags (rule engine)

- **COURT** (lawyer): A court process has started. Court deadlines are strict - get a lawyer now, even if only to file a reply.

- **URGENT_DEADLINE** (lawyer): There is a deadline on 2026-11-28 - within 15 days. Get a lawyer now.

## Case file

```json

{
 "problem_type": "notice",
 "problem_subtype": "court summons for loan recovery",
 "user_language": "Hindi written in Roman (English) letters, the way the person wrote",
 "state": null,
 "city": null,
 "summary": "User has received a court summons regarding a loan recovery case filed by a bank, with a hearing scheduled on 28 November 2026.",
 "user_goal": "to understand what steps to take in response to the court summons",
 "user_role": "other",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "timeline": [
  {
   "date": "2026-11-28",
   "event": "court hearing for loan recovery case",
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
  "loan agreement",
  "court summons copy",
  "bank recovery notice",
  "any correspondence with the bank"
 ],
 "risk_signals": [
  "court summons",
  "loan recovery case"
 ],
 "deadline_mentioned": {
  "date": "2026-11-28",
  "what": "court hearing"
 },
 "follow_up_questions": [
  "Aap kis state aur city mein rehte hain?",
  "Bank ka naam aur loan ka amount kya hai?",
  "Kya aapke paas court summons ya bank ki notice ka copy hai?",
  "Kya aapne bank se koi settlement ya repayment ka proposal kiya hai?"
 ]
}

```

## Calculation (code)

## Where you stand

Aapko bank ke loan recovery case ka court summons mila hai aur hearing 28 Nov 2026 ko hai. Aapke paas abhi tak loan agreement, summons ki copy ya bank ki notice nahi hai, jo aapke defence ke liye zaroori saboot ho sakte hain. Summons aane se aapke paas limited samay hai aur court ki deadline strict hoti hai, isliye turant lawyer se milna zaroori hai. Agar aapke paas loan ka likhit agreement ya bank ke saath koi settlement ki baat-cheet ka record ho, to aapka case majboot ho sakta hai. [KB:lsa_s12_legal_aid]

## Options

1. **Summons ki copy aur loan documents ikattha karein** (1-2 din, free): Bank se ya court clerk se summons ki hard copy aur loan agreement ki copy maangein. Agar email ya WhatsApp me koi communication hai to uska screenshot lein.

2. **Free legal aid ya lawyer se milen** (2-5 din, free (if eligible)): NALSA helpline 15100 par call karein ya apne najdeeki District Legal Services Authority se free lawyer ke liye apply karein. Agar aap eligible hain to free legal aid mil sakti hai. [KB:lsa_s12_legal_aid]

3. **Lawyer ke through written reply file karein** (5-7 din (lawyer ke schedule par depend), court fee + lawyer fees (free legal aid if eligible)): Lawyer aapke paas available saboot dekhkar court me written reply (defence) file karega, ya settlement proposal bhejega. Yeh reply hearing se pehle file karna zaroori hai.

## What I don't know

- Loan ka exact amount, interest rate aur repayment schedule

- Aap kis state/city me rehte hain, jo local court rules par asar daal sakta hai

- Bank ka naam aur aapke loan ka type (personal, home, etc.)

## Needs lawyer: True - Court process shuru ho chuka hai aur hearing 28 Nov 2026 ko hai. Court ki deadlines strict hoti hain, isliye aapko abhi lawyer ki madad chahiye, chahe free legal aid ke through ho.

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