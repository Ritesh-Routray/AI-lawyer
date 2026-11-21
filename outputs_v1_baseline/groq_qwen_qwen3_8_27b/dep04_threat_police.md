# dep04_threat_police  (groq:qwen/qwen3.8-27b)

## Input

Landlord in Noida is refusing to return my 40000 deposit and when I went to ask, his son pushed me and threatened to beat me up if I come again. Should I go to the police? I also want my money.

## Reply shown to user

I am sorry you are dealing with this. Your safety is the first priority. Since the landlord's son pushed you and threatened violence, you should not return to the property. I strongly recommend you file a police complaint (FIR) at the nearest Noida police station to record this incident. This is a criminal matter, and I am not a lawyer, so please consult one for specific advice on how to handle the police interaction. 

Regarding the Rs 40,000 deposit, you have a strong claim if you can prove you paid it. Your first step after ensuring your safety is to send a written demand letter to the landlord asking for the return of the deposit within 7 days. Keep a copy of this letter. If they ignore you, you can then approach a civil court or the Rent Authority. Do you have a bank statement or receipt showing the deposit payment?

## Red flags (rule engine)

- **CRIMINAL** (lawyer): This involves police or possible criminal matters. Talk to a lawyer before you act or say anything.

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit retention with physical threat",
 "user_language": "English",
 "state": "Uttar Pradesh",
 "city": "Noida",
 "summary": "The user is a tenant in Noida whose landlord is refusing to return a security deposit of 40,000 rupees. During a confrontation, the landlord's son physically pushed the user and threatened violence if they returned to the property.",
 "user_goal": "Recover the 40000 rupee security deposit and seek guidance on whether to file a police complaint regarding the threats.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": null,
   "event": "Landlord refused to return the security deposit",
   "proof": null
  },
  {
   "date": null,
   "event": "User visited landlord to ask for deposit; landlord's son pushed user and threatened violence",
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
  "bank statement or receipt showing deposit payment",
  "written communication (messages/emails) regarding deposit return",
  "police FIR or complaint record regarding the threat"
 ],
 "risk_signals": [
  "physical assault",
  "threat of violence",
  "police involvement"
 ],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Do you have a written rent agreement and proof of the 40000 deposit payment (bank transfer/receipt)?",
  "When did you move out of the property, and did you hand over the keys to the landlord?",
  "Did you file a police complaint (FIR) regarding the push and threats, or is this still just a verbal threat?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 40,000

- Amount to claim: Rs 40,000

## Where you stand

You are in a strong position to recover your Rs 40,000 deposit, but the situation has become dangerous due to the physical threat. Your main strength is the clear amount owed, but your biggest weakness is the lack of written proof like a rent agreement or payment receipt [KB:deposit_civil_route]. The landlord's son's actions create a serious safety risk that needs immediate attention separate from the money claim. Because there is a criminal angle involving assault and threats, you must be very careful about how you proceed.

## Options

1. **Prioritize Safety & Police Complaint** (1-2 hours, Free): Do not return to the property. Go to the nearest police station in Noida to file a complaint (FIR) regarding the push and threats. This creates an official record of the criminal act and protects you from further harassment.

2. **Send Written Demand for Deposit** (1 day, Low (postage/printing)): Send a formal written demand letter or email to the landlord for the Rs 40,000. Clearly state that you have vacated the property and demand the return of the deposit within 7 days. Keep a copy of this communication.

3. **Consult a Lawyer for Civil Recovery** (1-2 weeks, Lawyer fees (varies)): If the landlord ignores the demand, consult a lawyer to send a legal notice or file a civil money recovery suit. A lawyer can also advise on the criminal complaint strategy to ensure it doesn't negatively impact your civil claim.

4. **Seek Free Legal Aid** (Immediate, Free): If you cannot afford a private lawyer, contact the District Legal Services Authority (DLSA) in Noida or call the NALSA helpline at 15100 for free legal advice and representation.

## What I don't know

- Whether Uttar Pradesh has adopted the Model Tenancy Act [KB:mta_s11_deposit], which would affect the specific rules for deposit return.

- The exact terms of your rent agreement regarding deductions for damages or unpaid rent.

- Whether you have any witnesses to the physical threat.

## Needs lawyer: True - The case involves a criminal threat and physical assault, which requires careful legal handling to avoid compromising your safety or civil claim. A lawyer is needed to guide the police complaint and subsequent civil recovery.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route"
 ]
}

```