# Raw outputs (unedited)

Each `<model>/<case>.json` holds the input, the full pipeline output and its metrics:
- the case file
- the rule-engine flags
- the code-computed claim
- the **raw** model assessment (`assessment_raw`)
- the **validated** assessment
- the guardrail report
- for some cases, a drafted document

Each `<case>.md` is the same result in readable form. A case that failed has an `.error.txt` instead.

| Model | Code version | Cases | Notes |
|---|---|---|---|
| `gemini:gemini-3.5-flash-lite` | final (v2) | 18/18 | Free tier. About 8 seconds per case. In the first full v2 pass, 2 cases returned malformed JSON and 1 hit a network error. A one-shot "repair your JSON" retry was added, and those 3 cases were rerun. |
| `groq:openai/gpt-oss-120b` | v1 | 16/18 | 2 cases failed on network errors (retry logic added afterwards). The v2 rerun hit Groq's free **200k tokens/day** cap; that failed run is archived under `outputs_v1_baseline/_unused/failed_v2_runs/`. |
| `groq:qwen/qwen3.8-27b` | v1 | 11/18 | 7 cases failed: Groq's free tier caps this model at **1,000 output tokens/minute**, below what one assessment needs. Set `MAX_OUTPUT_TOKENS=1000` to stay under it. |

What changed between v1 and v2:
- the intake prompt says which amount field to use
- a rule escalates notices sent by the other side's lawyer
- the reply is written in the user's own script (Hinglish in Roman letters, Hindi in Devanagari)
- the app adds a code-written honesty note when someone asks for case law
- the citation checker no longer flags "IFSC Code" or "Code on Wages" by mistake
- the test case `adv02` now accepts any problem type, because the refusal is scored separately

**v3 (RAG), the current Gemini row.** The assistant now also retrieves official-text sections (BNS, BNSS, Constitution, Consumer Protection Act, Code on Wages, Model Tenancy Act); each `.json` has a `retrieval` block listing them. Compared with v2 (saved in `outputs_v2_pre_rag/`):
- Quality scores are unchanged: type 94%, every other score 100%.
- **13 of 18 cases now cite official text**, against 0 before RAG.
- **3 citations were dropped by the support check** because the sentence didn't match what the section says (see `guardrail_report.support_check`).

The support check is English-only and conservative: it can also drop a valid citation when the claim is vague.

`outputs_v1_baseline/` keeps the v1 run for comparison. `leaderboard.csv` is the per-model summary, and `metrics.csv` has one row per case.

Not scored automatically: the quality of drafted documents and the tone of replies. These need a human (ideally a lawyer) to rate them. A sample of drafts is in the `.md` files for `dep01`, `con01` and `sal01`.
