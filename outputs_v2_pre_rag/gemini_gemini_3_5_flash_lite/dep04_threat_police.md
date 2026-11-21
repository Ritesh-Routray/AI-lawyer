# dep04_threat_police  (gemini:gemini-3.5-flash-lite)

## Input

Landlord in Noida is refusing to return my 40000 deposit and when I went to ask, his son pushed me and threatened to beat me up if I come again. Should I go to the police? I also want my money.

## Reply shown to user

Hello. I understand you are trying to recover your 40000 rupees security deposit in Noida, but facing threats and physical pushing makes this a serious safety matter rather than a simple money dispute. When physical violence or threats are involved, it is important not to handle it alone. Your first priority should be your safety, which may involve filing a police complaint about the threats. For recovering your money, a lawyer can help send a formal notice or guide you through the civil recovery process [KB:deposit_civil_route]. You can also reach out to the District Legal Services Authority for free legal assistance if needed [KB:lsa_s12_legal_aid]. Do you currently have any audio recordings, text messages, or witnesses to the threats made by the landlord's son?

## Red flags (rule engine)

- **CRIMINAL** (lawyer): This involves police or possible criminal matters. Talk to a lawyer before you act or say anything.

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "landlord refusing security deposit refund and issuing threats",
 "user_language": "English",
 "state": "Uttar Pradesh",
 "city": "Noida",
 "summary": "The user states that their landlord in Noida is refusing to return a security deposit of 40000 rupees. When the user went to ask for the money, the landlord's son physically pushed them and threatened them.",
 "user_goal": "Get the security deposit refunded and understand how to handle the threats.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": null,
   "event": "Landlord refused to return the security deposit of 40000",
   "proof": null
  },
  {
   "date": null,
   "event": "Landlord's son pushed the user and threatened to beat them up when asked for money",
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
  "chat messages or call logs regarding deposit or threats"
 ],
 "risk_signals": [
  "threats",
  "physical violence/pushing"
 ],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Do you have a written rent agreement or receipts for the 40000 deposit transfer?",
  "When did you vacate the property and ask for the refund?",
  "Do you have any audio, video, or message proof of the threats made by the landlord's son?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 40,000

- Amount to claim: Rs 40,000

## Where you stand

You are in a difficult position because your landlord's family has used physical force and threats, which is a serious safety concern [KB:deposit_civil_route]. While you have a valid claim for your security deposit under contract principles [KB:ica_s73], the presence of violence means you should not confront them alone. Because there is a criminal/safety angle involving threats and pushing, you need to consult a lawyer or approach the police before taking further steps. You can also contact the Legal Services Authority for free guidance if needed [KB:lsa_s12_legal_aid].

## Options

1. **Report threats to local police** (Immediately, Free): File a police complaint regarding the physical pushing and threats of violence.

2. **Consult a lawyer for safety and recovery** (1-3 days, Varies): Speak with a lawyer to handle both the threat aspect and the legal notice for your deposit recovery [KB:deposit_civil_route].

## What I don't know

- Whether you have a written rent agreement specifying deposit return terms

- If there are any independent witnesses to the physical pushing and threats

## Needs lawyer: True - A lawyer is needed immediately because the situation involves physical violence, threats, and potential criminal conduct, which goes beyond a simple civil money dispute.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "ica_s73",
  "lsa_s12_legal_aid"
 ]
}

```