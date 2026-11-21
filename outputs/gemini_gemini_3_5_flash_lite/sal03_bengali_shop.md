# sal03_bengali_shop  (gemini:gemini-3.5-flash-lite)

## Input

আমি কলকাতায় একটা দোকানে কাজ করতাম, মাসে ১২০০০ টাকা বেতন। মালিক দুই মাসের বেতন দেয়নি এবং আমাকে কাজ থেকে বের করে দিয়েছে। কোনো লিখিত কাগজ নেই।

## Reply shown to user

নমস্কার। আপনার কলকাতার ওই দোকান থেকে দুই মাসের মোট ২৪০০০ টাকার বকেয়া বেতন পাওয়ার অধিকার রয়েছে [KB:cow_s17]। চাকরি চলে যাওয়ার পর দুই দিনের মধ্যে বقেয়া মেটানোর নিয়ম থাকলেও [KB:src_cow_2019_17], আপনার কাছে লিখিত চুক্তি বা পে-স্লিপ না থাকায় একটু সমস্যা হতে পারে [KB:cow_s45]। প্রথম ধাপে আপনি মালিককে হোয়াটসঅ্যাপ বা মেসেজ করে আপনার বকেয়া টাকার কথা লিখিতভাবে জানাতে পারেন, যাতে প্রমাণের একটি ভিত্তি তৈরি হয়। এরপরও কাজ না হলে শ্রম দপ্তরে অভিযোগ জানানোর রাস্তা খোলা আছে [KB:cow_s45]। আপনার কি মালিকের সাথে আগে বেতনের বিষয়ে কোনো চ্যাট বা মেসেজ হয়েছে যা প্রমাণ হিসেবে দেখানো যায়?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "salary",
 "problem_subtype": "unpaid salary and wrongful termination",
 "user_language": "Bengali written in Bengali script (not Roman letters), the way the person wrote",
 "state": "West Bengal",
 "city": "Kolkata",
 "summary": "The user worked at a shop in Kolkata with a monthly salary of 12000 rupees. The employer terminated their employment and has not paid two months of salary, and there is no written employment contract.",
 "user_goal": "Get the unpaid salary for two months",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "employer"
 },
 "timeline": [
  {
   "date": null,
   "event": "Worked at a shop in Kolkata with a monthly salary of 12000 rupees",
   "proof": null
  },
  {
   "date": null,
   "event": "Terminated from work and two months of salary not paid",
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
  "payslips",
  "bank statements showing salary credits",
  "appointment letter"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "মালিকের নাম বা দোকানের নাম কি আপনার জানা আছে?",
  "কোন কোন মাসের বেতন বাকি আছে?",
  "বেতন কি ব্যাঙ্কে জমা হতো নাকি নগদে দেওয়া হতো?"
 ]
}

```

## Calculation (code)

- Monthly salary Rs 12,000 x 2 unpaid month(s) = Rs 24,000

- Amount to claim: Rs 24,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Code on Wages, 2019 Section 54  p.27

- Code on Wages, 2019 Section 17  p.12

- Code on Wages, 2019 Section 45  p.23

- Code on Wages, 2019 Section 18  p.12

- Code on Wages, 2019 Section 48  p.24

- Code on Wages, 2019 Section 16  p.12

- Code on Wages, 2019 Section 27  p.17

- Code on Wages, 2019 Section 12  p.11

## Where you stand

আপনার দুই মাসের বকেয়া বেতন (মোট ২৪০০০ টাকা) দাবি করার অধিকার আপনার আছে [KB:cow_s17], কারণ চাকরি থেকে বরখাস্ত করার পর দুই কার্যদিবসের মধ্যে পাওনা মিটিয়ে দেওয়ার নিয়ম রয়েছে [KB:src_cow_2019_17]। তবে আপনার কাছে নিয়োগপত্র বা পে-স্লিপের মতো প্রমাণ না থাকায় কিছুটা অসুবিধা হতে পারে [KB:cow_s45]। আপনি শ্রম দপ্তরে বা নির্ধারিত কর্তৃপক্ষের কাছে অভিযোগ জানাতে পারেন [KB:cow_s45], তবে লিখিত চুক্তি না থাকায় প্রমাণ জোগাড় করা জরুরি। নির্দিষ্ট সময়ের মধ্যে (সাধারণত ৩ বছরের মধ্যে) এই দাবি করতে হবে [KB:cow_s45]।

## Options

1. **মালিকের সাথে সরাসরি কথা বলুন বা লিখিত বার্তা পাঠান** (১-২ দিন, বিনামূল্যে): মালিককে হোয়াটসঅ্যাপে বা লিখিতভাবে আপনার বকেয়া দুই মাসের বেতনের কথা মনে করিয়ে দিন এবং মিটিয়ে দিতে বলুন।

2. **স্থানীয় শ্রম দপ্তরে যোগাযোগ করুন** (কয়েক সপ্তাহ, কম খরচ / বিনামূল্যে): কলকাতার স্থানীয় শ্রম দপ্তরে বা লেবার কমিশনার অফিসে বকেয়া বেতনের জন্য অভিযোগ দায়ের করুন।

## What I don't know

- মালিকের সাথে আপনার মৌখিক বা অন্য কোনো লিখিত চুক্তি ছিল কিনা তা আমি জানি না।

- আপনার বেतन কি ব্যাঙ্কে জমা হতো নাকি নগদে দেওয়া হতো তার কোনো প্রমাণ আছে কিনা তা স্পষ্ট নয়।

## Needs lawyer: False - যেহেতু এটি একটি সাধারণ বকেয়া বেতনের মামলা এবং কোনো পুলিশ বা আদালতের নোটিশ নেই, তাই আপনি নিজেই শ্রম দপ্তরে অভিযোগ বা মালিকের সাথে যোগাযোগ করতে পারেন।

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "cow_s17",
  "cow_s45",
  "src_cow_2019_17"
 ],
 "support_check": "not auto-checked (non-English reply; cross-encoder is English-only)"
}

```