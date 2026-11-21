# not02_court_summons  (gemini:gemini-3.5-flash-lite)

## Input

Mujhe court se summons aaya hai, bank ne loan recovery ka case kiya hai, hearing 28 November 2026 ko hai. Kya karun?

## Reply shown to user

Namaste! Aapko bank loan recovery case mein court summons mila hai aur hearing 28 November 2026 ko hai. Kyunki yeh court ka mamla hai, ismein deri nahi karni chahiye aur turant ek vakil ki madad leni chahiye taaki aap court mein apna jawab time par de sakein. Agar aapke paas vakil ki fees ke liye paise nahi hain, toh aap NALSA helpline (15100) par call karke DLSA se free legal aid bhi le sakte hain. Kya aapne apne loan agreement ya bank ke notices ko ek jagah collect kar liya hai?

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
 "summary": "The user received a court summons regarding a loan recovery case filed by a bank, with a scheduled hearing on 28 November 2026. They are seeking guidance on what to do next.",
 "user_goal": "Understand how to respond to the court summons and loan recovery case",
 "user_role": "other",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "timeline": [
  {
   "date": "2026-11-28",
   "event": "Court hearing scheduled for loan recovery case",
   "proof": "court summons"
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
  "court summons"
 ],
 "evidence_missing": [
  "loan agreement",
  "bank loan account statements",
  "notice received from bank before the court case"
 ],
 "risk_signals": [
  "court summons/hearing"
 ],
 "deadline_mentioned": {
  "date": "2026-11-28",
  "what": "Court hearing date"
 },
 "follow_up_questions": [
  "Aap kaun se state aur city mein rehte hain?",
  "Kya aapke paas bank ka loan agreement ya loan account statement hai?",
  "Kya court summons ke sath bank ki taraf se koi notice ya copy mili thi?"
 ]
}

```

## Calculation (code)

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 69  p.21

- Constitution of India Article 39A (against moral and material abandonment.]) p.2

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 68  p.21

- Constitution of India Article 43  p.2

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 70  p.21

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 63 (A.-Summons) p.20

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 71  p.21

- Bharatiya Nagarik Suraksha Sanhita, 2023 Section 91  p.26

## Where you stand

Aapko bank loan recovery case ke silsile mein court summons mila hai aur hearing 28 November 2026 ko hai. Kyunki yeh ek court matter hai aur deadline nazdeek hai, aapko turant ek lawyer ki zarurat hai taaki aap apna jawab sahi samay par daakhil kar sakein [KB:src_bnss_2023_63]. Hamare paas loan agreement ya bank statements nahi hain, isliye case ki gehraai se jaanch ek vakil hi kar sakte hain. Agar aap financially kamzor hain, toh aap District Legal Services Authority (DLSA) se free legal aid bhi le sakte hain [KB:lsa_s12_legal_aid].

## Options

1. **Free Legal Aid Contact** (1-2 din, free): District Legal Services Authority (DLSA) ya NALSA helpline (15100) par sampark karein agar aapko muft vakil ki madad chahiye.

2. **Hire a Lawyer** (Turant (hearing se pehle), Lawyer ki fees par nirbhar hai): Ek civil ya banking matters ke vakil se milein aur court summons unhe dikhakar agla kadam uthayein.

## What I don't know

- Loan ki exact rakam aur agreement ki shartein kya hain.

- Kya bank ne pehle koi legal notice bheja tha ya nahi.

- Kaunsa state aur local jurisdiction lagu hota hai.

## Needs lawyer: True - Aapko court summons mil chuka hai aur hearing ki date fixed hai. Court ke mamlo mein strict deadlines hoti hain, isliye turant ek lawyer ki zarurat hai.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "lsa_s12_legal_aid",
  "src_bnss_2023_63"
 ],
 "support_check": "not auto-checked (non-English reply; cross-encoder is English-only)"
}

```