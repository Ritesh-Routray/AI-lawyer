# dep01_hinglish_deductions  (groq:qwen/qwen3.8-27b)

## Input

Maine Bangalore mein 2 saal flat rent pe liya tha, rent 18000 tha aur 60000 deposit diya tha bank transfer se. March 2026 mein flat khali kar diya, keys bhi de di. Ab landlord bol raha hai painting aur cleaning ke 25000 katenge aur baaki bhi abhi nahi de raha, 6 mahine ho gaye. Agreement mere paas hai.

## Reply shown to user

Aapka case strong hai kyunki aapke paas rent agreement aur bank record hai. Landlord ne 6 mahine se paise nahi diye, jo ki galat hai. Pehle step: Landlord ko WhatsApp par clear message bhejein ki aapko Rs 35,000 (ya Rs 60,000 agar deduction proof nahi hai) wapas chahiye. Unse 25,000 ke deduction ke liye bills ya photos maangein. Agar wo reply nahi karta, toh agla step legal notice hoga. Kya landlord ne abhi tak koi written proof diya hai 25,000 ke deduction ke liye?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit not returned after deductions",
 "user_language": "Hinglish",
 "state": "Karnataka",
 "city": "Bangalore",
 "summary": "The user rented a flat in Bangalore for two years with a monthly rent of 18000 and a security deposit of 60000. After vacating the property in March 2026, the landlord has withheld the deposit, claiming 25000 for painting and cleaning, and has not returned the balance for six months.",
 "user_goal": "To recover the remaining security deposit from the landlord.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2024-03",
   "event": "Started renting the flat (inferred from '2 saal' before March 2026)",
   "proof": null
  },
  {
   "date": "2026-03",
   "event": "Vacated the flat and handed over keys",
   "proof": null
  },
  {
   "date": "2026-09",
   "event": "Six months have passed since vacating; landlord still withholding money",
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
  "amount_refunded": 0
 },
 "evidence_have": [
  "Rent agreement",
  "Bank transfer record for deposit"
 ],
 "evidence_missing": [
  "Written communication from landlord regarding the 25000 deduction (message/letter)",
  "Move-out inspection report or photos of the flat's condition",
  "Proof of key handover (message/receipt)"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Kya landlord ne 25000 ke deduction ka koi written proof ya bill diya hai?",
  "Flat khali karne ke waqt koi joint inspection hua tha ya photos li gayi thin?",
  "Abhi tak landlord se baat kaise ki hai (phone, WhatsApp, ya in person)? Koi reply aaya hai?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 60,000

- Less deductions the landlord claims: - Rs 25,000

- Amount to claim: Rs 35,000

## Where you stand

Aapke paas strong case hai kyunki aapke paas rent agreement aur deposit ka bank transfer record hai. Landlord ne 6 mahine se paise nahi diye, jo ki galat hai. Aapka deposit (Rs 60,000) 2 mahine ke rent (Rs 36,000) se zyada hai, lekin Model Tenancy Act sirf un states mein lagta hai jinhone ise adopt kiya hai, isliye aapka rent agreement aur Karnataka ki local laws yahan zyada matter karte hain [KB:mta_s11_deposit]. Landlord ka 25,000 ka deduction sirf tab valid hai agar unke paas damage ke bills ya photos hain, warna aap poora deposit claim kar sakte hain. Aapke paas 3 saal ka time hai civil court mein case file karne ke liye, lekin pehle soft steps try karna chahiye [KB:deposit_civil_route].

## Options

1. **Written Demand (WhatsApp/Email)** (1-2 din, Free): Landlord ko ek clear message bhejein ki aapko Rs 35,000 (ya Rs 60,000 agar deduction proof nahi hai) wapas chahiye. Unse 25,000 ke deduction ke liye bills ya photos maangein. Deadline dein (e.g., 7 din).

2. **Legal Notice** (1-2 hafte, Low (lawyer fee)): Agar landlord reply nahi karta, toh ek lawyer se legal notice bhejwayein. Isme aap apna case clearly likh sakte hain aur interest bhi claim kar sakte hain. Yeh step court case se pehle ka last warning hai.

3. **Civil Money Recovery Suit** (3-6 mahine ya zyada, Court fees + lawyer fee): Agar notice ke baad bhi paise nahi milte, toh aap apne area ke civil court mein money recovery suit file kar sakte hain. Yeh formal legal process hai jisme court se order aayega.

## What I don't know

- Kya Karnataka ne Model Tenancy Act [KB:mta_s11_deposit] adopt kiya hai? (Isse deposit cap ka rule change ho sakta hai)

- Rent agreement mein kya specific terms hain deposit return ke baare mein?

- Kya landlord ne koi written proof diya hai 25,000 ke deduction ke liye?

## Needs lawyer: False - Abhi ke liye lawyer zaroori nahi hai kyunki aap pehle written demand aur legal notice bhej sakte hain. Agar landlord notice ke baad bhi paise nahi deta, toh tab lawyer ki zaroorat hogi civil case file karne ke liye.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "mta_s11_deposit"
 ]
}

```

## Draft: Legal Notice for Recovery of Security Deposit

```

Date: [Current Date]

From:
[Your Name]
[Your Address]
[Your Phone Number]

To:
[Landlord's Name]
[Landlord's Address]

Subject: Legal Notice for Recovery of Security Deposit of Rs 35,000

Dear Sir/Madam,

1. I, [Your Name], am the tenant of the residential flat located at [Flat Address], Bangalore, Karnataka, which I rented from you, the landlord, for a period of two years starting from [Start Date of Tenancy].

2. As per our rent agreement, I paid a security deposit of Rs 60,000, which was received by you via bank transfer on [Date of Deposit Payment].

3. I vacated the said premises and handed over the keys to you in March 2026. Despite the fact that six months have passed since the handover, you have failed to return the balance of the security deposit.

4. You have withheld the deposit, claiming a deduction of Rs 25,000 towards painting and cleaning. However, you have not provided any written communication, bills, or photographic evidence to substantiate these deductions. Under the terms of our agreement and general principles of tenancy, deductions are only valid for unpaid rent or damage beyond normal wear and tear, which must be proven.

5. Therefore, the balance amount of the security deposit due to me is calculated as follows:
   - Total Security Deposit Paid: Rs 60,000
   - Less: Claimed Deductions (unsubstantiated): - Rs 25,000
   - Total Amount Due to Me: Rs 35,000

6. Your failure to return the security deposit constitutes a breach of the tenancy agreement. Under Section 73 of the Indian Contract Act, 1872 [KB:ica_s73], I am entitled to claim compensation for the loss that naturally arose from this breach of contract.

7. I hereby call upon you to pay the sum of Rs 35,000 within 15 days of the receipt of this notice. 

8. Please note that if you fail to make the payment within the stipulated time, I shall be constrained to initiate legal proceedings against you for the recovery of the said amount, along with interest and costs, in the appropriate civil court or Rent Authority in Bangalore. 

9. This notice is issued without prejudice to my other rights and remedies available under the law.

Yours faithfully,

[Your Name]
[Your Signature]

```

Explanation for user: Yeh ek formal legal notice hai jo aapko apne landlord ko bhejna hai. Isme aapne bataya hai ki aapne 60,000 ka deposit diya tha aur abhi tak 35,000 wapas nahi mil raha. Aapne 15 din ka time diya hai ki landlord paise wapas kare, warna aap court mein case file kar sakte hain. Is notice ko bhejne ke baad, agar landlord paise nahi deta, toh aapko civil court ya Rent Authority mein jaana hoga. Is notice ko bhejne se pehle, aapko apne paas rent agreement aur bank transfer proof ready rakhna chahiye.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["ica_s73"]}