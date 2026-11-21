# dep01_hinglish_deductions  (gemini:gemini-3.5-flash)

## Input

Maine Bangalore mein 2 saal flat rent pe liya tha, rent 18000 tha aur 60000 deposit diya tha bank transfer se. March 2026 mein flat khali kar diya, keys bhi de di. Ab landlord bol raha hai painting aur cleaning ke 25000 katenge aur baaki bhi abhi nahi de raha, 6 mahine ho gaye. Agreement mere paas hai.

## Reply shown to user

Main koi lawyer nahi hoon, par main aapki madad kar sakta hoon. Aapka case strong hai kyunki aapke paas deposit payment ka bank record aur rent agreement dono hain [KB:deposit_civil_route].

Landlord bina valid repair bills ya bina damage proof ke 25,000 rupees nahi kaat sakta, jab tak ki normal wear-and-tear ke alawa koi bada nuksan na hua ho [KB:ica_s73].

Pahla step yeh hai ki aap landlord ko ek formal message/email bhejein, jisme unse painting aur cleaning ke bills maangein aur apna poora security deposit refund karne ki demand karein [KB:deposit_civil_route]. Agar woh refuse karte hain, toh aap unhe legal notice bhej sakte hain.

Kya aapke rent agreement mein flat khali karte waqt painting charges dene ka koi rule likha hua hai?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "landlord withholding security deposit with excessive deductions",
 "user_language": "Hinglish",
 "state": "Karnataka",
 "city": "Bangalore",
 "summary": "The user rented a flat in Bangalore for 2 years with a monthly rent of 18000 rupees and paid a security deposit of 60000 rupees via bank transfer. They vacated the flat and handed over the keys in March 2026. The landlord is refusing to return the deposit, demanding an unreasonable deduction of 25000 rupees for painting and cleaning.",
 "user_goal": "Get full refund of the security deposit without unfair deductions.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-03",
   "event": "Vacated the flat and handed over the keys",
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
  "rent agreement",
  "bank transfer record of security deposit"
 ],
 "evidence_missing": [
  "bank statement showing deposit payment",
  "written communication/chat logs with landlord regarding deposit return and deductions",
  "photos/videos of flat condition at the time of vacating"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Kya aapke paas landlord ke saath WhatsApp messages ya emails hain jisme unhone 25,000 deduction ki baat ki hai?",
  "Kya flat khali karte waqt ki photos ya videos hain aapke paas?",
  "Kya rent agreement mein painting/cleaning charges ke baare mein koi rule likha tha?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 60,000

- Less deductions the landlord claims: - Rs 25,000

- Amount to claim: Rs 35,000

## Where you stand

Aapka case strong hai kyunki aapke paas rent agreement aur bank transfer record hai 60,000 rupees ka [KB:deposit_civil_route]. Landlord painting ya cleaning ke naam par 25,000 rupees tabhi kat sakta hai agar agreement mein aisi koi shart ho ya damage normal wear and tear se zyada ho [KB:ica_s73]. Agar landlord koi original bill ya bill ka proof nahi deta, toh yeh deduction unfair hai. Model Tenancy Act residential deposit ko 2 mahine ke rent tak limit karta hai, par yeh state laws par depend karta hai [KB:mta_s11_deposit].

## Options

1. **Formal Written Notice / Message** (1-2 days to send, Free): Landlord ko ek formal WhatsApp message ya email bhejein. Payment ka proof attach karein aur 25,000 deduction ke bills/receipts maangein. 7-10 din mein full 60,000 rupees refund karne ki demand karein.

2. **Legal Notice via Advocate** (1-2 weeks, Low to moderate legal fees): Agar landlord message ka jawab na de ya refuse kare, toh ek lawyer ke zariye formal Legal Notice bhijwayein.

3. **Civil Court / Recovery Dispute** (Several months, Court fee and legal fee): Legal notice ke baad bhi paisa na mile toh money recovery suit ya local civil court/authority mein case file karein [KB:deposit_civil_route]. Agar eligible hain toh DLSA helpline 15100 par free legal assistance le sakte hain [KB:lsa_s12_legal_aid].

## What I don't know

- Karnataka local rent rules ke under exact court/authority procedurally kaise apply hoti hai.

- Kya aapke rent agreement mein painting clause explicitly mention hai ya nahi.

## Needs lawyer: False - Abhi initial legal demand message aur formal steps aap khud le sakte hain. Case file karne ya legal notice bhejne ke stage par lawyer ki zarurat padegi.

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

## Draft: Legal Notice for Refund of Security Deposit

```

Date: [Date of sending notice]

From:
[Your Name]
[Your Address]
Bangalore, Karnataka

To:
[Landlord Name]
[Landlord Address]
Bangalore, Karnataka

Subject: DEMAND NOTICE FOR REFUND OF UNPAID SECURITY DEPOSIT AMOUNTING TO RS. 35,000/-

Sir/Madam,

Under instructions and authority from myself, I hereby serve you with this formal Legal Notice:

1. That I rented your residential flat in Bangalore, Karnataka, for a tenure of 2 years at a monthly rent of Rs. 18,000/-.
2. That at the time of entering the tenancy, I paid a total security deposit amount of Rs. 60,000/- via bank transfer.
3. That I duly vacated the flat and handed over the keys to you in March 2026.
4. That despite vacating the premises, you have failed to return the full security deposit and are making an unreasonable deduction of Rs. 25,000/- towards painting and cleaning without lawful justification or proof of damage beyond normal wear and tear.
5. That under Section 73 of the Indian Contract Act, 1872 [KB:ica_s73], a party suffering from a breach of contract is entitled to receive compensation for any loss or damage caused thereby. Retaining the deposit without justification constitutes a breach of the tenancy agreement terms.

I hereby call upon you to pay the sum of Rs. 35,000/- (Rupees Thirty-Five Thousand Only) to my bank account within 15 days of the receipt of this notice.

Take note that if you fail to repay the said amount within the stipulated period of 15 days, I shall be constrained to initiate appropriate legal proceedings against you, including filing a civil suit for recovery of money [KB:deposit_civil_route], entirely at your risk as to costs and consequences.

Yours faithfully,


_______________________
[Your Name]
[Your Phone Number]

```

Explanation for user: Yeh ek formal demand notice hai jo aapke landlord ko aapka security deposit wapas karne ke liye bheja ja raha hai. Isme likha hai ki aapne March 2026 mein flat khali kar diya tha aur 60,000 rupees ka deposit diya tha. Isme humne 25,000 rupees ki unreasonble deduction ko challenge karke remaining 35,000 rupees 15 dino ke andar refund karne ki maang ki hai. Agar landlord 15 dino me paise nahi deta, toh aap unke khilaaf court mein civil recovery suit file kar sakte hain.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["deposit_civil_route", "ica_s73"]}