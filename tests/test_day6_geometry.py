"""Document-data integrity only: no CAD generation or solver execution."""
import copy
import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read_table(name):
    with (ROOT / 'data/day-06' / name).open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    if not rows or any(None in r or any(v is None for v in r.values()) for r in rows):
        raise ValueError('Empty or malformed CSV')
    return rows


def validate_geometry(rows):
    ids = [r['id'] for r in rows]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate geometry ID')
    for r in rows:
        status = r['verification_status']
        if status not in {'published_apparatus', 'published_numerical', 'missing', 'proposed'}:
            raise ValueError('Unknown evidence status')
        if not all(r[k] for k in ('component', 'dimension', 'coordinate_system',
                                 'original_source', 'page_or_figure',
                                 'remaining_uncertainty', 'initial_cfd_inclusion')):
            raise ValueError('Incomplete provenance or scope')
        if status == 'missing' and r['value']:
            raise ValueError('Missing quantity cannot contain a guessed value')
        if status.startswith('published'):
            if '10.1016/j.nucengdes.2023.112285' not in r['original_source']:
                raise ValueError('Published value requires inspected source')
            if not r['page_or_figure'].startswith('p.') or not r['unit']:
                raise ValueError('Published value requires page and units')
            float(r['value'])
        if status == 'published_numerical' and r['initial_cfd_inclusion'] != 'comparison_only':
            raise ValueError('Code heat structures cannot silently become apparatus CAD')


class Day6GeometryTests(unittest.TestCase):
    def setUp(self):
        self.rows = read_table('F7_Geometry_Parameter_Register.csv')
        self.by_id = {r['id']: r for r in self.rows}

    def test_register_integrity_and_component_coverage(self):
        validate_geometry(self.rows)
        required = {'Vessel cylindrical body', 'Vessel top head', 'Vessel bottom region',
                    'Sodium discharge nozzle', 'Sodium inlet pipe', 'Catch pan',
                    'Catch-pan supporting structure', 'First insulation layer',
                    'Second insulation layer', 'Air inlet', 'Exhaust outlet',
                    'Gas volume', 'Sodium pool region', 'Relevant instrument locations'}
        self.assertTrue(required <= {r['component'] for r in self.rows})

    def test_approved_values_and_qualifiers(self):
        expected = {'G001': '2.2', 'G002': '1.3', 'G003': '3.0', 'G004': '1.0',
                    'G005': '6', 'G006': '50', 'G007': '50', 'G008': '0.1',
                    'G009': '1.5', 'G010': '0.28', 'G011': '0.30',
                    'G012': '3.3', 'G013': '1500', 'G014': '3.0'}
        for key, value in expected.items():
            self.assertEqual(self.by_id[key]['value'], value)
        for key in ('G001', 'G002', 'G014'):
            self.assertIn('approximately', self.by_id[key]['qualifier'])
        self.assertEqual(self.by_id['G012']['qualifier'], 'average')

    def test_nozzle_cases_and_pool_observables_remain_separate(self):
        self.assertNotEqual(self.by_id['G008']['value'], self.by_id['G009']['value'])
        for key in ('G010', 'G011'):
            self.assertEqual(self.by_id[key]['role'], 'validation_observable')
            self.assertNotEqual(self.by_id[key]['value'], self.by_id['G004']['value'])

    def test_missing_guess_is_rejected(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r['verification_status'] == 'missing')['value'] = '0.01'
        with self.assertRaises(ValueError):
            validate_geometry(rows)

    def test_numerical_promotion_is_rejected(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r['verification_status'] == 'published_numerical')[
            'initial_cfd_inclusion'] = 'required_pending_geometry'
        with self.assertRaises(ValueError):
            validate_geometry(rows)

    def test_missing_provenance_and_duplicate_id_are_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['page_or_figure'] = ''
        with self.assertRaises(ValueError):
            validate_geometry(rows)
        with self.assertRaises(ValueError):
            validate_geometry(self.rows + [self.rows[0]])

    def test_regions_are_proposals_with_open_dependencies(self):
        rows = read_table('F7_Regions_and_Boundaries.csv')
        self.assertEqual(len(rows), len({r['id'] for r in rows}))
        for r in rows:
            self.assertEqual(r['verification_status'], 'proposed_mapping')
            self.assertTrue(r['unresolved'])
            self.assertTrue(r['source_basis'].startswith('L2023 p.'))
        pan = next(r for r in rows if r['region_or_boundary'] == 'F7_Pan')
        self.assertEqual(pan['material'], 'Carbon steel')


if __name__ == '__main__':
    unittest.main()
