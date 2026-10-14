"""Integrity tests for pending construction records, never CAD validation."""
import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with (ROOT / path).open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    if not rows or any(None in r or any(v is None for v in r.values()) for r in rows):
        raise ValueError('Malformed CSV record')
    return rows


class Day8RegisterTests(unittest.TestCase):
    def setUp(self):
        self.components = read_csv('data/day-08/F7_CAD_Component_Register.csv')
        self.audit = read_csv('data/day-08/F7_CAD_Geometry_Audit.csv')

    def test_component_hierarchy_and_source_mapping(self):
        names = {r['name'] for r in self.components}
        self.assertEqual(len(names), len(self.components))
        self.assertEqual(len({r['id'] for r in self.components}), len(self.components))
        old_names = {r['name'] for r in read_csv(
            'data/day-07/F7_Regions_Interfaces_and_Surface_Names.csv')}
        for r in self.components:
            if r['parent']:
                self.assertIn(r['parent'], names)
            for ref in filter(None, r['day7_reference'].split(';')):
                self.assertIn(ref, old_names)
            self.assertTrue(r['source_or_assumption'])
            self.assertTrue(r['construction_gate'])
        for name in ('Vessel', 'Catch_Pan', 'Insulation_Layer_1', 'Insulation_Layer_2',
                     'Sodium_Inlet', 'Air_Inlet', 'Exhaust', 'Instrumentation'):
            row = next(r for r in self.components if r['name'] == name)
            self.assertEqual(row['parent'], '01_Experimental_Apparatus')

    def test_no_fabricated_execution_or_observations(self):
        for r in self.components:
            self.assertEqual(r['execution_status'], 'not_created')
            self.assertEqual(r['evidence_file'], '')
        for r in self.audit:
            self.assertEqual(r['cad_status'], 'pending')
            for column in ('cad_value', 'difference', 'evidence_file'):
                self.assertEqual(r[column], '')

    def test_source_values_units_and_unknowns_are_preserved(self):
        old = read_csv('data/day-07/F7_Parametric_CAD_Input_Register.csv')
        by_key = {(r['dimension'], r['configuration']): r for r in self.audit}
        self.assertEqual(len(by_key), len(old))
        for r in old:
            new = by_key[(r['parameter'], r['configuration'])]
            for column in ('value', 'unit', 'status', 'source_ids'):
                self.assertEqual(new[column], r[column])
            if r['status'] == 'unresolved':
                self.assertEqual(new['value'], '')
            if r['parameter'] == 'pool_final_area_observed':
                self.assertEqual(new['status'], 'observable_not_driver')

    def test_placeholders_cases_and_provisional_geometry_are_distinct(self):
        by_name = {r['name']: r for r in self.components}
        for name in ('Air_Inlet_Provisional', 'Exhaust_Provisional'):
            self.assertEqual(by_name[name]['entity_kind'], 'empty_surface_slot')
        for number in (1, 2):
            row = by_name[f'Nozzle_F7_{number}_Position']
            self.assertEqual(row['entity_kind'], 'height_reference')
            self.assertEqual(row['configuration'], f'F7_{number}')
        for name in ('Vessel_Top_Approximation', 'Vessel_Bottom_Approximation'):
            self.assertEqual(by_name[name]['configuration'], 'P0')
            self.assertEqual(by_name[name]['parent'], 'F7_P0_Provisional_Envelope.sim')


if __name__ == '__main__':
    unittest.main()
