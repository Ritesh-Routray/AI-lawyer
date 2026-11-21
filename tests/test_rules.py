"""Unit tests for the deterministic (non-LLM) safety layers. Run: pytest -q"""
from datetime import date

from ai_lawyer import calculator, escalation, guardrails, kb
from ai_lawyer.redact import redact, restore


def test_validator_keeps_kb_backed_and_removes_invented():
    entries = kb.retrieve("consumer")
    text = ("File within 2 years under Section 69 of the Consumer Protection Act, 2019 [KB:cpa_limitation]. "
            "Also Section 420 IPC applies, see Rajesh Kumar v. Amazon Seller Services (2021) 3 SCC 45. "
            "The Sale of Goods Act, 1930 also helps [KB:made_up_id].")
    clean, r = guardrails.validate(text, entries)
    assert "Section 69" in clean and "[KB:cpa_limitation]" in clean
    assert "420" not in clean and "IPC" not in clean
    assert "Rajesh Kumar" not in clean
    assert "Sale of Goods" not in clean
    assert "made_up_id" not in clean
    assert r["removed_count"] >= 4


def test_validator_section_from_other_problem_type_is_removed():
    # Section 17 (Code on Wages) is real, but not in the consumer KB slice we gave the model
    clean, r = guardrails.validate("Section 17 of the Code on Wages, 2019 says...", kb.retrieve("consumer"))
    assert guardrails.REMOVED in clean


def test_escalation_rules():
    case = {"problem_type": "deposit", "amounts": {"deposit_paid": 50000}, "timeline": []}
    codes = {f["code"] for f in escalation.check("landlord threatened me and called police", case)}
    assert "CRIMINAL" in codes
    assert escalation.top_severity(escalation.check("can you backdate the agreement", case)) == "refuse"
    old = {"problem_type": "consumer", "timeline": [{"date": "2023-01-10"}], "amounts": {}}
    assert "TIME_LIMIT" in {f["code"] for f in escalation.check("refund", old, today=date(2026, 11, 20))}


def test_calculator_deposit():
    c = calculator.compute({"problem_type": "deposit",
                            "amounts": {"deposit_paid": 60000, "deductions_claimed": 15000, "monthly_rent": 20000}})
    assert c["total"] == 45000
    assert any("2 months" in n for n in c["notes"])


def test_redaction_roundtrip():
    s = "Call me on 9876543210, aadhaar 2345 6789 0123, PAN ABCDE1234F, mail a.b@gmail.com, upi ravi@okaxis"
    masked, m = redact(s)
    for secret in ("9876543210", "2345 6789 0123", "ABCDE1234F", "a.b@gmail.com", "ravi@okaxis"):
        assert secret not in masked
    assert restore(masked, m) == s
    # amounts are not masked
    assert redact("deposit was 45000 and 1,20,000")[0] == "deposit was 45000 and 1,20,000"


def test_validator_ignores_non_law_codes():
    clean, r = guardrails.validate("Send to account, IFSC Code [IFSC_1]. Limitation Act applies.", kb.retrieve("deposit"))
    assert r["removed_count"] == 0, r


def test_validator_code_on_wages_after_capitalised_word():
    # regression: Hinglish "Aap Code on Wages" was wrongly removed (found in Gemini eval run)
    clean, r = guardrails.validate("Aap Code on Wages, 2019 ke tahat claim kar sakte hain [KB:cow_s45]", kb.retrieve("salary"))
    assert r["removed_count"] == 0, r


def _rag_entry(act, aliases, sec, unit="Section"):
    return {"id": f"src_x_{sec}", "kind": "law", "act": act, "act_aliases": aliases, "sections": [sec],
            "unit": unit, "status": "primary", "plain": "", "title": "", "source_url": "u", "checked_on": "p.1"}


def test_validator_rejects_right_number_wrong_act():
    entries = [_rag_entry("Consumer Protection Act, 2019", ["Consumer Protection Act"], "69")]
    ok, r1 = guardrails.validate("Section 69 of the Consumer Protection Act, 2019 sets 2 years.", entries)
    assert r1["removed_count"] == 0, r1
    bad, r2 = guardrails.validate("Section 69 of the Code on Wages, 2019 applies.", entries)
    assert guardrails.REMOVED in bad


def test_validator_accepts_retrieved_article():
    entries = [_rag_entry("Constitution of India", ["Constitution"], "39A", unit="Article")]
    _, r = guardrails.validate("Article 39A of the Constitution of India promises free legal aid.", entries)
    assert r["removed_count"] == 0, r


def test_bm25_ranks_matching_section_first():
    from ai_lawyer.rag import BM25
    docs = ["wages shall be paid before the seventh day", "security deposit refund landlord", "complaint within two years"]
    s = BM25(docs).scores("landlord deposit")
    assert s.index(max(s)) == 1


def test_support_check_drops_misattached_official_citation():
    e = _rag_entry("Model Tenancy Act, 2021", ["Model Tenancy Act"], "11")
    e["plain"] = "11. (1) The security deposit to be paid by the tenant shall not exceed two months' rent."
    scorer = lambda claim, text: 5.0 if "deposit" in claim.lower() else -11.0   # stand-in for the cross-encoder
    obj = {"reply": f"Deposit is capped at two months [KB:{e['id']}]. Threats are a police matter [KB:{e['id']}]."}
    out, rep = guardrails.check_support(obj, [e], scorer)
    assert out["reply"].count(f"[KB:{e['id']}]") == 1 and len(rep["unsupported"]) == 1
