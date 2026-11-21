# dep03_hindi_mumbai  (gemini:gemini-3.5-flash)

## Input

मैंने मुंबई में फ्लैट किराए पर लिया था। किराया 25000 और डिपॉजिट 1,00,000 रुपये था। जुलाई 2026 में घर खाली किया। मकान मालिक कहता है नया किरायेदार आएगा तब पैसे देगा। मेरे पास रजिस्टर्ड एग्रीमेंट और बैंक ट्रांसफर की रसीद है।

## Reply shown to user

नमस्ते! मैं न्याय साथी हूँ। मैं वकील नहीं हूँ, लेकिन आपकी मदद कर सकता हूँ।

आपका पक्ष मजबूत है क्योंकि आपके पास रजिस्टर्ड रेंट एग्रीमेंट और 1,00,000 रुपये जमा करने की बैंक रसीद मौजूद है। मकान मालिक का यह कहना कि नया किराएदार आने पर ही पैसे मिलेंगे, अनुबंध का उल्लंघन है [KB:ica_s73]। मकान मालिक को एग्रीमेंट के अनुसार पैसे लौटाने होंगे [KB:mta_s11_deposit]।

सबसे पहला कदम यह है कि आप मकान मालिक को WhatsApp या Email पर एक लिखित मैसेज भेजें और 7 दिनों के भीतर पैसे लौटाने को कहें। अगर वे फिर भी पैसे नहीं देते, तो आप उन्हें लीगल नोटिस भेज सकते हैं [KB:deposit_civil_route]। अगर आपको कानूनी सहायता की आवश्यकता हो और आप पात्र हैं, तो DLSA से मुफ्त सहायता भी ली जा सकती है [KB:lsa_s12_legal_aid]।

क्या आपने मकान मालिक को चाबी सौंपते समय या बाद में पैसे मांगने के लिए कोई मैसेज या ईमेल भेजा है?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit withholding by landlord",
 "user_language": "Hindi",
 "state": "Maharashtra",
 "city": "Mumbai",
 "summary": "The user rented a flat in Mumbai with a monthly rent of Rs 25,000 and a security deposit of Rs 1,00,000. They vacated the property in July 2026. The landlord is withholding the deposit, stating it will only be returned after a new tenant moves in.",
 "user_goal": "Get the security deposit of Rs 1,00,000 refunded from the landlord.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-07",
   "event": "Vacated the rented flat in Mumbai",
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
  "registered rent agreement",
  "bank transfer receipt for deposit"
 ],
 "evidence_missing": [
  "written communication asking for refund (WhatsApp/Email)",
  "flat handover photos/acknowledgement"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "क्या मकान मालिक ने सिक्योरिटी डिपॉजिट में से कोई कटौती (deduction) की मांग की है?",
  "क्या आपने मकान मालिक को चाबी सौंपते समय कोई लिखित रसीद या मैसेज (WhatsApp/Email) लिया था?",
  "क्या आपने मकान मालिक को डिपॉजिट वापस करने के लिए कोई औपचारिक नोटिस या मैसेज भेजा है?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 100,000

- Amount to claim: Rs 100,000

## Where you stand

आपका पक्ष काफी मजबूत है क्योंकि आपके पास रजिस्टर्ड रेंट एग्रीमेंट और बैंक ट्रांसफर की रसीद मौजूद है। मकान मालिक का यह कहना कि नया किराएदार आने के बाद ही डिपॉजिट मिलेगा, कानूनन या एग्रीमेंट के तहत सही शर्त नहीं मानी जा सकती [KB:ica_s73]। आपने जुलाई 2026 में फ्लैट खाली कर दिया है, इसलिए मकान मालिक को जायज कटौती काटकर बाकी पैसे तुरंत वापस करने चाहिए [KB:mta_s11_deposit]। बस आपको चाबी सौंपने और लिखित मांग का सबूत मजबूत करना होगा।

## Options

1. **लिखित मांग (WhatsApp / Email)** (1-2 दिन, मुफ्त): मकान मालिक को मैसेज या ईमेल भेजकर साफ लिखें कि आपने फ्लैट खाली कर दिया है, एग्रीमेंट और बैंक रसीद के मुताबिक 1,00,000 रुपये का सिक्योरिटी डिपॉजिट 7 दिनों में वापस करें।

2. **लीगल नोटिस (Legal Notice)** (7-15 दिन, कम / वकील की फीस पर निर्भर): यदि मैसेज का सही जवाब न मिले, तो किसी वकील के ज़रिए या स्वयं मकान मालिक को एक औपचारिक लीगल नोटिस भेजें [KB:deposit_civil_route]।

3. **सिविल कोर्ट में वसूली का केस (Money Suit)** (कुछ महीने से अधिक, कोर्ट फीस और वकील का खर्च): यदि लीगल नोटिस के बाद भी पैसे न मिलें, तो पैसे की वसूली के लिए सिविल कोर्ट या रेंट अथॉरिटी में केस दर्ज कर सकते हैं [KB:deposit_civil_route]।

## What I don't know

- क्या महाराष्ट्र में मॉडल टैनेंसी एक्ट की शर्तें पूरी तरह लागू की गई हैं या लोकल रेंट कंट्रोल एक्ट के तहत मामला आता है, यह एक वकील स्पष्ट कर सकता है।

- क्या मकान मालिक ने किसी मरम्मत या बिजली बिल का दावा किया है।

## Needs lawyer: False - अभी मामला शुरुआती स्तर पर है। आप पहले लिखित संदेश और औपचारिक नोटिस के ज़रिए खुद पैसे मांगने की कोशिश कर सकते हैं। अगर मकान मालिक मना करता है या नोटिस का जवाब नहीं देता, तब केस दर्ज करने के लिए वकील की ज़रूरत होगी।

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "ica_s73",
  "lsa_s12_legal_aid",
  "mta_s11_deposit"
 ]
}

```