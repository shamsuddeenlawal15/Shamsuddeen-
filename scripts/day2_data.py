#!/usr/bin/env python3
"""Build/check the additive Day 2 database; checks do not verify scientific accuracy.

Day 1 records are immutable. Edit Parameter_Additions.csv and the source register,
then run ``python scripts/day2_data.py --build``. The default ``--check`` compares
the saved combined database against those inputs, including row order.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
BASELINE_COMMIT = "f14ebf1ce7bd1a9e3991f31df5c74628e58dfe63"
BASELINE_PATH = "data/processed/parameters.csv"
ADDITIONS_PATH = "data/processed/day-02/Parameter_Additions.csv"
COMBINED_PATH = "data/processed/day-02/Updated_Parameter_Database.csv"
SOURCES_PATH = "references/day-02/sources.json"
BASE_COLUMNS = [
    "parameter_id", "test_id", "category", "parameter_name", "symbol",
    "value_text", "value_numeric", "unit", "source_document", "source_page",
    "source_locator", "provenance_type", "verification_status", "notes",
]
EXTRA_COLUMNS = [
    "day_added", "source_id", "source_access_status", "evidence_kind",
    "supersedes", "derivation", "verification_basis",
]
COLUMNS = BASE_COLUMNS + EXTRA_COLUMNS
LEGACY_SUFFIX = dict(zip(EXTRA_COLUMNS, [
    "1", "L2023", "read", "legacy_record", "", "",
    "Copied without changing Day 1 fields; verified denotes source transcription "
    "or checked absence only.",
]))
PROVENANCE = {"published", "derived", "missing"}
VERIFICATION = {"verified", "needs_secondary_check", "unverified", "blocked"}
ACCESS = {"read", "not_retrieved"}
EVIDENCE = {
    "legacy_record", "published_statement", "published_equation",
    "missing_from_article", "derived_interpretation", "source_unavailable",
}


def read_csv(path: Path, columns: list[str]) -> list[dict[str, str]]:
    """Reject ragged CSV records instead of accepting DictReader's extra keys."""
    with path.open(encoding="utf-8", newline="") as stream:
        try:
            records = list(csv.reader(stream, strict=True))
        except csv.Error as exc:
            raise ValueError(f"{path}: invalid CSV: {exc}") from exc
    if not records or records[0] != columns:
        raise ValueError(f"{path}: expected exact {len(columns)}-column header")
    rows = []
    for number, record in enumerate(records[1:], start=2):
        if len(record) != len(columns):
            raise ValueError(
                f"{path}: record {number}: expected {len(columns)} fields, "
                f"found {len(record)}"
            )
        rows.append(dict(zip(columns, record)))
    return rows


def source_index(records: object) -> dict[str, dict[str, object]]:
    if not isinstance(records, list):
        raise ValueError("source register must be a JSON array")
    result = {}
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("source register entries must be objects")
        sid = record.get("source_id")
        if not isinstance(sid, str) or not sid.strip() or sid != sid.strip():
            raise ValueError("source register has missing/invalid source_id")
        if sid in result:
            raise ValueError(f"source register has duplicate source_id {sid}")
        if record.get("access_status") not in ACCESS:
            raise ValueError(f"source {sid}: invalid access_status")
        result[sid] = record
    return result


def unique_rows(rows: list[dict[str, str]], columns: list[str], label: str) -> None:
    seen = set()
    for number, row in enumerate(rows, start=2):
        if set(row) != set(columns) or any(not isinstance(v, str) for v in row.values()):
            raise ValueError(f"{label}: record {number}: invalid column set/value type")
        pid = row["parameter_id"]
        if not pid.strip() or pid != pid.strip() or pid in seen:
            raise ValueError(f"{label}: missing/duplicate/invalid parameter_id {pid!r}")
        seen.add(pid)


def combine_rows(
    baseline: list[dict[str, str]], additions: list[dict[str, str]],
) -> list[dict[str, str]]:
    unique_rows(baseline, BASE_COLUMNS, "Day 1 baseline")
    unique_rows(additions, COLUMNS, "Day 2 additions")
    return [{**row, **LEGACY_SUFFIX} for row in baseline] + [dict(row) for row in additions]


def validate_rows(
    rows: list[dict[str, str]], sources: dict[str, dict[str, object]],
) -> None:
    unique_rows(rows, COLUMNS, "combined database")
    identifiers = {row["parameter_id"] for row in rows}
    for row in rows:
        pid = row["parameter_id"]

        def fail(message: str) -> None:
            raise ValueError(f"{pid}: {message}")

        provenance = row["provenance_type"]
        status = row["verification_status"]
        if provenance not in PROVENANCE:
            fail("invalid provenance_type")
        if status not in VERIFICATION:
            fail("invalid verification_status")
        if row["evidence_kind"] not in EVIDENCE:
            fail("invalid evidence_kind")
        sid = row["source_id"]
        if sid not in sources:
            fail(f"unknown source_id {sid!r}")
        access = sources[sid]["access_status"]
        if row["source_access_status"] != access:
            fail("source_access_status disagrees with source register")
        if row["day_added"] not in {"1", "2"}:
            fail("invalid day_added")
        numeric = row["value_numeric"].strip()
        if numeric:
            try:
                finite = math.isfinite(float(numeric))
            except ValueError:
                finite = False
            if not finite:
                fail("value_numeric must be a finite number")
            if access != "read":
                fail("numeric value requires a read source")
        if provenance == "missing" and numeric:
            fail("missing record must have empty value_numeric")
        if row["evidence_kind"] == "source_unavailable" and (
            provenance != "missing" or status != "blocked" or access != "not_retrieved"
        ):
            fail("source_unavailable requires missing/blocked/not_retrieved")
        supersedes = row["supersedes"]
        if supersedes and (supersedes not in identifiers or supersedes == pid):
            fail("supersedes must name an existing, different parameter_id")
        if row["day_added"] == "1":
            if any(row[key] != value for key, value in LEGACY_SUFFIX.items()):
                fail("inherited Day 1 metadata changed")
            continue
        if row["evidence_kind"] == "legacy_record":
            fail("new Day 2 record cannot be legacy_record")
        if provenance == "published" and row["evidence_kind"] not in {
            "published_statement", "published_equation",
        }:
            fail("published record requires published evidence_kind")
        if provenance == "derived":
            if not row["derivation"].strip():
                fail("derived record requires derivation")
            if row["evidence_kind"] != "derived_interpretation":
                fail("derived record requires derived_interpretation evidence_kind")
        if status == "verified" or provenance == "published":
            if access != "read":
                fail("verified/published record requires a read source")
            required = ("source_document", "source_page", "source_locator", "verification_basis")
            absent = [key for key in required if not row[key].strip()]
            if absent:
                fail("verified/published record missing " + ", ".join(absent))
        if provenance == "published":
            absent = [key for key in ("value_text", "unit") if not row[key].strip()]
            if absent:
                fail("published record missing " + ", ".join(absent))


def validate_combined(
    actual: list[dict[str, str]], baseline: list[dict[str, str]],
    additions: list[dict[str, str]], sources: dict[str, dict[str, object]],
) -> None:
    expected = combine_rows(baseline, additions)
    validate_rows(expected, sources)
    validate_rows(actual, sources)
    if actual != expected:
        raise ValueError(
            "combined database differs from immutable Day 1 rows + Day 2 additions "
            "(including row order and inherited metadata); run --build after review"
        )


def check_baseline(root: Path) -> None:
    """Compare bytes with the accepted commit; do not trust the working CSV alone."""
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"{BASELINE_COMMIT}:{BASELINE_PATH}"],
        capture_output=True, check=False,
    )
    if result.returncode:
        raise ValueError(f"cannot read accepted baseline commit {BASELINE_COMMIT}")
    if (root / BASELINE_PATH).read_bytes() != result.stdout:
        raise ValueError(f"Day 1 baseline changed from accepted commit {BASELINE_COMMIT}")


def run(root: Path, *, build: bool = False) -> tuple[int, int, int]:
    check_baseline(root)
    baseline = read_csv(root / BASELINE_PATH, BASE_COLUMNS)
    additions = read_csv(root / ADDITIONS_PATH, COLUMNS)
    with (root / SOURCES_PATH).open(encoding="utf-8") as stream:
        sources = source_index(json.load(stream))
    if any(row["day_added"] != "2" for row in additions):
        raise ValueError("every additions record must have day_added=2")
    expected = combine_rows(baseline, additions)
    validate_rows(expected, sources)
    target = root / COMBINED_PATH
    if build:
        # Complete validation before opening the generated output for writing.
        output = io.StringIO(newline="")
        writer = csv.DictWriter(output, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(expected)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output.getvalue(), encoding="utf-8", newline="")
    validate_combined(read_csv(target, COLUMNS), baseline, additions, sources)
    return len(baseline), len(additions), len(expected)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--build", action="store_true", help="rebuild combined CSV from validated inputs")
    action.add_argument("--check", action="store_true", help="check existing combined CSV (default)")
    args = parser.parse_args(argv)
    try:
        baseline, added, total = run(ROOT, build=args.build)
    except (OSError, ValueError, csv.Error) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Day 2 data integrity: PASS ({baseline} preserved + {added} added = {total} records)")
    print("Checks verify data structure, provenance constraints and preservation; they do not guarantee scientific accuracy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
