# not02_court_summons  (groq:qwen/qwen3.8-27b)

## Input

Mujhe court se summons aaya hai, bank ne loan recovery ka case kiya hai, hearing 28 November 2026 ko hai. Kya karun?

## Reply shown to user

Aapke khilaaf bank ne court mein loan recovery case file kiya hai aur aapko summons mila hai. Hearing 28 November 2026 ko hai, jo ki abhi 15 din ke andar hai. Aapko abhi lawyer ki zaroorat hai kyunki court process shuru ho chuka hai aur deadlines strict hain. Agar aapke paas paisa nahi hai, toh District Legal Services Authority (DLSA) se free lawyer le sakte hain. Pehle bank se likh kar loan agreement aur bank statements maangein, taaki aapko pata chale ki bank ne kitna paisa diya aur aapne kitna wapas kiya. Kya aapne abhi tak kisi lawyer se baat ki hai?

## Red flags (rule engine)

- **COURT** (lawyer): A court process has started. Court deadlines are strict - get a lawyer now, even if only to file a reply.

- **URGENT_DEADLINE** (lawyer): There is a deadline on 2026-11-28 - within 15 days. Get a lawyer now.

## Case file

```json

{
 "problem_type": "notice",
 "problem_subtype": "bank loan recovery summons",
 "user_language": "Hinglish",
 "state": null,
 "city": null,
 "summary": "The user received a court summons regarding a loan recovery case filed by a bank. The hearing is scheduled for 28 November 2026. The user is seeking guidance on how to proceed.",
 "user_goal": "Understand the summons and know the next steps to take before the hearing.",
 "user_role": "other",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "timeline": [
  {
   "date": null,
   "event": "Received court summons for loan recovery case",
   "proof": null
  },
  {
   "date": "2026-11-28",
   "event": "Court hearing scheduled",
   "proof": "Court summons"
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
  "Court summons"
 ],
 "evidence_missing": [
  "Loan agreement",
  "Bank statements showing loan disbursement and repayments",
  "Any previous communication or demand letters from the bank"
 ],
 "risk_signals": [
  "court summons",
  "court hearing"
 ],
 "deadline_mentioned": {
  "date": "2026-11-28",
  "what": "Court hearing for loan recovery case"
 },
 "follow_up_questions": [
  "Aap kis state aur city mein rehte hain?",
  "Summons mein bank ka naam aur case number kya likha hai?",
  "Kya aapke paas loan agreement ya bank se koi purani letter hai?",
  "Kya aapne abhi tak kisi lawyer se baat ki hai?"
 ]
}

```

## Calculation (code)

## Where you stand

Aapke khilaaf bank ne court mein loan recovery case file kiya hai aur aapko summons mila hai. Aapke paas abhi sirf summons hai, lekin loan agreement, bank statements aur purani letters missing hain, jo aapki defense ke liye bahut zaroori hain. Court hearing 28 November 2026 ko hai, jo ki abhi 15 din ke andar hai. Aapki position abhi weak hai kyunki aapke paas proof nahi hai ki aapne kitna paisa diya ya kya bank ne galat calculation ki hai. Aapko abhi lawyer ki zaroorat hai kyunki court process shuru ho chuka hai aur deadlines strict hain.

## Options

1. **Lawyer se turant baat karein** (1-2 din, Free (DLSA) ya low (private lawyer)): Kisi local lawyer se milne ka arrangement karein jo court cases handle karta hai. Unhe summons aur jo bhi documents hain dikhayein. Agar aapke paas paisa nahi hai, toh District Legal Services Authority (DLSA) se free lawyer le sakte hain [KB:lsa_s12_legal_aid].

2. **Bank se documents maangein** (7-15 din, Free): Bank ke branch ya customer care ko likh kar (email/letter) loan agreement, bank statements aur saare demand letters maangein. In documents mein aapko pata chalega ki bank ne kitna paisa diya, aapne kitna wapas kiya, aur kya calculation sahi hai.

3. **Court mein reply file karwayein** (Before 28 November 2026, Court fee + lawyer fee): Lawyer ke saath mil kar court mein apna reply file karwayein. Isme aap bank ke claims ko challenge kar sakte hain agar unke paas proof nahi hai ya calculation galat hai. Agar aap court mein nahi jaate, toh case aapke khilaaf ho sakta hai.

## What I don't know

- Aap kis state aur city mein rehte hain (is se pata chalega ki kaunsi court hai aur DLSA kaunsa hai).

- Summons mein bank ka naam aur case number kya hai.

- Kya aapke paas loan agreement ya bank se koi purani letter hai.

- Kya aapne abhi tak kisi lawyer se baat ki hai.

## Needs lawyer: True - Court process shuru ho chuka hai aur hearing 28 November 2026 ko hai, jo ki abhi 15 din ke andar hai. Court deadlines strict hain aur agar aap lawyer ke bina court mein nahi jaate, toh case aapke khilaaf ho sakta hai. Aapko abhi lawyer ki zaroorat hai.

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