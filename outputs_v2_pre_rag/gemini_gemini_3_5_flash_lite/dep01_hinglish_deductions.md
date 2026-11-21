# dep01_hinglish_deductions  (gemini:gemini-3.5-flash-lite)

## Input

Maine Bangalore mein 2 saal flat rent pe liya tha, rent 18000 tha aur 60000 deposit diya tha bank transfer se. March 2026 mein flat khali kar diya, keys bhi de di. Ab landlord bol raha hai painting aur cleaning ke 25000 katenge aur baaki bhi abhi nahi de raha, 6 mahine ho gaye. Agreement mere paas hai.

## Reply shown to user

Hello! Aapne Bangalore mein 2 saal flat rent par rakha aur 60,000 deposit diya tha, jisme se landlord ne 25,000 paint aur cleaning ke naam par rok liya hai. Aapke paas rent agreement aur bank transfer receipt hai, jo ki achha proof hai. Normal wear and tear ke liye landlord deduction nahi kar sakta [KB:mta_s11_deposit], aur agreement ke mutabiq deposit na lautana breach of contract hai [KB:ica_s73]. Aapka pehla kadam yeh hona chahiye ki aap landlord ko WhatsApp ya written message bhejiye aur 25,000 ke kharche ke bills ya receipts maangte hue apna poora deposit wapas maangein. Agar woh jawab na dein toh ek formal demand notice bhejna padega [KB:deposit_civil_route]. Kya landlord ke sath pehle WhatsApp ya phone par deposit ko lekar koi baat hui hai?

## Red flags (rule engine)

## Case file

```json

{
 "problem_type": "deposit",
 "problem_subtype": "landlord withholding security deposit and making deductions for painting and cleaning",
 "user_language": "Hinglish",
 "state": "Karnataka",
 "city": "Bangalore",
 "summary": "The user rented a flat in Bangalore for 2 years with a monthly rent of 18000 and a security deposit of 60000 paid via bank transfer. They vacated the flat and handed over the keys in March 2026, but 6 months have passed and the landlord is refusing to return the full deposit, claiming a deduction of 25000 for painting and cleaning.",
 "user_goal": "Get back the full security deposit without unjustified deductions from the landlord",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "timeline": [
  {
   "date": "2026-03",
   "event": "Vacated the flat and handed over keys to the landlord",
   "proof": "keys handed over"
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
  "bank transfer receipt for deposit"
 ],
 "evidence_missing": [
  "photos or videos of flat condition when vacating",
  "written communication with landlord regarding the deposit"
 ],
 "risk_signals": [],
 "deadline_mentioned": {
  "date": null,
  "what": null
 },
 "follow_up_questions": [
  "Kya aapke paas deposit transfer ka bank statement hai?",
  "Kya landlord ke sath chat ya messages mein koi baat hui hai deposit ya painting charges ko lekar?",
  "Kya flat khali karte waqt ki koi photos ya videos hain aapke paas?"
 ]
}

```

## Calculation (code)

- Deposit paid: Rs 60,000

- Less deductions the landlord claims: - Rs 25,000

- Amount to claim: Rs 35,000

## Where you stand

Aapka 60,000 ka deposit landlord ke paas hai aur unhone 25,000 paint aur cleaning ke naam par kaat liya hai, jabki 6 mahine beet chuke hain. Aapke paas rent agreement aur deposit transfer ki bank receipt hai, jo ki strong proof hain. Lekin flat khali karte waqt ki photos ya videos aur landlord ke sath written chat nahi hona aapki thodi weak point hai. Normal wear and tear ke liye deductions nahi ki ja sakti [KB:mta_s11_deposit], aur agreement todne ya deposit na lautane par compensation manga ja sakta hai [KB:ica_s73].

## Options

1. **WhatsApp ya Written Message bhejein** (1-2 din, free): Landlord ko WhatsApp ya message karke clear puchiye ki 25,000 ka breakdown aur bills kya hain, aur apna bacha hua deposit wapas maangein.

2. **Formal Written Demand Notice** (1 hafta, low): Ek formal written demand notice bhejein jismein clear likha ho ki deduction unjustified hai aur poora paisa wapas kiya jaye.

3. **Civil Recovery / Legal Route** (Kuch mahine, court fee): Agar landlord paise na de, toh civil court ya rent authority mein money recovery ka rasta apna sakte hain.

## What I don't know

- Kya Karnataka government ne Model Tenancy Act [KB:mta_s11_deposit] ko poori tarah adopt kiya hai ya nahi.

- Kya flat mein koi sach mein aisi damage thi jo normal wear and tear se zyada ho.

## Needs lawyer: False - Abhi koi court case, police matter ya legal notice landlord ki taraf se nahi aaya hai. Aap pehle khud written message ya demand bhej kar koshish kar sakte hain.

## Guardrail report

```json

{
 "removed_count": 0,
 "items": [],
 "kb_cited": [
  "deposit_civil_route",
  "ica_s73",
  "mta_s11_deposit"
 ]
}

```

## Draft: Legal Demand Notice for Refund of Security Deposit

```

Date: [Date of sending notice]

From:
[Your Name]
[Your Address]
Phone: [PHONE_1]

To:
[Landlord's Name]
[Landlord's Address]

Subject: Demand for Refund of Security Deposit amounting to Rs. 35,000

Dear [Landlord's Name],

1. That I, the undersigned, was a tenant at your property located at [Property Address, Bangalore] under a rent agreement for a period of 2 years with a monthly rent of Rs. 18,000.

2. That at the commencement of the tenancy, I paid a security deposit of Rs. 60,000 via bank transfer.

3. That I vacated the said flat and handed over the keys to you in March 2026.

4. That a period of 6 months has passed since I vacated the premises, but you have failed to refund the full security deposit and have wrongfully claimed a deduction of Rs. 25,000 towards painting and cleaning, leaving an unjustified withheld amount.

5. That as per Section 73 of the Indian Contract Act, 1872 [KB:ica_s73], compensation is due for loss caused by the breach of terms regarding the return of the deposit. Furthermore, under the general principles of tenancy and the Model Tenancy Act, 2021 [KB:mta_s11_deposit], security deposits are expected to be returned upon handing back the premises minus lawful dues for actual damage beyond normal wear and tear, which has not been substantiated with valid bills or proof.

6. Therefore, through this notice, I demand that you pay the total outstanding amount of Rs. 35,000 within 15 days of receiving this notice.

7. If you fail to clear the said amount within the stipulated 15 days, I shall be constrained to initiate lawful next steps, including filing a civil money recovery suit or approaching the appropriate forum as per the civil recovery route [KB:deposit_civil_route], and you shall be liable for all additional costs and legal consequences.

Sincerely,

[Your Name]
[Your Signature]

```

Explanation for user: Yeh document ek formal legal demand notice hai jo aapke landlord ko bheja jayega. Isme aapne apne 60,000 rupaye ke deposit, 25,000 ki galat deduction, aur bache hue 35,000 rupaye wapas maangne ki baat ki hai. Isme Section 73 of the Indian Contract Act, 1872 [KB:ica_s73] ka hawala diya gaya hai ki agreement todne par nuksaan ka compensation banta hai. Landlord ko 15 din ka samay diya gaya hai payment karne ke liye. Agar woh nahi mante, toh aap aage civil court ya legal proceedings shuru kar sakte hain.

Draft guardrail: {"removed_count": 0, "items": [], "kb_cited": ["deposit_civil_route", "ica_s73", "mta_s11_deposit"]}