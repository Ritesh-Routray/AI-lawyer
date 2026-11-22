# ⚖️ Nyay Saathi: an AI legal-help assistant for everyday problems in India

People can talk to it by text or voice, in Hindi, English, Hinglish, Tamil, Bengali or other languages, about three common money problems:

| Covers in depth | Explains | Detects and hands off to a lawyer / legal aid |
|---|---|---|
| Security deposit not returned · Consumer refunds (e-commerce, services, UPI/bank) · Unpaid salary / final settlement | Legal notices you received | Criminal / police matters, domestic violence, court summons, property ownership, time-barred claims, forging documents (refused) |

## What it does
1. **Builds the case.** It turns a messy story into a structured case file: parties, a dated timeline, amounts, proof you have and proof you're missing. It then asks 2–4 follow-up questions in your language.
2. **Evidence locker.** Upload WhatsApp screenshots, UPI receipts or a rent agreement, or an exported WhatsApp chat (.txt). It reads the dates and amounts and adds them to your timeline, with each fact linked to its source file.
3. **Claim calculator.** The amount to claim is computed **in code**, not by the AI.
4. **Where you stand and your options**, from a polite message up to a formal complaint, in plain language. Every legal point comes with a **citation receipt**: the law, a link to the source, whether it's been verified, and the date it was checked.
5. **Documents.** It drafts a polite WhatsApp message, a legal notice, a consumer complaint or a wage-claim application. You can download them as .docx, with a plain-language explanation in your language.
6. **Lawyer hand-off.** A one-page case brief for a legal-aid lawyer, plus **calendar reminders** (.ics) for follow-ups and time limits.
7. **Practise.** The AI plays your landlord, employer or customer-care agent, then scores how you argued.
8. **Model leaderboard.** The same 18 test cases run on any number of models, compared on accuracy, how many invented legal references were caught, latency and cost.

### It stays with you after the first answer ([ai_lawyer/companion.py](ai_lawyer/companion.py), all code, no AI)
9. **Deadline countdown.** Time limits worked out from your own dates, each tied to the law it comes from: 2 years to file a consumer complaint (CPA s.69), 3 years for a wage claim (Code on Wages s.45(6)), and "your employer had to pay your final wages within 2 working days of your resignation" (s.17(2)), shown as days late. Logged steps add follow-up dates (15 days after a legal notice, 1 month for a grievance officer).
10. **Claim tracker.** Log what happened ("sent a message", "they paid part", "refused"). A rule ladder works out the next step and when: wait, send a legal notice, or file a complaint. A **Draft it for me** button writes the right document. Part payments reduce the amount still owed.
11. **Is it worth it?** A per-route table (cost, time, lawyer needed) and an honest verdict. Example: for a small deposit, a court case may cost more time than it recovers. Example: the wage authority can award compensation of up to 10 times the claim (s.45(2), quoted from the official text).
12. **Where to get help.** Verified national channels (NALSA 15100, Consumer Helpline 1915, e-Jagriti, RBI complaint portal), plus map searches for your DLSA, Labour Commissioner office or civil court, using your city.
13. **Got a notice?** Upload a photo or PDF of a notice you received, or paste its text. It explains the notice in your language, counts down to the reply deadline, and escalates notices from lawyers and courts by rule. It also **checks every law the notice cites** against the official texts: it flags IPC/CrPC citations (replaced in 2024) and section numbers that don't exist, and links to the real section. One click drafts a reply, or turns the notice into your case.
14. **Listen.** Replies are read aloud in your language using the browser's built-in voices. It's free, and no audio is sent anywhere.
15. **How I got this answer.** A step-by-step trace for each answer: what was masked, which rules fired, what the calculator found, which sections were searched, and what the fact-checker removed, struck through.
16. **Save, resume, share.** Save the whole case as a private `.json` and load it later to carry on. Download a **shareable case page** (.html, printable to PDF) for family or a legal-aid lawyer; personal details stay masked in it.

## How it avoids inventing laws
1. **A curated knowledge base** ([kb/laws.yaml](kb/laws.yaml)). These are the only laws it may cite. Each entry has a source URL, a status (verified / secondary / unverified) and the date it was checked.
2. **Cite-by-tag.** The model must tag every legal claim with `[KB:id]`, and it only ever sees the entries relevant to the problem type.
3. **A post-generation validator** ([ai_lawyer/guardrails.py](ai_lawyer/guardrails.py)), written in code. Any section number, Act name, IPC/CrPC mention or case-law citation that isn't backed by a supplied KB entry is **removed** and replaced with a visible marker. Each removal is counted, and the count is a metric.
4. **No case law, ever.** Precedent is where models invent the most.
5. **Known traps are in the prompt.** IPC/CrPC were replaced by BNS/BNSS on 1 July 2024. The Payment of Wages Act was replaced by the Code on Wages from 21 November 2025. The RBI 2021 Ombudsman scheme was replaced by RB-IOS 2026.
6. **Escalation is decided by rules in code** ([ai_lawyer/escalation.py](ai_lawyer/escalation.py)), and those rules override the model.
7. **Personal data is masked** ([ai_lawyer/redact.py](ai_lawyer/redact.py)). Phone, Aadhaar, PAN, bank account, IFSC, UPI and email are hidden before any API call, and put back only in your local documents.

## Law library (RAG over official texts)
Besides the curated notes, the assistant searches the **full official text** of the Acts. Before answering, it retrieves the sections relevant to the case. The model may cite a section **only if it was shown that section's text**, and the citation receipt links to the exact page of the official PDF.

| Source | Sections indexed | Used for |
|---|---|---|
| Bharatiya Nyaya Sanhita, 2023 (BNS) | 357 | notices and out-of-scope triage only, never to advise on money claims |
| Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS) | 531 | notices and out-of-scope triage |
| Constitution of India (Parts I–XXII and Schedules) | 434 Articles (incl. inserted ones like 21A, 39A) + 12 Schedules | all problem types (e.g. Art. 39A, free legal aid) |
| Consumer Protection Act, 2019 | 107 | consumer cases and notices |
| Code on Wages, 2019 | 69 | salary cases and notices |
| Model Tenancy Act, 2021 | 47 | deposit cases and notices (a model law: binds only where a state adopted it) |

- **Sources** ([corpus/sources.yaml](corpus/sources.yaml)). These are official mirrors: MEA for the Constitution, Delhi UDD for the Model Tenancy Act, and PRS Legislative Research copies of the Gazette text. India Code timed out from our network. [corpus/raw/manifest.json](corpus/raw/manifest.json) records each file's URL, SHA-256 and download date.
- **Chunking** ([ai_lawyer/rag.py](ai_lawyer/rag.py)). One chunk per Section or Article, keeping the page number and margin heading. A new section starts only when its number continues the running sequence, which skips the table of contents and footnotes. Inserted provisions like `39A` are handled. In total there are 2,060 chunks.
- **Search.** BM25 (pure Python) and dense embeddings (`bge-small-en-v1.5`, run locally) are combined by reciprocal-rank fusion. A cross-encoder (`ms-marco-MiniLM-L-6`) then reranks the results, and they are filtered to the Acts relevant to the problem type. Multi-query retrieval adds fixed questions for each problem type ("where to file", "time limit"), so the key sections show up even when the story's wording doesn't mention them. Without sentence-transformers it falls back to BM25 only.
- **Validation.** Retrieved sections become citable entries, so the same validator applies. It also rejects a section number cited with the wrong Act (e.g. "Section 69 of the Code on Wages" when only s.69 of the Consumer Protection Act was retrieved).
- **Retrieval benchmark** (`python scripts/eval_retrieval.py`, 20 queries with the section a lawyer would point to):

| Config | hit@1 | hit@3 | hit@5 | MRR |
|---|---|---|---|---|
| BM25 only | 30% | 60% | 80% | 0.47 |
| Hybrid (BM25 + dense) | 55% | 85% | 90% | 0.70 |
| Hybrid + reranker (default) | 50% | 75% | 95% | 0.66 |

To rebuild: `python scripts/fetch_corpus.py && python scripts/build_index.py`. To add an Act, add it to `sources.yaml` and run both commands again.

## Run it
```bash
pip install -r requirements.txt
cp .env.example .env        # add a free GROQ_API_KEY or GEMINI_API_KEY, then load it into your shell
streamlit run app.py
```

## Swap the model (one string)
```bash
MODEL=groq:openai/gpt-oss-120b    # free
MODEL=gemini:gemini-3.5-flash-lite         # free tier
MODEL=openai:gpt-4.1-mini
MODEL=anthropic:claude-sonnet-5-5
MODEL=ollama:llama3.1                 # local
MODEL=custom:<name>  CUSTOM_BASE_URL=... CUSTOM_API_KEY=...   # any OpenAI-compatible API
```
You can also change the model in the app's sidebar. All prompts live in [prompts/](prompts/) as plain markdown.
For reasoning models (Gemini 3.x, gpt-oss), `REASONING_EFFORT` defaults to `low`. Extraction and drafting don't need deep thinking, and this cuts latency several times over. Screenshots are read with `EVIDENCE_MODEL`, which defaults to Gemini when the chat model is a Groq text model. A sample exported WhatsApp chat for the evidence locker is in [samples/](samples/).

## Evaluate
```bash
pytest -q                                                    # 18 unit tests: guardrails, rules, redaction, deadlines, tracker, notice law check (no API needed)
python run_eval.py --models groq:openai/gpt-oss-120b,gemini:gemini-3.5-flash-lite
python run_eval.py --story "Mera landlord deposit nahi de raha..."   # run a brand-new input
```
Raw, unedited outputs go to `outputs/<model>/<case>.json|.md`. Metrics go to `outputs/metrics.csv` and the comparison to `outputs/leaderboard.csv`.

## Limits (honest)
- The knowledge base is small (16 entries). Rent law differs by state, and only the Model Tenancy Act is included, flagged as applying only where adopted.
- Several entries are marked `secondary` or `unverified` and show a "verify" badge. A lawyer should review the KB before real use.
- The validator matches by section number and Act name. A real section number paired with the wrong Act could slip through in rare cases, and Hindi or regional-language Act names are only partly matched.
- Escalation keywords can misfire. For example, "landlord says my receipt is fake" triggers the refusal rule.
- The voice feature needs a Whisper endpoint (Groq free or OpenAI). Reading images needs a vision-capable model.
- **RAG limits.**
  - The texts are mirrors, not India Code itself.
  - The Code on Wages copy is the Bill as passed by the Lok Sabha.
  - The Constitution copy from the MEA site may not include the latest amendments.
  - Long sections are split into parts, and a continuation part lacks the section's opening words.
  - The retrieval benchmark has only 20 queries, written by me. Treat its numbers as indicative.
  - The citation support check runs only on English replies.
  - Loading the embedding and reranking models takes about 40 seconds the first time; after that, each search takes about 0.3 seconds.
- This is not legal advice. Free legal aid: NALSA **15100**.

## Author

Ritesh Routray (123CR0831, Ceramic Engineering). Built for Kuku FM's AI Generalist assignment, Problem 2.
