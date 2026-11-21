# dep04_threat_police  (gemini:gemini-3.5-flash)

## Input

Landlord in Noida is refusing to return my 40000 deposit and when I went to ask, his son pushed me and threatened to beat me up if I come again. Should I go to the police? I also want my money.

## Reply shown to user

I am so sorry you had to go through this. I am an assistant, not a lawyer, but your safety is the most important thing right now. 

Because the landlord's son physically pushed and threatened you, this is not just a deposit dispute—it involves a serious criminal angle. You have a legal right to claim your Rs 40,000 security deposit back [KB:ica_s73, KB:deposit_civil_route], but because of the physical threat, you should speak to a lawyer or legal advice provider before taking any step alone.

If you qualify, you can get free legal assistance through the District Legal Services Authority or call the NALSA helpline at 15100 [KB:lsa_s12_legal_aid]. A lawyer can guide you on reporting the assault to the police safely while also sending a legal notice to recover your money.

Do you have a written rent agreement or any bank receipts showing the Rs 40,000 payment?

## Red flags (rule engine)

- **CRIMINAL** (lawyer): This involves police or possible criminal matters. Talk to a lawyer before you act or say anything.

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "deposit non-refund with physical threat",
 "user_language": "English",
 "state": "Uttar Pradesh",
 "city": "Noida",
 "summary": "The user is demanding the return of a 40,000 INR security deposit from their landlord in Noida. When the user confronted the landlord, the landlord's son physically pushed and threatened the user with violence.",
 "user_goal": "Wants to know if they should report the landlord to the police and wants to recover the deposit money.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": null,
   "event": "User asked for the return of the deposit, and the landlord's son pushed and threatened them.",
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
  "chat history or written communication demanding refund",
  "cctv footage or witness details of the physical threat"
 ],
 "risk_signals": [
  "physical assault / pushed by landlord's son",
  "threat of violence"
 ],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Do you have a registered rent agreement or rent receipts for the deposit payment?",
  "When did you vacate the property, or when was the deposit due for refund?",
  "Do you have any WhatsApp messages or call recordings of the landlord refusing the deposit or making threats?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 40,000

- Amount to claim: Rs 40,000

## Where you stand

You have a clear financial claim to recover your security deposit of Rs 40,000 [KB:ica_s73]. However, because you were physically pushed and threatened with violence, your safety comes first and this has taken a criminal dimension. While deposit disputes can generally be resolved through written demand or civil court [KB:deposit_civil_route], physical threats require immediate legal protection. You currently lack written evidence of the incident and rent agreement details, which weakens your immediate position without formal legal help.

## Options

1. **Consult a lawyer or Legal Aid immediately** (Immediate (1-2 days), Varies / Free via Legal Aid if eligible): Before taking further direct action against the landlord, speak with a legal professional or file a report regarding the physical threat and assault.

2. **Gather documentary evidence** (1-3 days, Free): Collect bank statements showing the deposit payment of Rs 40,000 and try to get written or message acknowledgement of the deposit amount.

3. **Send a legal notice for deposit recovery** (1-2 weeks, Lawyer fee): Have a lawyer issue a formal legal notice demanding the refund of Rs 40,000 [KB:ica_s73] while noting the unlawful conduct.

## What I don't know

- Whether you have a written or registered rent agreement.

- Whether you have reported the physical assault and threat to the local police.

- Whether you have vacated the premises completely.

## Needs lawyer: True - There is a serious safety concern involving physical assault and threat of violence, which involves potential police/criminal action. You need professional legal guidance before confronting the landlord or filing complaints.

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