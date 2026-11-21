# con01_ecom_refund  (gemini:gemini-3.5-flash-lite)

## Input

I ordered a phone worth Rs 32,999 on an e-commerce site on 2 Sept 2026. It was delivered with a cracked screen, I returned it on 5 Sept and they picked it up, but the refund still hasn't come. Customer care keeps saying 7-10 days. I have the order invoice and pickup receipt. I live in Hyderabad.

## Reply shown to user

As a consumer who returned a damaged phone worth Rs 32,999, you have a strong right to a full refund [KB:cpa_consumer_def]. Because you have your order invoice and pickup receipt, you already possess key proof of the transaction and return. E-commerce platforms are required to resolve grievances within a specific timeframe once notified in writing [KB:ecom_grievance_officer]. Since your refund is delayed, your best first step is to write directly to the platform's grievance officer or file a free complaint with the National Consumer Helpline [KB:forum_nch]. If that does not work, you can file a complaint online on the e-Jagriti portal without paying any court fee for claims under Rs 5 lakh [KB:cpa_fee_nil_5lakh] [KB:forum_ejagriti]. Do you have any complaint reference numbers or chat transcripts from when you previously spoke with customer care?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "e-commerce refund not processed for damaged product",
 "user_language": "English",
 "state": "Telangana",
 "city": "Hyderabad",
 "summary": "The user ordered a phone worth Rs 32,999 on an e-commerce site on 2026-09-02, which arrived with a cracked screen. They returned it on 2026-09-05, but the refund is still pending despite customer care delays.",
 "user_goal": "Get the full refund for the returned damaged phone",
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
   "event": "Returned the phone with a cracked screen and it was picked up",
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
  "customer care chat transcripts or complaint reference numbers"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": "Customer care says 7-10 days"
 },
 "follow_up_questions": [
  "Do you have any written communication, chat transcripts, or complaint reference numbers from customer care regarding the refund?",
  "What is the name of the e-commerce platform where you placed the order?"
 ]
}

```

## Calculation (code)

- Amount paid: Rs 32,999

- Refund due: Rs 32,999

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Consumer Protection Act, 2019 Section 94 (MISCELLANEOUS) p.34

- Consumer Protection Act, 2019 Section 69  p.28

- Consumer Protection Act, 2019 Section 35  p.18

- Consumer Protection Act, 2019 Section 89  p.33

- Consumer Protection Act, 2019 Section 34  p.17

- Consumer Protection Act, 2019 Section 47  p.23

- Consumer Protection Act, 2019 Section 20  p.14

- Consumer Protection Act, 2019 Section 84  p.31

## Where you stand

You are a consumer who purchased a defective product that arrived with a cracked screen, making you eligible for a full refund of Rs 32,999 under the Consumer Protection Act [KB:cpa_consumer_def]. Having your order invoice and pickup receipt gives you strong initial proof of the purchase and return. However, your case would be even stronger with customer care chat transcripts or complaint reference numbers [KB:ecom_grievance_officer]. Since the return was completed recently on September 5, 2026, you are well within the standard 2-year time limit to pursue a consumer complaint [KB:cpa_limitation].

## Options

1. **Contact E-commerce Grievance Officer** (1-2 days, free): Write a formal email to the platform's grievance officer demanding your refund of Rs 32,999, attaching your order invoice and pickup receipt.

2. **File a complaint on National Consumer Helpline [KB:forum_nch]** (1-2 weeks, free): Call 1915 or file your grievance online at consumerhelpline.gov.in to get pre-litigation mediation help.

3. **File a Consumer Commission Complaint** (1-3 months, free): File a complaint online through the e-Jagriti [KB:forum_ejagriti] portal if the company fails to refund your money.

## What I don't know

- Whether the e-commerce platform's internal warehouse team has already processed or rejected the return.

- The exact name of the e-commerce platform and their specific refund policies.

## Needs lawyer: False - You can handle the initial grievance steps and consumer helpline complaints yourself without a lawyer, especially since no court case has been filed yet.

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
 ],
 "support_check": {
  "checked": 0,
  "unsupported": []
 }
}

```

## Draft: Consumer Complaint before the District Consumer Disputes Redressal Commission, Hyderabad

```

BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, HYDERABAD, TELANGANA

Consumer Complaint No. [Insert Year if any, or leave blank]/2026

IN THE MATTER OF:
[Your Name]
[Your Address]
Hyderabad, Telangana - [PIN Code]
...Complainant

VERSUS

[Name of E-Commerce Company]
[Address of E-Commerce Company / Corporate Office]
...Opposite Party

COMPLAINT UNDER SECTION 35 OF THE CONSUMER PROTECTION ACT, 2019 [KB:src_cpa_2019_35]

MOST RESPECTFULLY SHOWETH:

1. That the Complainant is an ordinary resident of Hyderabad, Telangana, and falls within the definition of a "consumer" under Section 2(7) of the Consumer Protection Act, 2019 [KB:cpa_consumer_def], having purchased goods for consideration from the Opposite Party.

2. That on 2026-09-02, the Complainant ordered a phone worth Rs 32,999 on the e-commerce site of the Opposite Party, vide order invoice [mention order number if available].

3. That upon delivery, the said phone arrived with a cracked screen, rendering it defective and unusable.

4. That the Complainant promptly initiated a return through the platform, and the defective phone was picked up by the Opposite Party's logistics partner on 2026-09-05, as evidenced by the pickup receipt.

5. That despite the successful return and passage of the stipulated time frame, the Opposite Party has failed to process the refund of Rs 32,999. Customer care has delayed the matter indefinitely under the pretext that it takes 7-10 days, amounting to a deficiency in service and unfair trade practice under Section 2(11) and Section 2(47) of the Consumer Protection Act, 2019 [KB:cpa_consumer_def].

6. That the cause of action arose continuously starting from 2026-09-02 when the order was placed, on 2026-09-05 when the defective product was returned, and persists daily as the refund remains unpaid. The complaint is being filed well within the two-year limitation period under Section 69 of the Consumer Protection Act, 2019 [KB:cpa_limitation].

7. That this Commission has territorial and pecuniary jurisdiction to entertain this complaint under Section 34 of the Consumer Protection Act, 2019 [KB:src_cpa_2019_34], as the Opposite Party carries on business within Hyderabad and the value of the goods paid as consideration does not exceed one crore rupees.

PRAYER

In light of the facts mentioned above, the Complainant prays that this Hon'ble Commission may be pleased to:

a) Direct the Opposite Party to refund the principal amount of Rs 32,999 to the Complainant;

b) Award appropriate compensation for mental agony and harassment, along with litigation costs, as this Hon'ble Commission deems fit.

LIST OF DOCUMENTS TO ATTACH:
1. Copy of the order invoice dated 2026-09-02
2. Copy of the pickup receipt dated 2026-09-05
3. Any customer care chat transcripts or complaint reference numbers [if available]

VERIFICATION

I, [Your Name], the Complainant above named, do hereby verify that the contents of paragraphs 1 to 7 are true to my personal knowledge and belief, and no part of it is false and nothing material has been concealed therein.

Verified at Hyderabad on this [date] day of [month], 2026.

[Your Signature]
[Your Name]

```

Explanation for user: This document is a formal consumer complaint drafted for the District Consumer Disputes Redressal Commission in Hyderabad under the Consumer Protection Act, 2019. It details how you ordered a phone, received a damaged product, returned it successfully, but failed to get your refund of Rs 32,999 despite customer care delays. It requests the Commission to order the e-commerce company to refund your money along with compensation and costs. After filling in all the bracketed placeholders and attaching your proofs, you can file this complaint online through the e-Jagriti portal or physically at your local District Commission.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["cpa_consumer_def", "cpa_limitation", "src_cpa_2019_34", "src_cpa_2019_35"]}