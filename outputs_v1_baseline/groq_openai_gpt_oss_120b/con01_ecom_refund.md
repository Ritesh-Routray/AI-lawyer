# con01_ecom_refund  (groq:openai/gpt-oss-120b)

## Input

I ordered a phone worth Rs 32,999 on an e-commerce site on 2 Sept 2026. It was delivered with a cracked screen, I returned it on 5 Sept and they picked it up, but the refund still hasn't come. Customer care keeps saying 7-10 days. I have the order invoice and pickup receipt. I live in Hyderabad.

## Reply shown to user

You are a consumer under the Consumer Protection Act, 2019 [KB:cpa_consumer_def], and you have solid proof of purchase and return. The first step is to write to the e‑commerce platform’s grievance officer, as the rules require a written complaint and give them 48 hours to acknowledge and one month to resolve [KB:ecom_grievance_officer]. If they do not respond, call the free National Consumer Helpline (1915) to have them intervene [KB:forum_nch]. Should these efforts fail, you can file a complaint yourself on the e‑Jagriti portal; there is no filing fee for amounts up to Rs 5 lakh and the District Commission has jurisdiction [KB:cpa_jurisdiction_2021][KB:cpa_fee_nil_5lakh]. Do you have the email address or contact details of the platform’s grievance officer, or would you need help locating it?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "e-commerce refund not processed",
 "user_language": "English",
 "state": "Telangana",
 "city": "Hyderabad",
 "summary": "The user ordered a phone for Rs 32999 on 2 Sep 2026, received it with a cracked screen, returned it on 5 Sep 2026, and has not received the refund despite promises of 7-10 days.",
 "user_goal": "Obtain the pending refund for the returned phone.",
 "user_role": "consumer",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "timeline": [
  {
   "date": "2026-09-02",
   "event": "Placed order for phone",
   "proof": "order invoice"
  },
  {
   "date": "2026-09-05",
   "event": "Returned phone; pickup by e‑commerce courier",
   "proof": "pickup receipt"
  },
  {
   "date": null,
   "event": "Refund not received; customer care says 7-10 days",
   "proof": null
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
  "refund acknowledgment email or reference number",
  "communication from customer care confirming refund timeline"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": ""
 },
 "follow_up_questions": [
  "Which e‑commerce platform did you order from?",
  "Do you have any email or chat communication confirming the refund timeline?",
  "Has the company provided a refund reference number or acknowledgment?"
 ]
}

```

## Calculation (code)

- Amount paid: Rs 32,999

- Refund due: Rs 32,999

## Where you stand

You are a consumer under the Consumer Protection Act, 2019 [KB:cpa_consumer_def]. You have clear proof of purchase (order invoice) and return (pickup receipt). The amount (Rs 32,999) is well below the Rs 5 lakh fee‑free limit and within the 2‑year filing period [KB:cpa_limitation]. Weaknesses: you lack a refund acknowledgment or reference number, and you have not yet approached the e‑commerce platform’s grievance officer, which is required before filing a complaint.

## Options

1. **Write to the grievance officer** (1‑2 days to draft and send, free): Send a formal email or registered post to the platform’s grievance officer stating the order details, defect, return date, and demand the refund within 7‑10 days. Keep a copy for records.

2. **Call the National Consumer Helpline [KB:forum_nch]** (same day, free): Dial 1915 or file online at consumerhelpline.gov.in. Provide the same details and ask them to forward a complaint to the company. Note the reference number they give you.

3. **File a complaint with the District Consumer Commission** (1‑2 weeks for the commission to issue a notice, nil filing fee; possible modest court costs for service of notice): Use the e‑Jagriti portal to lodge a consumer complaint. Attach the invoice, pickup receipt, and any correspondence (including the grievance‑officer email). No filing fee is required for amounts up to Rs 5 lakh [KB:cpa_fee_nil_5lakh].

4. **Send a legal notice (optional)** (3‑5 days to prepare and send, low (postage, possible lawyer draft fee)): If the above steps fail, draft a legal notice demanding refund and possible compensation, and send it by registered post. This often prompts payment before court proceedings.

## What I don't know

- The exact name and contact details of the e‑commerce platform’s grievance officer.

- Whether the platform has already sent a refund confirmation that you missed.

- If any state‑specific consumer rules in Telangana differ from the central Act.

## Needs lawyer: False - The dispute is a straightforward refund claim under the Consumer Protection Act [KB:cpa_consumer_def], with a low monetary value and no court case yet. You can pursue the steps yourself; a lawyer becomes useful only if the commission orders litigation or the company threatens legal action.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cpa_consumer_def",
  "cpa_fee_nil_5lakh",
  "cpa_jurisdiction_2021",
  "cpa_limitation",
  "ecom_grievance_officer",
  "forum_nch"
 ]
}

```

## Draft: Consumer Complaint before the District Consumer Disputes Redressal Commission, Hyderabad

```

Before the Hon’ble District Consumer Disputes Redressal Commission, Hyderabad

1. **Complainant:**
   Name: [Your Name]
   Address: [Your Complete Address]
   Phone: [PHONE_1]
   Email: [Your Email]

2. **Opposite Party (E‑commerce Seller):**
   Name: [Company Name]
   Registered Office: [Company Address]
   Phone: [Company Phone]
   Email: [Company Email]

3. **Facts of the Case**
   1. On 02‑09‑2026, the complainant placed an order for a mobile phone priced at Rs. 32,999 on the e‑commerce platform of the opposite party. (Annexure‑A: Order Invoice)
   2. The phone was delivered with a cracked screen, which constituted a defect.
   3. The complainant returned the defective phone on 05‑09‑2026; the e‑commerce courier collected the item. (Annexure‑B: Pickup Receipt)
   4. Despite repeated follow‑ups, the opposite party has not credited the refund amount of Rs. 32,999. Customer care repeatedly assures that the refund will be processed within 7‑10 days, but the period has elapsed and no refund has been received. (No refund acknowledgment or reference number is available.)
   5. The complainant lodged a grievance with the e‑commerce platform’s Grievance Officer on [date of grievance] as required under the Consumer Protection (E‑Commerce) Rules, 2020, but no satisfactory resolution was obtained. (Annexure‑C: Grievance communication – placeholder)
   6. The complainant also approached the National Consumer Helpline (1915) on [date of NCH contact]; the helpline forwarded the complaint but the refund remains pending. (Annexure‑D: NCH reference – placeholder)

4. **Grounds for Complaint**
   a) The opposite party has committed a *deficiency in service* by delivering a defective product and refusing to refund the amount paid. (Consumer Protection Act, 2019 – sections 2(7), 2(11) [KB:cpa_consumer_def])
   b) The refusal to refund after the product was returned amounts to an *unfair trade practice* under the same Act. (Consumer Protection Act, 2019 – section 2(47) [KB:cpa_consumer_def])
   c) The complainant has attempted pre‑litigation redress through the grievance officer and the National Consumer Helpline, as prescribed under the Consumer Protection (E‑Commerce) Rules, 2020 and the NCH guidelines.

5. **Jurisdiction & Limitation**
   The value of the goods involved is Rs. 32,999, which falls within the jurisdiction of the District Commission (up to Rs. 50 lakh). (Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021 – sections 3,4,5 [KB:cpa_jurisdiction_2021])
   The complaint is filed within two years from the date of the cause of action, complying with the limitation period. (Consumer Protection Act, 2019 – section 69 [KB:cpa_limitation])

6. **Relief Sought**
   a) Refund of the full amount paid: Rs. 32,999.
   b) Compensation for the inconvenience and mental agony caused by the delay, as may be determined by the Commission.
   c) Recovery of all costs incurred in filing and pursuing the complaint, including court fees (nil as per rule) and any other expenses as deemed fit.
   d) Any other relief that the Hon’ble Commission may deem appropriate in the interest of justice.

7. **Documents Attached**
   1. Order Invoice (Annexure‑A)
   2. Pickup Receipt (Annexure‑B)
   3. Copy of grievance communication with the e‑commerce grievance officer (Annexure‑C) – placeholder
   4. NCH reference/communication (Annexure‑D) – placeholder
   5. Affidavit of the complainant (Annexure‑E)

8. **Verification**
   I, [Your Name], the complainant above, do hereby verify that the contents of this complaint are true to the best of my knowledge and belief, and that no material fact has been concealed.
   Verified at Hyderabad on this [date of filing] day of [month] 2026.
   Signature: ______________________

Date: [date of filing]

```

Explanation for user: This document is a formal consumer complaint to be filed with the District Consumer Disputes Redressal Commission in Hyderabad. It lists you as the complainant, the e‑commerce seller as the opposite party, and sets out the facts, the deficiency in service, and the relief you are seeking (full refund, compensation and costs). After you fill in the placeholders and attach the listed documents, you can file it online via the e‑Jagriti portal or submit it in person. The Commission will then issue notice to the seller and schedule a hearing.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["cpa_consumer_def", "cpa_jurisdiction_2021", "cpa_limitation"]}