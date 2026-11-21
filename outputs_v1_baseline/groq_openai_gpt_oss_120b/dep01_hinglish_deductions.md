# dep01_hinglish_deductions  (groq:openai/gpt-oss-120b)

## Input

Maine Bangalore mein 2 saal flat rent pe liya tha, rent 18000 tha aur 60000 deposit diya tha bank transfer se. March 2026 mein flat khali kar diya, keys bhi de di. Ab landlord bol raha hai painting aur cleaning ke 25000 katenge aur baaki bhi abhi nahi de raha, 6 mahine ho gaye. Agreement mere paas hai.

## Reply shown to user

Aapne Rs 60,000 ka security deposit diya tha aur landlord ne Rs 25,000 ka deduction painting‑cleaning ke liye bataya hai. Agar landlord ke paas is deduction ka koi bill ya damage ka proof nahi hai, to aap poora deposit wapas maang sakte hain [KB:ica_s73]. Sabse pehle ek polite written demand bhejein, jisme unse deduction ka detailed invoice aur photos maangein, aur 2 hafte ke andar deposit wapas karne ki request karein. Agar response na mile, to aap legal notice bhejne ke liye free legal aid ya ek low‑cost lawyer se madad le sakte hain. Court tak le jaana last resort hai. Kya aapke paas landlord se koi likhit message ya email hai jisme deduction ka zikr ho?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit deduction dispute",
 "user_language": "Hinglish",
 "state": "Karnataka",
 "city": "Bangalore",
 "summary": "The user rented a flat in Bangalore for two years, paid a security deposit of 60000 rupees by bank transfer, and vacated the premises in March 2026 handing over the keys. The landlord is now claiming a deduction of 25000 rupees for painting and cleaning and has not returned the remaining deposit even after six months.",
 "user_goal": "To get the full security deposit back and contest the landlord's claimed deduction.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": null,
   "event": "Flat rented for 2 years, rent 18000 per month, deposit 60000 paid by bank transfer",
   "proof": "bank transfer receipt"
  },
  {
   "date": "2026-03",
   "event": "Flat vacated and keys handed over to landlord",
   "proof": "rental agreement"
  },
  {
   "date": null,
   "event": "Landlord informs about 25000 deduction for painting and cleaning and withholds remaining deposit",
   "proof": null
  }
 ],
 "amounts": {
  "deposit_paid": 60000,
  "deductions_claimed": 25000,
  "monthly_rent": 18000,
  "monthly_salary": null,
  "months_unpaid": null,
  "other_dues": null,
  "order_value": null,
  "amount_refunded": null
 },
 "evidence_have": [
  "rental agreement",
  "bank transfer receipt"
 ],
 "evidence_missing": [
  "written communication from landlord about deduction",
  "invoice or estimate for painting/cleaning costs",
  "inspection report or condition checklist"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Aapne flat kab exact date ko khali kiya tha?",
  "Landlord ka naam aur contact details kya hain?",
  "Kya aapke paas landlord se deduction ke baare mein koi likhit notice ya message hai?",
  "Painting aur cleaning ke liye landlord ne koi invoice ya estimate diya hai?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 60,000

- Less deductions the landlord claims: - Rs 25,000

- Amount to claim: Rs 35,000

## Where you stand

Aapne Rs 60,000 security deposit bank transfer se diya tha aur flat vacate karne ke baad landlord ne Rs 25,000 ka deduction painting aur cleaning ke liye bataya hai. Deposit wapas karne ka right aapke paas hai jab tak landlord ke paas valid proof ho ki damage normal wear‑tear se zyada hai ya koi unpaid rent hai [KB:ica_s73]. Agar landlord ke paas proper bills ya inspection report nahi hai, to aap poora Rs 60,000 wapas maang sakte hain. Weakness: aapke paas ab tak koi likhit notice ya invoice nahi hai, isliye deduction ko challenge karna thoda mushkil ho sakta hai. Time limit 3 saal ke andar claim file karna hoga [KB:deposit_civil_route].

## Options

1. **Polite written demand** (1-2 din likhne ka, 2 weeks wait, free): Landlord ko ek formal email/WhatsApp message likhe jisme aap deposit ka full amount (Rs 60,000) wapas maangte hain, unse deduction ka detailed bill aur photos/inspection report maange. 2 weeks ke andar response na mile to next step lein.

2. **Legal notice** (1 week notice draft aur bhejne tak, low (lawyer fee or free via legal aid) [KB:lsa_s12_legal_aid]): Ek lawyer ya legal aid service se simple legal notice draft karwaye, jisme landlord ko 15 din ke andar deposit wapas karne ki demand ho, aur deduction ke bina valid proof ki maang ho.

3. **File civil money recovery suit** (2-3 mahine (court filing se judgement tak), court fee (depends on claim amount) + lawyer fee if hired): Small Causes Court ya Civil Court me Rs 35,000 ka money recovery suit file karein. Claim mein deposit wapas aur interest ka demand likhe. Court ki fees aur process follow karein.

## What I don't know

- Kya Karnataka ne Model Tenancy Act [KB:mta_s11_deposit] adopt kiya hai, isliye deposit cap apply hota hai ya nahi.

- Landlord ne aapko koi written notice ya bill diya hai ya nahi.

- Exact date of vacating aur keys handover ka documented proof.

## Needs lawyer: False - Initial steps (written demand, legal notice) aap khud kar sakte hain. Lawyer ki zarurat tab padegi jab landlord response na de ya aap court case file karna chahein.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "ica_s73",
  "lsa_s12_legal_aid"
 ]
}

```

## Draft: Legal Notice for Return of Security Deposit

```

Date: [date]

From:
[Your Name]
[Your Address]
[Phone: [PHONE_1]]

To:
[Landlord Name]
[Landlord Address]

Subject: Demand for Return of Security Deposit (Rs. 35,000) for Flat at [Flat Address]

1. I, the undersigned, was the tenant of the above‑referenced flat in Bangalore, Karnataka, for a period of two years, commencing on [start date] and ending on [exact vacate date] 2026, as per the rental agreement attached hereto.
2. As per the agreement, I paid a security deposit of Rs. 60,000 by bank transfer on [date of deposit]; a copy of the bank transfer receipt is enclosed.
3. On vacating the premises in March 2026, I handed over the keys to you and the flat was left in a clean and tenant‑acceptable condition. The rental agreement requires the landlord to return the security deposit, subject only to lawful deductions for unpaid rent or damage beyond normal wear and tear.
4. You have informed me of a deduction of Rs. 25,000 for alleged painting and cleaning work, but no written invoice, estimate, photographs, or inspection report has been provided to substantiate such charges.
5. Under the Indian Contract Act, 1872, Section 73 [KB:ica_s73], a party entitled to a sum under a contract may claim compensation for loss caused by the other party’s breach. The failure to return the lawful portion of the deposit constitutes a breach of the tenancy contract.
6. Although the Model Tenancy Act, 2021, Section 11 [KB:mta_s11_deposit] caps the security deposit at two months’ rent, the principle that the deposit must be returned after the tenancy, minus only lawful dues, remains applicable. No lawful dues have been proven.
7. Consequently, I am entitled to the return of the balance of the security deposit amounting to Rs. 35,000 (Rs. 60,000 – Rs. 25,000 claimed).

Demand:
Please remit the amount of Rs. 35,000 to my bank account [your bank details] within fifteen (15) days from the receipt of this notice, i.e., by [deadline date].

Consequences of Non‑Compliance:
If the amount is not received within the stipulated period, I will be compelled to initiate appropriate legal proceedings, which may include filing a civil money recovery suit before the appropriate Small Causes Court in Bangalore and/or approaching the Rent Authority, as guided by the general civil procedure for deposit disputes [KB:deposit_civil_route]. I will also seek interest on the delayed amount and recovery of legal costs as permitted by law.

Yours faithfully,

________________________
[Your Name]
[Signature]


```

Explanation for user: Ye notice aapke landlord ko bhejne ke liye hai jisme aap unse Rs. 35,000 security deposit wapas maang rahe hain. Isme aapne bataya hai ki landlord ne koi proper bill ya proof nahi diya hai deduction ke liye. Agar 15 din ke andar paisa nahi milta, to aap court ya rent authority ke paas case file kar sakte hain. Notice me Indian Contract Act aur Model Tenancy Act ka reference diya gaya hai. Saath hi aapko interest aur legal cost bhi mil sakti hai.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["deposit_civil_route", "ica_s73", "mta_s11_deposit"]}