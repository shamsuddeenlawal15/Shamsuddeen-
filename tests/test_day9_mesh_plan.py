"""Planning-table arithmetic/integrity only; no generated mesh or CFD data."""
import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def table(name):
    with (ROOT / 'data/day-09' / name).open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    if not rows or any(None in r or any(v is None for v in r.values()) for r in rows):
        raise ValueError('Malformed planning table')
    return rows


class Day9MeshPlanTests(unittest.TestCase):
    def test_three_levels_and_scenario_arithmetic(self):
        rows = table('F7_Mesh_Level_Definition.csv')
        self.assertEqual([r['level'] for r in rows], ['coarse', 'medium', 'fine'])
        previous_high = 0
        for r in rows:
            low, high = int(r['target_cells_low']), int(r['target_cells_high'])
            self.assertGreater(low, previous_high)
            self.assertGreater(high, low)
            previous_high = high
            volume = float(r['reference_volume_m3'])
            self.assertEqual(volume, 3.0)
            self.assertAlmostEqual(float(r['equivalent_h_low_m']), (volume/high)**(1/3))
            self.assertAlmostEqual(float(r['equivalent_h_high_m']), (volume/low)**(1/3))
            self.assertAlmostEqual(float(r['scenario_ram_low_GB']), 2+low*4000/1e9)
            self.assertAlmostEqual(float(r['scenario_ram_high_GB']), 2+high*16000/1e9)

    def test_no_mesh_or_resource_observations_in_budget_table(self):
        for r in table('F7_Mesh_Level_Definition.csv'):
            self.assertEqual(r['status'], 'planning_scenario_not_mesh_controls')
            for key in ('actual_cells', 'measured_ram_GB', 'measured_runtime_s'):
                self.assertEqual(r[key], '')

    def test_all_domains_remain_blocked_and_ports_are_not_automatic_regions(self):
        rows = table('F7_Computational_Domain_Register.csv')
        self.assertEqual(len(rows), 9)
        self.assertEqual(len({r['id'] for r in rows}), len(rows))
        self.assertEqual(len({r['region_name'] for r in rows}), len(rows))
        for r in rows:
            self.assertEqual(r['included_in_current_mesh'], 'no')
            self.assertEqual(r['readiness'], 'blocked_geometry')
            self.assertEqual(r['evidence_file'], '')
            self.assertTrue(r['geometry_reference'])
            self.assertTrue(r['unresolved'])
            self.assertTrue(r['expected_interfaces'])
        by_name = {r['region_name']: r for r in rows}
        for name in ('AirInlet_Surface', 'Exhaust_Surface'):
            self.assertEqual(by_name[name]['entity_kind'], 'boundary_or_optional_duct')
        self.assertEqual(by_name['F7_Pool']['entity_kind'], 'conditional_surface_or_liquid')

    def test_cost_indices_are_cell_ratios_not_runtime_and_fine_cap_exceeded(self):
        rows = table('F7_Mesh_Level_Definition.csv')
        for r in rows:
            self.assertEqual(float(r['relative_cell_work_index']),
                             int(r['target_cells_low'])/int(rows[0]['target_cells_low']))
            self.assertEqual(float(r['relative_cell_work_index']),
                             int(r['target_cells_high'])/int(rows[0]['target_cells_high']))
        self.assertGreater(float(rows[-1]['scenario_ram_high_GB']), 20)
        self.assertEqual((20-2)*1e9/16000, 1125000)


if __name__ == '__main__':
    unittest.main()
