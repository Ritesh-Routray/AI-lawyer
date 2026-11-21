# sal03_bengali_shop  (groq:qwen/qwen3.8-27b)

## Input

আমি কলকাতায় একটা দোকানে কাজ করতাম, মাসে ১২০০০ টাকা বেতন। মালিক দুই মাসের বেতন দেয়নি এবং আমাকে কাজ থেকে বের করে দিয়েছে। কোনো লিখিত কাগজ নেই।

## Reply shown to user

আপনার অবস্থাটা হলো: মালিক ২ মাসের বেতন (মোট ২৪,০০০ টাকা) দিতে পারেননি, যা আইনত আপনার অধিকার। Code on Wages, 2019 অনুযায়ী, চাকরি থেকে বরখাস্ত হলে বেতন ২ কর্মদিবসের মধ্যে দিতে হয় [KB:cow_s17] এবং ৩ বছরের মধ্যে শ্রম দপ্তরে অভিযোগ করা যায় [KB:cow_s45]। আপনার সবচেয়ে বড় দুর্বলতা হলো চাকরির কোনো লিখিত প্রমাণ নেই। তাই প্রথম ধাপ: মালিককে WhatsApp-এ লিখুন যে বেতন দিতে হবে এবং তার উত্তরটি স্ক্রিনশট করে রাখুন। এরপর কলকাতার শ্রম কমিশনারের অফিসে লিখিত অভিযোগ দাখিল করুন। যদি মালিক শ্রম দপ্তরের নোটিশ উপেক্ষা করে, তাহলে NALSA হেল্পলাইন 15100-এ কল করে ফ্রি আইনি সহায়তা নিন [KB:lsa_s12_legal_aid]। আপনি ঠিক কখন থেকে কাজ করতেন এবং কখন বরখাস্ত হন?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid wages and termination",
 "user_language": "Bengali",
 "state": "West Bengal",
 "city": "Kolkata",
 "summary": "The user worked at a shop in Kolkata with a monthly salary of 12000 INR. The owner terminated their employment and has not paid the salary for the last two months. The user states they do not have any written documentation of the employment.",
 "user_goal": "To recover the unpaid salary for two months.",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [
  {
   "date": null,
   "event": "Employment termination and non-payment of salary for the last two months",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": null,
  "deductions_claimed": null,
  "monthly_rent": null,
  "monthly_salary": 12000,
  "months_unpaid": 2,
  "other_dues": null,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [],
 "evidence_missing": [
  "Bank statements showing salary credits",
  "Pay slips or salary slips",
  "Employment contract or offer letter",
  "Communication records (SMS/WhatsApp) with the employer regarding salary or termination"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "আপনি কখন থেকে এই দোকানে কাজ করতেন এবং কখন চাকরি থেকে বরখাস্ত হন?",
  "বেতন সাধারণত কীভাবে পেতেন (ক্যাশ, ব্যাংক ট্রান্সফার, UPI)?",
  "মালিকের সাথে বেতন বা চাকরির বিষয়ে কোনো লিখিত চুক্তি বা অফার লেটার ছিল কি না?"
 ]
}

```

## Calculation (code)

- Monthly salary Rs 12,000 x 2 unpaid month(s) = Rs 24,000

- Amount to claim: Rs 24,000

## Where you stand

আপনার অবস্থাটা হলো: মালিক ২ মাসের বেতন (মোট ২৪,০০০ টাকা) দিতে পারেননি, যা আইনত আপনার অধিকার। আপনার সবচেয়ে বড় দুর্বলতা হলো চাকরির কোনো লিখিত প্রমাণ (যেমন চুক্তি বা পে-স্লিপ) নেই, যা মামলায় বা অভিযোগে আপনার দাবি শক্তিশালী করে। তবে, Code on Wages, 2019 অনুযায়ী, চাকরি থেকে বরখাস্ত হলে বেতন ২ কর্মদিবসের মধ্যে দিতে হয় [KB:cow_s17] এবং ৩ বছরের মধ্যে সরকারি কর্তৃপক্ষের কাছে অভিযোগ করা যায় [KB:cow_s45]। আপনি এখনো সময়সীমার মধ্যে আছেন, তাই আপনার দাবি আইনত দাঁড়িয়ে আছে।

## Options

1. **লিখিত দাবি (WhatsApp/SMS)** (১ দিন, ফ্রি): মালিককে WhatsApp বা SMS-এ লিখুন যে ২ মাসের বেতন (২৪,০০০ টাকা) এখনো পাওয়া যায়নি এবং Code on Wages, 2019 অনুযায়ী তা দিতে হবে [KB:cow_s17]। তার উত্তরটি স্ক্রিনশট করে রাখুন।

2. **প্রমাণ সংগ্রহ** (৩-৫ দিন, ফ্রি): ব্যাংক স্টেটমেন্ট (যদি বেতন ব্যাংকে আসত), পুরনো পে-স্লিপ, বা সহকর্মীদের সাক্ষ্য (যে তারাও একই দোকানে কাজ করত) সংগ্রহ করুন।

3. **শ্রম কমিশনারের কাছে অভিযোগ** (১-২ সপ্তাহ (প্রক্রিয়া), ফ্রি / খুব কম (ফর্ম ফি)): কলকাতার শ্রম দপ্তর (Labour Department) বা শ্রম কমিশনারের অফিসে গিয়ে লিখিত অভিযোগ দাখিল করুন। Code on Wages, 2019 অনুযায়ী এটি ৩ বছরের মধ্যে করা যায় [KB:cow_s45]।

4. **ফ্রি আইনি সহায়তা** (১-২ সপ্তাহ, ফ্রি): যদি মালিক শ্রম দপ্তরের নোটিশ উপেক্ষা করে, তাহলে NALSA হেল্পলাইন 15100-এ কল করুন বা ডিস্ট্রিক্ট লিগ্যাল সার্ভিসেস অথরিটি (DLSA) থেকে ফ্রি আইনজীবী নিন [KB:lsa_s12_legal_aid]।

## What I don't know

- আপনি ঠিক কখন থেকে কাজ করতেন এবং কখন বরখাস্ত হন (তারিখ প্রয়োজন)।

- বেতন ক্যাশে নাকি ব্যাংকে পেতেন (প্রমাণের ধরন নির্ভর করে)।

- দোকানটি কি 'Code on Wages [KB:cow_s17]' এর আওতায় আসে (সাধারণত ১০+ কর্মী থাকলে)।

## Needs lawyer: False - এটি একটি সাধারণ বেতন দাবি। প্রথমে লিখিত দাবি এবং শ্রম দপ্তরের অভিযোগ নিজেই করা যায়। আইনজীবী প্রয়োজন হবে যদি মালিক শ্রম দপ্তরের নোটিশ উপেক্ষা করে বা মামলায় যায়।

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17",
  "cow_s45",
  "lsa_s12_legal_aid"
 ]
}

```