# con04_tamil_coaching  (gemini:gemini-3.5-flash-lite)

## Input

நான் சென்னையில் ஒரு கோச்சிங் சென்டரில் 45000 ரூபாய் கட்டினேன். இரண்டு வாரத்தில் வகுப்புகளை நிறுத்திவிட்டார்கள். பணத்தை திருப்பி தர மறுக்கிறார்கள். ரசீது என்னிடம் உள்ளது.

## Reply shown to user

வணக்கம்! நீங்கள் கோச்சிங் சென்டருக்கு செலுத்திய 45,000 ரூபாய் கட்டணத்தை திருப்பிக் தராதது நுகர்வோர் பாதுகாப்பு சட்டத்தின்படி [KB:cpa_consumer_def] சேவை குறைபாடாகும். உங்களிடம் ரசீது இருப்பது நல்ல பலம். ஆனால் பணத்தைத் திருப்பிக் கேட்பது தொடர்பான எழுத்துப்பூர்வமான கடிதம் அல்லது மின்னஞ்சல் உங்களிடம் இல்லை. நீங்கள் இரண்டு ஆண்டுகளுக்குள் [KB:cpa_limitation] [KB:src_cpa_2019_69] மாவட்ட நுகர்வோர் ஆணையத்தில் [KB:cpa_jurisdiction_2021] [KB:src_cpa_2019_34] புகார் அளிக்கலாம். 5 லட்சம் ரூபாய் வரை உள்ள வழக்குகளுக்கு நீதிமன்ற கட்டணம் கிடையாது [KB:cpa_fee_nil_5lakh]. முதல் படியாக, நேஷனல் கன்ஸ்யூமர் ஹெல்ப்லைன் (NCH) [KB:forum_nch] மூலம் புகார் அளிக்கலாம் அல்லது e-Jagriti portal [KB:forum_ejagriti] வழியாக நேரடியாக நுகர்வோர் கோர்ட்டில் புகார் பதிவு செய்யலாம் [KB:src_cpa_2019_35]. கோச்சிங் சென்டரிடம் பணத்தைத் திருப்பிக் கேட்பது தொடர்பாக வாட்ஸ்அப் அல்லது மின்னஞ்சல் மூலம் ஏதேனும் பேசி இருக்கிறீர்களா?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "coaching class refund not processed",
 "user_language": "Tamil written in Tamil script (not Roman letters), the way the person wrote",
 "state": "Tamil Nadu",
 "city": "Chennai",
 "summary": "The user paid 45000 rupees to a coaching center in Chennai. The classes were stopped within two weeks, and the center is refusing to refund the money. The user possesses a receipt.",
 "user_goal": "Get a refund of the 45000 rupees paid for the coaching classes",
 "user_role": "consumer",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "timeline": [
  {
   "date": null,
   "event": "Paid 45000 rupees to coaching center and classes stopped after two weeks",
   "proof": "Receipt"
  }
 ],
 "amounts": {
  "deposit_paid": null,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": null,
  "order_value": 45000,
  "amount_refunded": 0
 },
 "evidence_have": [
  "Receipt"
 ],
 "evidence_missing": [
  "Written communication or email asking for refund",
  "Terms and conditions or refund policy of the coaching center"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "கோச்சிங் சென்டர் பெயர் என்ன?",
  "பணம் செலுத்திய தேதி என்ன?",
  "பணத்தைத் திருப்பித் தருமாறு எழுத்துப்பூர்வமாக ஏதேனும் கோரிக்கை வைத்துள்ளீர்களா?"
 ]
}

```

## Calculation (code)

- Amount paid: Rs 45,000

- Refund due: Rs 45,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Consumer Protection Act, 2019 Section 88 (OFFENCES AND PENALTIES) p.33

- Consumer Protection Act, 2019 Section 69  p.28

- Consumer Protection Act, 2019 Section 35  p.18

- Consumer Protection Act, 2019 Section 89  p.33

- Consumer Protection Act, 2019 Section 34  p.17

- Consumer Protection Act, 2019 Section 47  p.23

- Consumer Protection Act, 2019 Section 20  p.14

- Consumer Protection Act, 2019 Section 72  p.29

## Where you stand

நீங்கள் கோச்சிங் சென்டருக்கு செலுத்திய 45,000 ரூபாய் கட்டணம் மற்றும் வகுப்புகள் பாதியில் நிறுத்தப்பட்ட விவகாரத்தில், நுகர்வோர் பாதுகாப்பு சட்டத்தின்படி [KB:cpa_consumer_def] நீங்கள் நுகர்வோர் ஆவீர்கள். வகுப்புகளை நிறுத்திவிட்டு பணத்தைத் திருப்பிக் தராதது சேவை குறைபாடாகும். உங்களிடம் பணம் செலுத்தியதற்கான ரசீது இருப்பது பலமான ஆதாரமாகும். இருப்பினும், கோச்சிங் சென்டரிடம் பணத்தைத் திருப்பிக் கோரி எழுத்துப்பூர்வமான கோரிக்கை அல்லது அவர்களின் விதிமுறைகள் (terms and conditions) உங்களிடம் இல்லாதது சிறிய பலவீனமாகும். பிரச்சன ஏற்பட்ட நாளிலிருந்து இரண்டு ஆண்டுகளுக்குள் [KB:cpa_limitation] [KB:src_cpa_2019_69] நீங்கள் மாவட்ட நுகர்வோர் ஆணையத்தில் [KB:cpa_jurisdiction_2021] [KB:src_cpa_2019_34] வழக்கு தொடரலாம்.

## Options

1. **தேசிய நுகர்வோர் உதவி மையம் (NCH)** (1-2 வாரங்கள், free): 1915 என்ற எண்ணை அழைத்து அல்லது consumerhelpline.gov.in இணையதளம் மூலம் புகார் அளிக்கவும்.

2. **e-Jagriti [KB:forum_ejagriti] போர்ட்டலில் நுகர்வோர் புகார்** (சில வாரங்கள் முதல் மாதங்கள் வரை, free): e-Jagriti [KB:forum_ejagriti] இணையதளம் வழியாக மாவட்ட நுகர்வோர் ஆணையத்தில் முறைப்படி புகார் பதிவு செய்யவும்.

## What I don't know

- கோச்சிங் சென்டரின் விதிமுறைகள் மற்றும் நிபந்தனைகளில் (Terms and Conditions) வகுப்புகள் பாதியில் நின்றால் பணப்பிடித்தம் பற்றிய விதிகள் உள்ளதா என்பது எனக்குத் தெரியாது.

## Needs lawyer: False - இது 5 லட்சம் ரூபாய்க்கும் குறைவான நுகர்வோர் பிரச்சனை என்பதால், நீங்களே கட்டணமின்றி நுகர்வோர் ஆணையத்தில் புகார் அளிக்கலாம் [KB:cpa_fee_nil_5lakh]. வழக்கறிஞர் கட்டாயமில்லை.

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
  "forum_ejagriti",
  "forum_nch",
  "src_cpa_2019_34",
  "src_cpa_2019_35",
  "src_cpa_2019_69"
 ],
 "support_check": "not auto-checked (non-English reply; cross-encoder is English-only)"
}

```