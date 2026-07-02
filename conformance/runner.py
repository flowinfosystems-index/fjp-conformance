"""FJP-CONF v0.1 — command-line runner.

Usage:
    python -m conformance.runner examples/passing_agent.json --level 2
    python -m conformance.runner path/to/record.json          # defaults to L2

Exit code 0 if the record conforms at the requested level, 1 otherwise.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from . import checks, schema

# A single Judgment-Grounded Record is small. Cap input to prevent a hostile file
# from exhausting memory or the JSON parser (matters if this runner is ever
# invoked on third-party-submitted records, e.g. a hosted verifier).
MAX_RECORD_BYTES = 1_048_576  # 1 MiB


class InvalidInput(Exception):
    """Raised when the input file cannot be read or parsed as a JSON object."""


def _load(path: str) -> dict:
    try:
        size = os.path.getsize(path)
    except OSError as e:
        raise InvalidInput(f"cannot access {path}: {e}") from e
    if size > MAX_RECORD_BYTES:
        raise InvalidInput(
            f"file is {size} bytes; exceeds {MAX_RECORD_BYTES}-byte limit for a "
            "single record")
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = fh.read(MAX_RECORD_BYTES + 1)
    except OSError as e:
        raise InvalidInput(f"cannot read {path}: {e}") from e
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise InvalidInput(f"not valid JSON: {e}") from e
    except RecursionError as e:
        raise InvalidInput("JSON nesting too deep") from e


def run(path: str, level: int) -> bool:
    record = _load(path)
    results = checks.evaluate(record, level)
    ok = checks.conforms(results)

    print(f"FJP-CONF v{schema.SPEC_VERSION}  —  {path}")
    print(f"Target level: L{level}\n")
    for res in results:
        mark = "PASS" if res.passed else "FAIL"
        print(f"  [{mark}] L{res.level}  {res.check_id}")
        if not res.passed:
            print(f"         -> {res.detail}")

    print()
    if ok:
        print(f"RESULT: conforms to FJP-CONF v{schema.SPEC_VERSION} Level {level}")
    else:
        failed = [r.check_id for r in results if not r.passed]
        print(f"RESULT: does NOT conform at Level {level} "
              f"({len(failed)} check(s) failed)")
    return ok


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="fjp-conform",
        description="Validate a Judgment-Grounded Record against FJP-CONF v0.1.",
    )
    p.add_argument("record", help="Path to a JSON record to validate.")
    p.add_argument("--level", type=int, default=2, choices=(0, 1, 2),
                   help="Target conformance level (0-2). L3 requires an adapter "
                        "and is validated programmatically, not from the CLI.")
    args = p.parse_args(argv)
    try:
        return 0 if run(args.record, args.level) else 1
    except InvalidInput as e:
        print(f"ERROR: invalid input — {e}", file=sys.stderr)
        return 2  # distinct from 1 (non-conforming) so CI can tell them apart


if __name__ == "__main__":
    sys.exit(main())
