# sal01_hindi_startup  (gemini:gemini-3.5-flash-lite)

## Input

मैं पुणे में एक स्टार्टअप में काम करता था, सैलरी 35000 महीना थी। अगस्त से अक्टूबर 2026 तक की सैलरी नहीं मिली। 31 अक्टूबर को मैंने इस्तीफा दे दिया। HR कहता है पैसे नहीं हैं, बाद में देंगे। मेरे पास ऑफर लेटर और पुरानी सैलरी स्लिप हैं।

## Reply shown to user

नमस्ते। आपकी स्थिति काफी हद तक स्पष्ट है। आपके पास ऑफर लेटर और पेस्लिप्स हैं, जो एक मजबूत आधार हैं। Code on Wages, 2019 के अनुसार, नौकरी छोड़ने पर आपके बकाया पैसों का भुगतान तुरंत होना चाहिए [KB:cow_s17] और आप 3 साल के भीतर लेबर अथॉरिटी के पास क्लेम कर सकते हैं [KB:cow_s45]। चूंकि HR फंड न होने की बात कह रहा है, सबसे पहले आपको उन्हें ईमेल या व्हाट्सएप पर लिखित रूप में अपनी बकाया सैलरी (3 महीने की कुल 105,000 रुपये) की मांग का मैसेज भेजना चाहिए ताकि आपके पास लिखित सबूत हो। क्या आपने कंपनी को अपनी बकाया सैलरी के लिए अभी तक कोई ईमेल या लिखित मैसेज भेजा है?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid salary and resignation dues",
 "user_language": "Hindi written in Devanagari script (not Roman letters), the way the person wrote",
 "state": "Maharashtra",
 "city": "Pune",
 "summary": "The user worked at a startup in Pune with a monthly salary of 35000 rupees. They did not receive their salary from August to October 2026 and resigned on October 31. The HR claims there are no funds and promised to pay later.",
 "user_goal": "To get the unpaid salary for August, September, and October 2026.",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [
  {
   "date": "2026-08",
   "event": "Salary for the month was not paid",
   "proof": null
  },
  {
   "date": "2026-09",
   "event": "Salary for the month was not paid",
   "proof": null
  },
  {
   "date": "2026-10-31",
   "event": "User resigned from the company",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": null,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": 35000,
  "months_unpaid": 3,
  "other_dues": null,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [
  "offer letter",
  "payslips"
 ],
 "evidence_missing": [
  "bank statements showing salary credits",
  "resignation email or acceptance letter",
  "written communication with HR regarding unpaid dues"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "क्या आपके पास HR की कोई लिखित बात (chat या email) है जिसमें उन्होंने पैसे देने से मना किया या बाद में देने को कहा?",
  "क्या आपने कंपनी को बकाया सैलरी के लिए कोई formal email या legal notice भेजा है?"
 ]
}

```

## Calculation (code)

- Monthly salary Rs 35,000 x 3 unpaid month(s) = Rs 105,000

- Amount to claim: Rs 105,000

## Where you stand

आपकी स्थिति मजबूत है क्योंकि आपके पास ऑफर लेटर और पेस्लिप्स जैसे सबूत हैं। कंपनी का अगस्त से अक्टूबर 2026 तक की सैलरी न देना कॉन्ट्रैक्ट का उल्लंघन है, जिसके लिए आप Code on Wages, 2019 [KB:cow_s17] के तहत अपनी बकाया राशि मांग सकते हैं। चूँकि आपने इस्तीफा दे दिया है, नियम के अनुसार आपके बकाया पैसे तय समय के भीतर मिलने चाहिए थे [KB:cow_s17]। कमजोरी यह है कि आपके पास HR के साथ हुई बातचीत या बैंक स्टेटमेंट का लिखित सबूत अभी नहीं है। आप लेबर कमिश्नर के पास 3 साल के भीतर शिकायत दर्ज कर सकते हैं [KB:cow_s45]।

## Options

1. **HR को लिखित रिमाइंडर भेजें** (1-2 दिन, free): HR या कंपनी को ईमेल या व्हाट्सएप पर अपनी बकाया सैलरी (35000 रुपये प्रति महीने के हिसाब से 3 महीने की कुल राशि) के लिए औपचारिक रूप से लिखित में मांग भेजें।

2. **लेबर कमिश्नर कार्यालय में शिकायत** (कुछ हफ्ते, low): अगर कंपनी पैसे नहीं देती है, तो आप लेबर डिपार्टमेंट या लेबर कमिश्नर के पास अनपेड सैलरी के लिए क्लेम फाइल कर सकते हैं [KB:cow_s45]।

## What I don't know

- क्या कंपनी के साथ हुए एग्रीमेंट में रेजिग्नेशन के बाद फुल एंड फाइनल सेटलमेंट (F&F) को लेकर कोई अलग शर्त थी।

- क्या कंपनी के पास वाकई फंड्स की कोई कानूनी समस्या है या वे सिर्फ टालमटोल कर रहे हैं।

## Needs lawyer: False - अभी मामला शुरुआती स्तर पर है और आप खुद HR को लिखकर या लेबर विभाग में शिकायत करके शुरुआत कर सकते हैं। वकील की जरूरत तब पड़ेगी जब कंपनी लेबर अधिकारी के सामने भी पैसे न दे और कोर्ट जाना पड़े।

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17",
  "cow_s45"
 ]
}

```

## Draft: LEGAL DEMAND NOTICE FOR UNPAID SALARY DUES

```

Date: [Current Date]

From:
[Your Name]
[Your Address]
Pune, Maharashtra
Phone: [PHONE_1]

To:
The Employer / Managing Director,
[Company Name],
Pune, Maharashtra

SUBJECT: DEMAND FOR PAYMENT OF UNPAID SALARY AND RESIGNATION DUES AMOUNTING TO RS. 105,000

Dear Sir/Madam,

1. That the undersigned was employed with your startup establishment in Pune at a monthly salary of Rs. 35,000, under the terms of our employment agreement and offer letter.

2. That the undersigned diligently performed their duties, but the monthly salary for the months of August 2026, September 2026, and October 2026 has not been paid to date, totaling Rs. 105,000.

3. That the undersigned formally resigned from the company on October 31, 2026. As per Section 17 of the Code on Wages, 2019 [KB:cow_s17], when an employee resigns, all due wages must be paid within the stipulated timelines. Further, under Section 73 of the Indian Contract Act, 1872 [KB:ica_s73], failure to pay agreed remuneration amounts to a breach of contract, entitling the employee to claim compensation for losses naturally arising from such breach.

4. That despite oral communications where your HR department acknowledged the dues and cited fund shortages with promises to pay later, no clearance has been provided.

5. Therefore, through this notice, you are formally called upon to clear the total outstanding dues amounting to Rs. 105,000 within 15 (fifteen) days from the receipt of this notice.

6. Please note that if you fail to make the payment within the stipulated 15 days, the undersigned shall be constrained to initiate lawful next steps, which include filing a formal claim for unpaid wages before the designated Labour Authority under Section 45 of the Code on Wages, 2019 [KB:cow_s45], and seeking appropriate legal remedies.

Sincerely,

[Your Signature]
[Your Name]

```

Explanation for user: यह कानूनी नोटिस आपकी रुकी हुई सैलरी के लिए कंपनी को भेजा जा रहा है। इसमें अगस्त, सितंबर और अक्टूबर 2026 की कुल 1,05,000 रुपये की बकाया राशि का स्पष्ट हिसाब दिया गया है। नोटिस मिलने के 15 दिनों के भीतर कंपनी को यह पैसा देने के लिए कहा गया है। यदि कंपनी पैसे नहीं देती है, तो आप लेबर कमिश्नर ऑफिस में श्रम अधिकारी के पास आधिकारिक शिकायत दर्ज करा सकते हैं। इस दस्तावेज़ को भेजने से कंपनी पर कानूनी दबाव बनेगा।

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["cow_s17", "cow_s45", "ica_s73"]}