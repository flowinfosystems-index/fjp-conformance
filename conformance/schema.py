"""FJP-CONF v0.1 — schema constants and canonical-identity helpers.

Stdlib only. No third-party dependencies, by design: a public conformance tool
must run anywhere with `python3` and nothing else.
"""

SPEC_VERSION = "0.1.0"

VALID_STATUSES = ("open", "triggered", "expired")

# Heuristic vacuity blocklist for L2 falsifier checks (case-insensitive substring).
# A first filter to catch trivially non-falsifiable conditions, not a full review.
VACUITY_BLOCKLIST = (
    "circumstances change",
    "things change",
    "the world changes",
    "the situation changes",
    "conditions change",
    "new information",
    "it becomes clear",
    "anything changes",
    "something changes",
    "market changes",  # too broad without a threshold
    "sentiment changes",
)

# Tokens that signal a concrete, checkable falsifier condition.
# Two families: (a) threshold/quantity/date comparators, (b) discrete,
# externally observable events. Stems are intentional ("cancel" catches
# cancels/cancelled/cancellation) — matching is case-insensitive substring.
CONCRETENESS_MARKERS = (
    # comparators / quantities / bounds
    "exceeds", "falls", "drops", "rises", "above", "below", "reaches",
    "within", "by ", "before", "after", "greater than", "less than",
    "more than", "fewer than", "at least", "at most", "declines", "increases",
    "%", "$", "per ", "no later than", "if not", "unless",
    # discrete observable events
    "announces", "files", "confirms", "denies", "misses", "beats",
    "resign", "cancel", "reject", "approv", "closes", "terminat",
    "withdraw", "delay", "acquir", "launch", "recall", "default",
    "downgrade", "upgrade", "steps down", "departs", "reaffirm", "raises",
    "cuts", "suspend", "rules", "votes", "signs", "expires", "settle",
)


def canonical_signal_id(signal: dict) -> str:
    """Identity of a signal: explicit `id` if present, else its description."""
    if not isinstance(signal, dict):
        return ""
    return str(signal.get("id") or signal.get("description") or "").strip()


def canonical_judgment_id(judgment: dict) -> str:
    """Identity of a judgment: explicit `id` if present, else its assessment."""
    if not isinstance(judgment, dict):
        return ""
    return str(judgment.get("id") or judgment.get("assessment") or "").strip()
