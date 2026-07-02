# FJP-CONF v0.1 — Judgment-Grounded Record: Field Reference

Normative field-level reference for the JGR defined in [`v0.1.md`](./v0.1.md).
Keywords MUST / MUST NOT / MAY per RFC 2119.

## Top level

| Field       | Type   | Required | Notes                                    |
|-------------|--------|----------|------------------------------------------|
| `record_id` | string | yes      | Stable, unique per record.               |
| `timestamp` | string | yes      | ISO 8601. When the record was emitted.   |
| `signal`    | object | yes      | See below.                               |
| `judgment`  | object | yes      | See below.                               |
| `action`    | object | yes      | See below.                               |
| `falsifier` | object | yes      | See below.                               |

## `signal` — what changed

| Field         | Type      | Required | Notes                                         |
|---------------|-----------|----------|-----------------------------------------------|
| `description` | string    | yes      | The observed change, in plain language.       |
| `sources`     | string[]  | L1+      | Attribution: URIs or stable identifiers.      |
| `observed_at` | string    | yes      | ISO 8601. When the change was observed.       |

At L0, `sources` MAY be empty. At L1+, it MUST contain at least one entry.

## `judgment` — why it matters

| Field        | Type   | Required | Notes                                            |
|--------------|--------|----------|--------------------------------------------------|
| `assessment` | string | yes      | Why the change warrants (or does not) an action. |
| `confidence` | number | yes      | In [0, 1].                                        |
| `signal_ref` | string | L1+      | MUST equal a `signal`'s identity (see chaining). |

## `action` — what should happen

| Field          | Type   | Required | Notes                                          |
|----------------|--------|----------|------------------------------------------------|
| `directive`    | string | yes      | The recommended or executed action.            |
| `target`       | string | no       | Who/what the action applies to.                |
| `judgment_ref` | string | L1+      | MUST equal the `judgment`'s identity.          |

## `falsifier` — what would make this wrong

| Field       | Type    | Required | Notes                                              |
|-------------|---------|----------|----------------------------------------------------|
| `condition` | string  | yes      | The concrete condition that reverses the judgment. |
| `checkable` | boolean | L2+      | MUST be `true` at L2+.                              |
| `status`    | string  | L2+      | `open` \| `triggered` \| `expired`.                |

### Chaining (L1+)

An JGR is single-record: it contains exactly one `signal`, one `judgment`, one
`action`. Chaining is validated by identity, not by pointer resolution across a
store:

- `judgment.signal_ref` MUST match the signal's canonical identity.
- `action.judgment_ref` MUST match the judgment's canonical identity.

Implementations MAY use `signal.description` (or an explicit `signal.id`, if
present) as the canonical identity. The reference checks in
[`conformance/checks.py`](../conformance/checks.py) accept either an explicit
`id` field or the canonical fallback.

### Falsifier vacuity (L2)

A falsifier MUST NOT be a vacuous catch-all (e.g. "if circumstances change").
The L2 check applies a heuristic first filter: the condition must reference a
concrete entity, threshold, quantity, or dated bound, and MUST NOT match the
vacuity blocklist. This is a *first filter*, not a substitute for review — it is
designed to catch trivially non-falsifiable conditions automatically.
