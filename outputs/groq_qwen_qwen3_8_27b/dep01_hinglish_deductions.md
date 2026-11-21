# dep01_hinglish_deductions  (groq:qwen/qwen3.8-27b)

## Input

Maine Bangalore mein 2 saal flat rent pe liya tha, rent 18000 tha aur 60000 deposit diya tha bank transfer se. March 2026 mein flat khali kar diya, keys bhi de di. Ab landlord bol raha hai painting aur cleaning ke 25000 katenge aur baaki bhi abhi nahi de raha, 6 mahine ho gaye. Agreement mere paas hai.

## Reply shown to user

Aapka case strong hai kyunki aapke paas rent agreement aur bank transfer proof hai. Landlord abhi tak 6 mahine se paisa nahi de raha, jo galat hai. Pehle unse WhatsApp/Email par written demand bhejein aur painting/cleaning ke bills maangein. Agar wo nahi dete, toh legal notice bhejein. Court case tak jaane se pehle yeh steps zaroori hain. Kya aapne abhi tak landlord se koi written message bheja hai deposit wapas lene ke liye?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "security deposit withheld with disputed deductions",
 "user_language": "Hinglish",
 "state": "Karnataka",
 "city": "Bangalore",
 "summary": "The user rented a flat in Bangalore for two years with a monthly rent of 18,000 INR and a security deposit of 60,000 INR. After vacating the property in March 2026, the landlord is withholding the deposit, claiming 25,000 INR for painting and cleaning, and has not returned the balance for six months.",
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
  "Rent agreement",
  "Bank transfer record for deposit"
 ],
 "evidence_missing": [
  "Written communication from landlord regarding deductions",
  "Inventory or condition report at the time of vacating",
  "Proof of key handover (e.g., message or receipt)"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Kya landlord ne painting/cleaning ke 25000 ke liye koi written estimate ya bill diya hai?",
  "Flat khali karne ke time koi inventory list ya condition report sign kiya tha?",
  "Abhi tak landlord se deposit wapas lene ke liye koi written notice ya message bheja hai?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 60,000

- Less deductions the landlord claims: - Rs 25,000

- Amount to claim: Rs 35,000

## Where you stand

Aapke paas strong case hai kyunki aapne deposit bank transfer se diya hai aur rent agreement bhi hai. Landlord abhi tak 6 mahine se paisa nahi de raha, jo galat hai. Aapka deposit (60,000) rent ke 2 mahine (36,000) se zyada hai, lekin Karnataka mein Model Tenancy Act [KB:mta_s11_deposit] adopt nahi hua hai, isliye aapka rent agreement aur state laws apply honge. Aapko abhi tak landlord se koi written proof nahi mila ki unhone painting/cleaning ke liye kitna kharcha kiya. Isliye, pehle unse written proof maangna zaroori hai.

## Options

1. **Written Demand via WhatsApp/Email** (1-2 din, Free): Landlord ko ek clear message bhejein ki aap 35,000 (ya 60,000 agar unke deductions valid nahi hain) wapas chahte hain. Unse painting/cleaning ke bills ya photos maangein. Deadline dein (e.g., 7 din).

2. **Legal Notice** (1-2 hafte, Low (lawyer's fee for notice)): Agar landlord reply nahi karta, toh ek lawyer ke through legal notice bhejein. Isme aap apna case clearly likhenge aur deadline denge. Yeh step court case se pehle ka standard step hai.

3. **Civil Money Recovery Suit** (3-6 mahine ya zyada, Court fees + lawyer fees): Agar notice ke baad bhi paisa nahi milta, toh aap civil court mein money recovery suit file kar sakte hain. Yeh 3 saal ke andar hona chahiye [KB:deposit_civil_route].

## What I don't know

- Kya aapke rent agreement mein deposit return ke specific terms hain?

- Kya landlord ne koi written estimate diya hai deductions ke liye?

- Kya aapke paas key handover ka koi proof hai?

## Needs lawyer: False - Abhi ke liye aap khud written demand aur legal notice ke liye lawyer se baat kar sakte hain. Court case tak jaane se pehle lawyer zaroori hai, lekin pehle steps aap khud kar sakte hain.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route"
 ]
}

```

## Draft: Legal Notice for Recovery of Security Deposit

```

Date: [Date]

From:
[Your Name]
[Your Address]
[Your Phone Number]

To:
[Landlord's Name]
[Landlord's Address]

Subject: Legal Notice for Recovery of Security Deposit of Rs 35,000

Dear [Landlord's Name],

1. I, [Your Name], am the tenant of the residential flat located at [Flat Address], Bangalore, Karnataka, which I rented from you, the landlord, for a period of two years. The monthly rent for the said property was Rs 18,000, and I paid a security deposit of Rs 60,000 at the commencement of the tenancy, as evidenced by the rent agreement and bank transfer records.

2. I vacated the said flat and handed over the keys to you in March 2026, thereby fulfilling all my obligations as a tenant under the rent agreement.

3. Despite the termination of the tenancy and the handover of the property, you have failed to return my security deposit. You have claimed a deduction of Rs 25,000 towards painting and cleaning, leaving a balance of Rs 35,000. However, you have not provided any written communication, bills, or estimates to substantiate these claimed deductions, nor have you returned the balance amount for the past six months.

4. Under Section 73 of the Indian Contract Act, 1872 [KB:ica_s73], I am entitled to claim compensation for the loss that naturally arose from your breach of the agreement to return the deposit. Furthermore, as per the general civil procedure for deposit disputes [KB:deposit_civil_route], a written demand is a necessary step before initiating legal proceedings.

5. In light of the above, I hereby demand that you pay the sum of Rs 35,000 (Rupees Thirty-Five Thousand only) within 15 days of the receipt of this notice. 

6. Please note that if the said amount is not paid within the stipulated period, I shall be constrained to initiate appropriate legal proceedings for the recovery of the said amount, along with any interest and costs that may be awarded by the competent court.

7. This notice is issued without prejudice to my other rights and remedies available under the law.

Yours faithfully,

[Your Name]
[Your Signature]

```

Explanation for user: Yeh ek legal notice hai jo aapko apne landlord ko bhejna hai. Isme aapne bataya hai ki aapne 60,000 ka deposit diya tha aur ab aap 35,000 wapas chahte ho kyunki landlord ne 25,000 ka deduction claim kiya hai bina kisi proof ke. Notice mein aapko 15 din ka time diya hai ki wo paisa wapas kare. Agar wo 15 din mein paisa nahi dete, toh aap court mein case kar sakte ho. Is notice ko bhejne se pehle, aapko apne naam, address aur landlord ki details fill karni hongi. Notice bhejne ke baad, aapko 15 din ka wait karna hoga.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["deposit_civil_route", "ica_s73"]}