"""Regression tests for provenance constraints, independent of scientific claims."""

import copy
import csv
import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "day2_data.py"
SPEC = importlib.util.spec_from_file_location("day2_data", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Day2DataTests(unittest.TestCase):
    def setUp(self):
        base = {column: "" for column in MODULE.BASE_COLUMNS}
        base.update({
            "parameter_id": "OLD-1", "test_id": "F7-1", "category": "geometry",
            "parameter_name": "test fixture", "value_text": "2", "value_numeric": "2",
            "unit": "m", "source_document": "original", "source_page": "2",
            "source_locator": "Section 2", "provenance_type": "published",
            "verification_status": "verified",
        })
        self.baseline = [base]
        extra = {column: "" for column in MODULE.COLUMNS}
        extra.update(base)
        extra.update({
            "parameter_id": "NEW-1", "day_added": "2", "source_id": "S2021",
            "source_access_status": "read", "evidence_kind": "published_statement",
            "verification_basis": "Direct page transcription",
        })
        self.additions = [extra]
        self.sources = MODULE.source_index([
            {"source_id": "L2023", "access_status": "read"},
            {"source_id": "S2021", "access_status": "read"},
            {"source_id": "F1998", "access_status": "not_retrieved"},
        ])

    def combined(self):
        return MODULE.combine_rows(self.baseline, self.additions)

    def write_records(self, records):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "fixture.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            csv.writer(stream).writerows(records)
        return path

    def test_valid_records_preserve_inputs(self):
        before = copy.deepcopy((self.baseline, self.additions))
        rows = self.combined()
        MODULE.validate_combined(rows, self.baseline, self.additions, self.sources)
        self.assertEqual((self.baseline, self.additions), before)
        self.assertEqual({key: rows[0][key] for key in MODULE.BASE_COLUMNS}, self.baseline[0])

    def test_csv_rejects_short_long_and_blank_records(self):
        for record in [["x"] * 20, ["x"] * 22, []]:
            with self.subTest(width=len(record)):
                path = self.write_records([MODULE.COLUMNS, record])
                with self.assertRaisesRegex(ValueError, "expected 21 fields"):
                    MODULE.read_csv(path, MODULE.COLUMNS)

    def test_csv_rejects_duplicate_or_reordered_header(self):
        for columns in [MODULE.COLUMNS[:-1] + [MODULE.COLUMNS[0]], list(reversed(MODULE.COLUMNS))]:
            path = self.write_records([columns])
            with self.assertRaisesRegex(ValueError, "exact 21-column header"):
                MODULE.read_csv(path, MODULE.COLUMNS)

    def test_tampered_legacy_value_rejected(self):
        rows = self.combined()
        rows[0]["value_numeric"] = "99"
        with self.assertRaisesRegex(ValueError, "immutable Day 1"):
            MODULE.validate_combined(rows, self.baseline, self.additions, self.sources)

    def test_tampered_legacy_metadata_rejected(self):
        rows = self.combined()
        rows[0]["verification_basis"] = "Changed"
        with self.assertRaisesRegex(ValueError, "inherited Day 1 metadata"):
            MODULE.validate_combined(rows, self.baseline, self.additions, self.sources)

    def test_unread_source_cannot_support_numeric_value(self):
        row = self.additions[0]
        row.update({"source_id": "F1998", "source_access_status": "not_retrieved"})
        with self.assertRaisesRegex(ValueError, "numeric value requires a read source"):
            MODULE.validate_rows(self.combined(), self.sources)

    def test_unread_source_cannot_support_verified_interpretation(self):
        self.additions[0].update({
            "source_id": "F1998", "source_access_status": "not_retrieved",
            "value_numeric": "", "provenance_type": "derived",
            "evidence_kind": "derived_interpretation", "derivation": "Interpretation",
        })
        with self.assertRaisesRegex(ValueError, "verified/published record requires a read source"):
            MODULE.validate_rows(self.combined(), self.sources)

    def test_missing_citation_rejected(self):
        for field in ["source_document", "source_page", "source_locator", "verification_basis"]:
            with self.subTest(field=field):
                rows = self.combined()
                rows[-1][field] = ""
                with self.assertRaisesRegex(ValueError, field):
                    MODULE.validate_rows(rows, self.sources)

    def test_nonfinite_and_nonnumeric_values_rejected(self):
        for value in ["NaN", "inf", "-Infinity", "1e999", "unknown"]:
            with self.subTest(value=value):
                rows = self.combined()
                rows[-1]["value_numeric"] = value
                with self.assertRaisesRegex(ValueError, "finite number"):
                    MODULE.validate_rows(rows, self.sources)

    def test_missing_records_cannot_have_numeric_values(self):
        self.additions[0].update({"provenance_type": "missing", "evidence_kind": "missing_from_article"})
        with self.assertRaisesRegex(ValueError, "missing record must have empty"):
            MODULE.validate_rows(self.combined(), self.sources)

    def test_missing_blocked_record_may_have_unavailable_source(self):
        self.additions[0].update({
            "value_numeric": "", "value_text": "not retrieved",
            "provenance_type": "missing", "verification_status": "blocked",
            "source_id": "F1998", "source_access_status": "not_retrieved",
            "evidence_kind": "source_unavailable", "source_page": "",
            "source_locator": "", "verification_basis": "",
        })
        MODULE.validate_rows(self.combined(), self.sources)
        self.additions[0]["verification_status"] = "unverified"
        with self.assertRaisesRegex(ValueError, "source_unavailable requires"):
            MODULE.validate_rows(self.combined(), self.sources)

    def test_derived_record_requires_derivation_and_kind(self):
        self.additions[0].update({"provenance_type": "derived", "evidence_kind": "derived_interpretation"})
        with self.assertRaisesRegex(ValueError, "requires derivation"):
            MODULE.validate_rows(self.combined(), self.sources)
        self.additions[0]["derivation"] = "Two times source value"
        self.additions[0]["evidence_kind"] = "published_statement"
        with self.assertRaisesRegex(ValueError, "requires derived_interpretation"):
            MODULE.validate_rows(self.combined(), self.sources)

    def test_duplicate_identifiers_rejected(self):
        self.additions[0]["parameter_id"] = "OLD-1"
        with self.assertRaisesRegex(ValueError, "duplicate"):
            MODULE.validate_rows(self.combined(), self.sources)

    def test_unknown_source_and_access_mismatch_rejected(self):
        rows = self.combined()
        rows[-1]["source_id"] = "UNKNOWN"
        with self.assertRaisesRegex(ValueError, "unknown source_id"):
            MODULE.validate_rows(rows, self.sources)
        rows = self.combined()
        rows[-1]["source_access_status"] = "not_retrieved"
        with self.assertRaisesRegex(ValueError, "disagrees"):
            MODULE.validate_rows(rows, self.sources)

    def test_duplicate_source_identifiers_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate source_id"):
            MODULE.source_index([
                {"source_id": "L2023", "access_status": "read"},
                {"source_id": "L2023", "access_status": "read"},
            ])

    def test_missing_or_self_supersedes_reference_rejected(self):
        for value in ["UNKNOWN", "NEW-1"]:
            with self.subTest(value=value):
                rows = self.combined()
                rows[-1]["supersedes"] = value
                with self.assertRaisesRegex(ValueError, "supersedes must name"):
                    MODULE.validate_rows(rows, self.sources)

    def test_output_reordering_is_detected(self):
        rows = list(reversed(self.combined()))
        with self.assertRaisesRegex(ValueError, "including row order"):
            MODULE.validate_combined(rows, self.baseline, self.additions, self.sources)


class RepositoryDataTests(unittest.TestCase):
    def test_accepted_day1_bytes_are_preserved(self):
        MODULE.check_baseline(MODULE.ROOT)

    def test_repository_combined_database_matches_inputs(self):
        baseline, added, total = MODULE.run(MODULE.ROOT)
        self.assertEqual(baseline, 57)
        self.assertGreater(added, 0)
        self.assertEqual(total, baseline + added)


if __name__ == "__main__":
    unittest.main()
