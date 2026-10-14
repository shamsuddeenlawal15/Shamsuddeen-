"""Physics framework integrity only; no model activation or physical calculation."""
import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def table(name):
    with (ROOT / 'data/day-10' / name).open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    if not rows or any(None in r or any(v is None for v in r.values()) for r in rows):
        raise ValueError('Malformed framework CSV')
    if len({r['id'] for r in rows}) != len(rows):
        raise ValueError('Duplicate framework ID')
    return rows


class Day10FrameworkTests(unittest.TestCase):
    def test_no_model_activated_or_availability_assumed(self):
        rows = table('F7_Physics_Continuum_Register.csv')
        self.assertEqual(len(rows), 15)
        self.assertEqual({r['stage'] for r in rows}, {'1', '2', '3'})
        for r in rows:
            self.assertEqual(r['activated_now'], 'no')
            self.assertEqual(r['status'], 'reserved_framework')
            self.assertEqual(r['starccm_2402_availability'], 'unverified_exact_build')
            self.assertEqual(r['license_requirement'], 'pending_local_entitlement_check')
            self.assertEqual(r['local_evidence'], '')
            self.assertTrue(r['purpose'])
            self.assertTrue(r['selection_reason_or_gate'])

    def test_material_identity_does_not_supply_property_values(self):
        rows = table('F7_Material_Property_Register.csv')
        self.assertEqual(len(rows), 27)
        required = {'Air', 'Vessel_stainless_steel', 'Pan_carbon_steel',
                    'Insulation_layer_1', 'Insulation_layer_2'}
        self.assertTrue(required <= {r['material'] for r in rows})
        self.assertEqual(len(rows), len({(r['material'], r['property']) for r in rows}))
        for r in rows:
            self.assertEqual(r['value'], '')
            self.assertEqual(r['correlation_or_evidence'], '')
            self.assertEqual(r['status'], 'pending')
            self.assertEqual(r['confidence'], 'identity_only_property_unverified')
            self.assertTrue(r['unit'])
            self.assertTrue(r['material_identity_source'].startswith('L2023 p'))
            self.assertIn('pending', r['property_source'])

    def test_region_aliases_and_contact_kinds_remain_consistent(self):
        rows = table('F7_Region_Interface_Definition.csv')
        names = {r['name'] for r in rows}
        self.assertEqual(len(names), len(rows))
        regions = {r['name'] for r in rows if 'region' in r['entity_kind']}
        continuum = {r['continuum_or_requirement'] for r in table('F7_Physics_Continuum_Register.csv')}
        for r in rows:
            self.assertEqual(r['assigned_now'], 'no')
            self.assertEqual(r['local_evidence'], '')
            self.assertEqual(r['status'], 'pending_geometry_and_model_review')
            self.assertIn(r['proposed_continuum'], continuum | {'none'})
            if 'region' not in r['entity_kind']:
                self.assertIn(r['side_a_or_day9_name'], regions)
                if r['side_b']:
                    self.assertIn(r['side_b'], regions)
        by_name = {r['name']: r for r in rows}
        self.assertEqual(by_name['Wall_Pan']['entity_kind'], 'conditional_solid_contact')
        self.assertEqual(by_name['Insulation_External']['entity_kind'], 'external_boundary')
        self.assertEqual(by_name['Insulation_External']['side_b'], '')
        self.assertNotEqual(by_name['Inlet_Region']['side_a_or_day9_name'],
                            by_name['Sodium_Feed_Region']['side_a_or_day9_name'])

    def test_monitors_have_no_results_and_reactions_are_later_stages(self):
        rows = table('F7_Monitor_and_Report_Definition.csv')
        self.assertEqual(len(rows), 16)
        for r in rows:
            self.assertEqual(r['status'], 'reserved_not_created')
            self.assertEqual(r['observed_value'], '')
            self.assertEqual(r['evidence_file'], '')
            self.assertTrue(r['definition'])
            self.assertTrue(r['sampling'])
            self.assertTrue(r['unit'])
            if r['id'].startswith('X'):
                self.assertEqual(r['stage'], '2')
            if r['id'].startswith('A'):
                self.assertEqual(r['stage'], '3')


if __name__ == '__main__':
    unittest.main()
