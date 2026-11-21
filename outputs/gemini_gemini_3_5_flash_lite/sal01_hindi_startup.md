# sal01_hindi_startup  (gemini:gemini-3.5-flash-lite)

## Input

मैं पुणे में एक स्टार्टअप में काम करता था, सैलरी 35000 महीना थी। अगस्त से अक्टूबर 2026 तक की सैलरी नहीं मिली। 31 अक्टूबर को मैंने इस्तीफा दे दिया। HR कहता है पैसे नहीं हैं, बाद में देंगे। मेरे पास ऑफर लेटर और पुरानी सैलरी स्लिप हैं।

## Reply shown to user

नमस्ते! आपका मामला काफी स्पष्ट है। पुणे के स्टार्टअप में अगस्त से अक्टूबर 2026 तक का आपका 35000 रुपये प्रति महीने के हिसाब से कुल 105,000 रुपये का वेतन बकाया है। कानून के मुताबिक इस्तीफा देने के 2 दिन के भीतर पूरा हिसाब मिलना चाहिए था [KB:src_cow_2019_17], और 'फंड नहीं है' यह कंपनी का बहाना कानूनन सही नहीं है। आपके पास ऑफर लेटर और सैलरी स्लिप्स हैं, जो आपके पक्ष को मजबूत करती हैं। सबसे पहले आपको कंपनी को लिखित में मेल या मैसेज भेजकर बकाया राशि की मांग करनी चाहिए। यदि वे मना करते हैं, तो आप श्रम विभाग (Labour Commissioner office) में शिकायत दर्ज कर सकते हैं [KB:cow_s45]। क्या आपके पास एचआर की कोई ऐसी चैट या ईमेल है जिसमें उन्होंने पैसे देने से मना किया है?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid salary and resignation dues",
 "user_language": "Hindi written in Devanagari script (not Roman letters), the way the person wrote",
 "state": "Maharashtra",
 "city": "Pune",
 "summary": "The user worked at a startup in Pune with a monthly salary of 35000 rupees. They did not receive their salary from August 2026 to October 2026 and resigned on October 31, 2026, but the HR claims there are no funds right now.",
 "user_goal": "To recover unpaid salary for August, September, and October 2026.",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [
  {
   "date": "2026-08",
   "event": "Salary unpaid for August",
   "proof": null
  },
  {
   "date": "2026-09",
   "event": "Salary unpaid for September",
   "proof": null
  },
  {
   "date": "2026-10-31",
   "event": "User resigned from the startup, HR stated funds are not available",
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
  "old salary slips"
 ],
 "evidence_missing": [
  "bank statements showing unpaid months",
  "resignation email or acceptance letter",
  "written communication with HR regarding unpaid dues"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "क्या आपके पास HR की कोई लिखित बात या चैट है जिसमें उन्होंने पैसे देने से मना किया है?",
  "क्या आपने अगस्त से अक्टूबर तक की अटेंडेंस या बैंक स्टेटमेंट का कोई सबूत रखा है?"
 ]
}

```

## Calculation (code)

- Monthly salary Rs 35,000 x 3 unpaid month(s) = Rs 105,000

- Amount to claim: Rs 105,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Code on Wages, 2019 Section 17  p.12

- Code on Wages, 2019 Section 45  p.23

- Code on Wages, 2019 Section 59  p.29

- Code on Wages, 2019 Section 18  p.12

- Code on Wages, 2019 Section 48  p.24

- Code on Wages, 2019 Section 54  p.27

- Code on Wages, 2019 Section 56  p.28

- Code on Wages, 2019 Section 43 (PAYMENT OF DUES, CLAIMS AND AUDIT) p.22

## Where you stand

आपकी स्थिति मजबूत है क्योंकि पुणे के स्टार्टअप में अगस्त से अक्टूबर 2026 तक का 35000 रुपये प्रति महीने का वेतन (कुल 105,000 रुपये) कंपनी द्वारा नहीं दिया गया है। Code on Wages, 2019 के अनुसार इस्तीफे के बाद 2 कामकाजी दिनों के भीतर पूरा वेतन मिलना चाहिए था [KB:src_cow_2019_17], और कंपनी के पास फंड न होने का बहाना वेतन रोकने का वैध कारण नहीं है। आपके पास ऑफर लेटर और पुरानी सैलरी स्लिप्स हैं, जो आपके रोजगार का प्रमाण हैं। हालांकि, यदि एचआर के साथ हुई बातचीत या बैंक स्टेटमेंट का लिखित प्रमाण नहीं है, तो यह कमजोरी हो सकती है, लेकिन इस कानून के तहत यह साबित करने की जिम्मेदारी employer पर है कि उसने भुगतान कर दिया है [KB:src_cow_2019_59], और आप 3 साल के भीतर श्रम विभाग के समक्ष दावा कर सकते हैं [KB:cow_s45].

## Options

1. **लिखित मांग पत्र भेजें** (1-2 दिन, फ्री): एचआर और मैनेजमेंट को ईमेल या लिखित रूप में अपना बकाया वेतन (105,000 रुपये) तुरंत देने का अनुरोध करें और Code on Wages [KB:cow_s17] का हवाला दें।

2. **श्रम विभाग (Labour Commissioner) के पास शिकायत दर्ज करें** (1-3 महीने, कम / फ्री): यदि कंपनी पैसे देने से मना करती है, तो पुणे के स्थानीय श्रम कार्यालय में वेतन भुगतान न होने की आधिकारिक शिकायत दर्ज करें।

## What I don't know

- क्या आपके पास इस्तीफे की ईमेल या लिखित स्वीकृति है?

- क्या कंपनी के पास रोजगार समझौते में कोई ऐसी शर्त थी जो इस भुगतान को प्रभावित करे?

## Needs lawyer: False - चूंकि यह स्पष्ट वेतन बकाया मामला है और अभी तक कोई अदालत का मामला या पुलिस शिकायत नहीं हुई है, आप पहले स्वयं श्रम विभाग में शिकायत दर्ज कर सकते हैं। यदि कंपनी कानूनी नोटिस भेजती है या मामला ज्यादा उलझता है, तब वकील की जरूरत पड़ेगी।

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s45",
  "src_cow_2019_17",
  "src_cow_2019_59"
 ],
 "support_check": "not auto-checked (non-English reply; cross-encoder is English-only)"
}

```

## Draft: Legal Notice for Recovery of Unpaid Salary and Dues

```

Date: [Current Date]

From:
[Your Name]
[Your Address]
Phone: [PHONE_1]

To:
[Employer/Startup Name or HR Name]
[Company Address, Pune, Maharashtra]

Subject: Legal Demand Notice for Payment of Unpaid Salary amounting to Rs. 105,000

Dear Sir/Madam,

1. That the undersigned, [Your Name], was employed with your startup located in Pune, Maharashtra, under an agreed monthly salary of Rs. 35,000, as per the offer letter and terms of employment.

2. That the undersigned diligently performed duties, but has not received salary for the months of August 2026, September 2026, and October 2026, totaling 3 unpaid months of service.

3. That the undersigned formally resigned from service on October 31, 2026. At the time of resignation, the HR department stated that funds were not available, which does not absolve the establishment of its statutory and contractual liabilities to clear pending wages.

4. That as per Section 17(2) of the Code on Wages, 2019 [KB:cow_s17], where an employee has resigned from service, the wages payable must be paid within two working days of the resignation. Furthermore, under Section 17(1) of the Code on Wages, 2019 [KB:cow_s17], monthly salary must be paid before the expiry of the seventh day of the succeeding month. The failure to pay the earned wages also constitutes a breach of the employment agreement under Section 73 of the Indian Contract Act, 1872 [KB:ica_s73].

5. That the total calculated amount due and payable by you to the undersigned is Rs. 105,000 (Monthly salary Rs. 35,000 x 3 unpaid months).

6. You are hereby called upon to pay the full and final calculated amount of Rs. 105,000 within 15 days of receiving this notice.

7. In the event of your failure to clear the said dues within the stipulated 15 days, the undersigned shall be constrained to initiate lawful next steps, including filing a claim before the appointed authority under Section 45 of the Code on Wages, 2019 [KB:cow_s45] and taking further legal proceedings for recovery along with applicable compensation.

Sincerely,

[Your Signature]
[Your Name]

```

Explanation for user: यह दस्तावेज़ आपकी बकाया सैलरी वसूलने के लिए एक कानूनी नोटिस है। इसमें अगस्त, सितंबर और अक्टूबर 2026 के महीनों की 35,000 रुपये प्रति माह के हिसाब से कुल 1,05,000 रुपये की बकाया राशि का जिक्र किया गया है। इसमें कंपनी को 15 दिन के भीतर पैसे चुकाने के लिए कहा गया है। अगर कंपनी पैसे नहीं देती है, तो आप लेबर डिपार्टमेंट या सक्षम प्राधिकारी के पास शिकायत दर्ज करने जैसे कानूनी कदम उठा सकते हैं। नोटिस भेजने के बाद आपको 15 दिन का इंतजार करना होगा।

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["cow_s17", "cow_s45", "ica_s73"]}