"""Synthetic unit fixtures only; no experimental measurements or CAD outputs."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import csv

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/F7_Geometry_Consistency_Checks.py'
spec = importlib.util.spec_from_file_location('geometry7', SCRIPT)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


class Day7Tests(unittest.TestCase):
    def setUp(self):
        self.params = g.load_parameters()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        raw = b'SYNTHETIC UNIT TEST - NOT CAD EVIDENCE'
        (self.base / 'fixture.txt').write_bytes(raw)
        self.data = {
            'schema_version': 1, 'case': 'F7-1', 'evidence_kind': 'synthetic_test',
            'solver_build': 'test_fixture', 'operator': 'unit_test',
            'export_date': 'test_only', 'coordinate_frame': 'F7_PROJECT_CARTESIAN',
            'measurement_scope': 'vessel_envelope_excluding_external_pipes',
            'artifacts': [{'path': 'fixture.txt', 'sha256': hashlib.sha256(raw).hexdigest()}],
            'bounds_m': {'x': [-0.65, 0.65], 'y': [-0.65, 0.65], 'z': [-0.2, 2.0]},
            'measurements': {'pan_area': {'value': 1.1, 'unit': 'm2'},
                             'nozzle_height': {'value': 0.1, 'unit': 'm'}},
            'topology': {'closed_shell_open_edges': 2, 'overlapping_solid_pairs': 1,
                         'fluid_components': 2},
            'names': ['F7_Gas', 'F7_Gas', 'unexpected_name']}

    def run_audit(self, data=None):
        return g.audit(self.data if data is None else data, self.params, self.base)

    def test_analytical_values_are_not_cad(self):
        result = g.analytical(self.params)
        self.assertAlmostEqual(result['ideal_cylinder_volume_m3'], 2.920110371511713)
        self.assertAlmostEqual(result['insulation_total_thickness_m'], 0.1)
        self.assertAlmostEqual(result['nozzle_height_difference_m'], 1.4)
        self.assertLess(result['pan_minus_cylinder_cross_section_m2'], 0)
        self.assertIn('not_actual_CAD', result['status'])

    def test_unit_conversion_and_rejected_units(self):
        self.assertAlmostEqual(g.source_value(self.params, 'V005', 'm'), 0.006)
        with self.assertRaises(ValueError):
            g.source_value(self.params, 'V005', 'm2')
        self.data['measurements']['nozzle_height']['unit'] = 'mm'
        with self.assertRaises(ValueError):
            self.run_audit()

    def test_dimensions_topology_and_names_report_defects(self):
        result = self.run_audit()
        self.assertAlmostEqual(result['comparisons']['pan_area']['difference'], 0.1)
        self.assertAlmostEqual(result['comparisons']['vessel_span_z']['difference'], 0)
        self.assertTrue(result['topology']['closed_shell_open_edges']['needs_review'])
        self.assertTrue(result['topology']['overlapping_solid_pairs']['needs_review'])
        self.assertTrue(result['topology']['fluid_components']['needs_review'])
        self.assertEqual(result['naming']['duplicates'], ['F7_Gas'])
        self.assertEqual(result['naming']['unregistered'], ['unexpected_name'])
        self.assertIn('F7_Pan', result['naming']['missing_core'])
        self.assertIn('not_CAD_approval', result['status'])
        self.assertEqual(result['evidence_kind'], 'synthetic_test')

    def test_case_specific_height(self):
        self.data['case'] = 'F7-2'
        self.assertAlmostEqual(self.run_audit()['comparisons']['nozzle_height']['difference'], -1.4)

    def test_absent_evidence_stays_pending(self):
        self.data.pop('bounds_m')
        self.data.pop('measurements')
        self.data.pop('topology')
        self.data.pop('names')
        result = self.run_audit()
        self.assertEqual(result['comparisons'], {})
        self.assertIn('gas_volume', result['pending'])
        self.assertIn('overlapping_solid_pairs', result['pending'])

    def test_nonfinite_boolean_negative_and_zero_measurements_rejected(self):
        for value in (float('nan'), float('inf'), True, -1, 0):
            with self.subTest(value=value):
                self.data['measurements']['pan_area']['value'] = value
                with self.assertRaises(ValueError):
                    self.run_audit()

    def test_invalid_bounds_and_scope_rejected(self):
        self.data['bounds_m']['x'] = [1, -1]
        with self.assertRaises(ValueError):
            self.run_audit()
        self.data['bounds_m']['x'] = [-1, 1]
        self.data['measurement_scope'] = 'whole assembly with ducts'
        with self.assertRaises(ValueError):
            self.run_audit()

    def test_invalid_counts_unknown_metrics_and_case_rejected(self):
        for field, value in [('topology', {'fluid_components': True}),
                             ('measurements', {'unknown': {'value': 1}}),
                             ('case', 'H1-A')]:
            data = copy.deepcopy(self.data)
            data[field] = value
            with self.assertRaises(ValueError):
                self.run_audit(data)

    def test_hash_mismatch_and_absent_artifact_rejected(self):
        self.data['artifacts'][0]['sha256'] = '0' * 64
        with self.assertRaises(ValueError):
            self.run_audit()
        self.data['artifacts'][0]['path'] = 'missing.txt'
        with self.assertRaises(OSError):
            self.run_audit()

    def test_cli_modes_and_duplicate_json_keys(self):
        good = subprocess.run([sys.executable, str(SCRIPT), 'analytic'], capture_output=True, text=True)
        self.assertEqual(good.returncode, 0)
        self.assertIn('not_actual_CAD', json.loads(good.stdout)['status'])
        path = self.base / 'input.json'
        path.write_text(json.dumps(self.data))
        audit = subprocess.run([sys.executable, str(SCRIPT), 'audit', '--evidence', str(path)],
                               capture_output=True, text=True)
        self.assertEqual(audit.returncode, 0, audit.stderr)
        path.write_text('{"case":"F7-1","case":"F7-2"}')
        bad = subprocess.run([sys.executable, str(SCRIPT), 'audit', '--evidence', str(path)],
                             capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertEqual(bad.stdout, '')
        self.assertIn('Duplicate JSON key', bad.stderr)

    def test_source_rows_preserve_day6_values_and_scope(self):
        with (ROOT / 'data/day-06/F7_Geometry_Parameter_Register.csv').open(newline='') as f:
            old = {r['id']: r for r in csv.DictReader(f)}
        for r in self.params.values():
            self.assertEqual(r['value'], old[r['day6_id']]['value'])
            self.assertEqual(r['unit'], old[r['day6_id']]['unit'])
        with (ROOT / 'data/day-07/F7_Parametric_CAD_Input_Register.csv').open(newline='') as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), len({(r['parameter'], r['configuration']) for r in rows}))
        for r in rows:
            if r['status'] == 'unresolved':
                self.assertEqual(r['value'], '')
            if r['parameter'] == 'pool_final_area_observed':
                self.assertEqual(r['status'], 'observable_not_driver')

    def test_all_cad_values_trace_to_sources_and_interfaces_resolve(self):
        with (ROOT / 'data/day-07/F7_Parametric_CAD_Input_Register.csv').open(newline='') as f:
            rows = list(csv.DictReader(f))
        for r in rows:
            self.assertNotIn(None, r)
            if r['value']:
                self.assertAlmostEqual(float(r['value']),
                                       g.source_value(self.params, r['source_ids'], r['unit']))
            else:
                self.assertEqual(r['status'], 'unresolved')
                self.assertTrue(r['source_ids'].startswith('Day6:'))
        with g.NAMES.open(newline='') as f:
            names = list(csv.DictReader(f))
        self.assertEqual(len(names), len({r['name'] for r in names}))
        regions = {r['name'] for r in names if 'region' in r['entity_kind']}
        for r in names:
            self.assertEqual(r['status'], 'proposed_not_created')
            if r['entity_kind'] == 'interface':
                self.assertIn(r['side_a'], regions)
                self.assertIn(r['side_b'], regions)
                self.assertEqual(len(r['paired_surface_names'].split(';')), 2)

    def test_schema_and_metadata_must_not_be_placeholders(self):
        for key, value in [('schema_version', True), ('evidence_kind', 'unknown'),
                           ('solver_build', 'pending'), ('coordinate_frame', 'unmapped'),
                           ('artifacts', [])]:
            data = copy.deepcopy(self.data)
            data[key] = value
            with self.assertRaises(ValueError):
                self.run_audit(data)


if __name__ == '__main__':
    unittest.main()
