# dep03_hindi_mumbai  (groq:openai/gpt-oss-120b)

## Input

मैंने मुंबई में फ्लैट किराए पर लिया था। किराया 25000 और डिपॉजिट 1,00,000 रुपये था। जुलाई 2026 में घर खाली किया। मकान मालिक कहता है नया किरायेदार आएगा तब पैसे देगा। मेरे पास रजिस्टर्ड एग्रीमेंट और बैंक ट्रांसफर की रसीद है।

## Reply shown to user

आपके पास लिखित किरायेदारी समझौता और डिपॉज़िट का बैंक ट्रांसफ़र रसीद है, जो आपके पक्ष में मजबूत सबूत है [KB:ica_s73]. लेकिन मकान मालिक की लिखित स्वीकृति या निरीक्षण रिपोर्ट नहीं है, इसलिए उन्हें डिपॉज़िट न लौटाने का कारण साबित करना कठिन हो सकता है. सबसे पहले, एक शिष्ट लिखित मांग पत्र भेजें जिसमें 7‑10 दिनों में पूरी राशि वापस करने का अनुरोध हो. यदि जवाब नहीं मिलता, तो वकील से कानूनी नोटिस तैयार करवाएँ, और फिर आवश्यक हो तो Small Causes Court में केस दायर करें. क्या आप अभी मांग पत्र तैयार करने में मदद चाहते हैं?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit return",
 "user_language": "Hindi",
 "state": "Maharashtra",
 "city": "Mumbai",
 "summary": "The user rented a flat in Mumbai, paying a monthly rent of 25000 INR and a security deposit of 100000 INR. They vacated the flat in July 2026, and the landlord says the deposit will be returned only when a new tenant arrives. The user has a registered agreement and bank transfer receipt.",
 "user_goal": "to get the full security deposit back",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": null,
   "event": "Flat rented and deposit paid",
   "proof": "bank transfer receipt"
  },
  {
   "date": "2026-07",
   "event": "Vacated the flat",
   "proof": null
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
  "landlord's written acknowledgment of deposit return",
  "move-out inspection report or receipt"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": ""
 },
 "follow_up_questions": [
  "किराए पर लेने की शुरुआत की तिथि क्या थी?",
  "आपने घर खाली करने की सही तारीख कब बताई थी?",
  "मकान मालिक का नाम और संपर्क विवरण क्या है?",
  "डिपॉजिट वापसी के बारे में कोई लिखित पत्र या संदेश है क्या?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 100,000

- Amount to claim: Rs 100,000

## Where you stand

आपके पास लिखित किरायेदारी समझौता और बैंक ट्रांसफ़र रसीद है, जो डिपॉज़िट भुगतान का ठोस प्रमाण है [KB:ica_s73]. यह आपके पक्ष में मजबूत सबूत है. लेकिन आपके पास मकान मालिक की लिखित स्वीकृति या निरीक्षण रिपोर्ट नहीं है, जिससे डिपॉज़िट वापसी में देरी का कारण साबित करना मुश्किल हो सकता है. यदि मकान मालिक डिपॉज़िट वापस करने से इनकार करता है, तो आपको आगे की कानूनी कार्रवाई करनी पड़ेगी.

## Options

1. **शिष्ट लिखित मांग पत्र** (1‑2 दिन, free): एक साधारण पत्र लिखें जिसमें आप डिपॉज़िट की पूरी राशि (₹100,000) की वापसी की मांग करें, vacate की तिथि, और 7‑10 दिनों के भीतर जवाब देने का अनुरोध करें. इसे ई‑मेल/WhatsApp पर भेजें और डिलीवरी रसीद रखें.

2. **कानूनी नोटिस भेजना** (1‑2 सप्ताह, low (वकील की फीस, लेकिन नोटिस स्वयं भी तैयार कर सकते हैं)): यदि 7‑10 दिनों में जवाब नहीं मिलता, तो वकील से एक औपचारिक कानूनी नोटिस तैयार करवाएँ जिसमें डिपॉज़िट की वापसी का आदेश हो और यदि नहीं किया गया तो आगे की सिविल कार्रवाई की चेतावनी हो.

3. **सिविल मुकदमा दायर करना** (2‑3 महीने (कोर्ट की कार्यवाही के अनुसार), court fee (सरकारी) + वकील की फीस (यदि आप वकील ले रहे हैं)): यदि नोटिस के बाद भी डिपॉज़िट नहीं मिलता, तो छोटे कारणों के न्यायालय (Small Causes Court) में डिपॉज़िट वसूली के लिए सिविल केस दाखिल करें. 3 साल की सीमा के भीतर दायर करना होगा [KB:deposit_civil_route].

## What I don't know

- क्या महाराष्ट्र ने Model Tenancy Act [KB:mta_s11_deposit] को अपनाया है (इससे डिपॉज़िट की अधिकतम सीमा प्रभावित हो सकती है).

- डिपॉज़िट में कोई कटौती (जैसे मरम्मत या बकाया किराया) का वास्तविक प्रमाण मौजूद है या नहीं.

## Needs lawyer: False - पहले दो कदम आप स्वयं कर सकते हैं; केवल तब वकील की जरूरत पड़ेगी जब मकान मालिक नोटिस के बाद भी डिपॉज़िट नहीं लौटाए या आप कोर्ट में केस दायर करना चाहें.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "ica_s73"
 ]
}

```