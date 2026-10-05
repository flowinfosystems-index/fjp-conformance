# Changelog

All notable changes to FJP-CONF are recorded here.

## [0.1.2] — 2026-10-04

### Fixed
- L2 vacuity heuristic: source-citation parentheticals such as `(per X)` are
  stripped before the concreteness test. Previously the `per ` quantity marker
  matched the citation, letting vacuous falsifiers (e.g. "Conditions may
  change. (per ...)") pass `L2.falsifier.concrete`. Spec text unchanged.

## [0.1.0] — 2026-07-02

Initial public draft.

- Defined the Judgment-Grounded Record (signal / judgment / action / falsifier).
- Defined conformance levels L0 (Structural), L1 (Grounded), L2 (Falsifiable),
  L3 (Accountable).
- Behavioral test suite (stdlib only) with CLI runner and L3 adapter interface.
- Reference passing/failing records and an example L3 adapter.

Released for public review and reference implementation. Method of importance
resolution is out of scope by design; only the externalized record is tested.
