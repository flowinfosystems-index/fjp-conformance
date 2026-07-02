"""FJP-CONF v0.1 — Judgment-Grounded Agent conformance suite."""

from .schema import SPEC_VERSION
from .checks import (
    Result,
    check_l0,
    check_l1,
    check_l2,
    check_l3,
    evaluate,
    conforms,
)
from .adapter import JudgmentGroundedAgent

__all__ = [
    "SPEC_VERSION",
    "Result",
    "check_l0",
    "check_l1",
    "check_l2",
    "check_l3",
    "evaluate",
    "conforms",
    "JudgmentGroundedAgent",
]
