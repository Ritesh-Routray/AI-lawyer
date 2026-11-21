# con04_tamil_coaching  (gemini:gemini-3.5-flash-lite)

## Input

நான் சென்னையில் ஒரு கோச்சிங் சென்டரில் 45000 ரூபாய் கட்டினேன். இரண்டு வாரத்தில் வகுப்புகளை நிறுத்திவிட்டார்கள். பணத்தை திருப்பி தர மறுக்கிறார்கள். ரசீது என்னிடம் உள்ளது.

## Reply shown to user

வணக்கம். நீங்கள் கோச்சிங் சென்டரில் செலுத்திய 45000 ரூபாய் கட்டணத்தை திரும்பப் பெறுவது நுகர்வோர் சட்டத்தின் கீழ் சாத்தியமாகும் [KB:cpa_consumer_def]. வகுப்புகள் இரண்டு வாரங்களில் நிறுத்தப்பட்டதும், பணத்தை தராமல் இருப்பதும் சேவை குறைபாடு ஆகும் [KB:cpa_consumer_def]. உங்களிடம் பணம் செலுத்திய ரசீது இருப்பது நல்ல பலம். முதற்கட்டமாக, சென்டருக்கு எழுத்துப்பூர்வமாக பணத்தை திருப்பிக் கோரி செய்தி அனுப்பவும். இது பலனளிக்கவில்லை என்றால், தேசிய நுகர்வோர் உதவி மையத்தை (NCH) 1915 என்ற எண்ணில் தொடர்பு கொண்டு இலவசமாகப் புகார் அளிக்கலாம் [KB:forum_nch]. 5 லட்சம் வரை உள்ள தொகைக்கு மாவட்ட நுகர்வோர் ஆணையத்தில் கட்டணம் எதுவும் செலுத்தத் தேவையில்லை [KB:cpa_fee_nil_5lakh]. பணத்தைத் திருப்பத் தருமாறு சென்டரிடம் ஏற்கனவே எழுத்துப்பூர்வமாக எதாவது கோரிக்கை விடுத்தீர்களா?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "consumer",
 "problem_subtype": "coaching class fee refund not processed",
 "user_language": "Tamil written in Tamil script (not Roman letters), the way the person wrote",
 "state": "Tamil Nadu",
 "city": "Chennai",
 "summary": "The user paid 45000 rupees to a coaching center in Chennai. The classes were stopped within two weeks, and the center is refusing to refund the money.",
 "user_goal": "Get a refund of the coaching fee paid",
 "user_role": "consumer",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "timeline": [
  {
   "date": null,
   "event": "Paid 45000 rupees to coaching center and classes stopped within two weeks",
   "proof": "receipt"
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
  "amount_refunded": null
 },
 "evidence_have": [
  "receipt"
 ],
 "evidence_missing": [
  "written refund request or communication with coaching center"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "கோச்சிங் சென்டரின் பெயர் என்ன?",
  "பணம் செலுத்திய தேதியைக் குறிப்பிட முடியுமா?",
  "பணத்தைத் திருப்பித் தருமாறு எழுத்துப்பூர்வமாக கோரிக்கை விடுத்தீர்களா?"
 ]
}

```

## Calculation (code)

- Amount paid: Rs 45,000

- Refund due: Rs 45,000

## Where you stand

நீங்கள் சென்னை கோச்சிங் சென்டரில் 45000 ரூபாய் செலுத்தி, இரண்டு வாரங்களில் வகுப்புகள் நிறுத்தப்பட்ட பிறகு பணம் கிடைக்காமல் இருப்பது நுகர்வோர் குறைபாடு ஆகும் [KB:cpa_consumer_def]. உங்களிடம் பணம் செலுத்தியதற்கான ரசீது உள்ளது, இது ஒரு பலமான ஆதாரம். ஆனால், சென்டரிடம் எழுத்துப்பூர்வமாக பணத்தைத் திருப்பித் தருமாறு கோரியதற்கான ஆதாரம் உங்களிடம் இல்லை [KB:cpa_consumer_def]. இந்த பிரச்சனையை நுகர்வோர் ஆணையம் மூலம் தீர்க்கலாம் [KB:cpa_jurisdiction_2021], மேலும் 2 ஆண்டுகளுக்குள் புகார் அளிக்க வேண்டும் [KB:cpa_limitation].

## Options

1. **எழுத்துப்பூர்வமான கோரிக்கை மற்றும் தேசிய நுகர்வோர் உதவி மையம்** (1-2 வாரங்கள், free): கோச்சிங் சென்டருக்கு வாட்ஸ்அப் அல்லது மின்னஞ்சல் மூலம் பணத்தைத் திருப்பித் தருமாறு முறையான கோரிக்கை அனுப்பவும். அவர்கள் பதிலளிக்கவில்லை என்றால், தேசிய நுகர்வோர் உதவி மையத்தின் (NCH) 1915 என்ற எண்ணில் தொடர்பு கொண்டு புகார் அளிக்கவும் [KB:forum_nch].

2. **நுகர்வோர் ஆணையத்தில் புகார்** (பல மாதங்கள் ஆகலாம், free): தேசிய நுகர்வோர் உதவி மையத்தில் தீர்வு கிடைக்கவில்லை என்றால், மாவட்ட நுகர்வோர் ஆணையத்தில் e-Jagriti தளம் மூலம் ஆன்லைனில் புகார் அளிக்கலாம் [KB:forum_ejagriti]. 5 லட்சம் வரை மதிப்புள்ள புகார்களுக்கு கட்டணம் இல்லை [KB:cpa_fee_nil_5lakh].

## What I don't know

- கோச்சிங் சென்டர் விதித்த ஒப்பந்த நிபந்தனைகளில் பணத்தை திருப்பிக் கொடுக்க முடியாது என்ற விதிகள் ஏதேனும் உள்ளதா என்பது எனக்குத் தெரியாது.

## Needs lawyer: False - இது ஆரம்ப கட்ட நுகர்வோர் பிரச்சனை என்பதால், நீங்களே நுகர்வோர் உதவி மையம் மற்றும் e-Jagriti [KB:forum_ejagriti] தளம் மூலம் புகார் அளிக்கலாம். பெரிய சிக்கல்கள் ஏற்பட்டால் மட்டுமே வழக்கறிஞர் தேவைப்படுவார்.

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
  "forum_nch"
 ]
}

```