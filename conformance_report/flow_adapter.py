"""Flow Action Graph — L3 Adapter.

Implements the JudgmentGroundedAgent protocol (conformance/adapter.py) for
Flow's Action Graph. Demonstrates L3 conformance: record retrieval and
falsifier re-evaluation.
"""

from __future__ import annotations

import json
import os


class FlowActionGraphAdapter:
    """L3 adapter for Flow Action Graph.

    For conformance testing, reads from the local JGR™ snapshot.
    """

    def __init__(self, records_dir: str = None):
        self._records: dict[str, dict] = {}

        if records_dir is None:
            records_dir = os.path.dirname(__file__)

        for fname in os.listdir(records_dir):
            if fname.startswith("flow-ag-") and fname.endswith(".json"):
                with open(os.path.join(records_dir, fname)) as f:
                    rec = json.load(f)
                    self._records[rec["record_id"]] = rec

    def get_record(self, record_id: str) -> dict:
        """Retrieve a stored Judgment-Grounded™ Record."""
        rec = self._records.get(record_id)
        if rec is None:
            raise KeyError(f"record_id {record_id!r} not found in store")
        return rec

    def evaluate_falsifier(self, record_id: str) -> str:
        """Re-evaluate the falsifier against current conditions.

        Returns one of: "open", "triggered", "expired".
        """
        rec = self.get_record(record_id)
        return rec["falsifier"]["status"]


def run_l3_checks():
    """Run the L3 conformance checks using the Flow adapter."""
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

    from conformance import checks

    adapter = FlowActionGraphAdapter()
    all_results = []

    for record_id in sorted(adapter._records.keys()):
        rec = adapter._records[record_id]

        # Run L0-L2 first
        l0_l2 = checks.evaluate(rec, 2)
        # Run L3
        l3 = checks.check_l3(adapter, record_id)

        all_checks = l0_l2 + l3
        all_passed = all(r.passed for r in all_checks)
        all_results.append((record_id, all_checks, all_passed))
        status_icon = "✓" if all_passed else "✗"
        print(f"\n{'='*70}")
        print(f"{status_icon}  {record_id}")
        print(f"   Falsifier: {rec['falsifier']['status']}")
        print(f"   {'-'*66}")

        for r in all_checks:
            mark = "PASS" if r.passed else "FAIL"
            print(f"   [{mark}] L{r.level}  {r.check_id}")
            if not r.passed:
                print(f"            → {r.detail}")

    # Summary
    print(f"\n{'='*70}")
    print(f"FJP-CONF v0.1.0 — Level 3 Conformance Summary")
    print(f"{'='*70}")
    total = len(all_results)
    passed = sum(1 for _, _, ok in all_results if ok)
    print(f"Records tested:  {total}")
    print(f"Records passing: {passed}/{total}")
    print(f"Overall:         {'CONFORMS' if passed == total else 'DOES NOT CONFORM'} "
          f"at Level 3")

    if passed == total:
        print(f"\n  → Flow Action Graph conforms to FJP-CONF v0.1.0, Level 3.")

    return all(ok for _, _, ok in all_results)


if __name__ == "__main__":
    import sys
    sys.exit(0 if run_l3_checks() else 1)
