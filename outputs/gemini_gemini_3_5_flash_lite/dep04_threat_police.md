# dep04_threat_police  (gemini:gemini-3.5-flash-lite)

## Input

Landlord in Noida is refusing to return my 40000 deposit and when I went to ask, his son pushed me and threatened to beat me up if I come again. Should I go to the police? I also want my money.

## Reply shown to user

Your situation is serious because it involves not just a disputed security deposit of Rs 40,000, but also physical threats and intimidation from the landlord's side. While tenants generally have a right to get their deposit back after handing over possession [KB:src_mta_2021_11], safety and criminal risks take priority. You should consult a lawyer or contact the District Legal Services Authority (DLSA) at helpline 15100 before taking further steps [KB:lsa_s12_legal_aid] [KB:deposit_civil_route]. Do you have any written records, such as bank transfer proofs or messages, showing that you paid the Rs 40,000 deposit?

## Red flags (rule engine)

- **CRIMINAL** (lawyer): This involves police or possible criminal matters. Talk to a lawyer before you act or say anything.

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "landlord refusing security deposit refund and threatening tenant",
 "user_language": "English",
 "state": "Uttar Pradesh",
 "city": "Noida",
 "summary": "The user states that their landlord in Noida is refusing to return their security deposit of 40000. When the user went to ask for the money, the landlord's son pushed them and threatened them.",
 "user_goal": "Get the security deposit back and understand whether to approach the police regarding the threats",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": null,
   "event": "Landlord refused to return the security deposit and landlord's son pushed and threatened the user",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": 40000,
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
  "rent agreement",
  "bank statement showing deposit transfer",
  "chat history or call recordings regarding the deposit"
 ],
 "risk_signals": [
  "threats",
  "violence",
  "police"
 ],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Do you have a written rent agreement or receipts showing you paid the 40000 deposit?",
  "Which state and city did this happen in?",
  "When did you vacate the property and ask for the refund?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 40,000

- Amount to claim: Rs 40,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Model Tenancy Act, 2021 Section 11  p.11

- Model Tenancy Act, 2021 Section 10  p.11

- Model Tenancy Act, 2021 Section 14  p.12

- Model Tenancy Act, 2021 Section 15  p.13

- Model Tenancy Act, 2021 Section 24  p.18

- Model Tenancy Act, 2021 Section 23  p.18

- Model Tenancy Act, 2021 Section 12 (RIGHTS AND OBLIGATIONS OF LANDLORD AND TENANT) p.12

## Where you stand

Your landlord in Noida is refusing to return your security deposit of Rs 40,000 [KB:deposit_civil_route], and you face a serious issue because the landlord's son reportedly pushed and threatened you. Since physical threats and violence are involved, this has crossed from a simple civil rental dispute into a potential criminal matter. Your strength is that security deposits must generally be refunded upon handing back possession [KB:src_mta_2021_11], but your weakness right now is the lack of written proof and the safety risk posed by threats. You must handle the safety aspect with priority.

## Options

1. **Consult a Lawyer / Legal Aid** (Immediately, Free via DLSA or nominal consultation fee): Because there are threats and physical intimidation involved, speak to a lawyer or approach the District Legal Services Authority (DLSA) for guidance before taking any further action.

2. **Report Threats to Police** (As soon as possible, Free): If you have been physically threatened or pushed, consider filing a police complaint regarding the intimidation and assault for your personal safety.

3. **Send a Written Demand Notice** (1-2 weeks, Low to moderate (lawyer fee)): Through a lawyer, send a formal written demand notice to the landlord for the return of your security deposit [KB:deposit_civil_route].

## What I don't know

- Whether you have a signed written rent agreement covering the exact terms of the deposit refund.

- Whether Uttar Pradesh has formally implemented specific provisions of the Model Tenancy Act [KB:mta_s11_deposit] locally.

- Whether there are any counter-claims or unpaid rent alleged by the landlord.

## Needs lawyer: True - A lawyer is needed because the situation involves physical threats, intimidation, and potential police/criminal angles rather than just a straightforward money recovery.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "lsa_s12_legal_aid",
  "src_mta_2021_11"
 ],
 "support_check": {
  "checked": 2,
  "unsupported": []
 }
}

```