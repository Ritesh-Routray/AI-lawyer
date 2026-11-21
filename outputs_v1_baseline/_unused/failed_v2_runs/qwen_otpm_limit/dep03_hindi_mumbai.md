# dep03_hindi_mumbai  (groq:qwen/qwen3.8-27b)

## Input

मैंने मुंबई में फ्लैट किराए पर लिया था। किराया 25000 और डिपॉजिट 1,00,000 रुपये था। जुलाई 2026 में घर खाली किया। मकान मालिक कहता है नया किरायेदार आएगा तब पैसे देगा। मेरे पास रजिस्टर्ड एग्रीमेंट और बैंक ट्रांसफर की रसीद है।

## Reply shown to user

आपकी स्थिति अच्छी है क्योंकि आपके पास रजिस्टर्ड एग्रीमेंट और बैंक रसीद है। मकान मालिक का 'नया किरायेदार ढूंढने' का बहाना कानूनी रूप से कमजोर है, खासकर अगर एग्रीमेंट में डिपॉजिट वापसी की स्पष्ट शर्तें हैं। सबसे पहले, मकान मालिक को WhatsApp या ईमेल पर एक स्पष्ट संदेश भेजें कि आपने घर खाली कर दिया है और डिपॉजिट वापस करने का अनुरोध है। उनसे लिखित में ही जवाब मांगें। अगर वे 7-10 दिनों में जवाब न दें, तो एक वकील के जरिए लीगल नोटिस भेजें। क्या आपने घर खाली करने की कोई लिखित सूचना (notice) मालिक को दी थी या यह सिर्फ मौखिक बातचीत थी?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit not returned after vacating",
 "user_language": "Hindi",
 "state": "Maharashtra",
 "city": "Mumbai",
 "summary": "The user rented a flat in Mumbai with a monthly rent of 25,000 INR and a security deposit of 1,00,000 INR. They vacated the property in July 2026, but the landlord is refusing to return the deposit, claiming it will be returned only when a new tenant is found. The user holds a registered agreement and bank transfer receipts.",
 "user_goal": "To recover the security deposit of 1,00,000 INR from the landlord.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": null,
   "event": "Signed registered rent agreement and paid security deposit",
   "proof": "Registered agreement, bank transfer receipt"
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
  "Registered rent agreement",
  "Bank transfer receipt for deposit"
 ],
 "evidence_missing": [
  "Written notice of vacating the property",
  "Communication with landlord regarding deposit return (messages/emails)",
  "Inventory/checklist of property condition at handover"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "क्या आपने मकान मालिक को घर खाली करने की लिखित सूचना (notice) दी थी?",
  "मकान मालिक ने डिपॉजिट वापस करने से इनकार करने का कोई लिखित कारण दिया है या यह सिर्फ मौखिक बातचीत थी?",
  "घर खाली करते समय क्या कोई लिखित हस्तान्तरण (handover) या चेकलिस्ट साइन की गई थी?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 100,000

- Amount to claim: Rs 100,000

## Where you stand

आपकी स्थिति काफी मजबूत है क्योंकि आपके पास रजिस्टर्ड एग्रीमेंट और बैंक ट्रांसफर रसीद है। मकान मालिक का नया किरायेदार ढूंढने का बहाना कानूनी रूप से कमजोर है, खासकर अगर एग्रीमेंट में डिपॉजिट वापसी की स्पष्ट शर्तें हैं। हालांकि, आपके पास घर खाली करने की लिखित सूचना (notice) और हस्तान्तरण (handover) की लिखित पुष्टि नहीं है, जो एक कमजोरी है। महाराष्ट्र में Model Tenancy Act लागू नहीं है, इसलिए आपका एग्रीमेंट और सामान्य सिविल कानून ही लागू होगा [KB:mta_s11_deposit]।

## Options

1. **लिखित डिमांड लेटर (WhatsApp/Email)** (1-2 दिन, free): मकान मालिक को एक स्पष्ट संदेश भेजें कि आपने घर खाली कर दिया है और डिपॉजिट वापस करने का अनुरोध है। उनसे लिखित में ही जवाब मांगें कि वे कब और कितना वापस करेंगे।

2. **लीगल नोटिस (Lawyer's Notice)** (1-2 हफ्ते, low (वकील की फीस)): एक वकील के जरिए औपचारिक नोटिस भेजें। इसमें साफ लिखा जाएगा कि अगर 7-15 दिनों में पैसा नहीं मिला तो आप सिविल कोर्ट में केस दर्ज करेंगे। यह अक्सर मालिकों को समझौते पर मजबूर करता है।

3. **सिविल कोर्ट में रिक्वेस्ट** (3-6 महीने या अधिक, court fee (राशि के हिसाब से)): अगर नोटिस का कोई असर नहीं पड़ता, तो आप अपने इलाके के सिविल कोर्ट (Small Causes Court) में पैसा वापस करने के लिए केस दर्ज कर सकते हैं।

## What I don't know

- आपके एग्रीमेंट में डिपॉजिट वापसी की शर्तें क्या हैं (क्या उसमें 'नया किरायेदार मिलने पर' वापसी की शर्त है?)

- महाराष्ट्र के स्थानीय किराया नियमों की सटीक विवरण जो सिविल कोर्ट में लागू होंगे।

## Needs lawyer: False - अभी के लिए आप खुद लिखित डिमांड भेज सकते हैं। वकील तभी ज़रूरी होगा जब मालिक लिखित डिमांड का जवाब न दे या सिविल कोर्ट में केस दर्ज करने की तैयारी शुरू हो।

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "mta_s11_deposit"
 ]
}

```