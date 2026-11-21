# not02_court_summons  (gemini:gemini-3.5-flash-lite)

## Input

Mujhe court se summons aaya hai, bank ne loan recovery ka case kiya hai, hearing 28 November 2026 ko hai. Kya karun?

## Reply shown to user

Namaste! Aapko bank loan recovery ke liye court ka summons mila hai aur 28 November 2026 ki hearing hai. Kyunki court ki baat hai, aapko turant ek lawyer ya apne nazdiki District Legal Services Authority (DLSA) se madad leni chahiye. Aap NALSA helpline 15100 par bhi call karke free guidance le sakte hain [KB:lsa_s12_legal_aid]. Loan agreement aur bank notices ko ek jagah ikattha karein. Kya aapke paas is loan se juda koi purana paper ya bank statement abhi available hai?

## Red flags (rule engine)

- **COURT** (lawyer): A court process has started. Court deadlines are strict - get a lawyer now, even if only to file a reply.

- **URGENT_DEADLINE** (lawyer): There is a deadline on 2026-11-28 - within 15 days. Get a lawyer now.

- **OUT_OF_SCOPE** (caution): This problem is outside what this assistant covers in depth (deposits, consumer refunds, unpaid salary). I can only give general direction.

## Case file

```json

{
 "problem_type": "other",
 "problem_subtype": "bank loan recovery court summons",
 "user_language": "Hinglish",
 "state": null,
 "city": null,
 "summary": "The user received a court summons regarding a loan recovery case filed by a bank. The upcoming court hearing is scheduled for 28 November 2026 and they are seeking guidance on what to do.",
 "user_goal": "Understand what actions to take regarding the court summons for loan recovery",
 "user_role": "other",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "timeline": [
  {
   "date": "2026-11-28",
   "event": "Court hearing scheduled for loan recovery case",
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
  "Bank notices or loan account statements"
 ],
 "risk_signals": [
  "court summons/hearing"
 ],
 "deadline_mentioned": {
  "date": "2026-11-28",
  "what": "Court hearing date"
 },
 "follow_up_questions": [
  "Aap kaunse state aur city mein rehte hain?",
  "Kya aapke paas loan agreement aur bank ki taraf se aaye purane notices ki copy hai?",
  "Bank ne kitne amount ke recovery ka case kiya hai?"
 ]
}

```

## Calculation (code)

## Where you stand

Aapko bank loan recovery ke liye court ka summons mila hai jiska hearing 28 November 2026 ko hai. Kyunki court ka notice aa chuka hai, yeh ek serious legal matter hai jisme time limit bahut strict hoti hai [KB:lsa_s12_legal_aid]. Hamare paas is case ke liye detailed legal provisions aur amounts ki jankari nahi hai, aur court cases ke liye aapko turant ek lawyer ki zarurat padegi [KB:lsa_s12_legal_aid]. Aap free ya subsidized legal aid ke liye District Legal Services Authority (DLSA) se bhi sampark kar sakte hain [KB:lsa_s12_legal_aid].

## Options

1. **Free Legal Aid Contact** (Turant, free): NALSA helpline 15100 par call karein ya apne nazdiki DLSA office ya Tele-Law center jayein free advice ke liye [KB:lsa_s12_legal_aid].

2. **Vakeel se milein** (1-3 din, Vakeel ki fees par nirbhar karta hai): Ek advocate se turant milein jo bank recovery cases dekhte hain aur court date se pehle apna jawab (written statement) taiyar karwayein.

## What I don't know

- Loan ka total kitna amount bacha hai

- Aapka state aur city kaunsa hai

- Bank ke sath loan agreement ki exact terms kya thi

## Needs lawyer: True - A court case and summons already exist, which requires immediate legal representation to file a proper reply before the hearing date.

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