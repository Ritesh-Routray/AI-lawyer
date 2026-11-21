# sal03_bengali_shop  (gemini:gemini-3.5-flash-lite)

## Input

আমি কলকাতায় একটা দোকানে কাজ করতাম, মাসে ১২০০০ টাকা বেতন। মালিক দুই মাসের বেতন দেয়নি এবং আমাকে কাজ থেকে বের করে দিয়েছে। কোনো লিখিত কাগজ নেই।

## Reply shown to user

আপনার দুই মাসের মোট ২৪০০০ টাকা বেতন বকেয়া রয়েছে, যা মালিকের নিয়ম অনুযায়ী বরখাস্ত হওয়ার ২ দিনের মধ্যে দেওয়ার কথা ছিল [KB:cow_s17]। আপনার কাছে নিয়োগপত্র বা বেতন স্লিপ না থাকায় প্রমাণ জোগাড় করা একটু জরুরি। আপনি চাইলে শ্রম দপ্তরে অভিযোগ জানাতে পারেন [KB:cow_s45]। আপনার কি মালিকের সাথে কথা বলার বা টাকা পাওয়ার কোনো চ্যাট বা অডিও রেকর্ড আছে?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid salary and termination without notice",
 "user_language": "Bengali written in Bengali script (not Roman letters), the way the person wrote",
 "state": "West Bengal",
 "city": "Kolkata",
 "summary": "The user worked at a shop in Kolkata with a monthly salary of 12000 rupees. The employer has not paid for two months of work and terminated the user without any written documentation.",
 "user_goal": "to get the unpaid salary for two months",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [
  {
   "date": null,
   "event": "Terminated from work by the employer without paying two months of salary",
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
  "appointment letter",
  "salary slips",
  "bank statements showing salary payments",
  "identity card of the shop"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "মালিকের নাম বা দোকানের নাম কি আপনার মনে আছে?",
  "শেষ কবে আপনি বেতন পেয়েছিলেন বা কত মাস ধরে কাজ করেছেন?",
  "আপনার কি কোনো চ্যাট বা অডিও রেকর্ড আছে মালিকের সাথে?"
 ]
}

```

## Calculation (code)

- Monthly salary Rs 12,000 x 2 unpaid month(s) = Rs 24,000

- Amount to claim: Rs 24,000

## Where you stand

আপনার মালিকের কাছে দুই মাসের ১২০০০ টাকা করে মোট ২৪০০০ টাকা বকেয়া রয়েছে [KB:cow_s17]। Code on Wages, 2019 অনুযায়ী কাজ ছাড়ার বা বরখাস্ত হওয়ার ২ দিনের মধ্যে সমস্ত পাওনা টাকা মিটিয়ে দেওয়ার নিয়ম আছে [KB:cow_s17]। আপনার মূল সমস্যা হলো আপনার কাছে কোনো লিখিত নিয়োগপত্র বা বেতন স্লিপ নেই, যা প্রমাণ করা একটু কঠিন হতে পারে। তবে আপনি চাইলে শ্রম দপ্তরে ৩ বছরের মধ্যে অভিযোগ জানাতে পারেন [KB:cow_s45]। চুক্তি ভঙ্গের জন্য আপনি ক্ষতিপূরণও দাবি করতে পারেন [KB:ica_s73]।

## Options

1. **মালিকের সাথে সরাসরি কথা বলুন বা মেসেজ করুন** (১-২ দিন, free): মালিককে ফোন করে বা হোয়াটসঅ্যাপে বকেয়া ২৪০০০ টাকা মিটিয়ে দেওয়ার অনুরোধ করুন এবং লিখিতভাবে উত্তর চান।

2. **শ্রম দপ্তরে অভিযোগ দায়ের করুন** (কয়েক সপ্তাহ, low): নির্দিষ্ট সরকারি কর্তৃপক্ষের কাছে বকেয়া বেতনের জন্য আবেদন করুন [KB:cow_s45]।

## What I don't know

- মালিকের কাছ থেকে কোনো লিখিত প্রমাণ না থাকায় আদালতে বা দপ্তরে তা প্রমাণ করা কতটা সহজ হবে তা নিশ্চিত নয়।

## Needs lawyer: False - প্রাথমিক পর্যায়ে আপনি নিজে বা শ্রম দপ্তরের সাহায্যে অভিযোগ করতে পারেন, তাই এখনই আইনজীবীর প্রয়োজন নেই। তবে পরিস্থিতি জটিল হলে বা আইনি নোটিশ পাঠানোর দরকার পড়লে আইনজীবীর সাহায্য নিতে পারেন।

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17",
  "cow_s45",
  "ica_s73"
 ]
}

```