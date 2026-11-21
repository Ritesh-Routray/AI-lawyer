# dep03_hindi_mumbai  (gemini:gemini-3.5-flash-lite)

## Input

मैंने मुंबई में फ्लैट किराए पर लिया था। किराया 25000 और डिपॉजिट 1,00,000 रुपये था। जुलाई 2026 में घर खाली किया। मकान मालिक कहता है नया किरायेदार आएगा तब पैसे देगा। मेरे पास रजिस्टर्ड एग्रीमेंट और बैंक ट्रांसफर की रसीद है।

## Reply shown to user

नमस्ते! आपका मामला मुंबई में मकान मालिक द्वारा 100,000 रुपये का सिक्योरिटी डिपॉजिट न लौटाने से जुड़ा है। मकान मालिक का यह कहना कि 'नया tenant मिलने पर पैसे देंगे' कानूनन गलत है, क्योंकि मकान खाली करते ही डिपॉजिट वापस मिलना नियम है [KB:src_mta_2021_11]। आपके पास रजिस्टर्ड एग्रीमेंट और बैंक रसीद जैसे अच्छे सबूत हैं। आप सबसे पहले मकान मालिक को व्हाट्सएप या लिखित संदेश भेजकर अपने पैसे तुरंत वापस मांगें [KB:deposit_civil_route]। अगर वे फिर भी न मानें, तो हम कानूनी नोटिस या सिविल कोर्ट के रास्ते जा सकते हैं। क्या मकान मालिक के साथ डिपॉजिट वापसी को लेकर आपकी पहले कोई लिखित बातचीत (WhatsApp या मैसेज) हुई है?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "landlord refusing to return security deposit after vacating",
 "user_language": "Hindi written in Devanagari script (not Roman letters), the way the person wrote",
 "state": "Maharashtra",
 "city": "Mumbai",
 "summary": "The user vacated their rented flat in Mumbai in July 2026. The landlord is withholding the 100000 rupees security deposit until a new tenant is found.",
 "user_goal": "Get the security deposit returned from the landlord",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-07",
   "event": "Vacated the rented flat",
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
  "move-out inspection photos or handover receipt",
  "written communication with landlord regarding deposit return"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "क्या मकान मालिक के साथ डिपॉजिट वापसी को लेकर कोई लिखित बातचीत (WhatsApp या मैसेज) हुई है?",
  "घर खाली करते समय क्या मकान मालिक ने कोई हैंडओवर रसीद या लिखित दस्तावेज दिया था?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 100,000

- Amount to claim: Rs 100,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Model Tenancy Act, 2021 Section 23  p.18

- Model Tenancy Act, 2021 Section 11  p.11

- Model Tenancy Act, 2021 Section 10  p.11

- Model Tenancy Act, 2021 Section 15  p.13

- Model Tenancy Act, 2021 Section 14  p.12

- Model Tenancy Act, 2021 Section 20  p.15

- Model Tenancy Act, 2021 Section 28  p.20

## Where you stand

आपकी स्थिति यह है कि आपने मुंबई में जुलाई 2026 में अपना किराए का मकान खाली कर दिया था और आपका 100,000 रुपये का सिक्योरिटी डिपॉजिट मकान मालिक के पास बकाया है। मकान मालिक का यह कहना कि नया tenant मिलने पर पैसे देंगे, कानूनन सही नहीं है क्योंकि मकान खाली करते ही डिपॉजिट वापस मिलना चाहिए [KB:src_mta_2021_11]। आपके पास रजिस्टर्ड एग्रीमेंट और बैंक ट्रांसफर रसीद जैसी मजबूत proof हैं, लेकिन मकान खाली करते समय की तस्वीरें या लिखित बातचीत की कमी थोड़ी कमजोरी है। आप मकान मालिक को लिखित नोटिस दे सकते हैं और अगर वे नहीं मानते हैं तो सिविल कोर्ट या रेंट अथॉरिटी का रुख कर सकते हैं [KB:deposit_civil_route]।

## Options

1. **लिखित मांग (Written Demand)** (1-2 दिन, free): मकान मालिक को व्हाट्सएप या ईमेल पर लिखित रूप से अपना डिपॉजिट तुरंत वापस करने के लिए कहें और एग्रीमेंट का हवाला दें।

2. **वकील का कानूनी नोटिस (Legal Notice)** (1 हफ्ते, low): यदि मकान मालिक पैसे देने से मना करे, तो किसी वकील के जरिए आधिकारिक कानूनी नोटिस भेजें।

3. **सिविल कोर्ट या रेंट अथॉरिटी में मामला दर्ज करना** (कुछ महीने, court fee): नोटिस का जवाब न मिलने पर सिविल कोर्ट में रिकवरी का मुकदमा दायर करें।

## What I don't know

- क्या मकान मालिक ने घर में किसी नुकसान के नाम पर कटौती का दावा किया है?

- क्या महाराष्ट्र सरकार ने मॉडल टेनेंसी एक्ट के इस प्रावधान को पूरी तरह से लागू किया है?

## Needs lawyer: False - फिलहाल यह पैसों की रिकवरी का साधारण मामला है और आप खुद लिखित मांग या नोटिस से शुरुआत कर सकते हैं। कोर्ट जाने या कानूनी नोटिस भेजने के समय वकील की जरूरत पड़ेगी।

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "src_mta_2021_11"
 ],
 "support_check": "not auto-checked (non-English reply; cross-encoder is English-only)"
}

```