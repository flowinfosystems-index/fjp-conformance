"""Reference L3 adapter — the minimal shape an Accountable agent exposes.

Run the L3 check against it:

    python examples/passing_agent_l3.py
"""

from __future__ import annotations

import json
import os
import sys

# Allow running directly (`python examples/passing_agent_l3.py`) by putting the
# repo root on the path.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conformance import check_l3
from conformance.adapter import JudgmentGroundedAgent


class ExampleAgent:
    """A trivial store-backed agent. A real agent would re-evaluate the
    falsifier against live data instead of returning a fixed status."""

    def __init__(self, records: dict):
        self._records = records

    def get_record(self, record_id: str) -> dict:
        return self._records[record_id]

    def evaluate_falsifier(self, record_id: str) -> str:
        # A real implementation checks the world here. This example reports the
        # stored status unchanged, which is a valid (if static) response.
        return self._records[record_id]["falsifier"]["status"]


def _load_example() -> dict:
    here = os.path.dirname(__file__)
    with open(os.path.join(here, "passing_agent.json"), encoding="utf-8") as fh:
        rec = json.load(fh)
    return {rec["record_id"]: rec}


if __name__ == "__main__":
    agent = ExampleAgent(_load_example())
    assert isinstance(agent, JudgmentGroundedAgent)  # structural protocol check
    rid = next(iter(agent._records))
    results = check_l3(agent, rid)
    for r in results:
        print(f"  [{'PASS' if r.passed else 'FAIL'}] {r.check_id}"
              + ("" if r.passed else f"  -> {r.detail}"))
    print("\nL3:", "PASS" if all(r.passed for r in results) else "FAIL")
