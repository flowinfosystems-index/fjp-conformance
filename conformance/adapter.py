"""FJP-CONF v0.1 — L3 agent adapter interface.

An agent claiming Level 3 (Accountable) implements this protocol so the
conformance suite can retrieve a past record and re-evaluate its falsifier.
The suite tests the *interface behavior*, never the agent's internal method.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class JudgmentGroundedAgent(Protocol):
    """Minimal interface an L3-conformant agent must expose."""

    def get_record(self, record_id: str) -> dict:
        """Return the stored Judgment-Grounded Record for `record_id`.

        MUST return a dict whose `record_id` equals the argument and which is a
        valid (L0) JGR. MAY raise if the id is unknown.
        """
        ...

    def evaluate_falsifier(self, record_id: str) -> str:
        """Re-evaluate the record's falsifier against the current world.

        MUST return one of: "open", "triggered", "expired".
        """
        ...
