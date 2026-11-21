"""Tests for the code-only companion features: deadlines, claim tracker, cost/benefit, notice law check."""
from datetime import date

from ai_lawyer import companion, kb, ui
from ai_lawyer.notice import check_law

TODAY = date(2026, 11, 21)
SALARY = {"problem_type": "salary", "timeline": [{"date": "2026-08", "event": "salary stopped"},
                                                 {"date": "2026-10-31", "event": "I resigned"}]}


def test_deadlines_limit_and_final_wages():
    d = {x["kind"]: x for x in companion.deadlines(SALARY, [], TODAY)}
    assert d["limit"]["date"] == date(2029, 8, 1) and d["limit"]["kb"] == "cow_s45"
    # resigned Sat 31 Oct -> 2 working days -> Tue 3 Nov; overdue by 18 days
    assert d["overdue"]["date"] == date(2026, 11, 3) and d["overdue"]["status"] == "overdue"


def test_consumer_limit_two_years_and_notice_followup():
    case = {"problem_type": "consumer", "timeline": [{"date": "2026-09-02", "event": "ordered"}]}
    items = companion.deadlines(case, [{"kind": "sent_notice", "date": "2026-11-10"}], TODAY)
    assert any(x["kind"] == "limit" and x["date"] == date(2028, 9, 2) for x in items)
    assert any(x["kind"] == "followup" and x["date"] == date(2026, 11, 25) for x in items)


def test_every_deadline_and_route_source_exists_in_kb():
    ids = set(kb.load_kb())
    for _, kb_id, _ in companion.LIMITS.values():
        assert kb_id in ids
    for routes in companion.ROUTES.values():
        for r in routes:
            assert r["kb"] is None or r["kb"] in ids, r


def test_next_step_ladder():
    calc = {"total": 105000}
    assert companion.next_step(SALARY, calc, [], TODAY)["doc"] == "whatsapp_message"
    wait = companion.next_step(SALARY, calc, [{"kind": "sent_message", "date": "2026-11-18"}], TODAY)
    assert wait["wait_until"] == date(2026, 11, 25) and wait["doc"] is None
    # refusal skips the wait; partial payment lowers what is still owed
    ev = [{"kind": "sent_message", "date": "2026-11-18"}, {"kind": "refused", "date": "2026-11-19"},
          {"kind": "paid_part", "date": "2026-11-19", "amount": 35000}]
    nx = companion.next_step(SALARY, calc, ev, TODAY)
    assert nx["doc"] == "legal_notice" and nx["remaining"] == 70000
    after_notice = [{"kind": "sent_notice", "date": "2026-10-01"}]
    assert companion.next_step(SALARY, calc, after_notice, TODAY)["doc"] == "labour_complaint"
    assert companion.next_step(SALARY, calc, [{"kind": "paid_full", "date": "2026-11-20"}], TODAY)["stage"] == 5


def test_cost_benefit_is_honest_about_small_deposits():
    small = companion.cost_benefit({"problem_type": "deposit"}, {"total": 8000})
    assert "more time than it recovers" in small["verdict"]
    assert "Nil up to Rs 5 lakh" in str(companion.cost_benefit({"problem_type": "consumer"}, {"total": 30000})["routes"])


def test_notice_law_check():
    assert check_law("Section 420 of the IPC")["verdict"] == "old"
    assert check_law("Section 318 of the Bharatiya Nyaya Sanhita, 2023")["verdict"] == "found"
    assert check_law("Section 999 of BNS")["verdict"] == "missing"
    assert check_law("Section 106, Transfer of Property Act")["verdict"] == "unknown"


def test_shareable_page_keeps_details_masked():
    result = {"case": {"summary": "Owner [PHONE_1] withheld deposit", "problem_type": "deposit", "timeline": []},
              "calculation": {"total": 35000, "lines": []}, "assessment": {"options": []}, "flags": [],
              "_pii_mapping": {"[PHONE_1]": "9876543210"}}
    html = ui.case_page(result, [], [], None, companion.EVENT_KINDS)
    assert "[PHONE_1]" in html and "9876543210" not in html
