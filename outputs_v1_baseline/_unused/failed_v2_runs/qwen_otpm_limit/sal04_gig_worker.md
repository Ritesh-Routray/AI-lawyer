# sal04_gig_worker  (groq:qwen/qwen3.8-27b)

## Input

I deliver food for an app in Jaipur. They deactivated my ID last week and are holding 8,500 of my earnings for the last 2 weeks. Support just sends automated replies. Am I an employee? Can I claim salary?

## Reply shown to user

You have a strong claim for the Rs 8,500 you earned, but you need proof to back it up. Right now, your biggest weakness is the lack of screenshots or a signed agreement. First, take screenshots of your app dashboard showing the balance and the deactivation date. Next, send a formal written demand to the platform's grievance officer, giving them 7 days to pay. If they ignore you, you can file a claim with the Labour Department in Rajasthan, which is a free process. Since you are a delivery partner, your legal status (employee vs. contractor) matters, but you can start with these steps regardless. Do you have access to your app dashboard to take those screenshots?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid gig worker earnings / withheld dues",
 "user_language": "English",
 "state": "Rajasthan",
 "city": "Jaipur",
 "summary": "The user is a food delivery partner in Jaipur whose account was deactivated last week. The platform is withholding 8,500 INR in earnings for the last two weeks, and support is only providing automated responses.",
 "user_goal": "Recover the withheld 8,500 INR in earnings and clarify employment status to determine if salary claims apply.",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "platform"
 },
 "timeline": [
  {
   "date": "2026-11-13",
   "event": "Account deactivated by the platform",
   "proof": null
  },
  {
   "date": null,
   "event": "Earnings for the last 2 weeks (approx. 2026-11-06 to 2026-11-13) withheld",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": null,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": 8500,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [],
 "evidence_missing": [
  "Delivery partner agreement or terms of service",
  "Earnings statement or app dashboard screenshot showing the 8500 INR balance",
  "Communication logs with support (screenshots of automated replies)",
  "Deactivation notification or email"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Which specific app or platform are you working for?",
  "Do you have a signed agreement or any written terms from the company?",
  "Can you share a screenshot of your earnings dashboard showing the 8500 INR balance?",
  "Did the company give any specific reason for deactivating your ID?"
 ]
}

```

## Calculation (code)

- Other dues (leave encashment, reimbursements, etc.): Rs 8,500

- Amount to claim: Rs 8,500

## Where you stand

You are a food delivery partner in Jaipur whose account was deactivated, and the platform is withholding Rs 8,500 in earnings. Your main strength is that you have a clear financial claim for money already earned. However, a major weakness is the lack of written proof, such as a signed agreement or screenshots of your earnings dashboard. It is also unclear if you are legally classified as an 'employee' or an 'independent contractor,' which determines if the Code on Wages applies directly to you [KB:cow_s17]. Without proof of the specific amount owed, it will be difficult to enforce your claim.

## Options

1. **Gather Digital Evidence** (1-2 hours, free): Take screenshots of your app dashboard showing the Rs 8,500 balance, the deactivation date, and all automated support replies. Save any emails or SMS notifications regarding the account closure.

2. **Formal Written Demand** (1 day, low (postage if using registered post)): Send a formal email or registered letter to the platform's grievance officer. State that you are owed Rs 8,500 for work completed, demand payment within 7 days, and mention that you will approach the Labour Department if unpaid.

3. **File Complaint with Labour Department** (2-4 weeks, free): If the platform ignores your demand, file a claim for unpaid wages before the Labour Commissioner in Rajasthan. This is a formal legal step to recover dues.

4. **Seek Free Legal Aid** (1-2 weeks, free): If you face difficulties or the platform disputes your status, contact the District Legal Services Authority (DLSA) in Jaipur or the NALSA helpline for free legal advice and representation.

## What I don't know

- Whether the platform classifies you as an 'employee' or 'independent contractor' in their contract.

- If the Rs 8,500 includes any penalties or deductions that the platform might claim are valid.

- The specific state-level rules in Rajasthan regarding gig worker protections beyond the central Code on Wages [KB:cow_s17].

## Needs lawyer: False - The amount is relatively small (Rs 8,500) and the first steps (demand letter, Labour Department complaint) can be done by you. A lawyer is not needed now, but you should consult one if the platform files a counter-claim or if the Labour Department rejects your case due to your 'contractor' status.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17"
 ]
}

```