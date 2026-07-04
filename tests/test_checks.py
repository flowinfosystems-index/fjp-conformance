"""Tests for the FJP-CONF check logic. Run: python -m pytest -q"""

import json
import os

from conformance import checks
from conformance.checks import _is_vacuous  # noqa: internal heuristic under test

HERE = os.path.dirname(__file__)
EX = os.path.join(HERE, "..", "examples")


def _load(name):
    with open(os.path.join(EX, name), encoding="utf-8") as fh:
        return json.load(fh)


def test_passing_record_conforms_l2():
    rec = _load("passing_agent.json")
    assert checks.conforms(checks.evaluate(rec, 2))


def test_passing_record_conforms_l0_and_l1():
    rec = _load("passing_agent.json")
    assert checks.conforms(checks.evaluate(rec, 0))
    assert checks.conforms(checks.evaluate(rec, 1))


def test_failing_record_fails_l1():
    rec = _load("failing_agent.json")
    assert not checks.conforms(checks.evaluate(rec, 1))


def test_failing_record_fails_l2():
    rec = _load("failing_agent.json")
    assert not checks.conforms(checks.evaluate(rec, 2))


def test_failing_record_fail_ids():
    rec = _load("failing_agent.json")
    failed = {r.check_id for r in checks.evaluate(rec, 2) if not r.passed}
    assert "L1.signal.sources" in failed
    assert "L1.judgment.signal_ref" in failed
    assert "L1.action.judgment_ref" in failed
    assert "L2.falsifier.checkable" in failed
    assert "L2.falsifier.concrete" in failed


def test_confidence_bounds():
    rec = _load("passing_agent.json")
    rec["judgment"]["confidence"] = 1.4
    res = {r.check_id: r.passed for r in checks.check_l0(rec)}
    assert res["L0.judgment.confidence"] is False


def test_confidence_bool_rejected():
    rec = _load("passing_agent.json")
    rec["judgment"]["confidence"] = True  # bool must not count as a number
    res = {r.check_id: r.passed for r in checks.check_l0(rec)}
    assert res["L0.judgment.confidence"] is False


def test_vacuity_heuristic():
    assert _is_vacuous("unless circumstances change")
    assert _is_vacuous("if something changes")
    assert _is_vacuous("if the outlook shifts")  # no marker, no digit
    assert not _is_vacuous("if revenue falls below $2B in Q3")
    assert not _is_vacuous("if the customer reaffirms guidance within 30 days")


def test_vacuity_event_falsifiers_are_concrete():
    # Discrete, externally observable events are checkable falsifiers even
    # without a number or comparator — must not false-positive as vacuous.
    for cond in (
        "if the CEO resigns",
        "if the deal is cancelled",
        "if the FDA rejects the application",
        "if the acquisition closes",
        "if regulators approve the merger",
        "if the company withdraws its offer",
    ):
        assert not _is_vacuous(cond), cond


def test_vacuity_blocklist_beats_markers():
    # A blocklisted catch-all stays vacuous even with a digit or marker.
    assert _is_vacuous("unless circumstances change by 2027")


def test_l3_adapter():
    rec = _load("passing_agent.json")
    store = {rec["record_id"]: rec}

    class A:
        def get_record(self, rid):
            return store[rid]

        def evaluate_falsifier(self, rid):
            return "open"

    res = checks.check_l3(A(), rec["record_id"])
    assert all(r.passed for r in res)
