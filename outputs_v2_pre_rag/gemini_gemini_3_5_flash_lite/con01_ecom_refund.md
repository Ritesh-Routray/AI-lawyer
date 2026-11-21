# con01_ecom_refund  (gemini:gemini-3.5-flash-lite)

## Input

I ordered a phone worth Rs 32,999 on an e-commerce site on 2 Sept 2026. It was delivered with a cracked screen, I returned it on 5 Sept and they picked it up, but the refund still hasn't come. Customer care keeps saying 7-10 days. I have the order invoice and pickup receipt. I live in Hyderabad.

## Reply shown to user

You have a solid consumer case to recover your Rs 32,999 refund because you possess the order invoice and the pickup receipt proving you returned the damaged phone [KB:cpa_consumer_def]. Since customer care missed their turnaround time, your first step is to file a written complaint with the platform's designated Grievance Officer, who is required to resolve it within a month [KB:ecom_grievance_officer]. If that fails, you can raise a free dispute on the National Consumer Helpline [KB:forum_nch], and eventually file a complaint on the e-Jagriti [KB:forum_ejagriti] portal without any court fee since your claim is under Rs 5 lakh [KB:cpa_fee_nil_5lakh, KB:forum_ejagriti]. Do you currently have any written chat or email transcripts from your previous conversations with customer care regarding this delayed refund?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "e-commerce refund not processed for damaged product",
 "user_language": "English",
 "state": "Telangana",
 "city": "Hyderabad",
 "summary": "The user ordered a phone worth Rs 32,999 on September 2, 2026, which arrived with a cracked screen. They returned it on September 5, 2026, but the e-commerce platform has not yet processed the refund despite customer care promising a 7-10 day turnaround.",
 "user_goal": "Get the full refund of Rs 32,999 processed and credited.",
 "user_role": "consumer",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "timeline": [
  {
   "date": "2026-09-02",
   "event": "Ordered a phone worth Rs 32,999 on an e-commerce site",
   "proof": "order invoice"
  },
  {
   "date": "2026-09-05",
   "event": "Returned the phone with a cracked screen and handed it over for pickup",
   "proof": "pickup receipt"
  }
 ],
 "amounts": {
  "deposit_paid": null,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": null,
  "order_value": 32999,
  "amount_refunded": null
 },
 "evidence_have": [
  "order invoice",
  "pickup receipt"
 ],
 "evidence_missing": [
  "chat or email transcripts with customer care"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": "Customer care stated 7-10 days for refund"
 },
 "follow_up_questions": [
  "What is the name of the e-commerce website?",
  "Do you have any written chat or email communication with customer care regarding the delayed refund?"
 ]
}

```

## Calculation (code)

- Amount paid: Rs 32,999

- Refund due: Rs 32,999

## Where you stand

You are in a strong position as a consumer since you have the order invoice and the pickup receipt proving the damaged item was returned [KB:cpa_consumer_def]. The e-commerce platform's failure to process your refund within the promised window constitutes a deficiency in service [KB:cpa_consumer_def]. You have up to 2 years from the date the problem arose to file a formal consumer complaint if needed [KB:cpa_limitation]. However, your case would be even stronger if you had written chat or email transcripts with customer care confirming your follow-ups [KB:ecom_grievance_officer].

## Options

1. **Contact E-commerce Grievance Officer** (1 to 30 days, free): Send a written complaint to the platform's Grievance Officer detailing your order number, return date, and the missing refund. They are required to acknowledge it within 48 hours and resolve it within a month [KB:ecom_grievance_officer].

2. **File a National Consumer Helpline [KB:forum_nch] Complaint** (1 to 4 weeks, free): File a free pre-litigation complaint online at consumerhelpline.gov.in or call 1915 to have them escalate the matter to the company [KB:forum_nch].

3. **File a Consumer Commission Complaint** (Several months, free filing fee up to Rs 5 lakh [KB:cpa_fee_nil_5lakh]): If the company still refuses the refund, file a consumer complaint online on the e-Jagriti portal [KB:forum_ejagriti]. For claims up to Rs 5 lakh, the District Commission filing fee is nil [KB:cpa_fee_nil_5lakh].

## What I don't know

- Whether the e-commerce platform claims they received a different item or if there is any hidden policy clause they rely on for rejection.

- Whether you have any written records of your past customer care chats.

## Needs lawyer: False - No court case or formal legal notice has been filed against you, and you can handle the initial grievance officer and consumer helpline complaints yourself without a lawyer.

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
  "forum_ejagriti",
  "forum_nch"
 ]
}

```

## Draft: Consumer Complaint Draft - District Consumer Disputes Redressal Commission

```

BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION,
HYDERABAD, TELANGANA

Consumer Complaint No. ______ of 2026

IN THE MATTER OF:
[Your Full Name]
[Your Address]
Hyderabad, Telangana - [PIN]
Phone: [PHONE_1] | Email: [EMAIL_1]
...Complainant

VERSUS

[Name of E-Commerce Company / Platform], 
Represented by its Managing Director / Grievance Officer,
[Address of Company if known, else [Company Address]]
...Opposite Party

COMPLAINT UNDER SECTION 2(7), 2(11), 2(47) OF THE CONSUMER PROTECTION ACT, 2019 [KB:cpa_consumer_def] READ WITH APPLICABLE RULES FOR DEFICIENCY IN SERVICE AND UNFAIR TRADE PRACTICE

MOST RESPECTFULLY SHOWETH:

1. That the Complainant is an individual residing at Hyderabad, Telangana, and falls within the definition of a "consumer" under Section 2(7) of the Consumer Protection Act, 2019 [KB:cpa_consumer_def], having purchased goods for consideration.

2. That the Opposite Party is an e-commerce platform engaged in online retail and delivery of goods, and is bound by the Consumer Protection (E-Commerce) Rules, 2020 [KB:ecom_grievance_officer].

3. That on September 2, 2026, the Complainant ordered a phone worth Rs 32,999 on the Opposite Party's e-commerce platform. The said transaction was duly completed, and an order invoice was generated [Proof: order invoice].

4. That upon delivery, the Complainant found that the phone arrived with a cracked screen, rendering it completely defective and unusable.

5. That the Complainant promptly initiated a return request, and on September 5, 2026, the defective phone was handed over to the Opposite Party's designated pickup agent, for which a pickup receipt was duly issued [Proof: pickup receipt].

6. That customer care representatives of the Opposite Party stated a turnaround time of 7-10 days for processing the refund of the paid amount.

7. That despite the lapse of the promised timeline and repeated follow-ups, the Opposite Party has failed and neglected to process or credit the refund of Rs 32,999 to the Complainant's account.

8. That the failure of the Opposite Party to refund the amount for a returned defective product constitutes a clear "deficiency in service" and an "unfair trade practice" under Section 2(11) and Section 2(47) of the Consumer Protection Act, 2019 [KB:cpa_consumer_def].

9. That the cause of action for the present complaint arose on September 2, 2026 (date of order), September 5, 2026 (date of return pickup), and continues daily as the Opposite Party has withheld the legitimate refund. The complaint is being filed well within the two-year limitation period prescribed under Section 69 of the Consumer Protection Act, 2019 [KB:cpa_limitation].

10. That this Commission has the pecuniary and territorial jurisdiction to entertain and try the present complaint under Section 3 of the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021 [KB:cpa_jurisdiction_2021], as the value of the goods paid for is Rs 32,999 (which is up to Rs 50 lakh) and the cause of action arose within Hyderabad, Telangana.

11. That the value of the goods paid for is Rs 32,999, and therefore, under the Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020 [KB:cpa_fee_nil_5lakh], the filing fee for this complaint is nil.

PRAYER
In view of the facts and circumstances mentioned above, the Complainant respectfully prays that this Hon'ble Commission may be pleased to:

a) Direct the Opposite Party to immediately refund the principal amount of Rs 32,999 to the Complainant;
b) Award appropriate compensation for mental agony and harassment, along with litigation costs, as this Hon'ble Commission deems fit and proper in the interests of justice.

VERIFICATION
Verified at Hyderabad on this [date] day of [month], 2026, that the contents of paragraphs 1 to 11 are true and correct to the best of my knowledge and belief, and nothing material has been concealed therefrom.


________________________
[Your Full Name]
Complainant

```

Explanation for user: This document is a formal consumer complaint drafted for the District Consumer Disputes Redressal Commission in Hyderabad. It details how you ordered a phone for Rs 32,999, received a damaged product, returned it on September 5, 2026, but never received your refund despite promises from customer care. It cites the Consumer Protection Act to demand your full refund of Rs 32,999 along with compensation and costs. After finalising and reviewing this draft, you can file it online through the e-Jagriti portal or submit it physically to the District Commission.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["cpa_consumer_def", "cpa_fee_nil_5lakh", "cpa_jurisdiction_2021", "cpa_limitation", "ecom_grievance_officer"]}