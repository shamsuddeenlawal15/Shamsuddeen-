#!/usr/bin/env python3
"""Validate Day 1 CSV structure and research-integrity invariants."""

from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PARAMETERS = ROOT / "data" / "processed" / "parameters.csv"
VALIDATION = ROOT / "data" / "processed" / "validation_matrix.csv"
EQUATIONS = ROOT / "data" / "processed" / "equations.csv"

PARAMETER_COLUMNS = [
    "parameter_id", "test_id", "category", "parameter_name", "symbol",
    "value_text", "value_numeric", "unit", "source_document", "source_page",
    "source_locator", "provenance_type", "verification_status", "notes",
]
VALIDATION_COLUMNS = [
    "validation_id", "test_id", "observable", "experimental_value",
    "experimental_unit", "experimental_source_page",
    "experimental_source_locator", "model_code", "predicted_value",
    "predicted_unit", "predicted_source_page", "predicted_source_locator",
    "comparison_metric", "reported_comparison", "verification_status", "notes",
]
EQUATION_COLUMNS = [
    "equation_id", "equation_number", "model", "equation_text", "variables",
    "source_page", "source_locator", "verification_status",
    "implementation_note",
]
PROVENANCE = {"published", "derived", "missing"}
STATUS = {"verified", "needs_secondary_check", "unverified", "blocked"}


def read_rows(path: Path, columns: list[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != columns:
            raise ValueError(f"{path}: unexpected columns: {reader.fieldnames}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path}: must contain at least one explicit status row")
    return rows


def validate_parameters(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        pid = row["parameter_id"]
        if not pid or pid in seen:
            raise ValueError(f"parameters.csv:{line}: missing/duplicate parameter_id")
        seen.add(pid)
        if row["provenance_type"] not in PROVENANCE:
            raise ValueError(f"parameters.csv:{line}: invalid provenance_type")
        if row["verification_status"] not in STATUS:
            raise ValueError(f"parameters.csv:{line}: invalid verification_status")
        if row["provenance_type"] == "published":
            required = ("value_text", "unit", "source_page", "source_locator")
            missing = [name for name in required if not row[name].strip()]
            if missing:
                raise ValueError(
                    f"parameters.csv:{line}: published row missing {', '.join(missing)}"
                )
        if row["verification_status"] == "verified" and not row["source_page"].strip():
            raise ValueError(f"parameters.csv:{line}: verified row needs source_page")


def validate_results(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        vid = row["validation_id"]
        if not vid or vid in seen:
            raise ValueError(f"validation_matrix.csv:{line}: missing/duplicate validation_id")
        seen.add(vid)
        if row["test_id"] not in {"F7-1", "F7-2"}:
            raise ValueError(f"validation_matrix.csv:{line}: invalid test_id")
        if row["model_code"] not in {"MELCOR", "SPHINCS"}:
            raise ValueError(f"validation_matrix.csv:{line}: invalid model_code")
        if row["verification_status"] not in STATUS:
            raise ValueError(f"validation_matrix.csv:{line}: invalid verification_status")
        if row["verification_status"] == "verified":
            required = (
                "experimental_value", "experimental_unit",
                "experimental_source_page", "experimental_source_locator",
                "predicted_value", "predicted_unit", "predicted_source_page",
                "predicted_source_locator",
            )
            missing = [name for name in required if not row[name].strip()]
            if missing:
                raise ValueError(
                    f"validation_matrix.csv:{line}: verified row missing {', '.join(missing)}"
                )


def validate_equations(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        eid = row["equation_id"]
        if not eid or eid in seen:
            raise ValueError(f"equations.csv:{line}: missing/duplicate equation_id")
        seen.add(eid)
        if row["model"] not in {"MELCOR", "SPHINCS"}:
            raise ValueError(f"equations.csv:{line}: invalid model")
        if row["verification_status"] not in STATUS:
            raise ValueError(f"equations.csv:{line}: invalid verification_status")
        required = ("equation_text", "variables", "source_page", "source_locator")
        missing = [name for name in required if not row[name].strip()]
        if missing:
            raise ValueError(f"equations.csv:{line}: missing {', '.join(missing)}")


def main() -> int:
    try:
        validate_parameters(read_rows(PARAMETERS, PARAMETER_COLUMNS))
        validate_results(read_rows(VALIDATION, VALIDATION_COLUMNS))
        validate_equations(read_rows(EQUATIONS, EQUATION_COLUMNS))
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("Day 1 data contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
