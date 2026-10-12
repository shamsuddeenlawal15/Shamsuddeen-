from pathlib import Path
import importlib.util
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_day1_data.py"
SPEC = importlib.util.spec_from_file_location("check_day1_data", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Day1DataTests(unittest.TestCase):
    def write_csv(self, header, row):
        temp = tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", delete=False)
        self.addCleanup(Path(temp.name).unlink)
        temp.write(",".join(header) + "\n")
        temp.write(",".join(row) + "\n")
        temp.close()
        return Path(temp.name)

    def test_repository_data_passes(self):
        MODULE.validate_parameters(MODULE.read_rows(MODULE.PARAMETERS, MODULE.PARAMETER_COLUMNS))
        MODULE.validate_results(MODULE.read_rows(MODULE.VALIDATION, MODULE.VALIDATION_COLUMNS))
        MODULE.validate_equations(MODULE.read_rows(MODULE.EQUATIONS, MODULE.EQUATION_COLUMNS))

    def test_published_parameter_requires_page(self):
        row = [""] * len(MODULE.PARAMETER_COLUMNS)
        for key, value in {
            "parameter_id": "X", "test_id": "F7-1", "category": "geometry",
            "parameter_name": "example", "value_text": "1", "unit": "m",
            "source_document": "paper", "source_locator": "Table X",
            "provenance_type": "published", "verification_status": "unverified",
            "notes": "test",
        }.items():
            row[MODULE.PARAMETER_COLUMNS.index(key)] = value
        path = self.write_csv(MODULE.PARAMETER_COLUMNS, row)
        with self.assertRaisesRegex(ValueError, "source_page"):
            MODULE.validate_parameters(MODULE.read_rows(path, MODULE.PARAMETER_COLUMNS))

    def test_verified_result_requires_source_fields(self):
        row = [""] * len(MODULE.VALIDATION_COLUMNS)
        for key, value in {
            "validation_id": "X", "test_id": "F7-2", "observable": "example",
            "model_code": "MELCOR", "verification_status": "verified",
            "notes": "test",
        }.items():
            row[MODULE.VALIDATION_COLUMNS.index(key)] = value
        path = self.write_csv(MODULE.VALIDATION_COLUMNS, row)
        with self.assertRaisesRegex(ValueError, "verified row missing"):
            MODULE.validate_results(MODULE.read_rows(path, MODULE.VALIDATION_COLUMNS))


if __name__ == "__main__":
    unittest.main()
