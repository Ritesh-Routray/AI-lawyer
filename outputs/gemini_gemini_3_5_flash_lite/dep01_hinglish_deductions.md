# dep01_hinglish_deductions  (gemini:gemini-3.5-flash-lite)

## Input

Maine Bangalore mein 2 saal flat rent pe liya tha, rent 18000 tha aur 60000 deposit diya tha bank transfer se. March 2026 mein flat khali kar diya, keys bhi de di. Ab landlord bol raha hai painting aur cleaning ke 25000 katenge aur baaki bhi abhi nahi de raha, 6 mahine ho gaye. Agreement mere paas hai.

## Reply shown to user

Namaste! Aapne Bangalore mein flat khali kar diya hai aur landlord ne 6 mahine se aapka Rs 60,000 ka security deposit rok rakha hai, jisme se Rs 25,000 painting aur cleaning ke naam par kaat liye hain. Landlord ko flat milne par deposit turant refund karna chahiye, aur deductions ke liye bills ya genuine nuksaan ka saboot dena zaroori hota hai [KB:src_mta_2021_11]. Aapke paas rent agreement aur bank transfer ka proof hai, jo ki acchi baat hai. Sabse pehle aapko landlord ko ek written message ya reminder bhejna chahiye ki wo deductions ke bills share karein ya pura paisa wapas karein [KB:ica_s73]. Agar wo nahi maante, toh ek legal notice bheja ja sakta hai [KB:deposit_civil_route]. Kya aapne vacating ke time flat ki condition ya cleaning ke liye landlord se WhatsApp par koi baat ki thi?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "landlord withholding security deposit and making unjustified deductions",
 "user_language": "Hinglish",
 "state": "Karnataka",
 "city": "Bangalore",
 "summary": "The user rented a flat in Bangalore for two years with a monthly rent of 18000 and a security deposit of 60000 paid via bank transfer. They vacated the flat and handed over the keys in March 2026, but the landlord is now deducting 25000 for painting and cleaning, has delayed the refund for 6 months, and is withholding the remaining amount.",
 "user_goal": "Get back the full security deposit from the landlord without unfair deductions",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-03",
   "event": "Vacated the flat and handed over the keys to the landlord",
   "proof": "keys handover / agreement"
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
  "rent agreement",
  "bank transfer proof of deposit"
 ],
 "evidence_missing": [
  "written communication or chat logs with the landlord regarding deposit refund",
  "photos or videos of flat condition when vacating"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Kya aapke aur landlord ke beech WhatsApp ya text pe deposit refund ko lekar koi baat hui hai?",
  "Kya aapke paas bank statement hai jisse deposit transfer ka proof dikhe?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 60,000

- Less deductions the landlord claims: - Rs 25,000

- Amount to claim: Rs 35,000

## Retrieved official text (hybrid (BM25 + dense) + anchor queries)

- Model Tenancy Act, 2021 Section 11  p.11

- Model Tenancy Act, 2021 Section 10  p.11

- Model Tenancy Act, 2021 Section 15  p.13

- Model Tenancy Act, 2021 Section 14  p.12

- Model Tenancy Act, 2021 Section 20  p.15

- Model Tenancy Act, 2021 Section 23  p.18

- Model Tenancy Act, 2021 Section 24  p.18

## Where you stand

Aapka security deposit Rs 60,000 tha aur landlord ne March 2026 mein flat khali karne ke baad bhi painting aur cleaning ke naam par Rs 25,000 kaat kar baaki amount rok liya hai, jabki 6 mahine se zyada ho chuke hain. Landlord ko deposit wapas karna hota hai, aur deductions sirf tabhi valid hote hain jab koi genuine nuksaan ya pending bills hon [KB:src_mta_2021_11]. Aapke paas rent agreement aur bank transfer ka proof hai, lekin written communication aur flat ki exit photos missing hain. Aap civil recovery route ya legal notice ka sahara le sakte hain [KB:deposit_civil_route].

## Options

1. **Written Demand Send Karein** (1-2 din, free): Landlord ko WhatsApp ya email par ek formal message bhejiye ki wo painting aur cleaning ke 25,000 Rs ke bills/photos share karein, warna pura Rs 60,000 refund karein.

2. **Legal Notice Bhejiye** (1 hafta, low): Agar landlord respond na kare, toh ek advocate ke zariye formal legal notice bhejiye jisme bacha hua amount maanga jaye.

3. **Civil Court / Small Causes Court** (Kuch mahine, court fee): Agar notice ke baad bhi paisa na mile, toh civil court ya Small Causes court mein money recovery suit file kar sakte hain.

## What I don't know

- Kya Karnataka sarkar ne Model Tenancy Act [KB:mta_s11_deposit] ko poori tarah adopt kiya hai ya nahi.

- Kya flat mein sach mein normal wear and tear se zyada nuksaan hua tha jiske liye deduction banta ho.

## Needs lawyer: False - Abhi tak koi court case ya police matter nahi hai; aap khud ek written demand bhej sakte hain. Lawyer ki zaroorat tab padegi jab legal notice bhejna ho ya court mein case karna pade.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "ica_s73",
  "src_mta_2021_11"
 ],
 "support_check": "not auto-checked (non-English reply; cross-encoder is English-only)"
}

```

## Draft: Legal Notice for Refund of Security Deposit

```

Date: [date you send this notice]

From:
[Your Name]
[Your Address]
Phone: [PHONE_1]

To:
[Landlord's Name]
[Landlord's Address]

Subject: Demand for Refund of Security Deposit amounting to Rs 35,000/- with respect to tenancy at [property address/flat details]

Dear [Landlord's Name],

1. That the tenant rented the residential flat situated at [property address] for a period of two years with a monthly rent of Rs 18,000/-, and paid a security deposit of Rs 60,000/- via bank transfer as per the rent agreement.
2. That the tenant successfully vacated the flat and handed over the keys to the landlord in March 2026.
3. That despite the vacation of the premises and peaceful handing over of possession, the landlord has unreasonably delayed the refund of the security deposit for a period of 6 months and has wrongfully deducted Rs 25,000/- towards painting and cleaning without providing any valid bills, receipts, or proof of damages beyond normal wear and tear.
4. That the landlord is legally bound to refund the security deposit upon taking over vacant possession, minus any lawful dues, in accordance with Section 11 of the Model Tenancy Act, 2021 [KB:mta_s11_deposit] and Section 73 of the Indian Contract Act, 1872 [KB:ica_s73] concerning compensation for breach of contract.

Therefore, the landlord is called upon to pay the calculated total amount of Rs 35,000/- to the tenant within 15 days of receiving this notice.

If the said amount is not paid within the stipulated period of 15 days, the tenant will be constrained to initiate lawful next steps, including filing a civil money recovery suit or initiating proceedings before the appropriate forum as provided under Civil recovery route [KB:deposit_civil_route].

Sincerely,

[Your Name]
[Your Signature]

```

Explanation for user: Yeh legal notice aapke landlord ko bheja jayega taaki woh aapka bacha hua security deposit (Rs 35,000) jaldi se wapas karein. Isme saaf likha hai ki aapne March 2026 mein flat khali karke keys de di thin, par landlord ne bina kisi sahi bill ya proof ke 25,000 kaat liye hain aur 6 mahine se paise roke hue hain. Is notice mein 15 din ka time diya gaya hai poore paise dene ke liye. Agar landlord 15 din ke andar payment nahi karta, toh aapke paas civil court ya appropriate forum mein legal action lene ka adhikaar hoga.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["deposit_civil_route", "ica_s73", "mta_s11_deposit"]}