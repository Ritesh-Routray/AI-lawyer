# dep03_hindi_mumbai  (gemini:gemini-3.5-flash-lite)

## Input

मैंने मुंबई में फ्लैट किराए पर लिया था। किराया 25000 और डिपॉजिट 1,00,000 रुपये था। जुलाई 2026 में घर खाली किया। मकान मालिक कहता है नया किरायेदार आएगा तब पैसे देगा। मेरे पास रजिस्टर्ड एग्रीमेंट और बैंक ट्रांसफर की रसीद है।

## Reply shown to user

नमस्ते! आपकी स्थिति काफी मजबूत है क्योंकि आपके पास रजिस्टर्ड एग्रीमेंट और बैंक ट्रांसफर की रसीद है [KB:deposit_civil_route]। मकान मालिक का यह कहना कि नया टेनेंट मिलने पर पैसे मिलेंगे, कानूनन सही नहीं है। चूंकि मकान मालिक डिपॉजिट नहीं लौटा रहा है, आप सबसे पहले उसे व्हाट्सएप या लिखित में डिपॉजिट वापसी का मैसेज भेजें [KB:deposit_civil_route]। इसके बाद भी बात न बने तो कानूनी नोटिस भेजा जा सकता है [KB:deposit_civil_route]। क्या आपने घर खाली करते समय कोई हैंडओवर रसीद या लिखित बात की थी?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "landlord refusing to return security deposit after vacating",
 "user_language": "Hindi written in Devanagari script (not Roman letters), the way the person wrote",
 "state": "Maharashtra",
 "city": "Mumbai",
 "summary": "The user rented a flat in Mumbai with a monthly rent of 25000 and a security deposit of 100000 rupees. They vacated the house in July 2026, but the landlord is withholding the deposit until a new tenant is found. The user possesses a registered agreement and bank transfer receipts.",
 "user_goal": "To get the security deposit refunded from the landlord",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-07",
   "event": "Vacated the rented flat in Mumbai",
   "proof": "Registered agreement and bank transfer receipt"
  }
 ],
 "amounts": {
  "deposit_paid": 100000,
  "deductions_claimed": null,
  "monthly_rent": 25000,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": null,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [
  "registered agreement",
  "bank transfer receipt"
 ],
 "evidence_missing": [
  "written notice or chat/messages asking for the deposit return",
  "flat inspection or handover report"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "क्या मकान मालिक को डिपॉजिट वापसी के लिए कोई लिखित नोटिस या मैसेज भेजा था?",
  "क्या घर खाली करते समय कोई हैंडओवर या निरीक्षण रसीद (inspection report) बनाई गई थी?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 100,000

- Amount to claim: Rs 100,000

## Where you stand



## Options

1. **लिखित मांग (Written Demand)** (1-2 दिन, फ्री): मकान मालिक को व्हाट्सएप या ईमेल पर साफ़ शब्दों में डिपॉजिट वापसी का लिखित अनुरोध भेजें और एग्रीमेंट का हवाला दें।

2. **वकील का नोटिस (Legal Notice)** (1 सप्ताह, कम): यदि मकान मालिक पैसे न लौटाए, तो किसी वकील के माध्यम से कानूनी नोटिस भेजें [KB:deposit_civil_route]।

## What I don't know

- क्या महाराष्ट्र सरकार ने मॉडल टेनेंसी एक्ट को पूरी तरह से अपनाया है या स्थानीय रेंट एक्ट लागू होता है।

## Needs lawyer: False - अभी कोई कोर्ट केस या पुलिस मामला नहीं है। पहले आप खुद लिखित मांग कर सकते हैं, वकील की जरूरत केवल कानूनी नोटिस या कोर्ट जाने के समय पड़ेगी।

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