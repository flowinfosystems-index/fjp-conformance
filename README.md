# FJP-CONF — Flow Judgment Protocol Conformance

**Flow Judgment Protocol™ (FJP)** is the judgment layer for AI agents and
enterprise decision systems. It determines what changed, whether it matters, what
matters most, and what should happen next.

**FJP-CONF** is the public, vendor-neutral conformance standard for FJP. It defines
what it means for an agent to make **accountable** decisions — decisions that can
be traced, challenged, and audited — and ships a runnable test suite so any
developer can verify their own agent.

- **Specification:** [`spec/v0.1.md`](./spec/v0.1.md) · field reference: [`spec/schema.md`](./spec/schema.md)
- **Canonical URL:** https://fjp.flowinfo.co/conformance/v0.1
- **Status:** v0.1.0 — public draft

FJP-CONF tests an agent's **observable output**, not its internal method. Two
agents may reach opposite conclusions and both conform. Conformance asserts that a
decision is *accountable* — not that it is *correct*.

## The idea in one paragraph

Retrieval-grade systems answer *what is true*. They do not answer *was this worth
acting on, and how would we know if it wasn't*. When an agent acts, three questions
must be answerable afterward: what did it act on, why did it judge that worth acting
on, and what would have made that judgment wrong. FJP-CONF defines the minimum
externalized structure — the **Judgment-Grounded Record** — that makes those
questions answerable, independent of how the agent decides.

## The Judgment-Grounded Record

For every action it recommends or takes, a conforming agent emits a record with
four components:

| Component   | Answers             |
|-------------|---------------------|
| `signal`    | what changed        |
| `judgment`  | why it matters      |
| `action`    | what should happen  |
| `falsifier` | what would make it wrong |

## Conformance levels

| Level | Name         | Adds                                                        |
|-------|--------------|-------------------------------------------------------------|
| L0    | Structural   | A well-formed record with all four components.              |
| L1    | Grounded     | Attributable signal; the action traces back to it.          |
| L2    | Falsifiable  | A concrete, checkable condition that would reverse the call. |
| L3    | Accountable  | Records are retained and the falsifier can be re-evaluated.  |

## Quickstart

Requires Python 3.11+. No third-party dependencies.

```bash
# validate a record at Level 2
python -m conformance.runner examples/passing_agent.json --level 2

# a non-conforming record
python -m conformance.runner examples/failing_agent.json --level 2
```

Exit codes: `0` conforms · `1` does not conform · `2` invalid input.

Programmatic use:

```python
from conformance import evaluate, conforms

results = evaluate(record, level=2)
print(conforms(results))
```

Level 3 requires your agent to implement a small adapter
(`get_record`, `evaluate_falsifier`); see [`conformance/adapter.py`](./conformance/adapter.py)
and [`examples/passing_agent_l3.py`](./examples/passing_agent_l3.py).

Run the tests:

```bash
python -m pytest -q
```

## Claiming conformance

A conformance claim names a level and version and is reproducible by running this
suite against your agent's output:

> "Conforms to FJP-CONF v0.1, Level 2."

Authoritative verification and any official FJP-CONF certification are administered
by Flow Information Systems. This open suite lets anyone self-check; see
[`TRADEMARKS.md`](./TRADEMARKS.md) for what you may and may not call your
implementation.

## License and trademarks

Source code is licensed under the Apache License, Version 2.0 — see
[`LICENSE`](./LICENSE). The code license does **not** grant rights in the
trademarks.

**Flow Judgment Protocol™, FJP™, FJP-CONF™, Judgment-Grounded Agent™,** and
**"DNS resolves location. Flow resolves importance."™** are trademarks of
**Flow Information Systems** (https://flowinfo.co). See [`NOTICE`](./NOTICE) and
[`TRADEMARKS.md`](./TRADEMARKS.md).
