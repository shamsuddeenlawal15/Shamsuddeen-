"""Synthetic software fixtures only. No fixture is STAR-CCM+ evidence."""
import contextlib
import csv
import importlib.util
import io
import json
import math
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "H1_Postprocessing.py"
SPEC = importlib.util.spec_from_file_location("h1", SCRIPT)
h1 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(h1)


class H1Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def fixture(self, name="fixture", case="H1-B", cells=2, dt=1.0, error=0.0):
        directory = self.root / name
        directory.mkdir()
        meta = {
            "schema_version": 1, "run_id": name, "case": case,
            "run_status": "completed", "evidence_kind": "synthetic_test",
            "solver_build": "TEST_FIXTURE_NOT_SOLVER", "os": "TEST_FIXTURE",
            "processes": 4, "cells": cells, "dt_s": dt, "end_time_s": 2.0,
            "physics_id": "synthetic-fixture", "spatial_scheme": "fixture",
            "temporal_scheme": "fixture", "iteration_policy": "fixture",
            "mesh_family": "fixture", "mesh_id": f"fixture-{cells}",
            "geometry_id": "cube", "initialization": "analytical-cell-average",
            "reference_sampling": "cell_average", "mesh_geometry": "orthogonal_rectangular",
            "parameters": {"L_m": .1, "rho_kg_m3": 1., "c_J_kgK": 1000.,
                           "k_W_mK": .1, "mu_Pa_s": .001, "T0_K": 300.,
                           "q_vol_W_m3": 100. if case == "H1-B" else 0.,
                           "lid_speed_m_s": .1 if case == "H1-D" else 0.},
        }
        self.write_meta(directory, meta)
        monitors, fields = [], []
        for step in range(round(2/dt)+1):
            t = step*dt
            energy = .1*t if case == "H1-B" else 0.
            monitors.append([t, .001, 0., 0., energy if case != "H1-D" else "",
                             0. if case != "H1-D" else "",
                             .1 if case == "H1-B" else ("" if case == "H1-D" else 0.),
                             0., 0., 0.])
            if step not in (0, round(2/dt)) or case == "H1-D":
                continue
            for i in range(cells):
                a, b = i*.1/cells, (i+1)*.1/cells
                if case == "H1-C":
                    # Independent expression; no call to production reference function.
                    avg = cells*(math.sin(math.pi*(i+1)/cells)-math.sin(math.pi*i/cells))/math.pi
                    temp = 300 + avg*math.exp(-.01*math.pi**2*t)
                else:
                    temp = 300 + (.1*t if case == "H1-B" else 0.)
                fields.append([t, str(i), a, b, .001/cells, temp+error])
        self.write_rows(directory / "monitors.csv", h1.MONITOR_COLUMNS, monitors)
        if fields:
            self.write_rows(directory / "fields.csv", h1.FIELD_COLUMNS, fields)
        return directory

    def write_meta(self, directory, meta):
        (directory / "manifest.json").write_text(json.dumps(meta), encoding="utf-8")

    def write_rows(self, path, columns, rows):
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(columns)
            writer.writerows(rows)

    def mutate_csv(self, path, columns, mutate):
        rows = h1.read_csv(path, columns)
        mutate(rows)
        self.write_rows(path, columns, [[row[key] for key in columns] for row in rows])

    def test_uniform_and_heating_analytical_values(self):
        self.assertEqual(h1.analytical_temperature("H1-A", 10, 0, .1), 300)
        self.assertEqual(h1.analytical_temperature("H1-B", 10, 0, .1), 301)

    def test_cosine_cell_average_and_decay(self):
        self.assertAlmostEqual(h1.analytical_temperature("H1-C", 0, 0, .05), 300+2/math.pi)
        self.assertAlmostEqual(h1.analytical_temperature("H1-C", 10, 0, .05),
                               300+(2/math.pi)*math.exp(-.1*math.pi**2))
        self.assertAlmostEqual(h1.analytical_temperature("H1-C", 3, 0, .1), 300)
        self.assertAlmostEqual(h1.analytical_temperature("H1-C", 0, 0, .05, "cell_center"),
                               300+math.cos(math.pi/4))

    def test_irregular_time_trapezoid(self):
        self.assertEqual(h1.trapezoids([0, 1, 3], [0, 2, 6]), [0, 1, 9])
        with self.assertRaises(ValueError):
            h1.trapezoids([0, 0], [1, 1])

    def test_heating_end_to_end_and_cli(self):
        directory = self.fixture()
        report = h1.analyze_run(directory)
        self.assertAlmostEqual(report["balances"]["energy_balance"]["max_error_J"], 0)
        self.assertLess(report["analytical_errors"][-1]["L2_K"], 1e-12)
        self.assertLess(abs(report["analytical_errors"][-1]["field_minus_monitor_energy_J"]), 1e-12)
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(h1.main(["run", str(directory)]), 0)
        self.assertEqual(json.loads(out.getvalue())["manifest"]["evidence_kind"], "synthetic_test")

    def test_zero_input_has_no_relative_energy_error(self):
        report = h1.analyze_run(self.fixture(case="H1-A"))
        self.assertIsNone(report["balances"]["energy_balance"]["relative_final_error"])

    def test_mass_outward_sign_and_thermal_sign(self):
        directory = self.fixture()
        def modify(rows):
            for row in rows:
                t = float(row["time_s"])
                row.update(mass_kg=str(.001-1e-5*t), mass_out_kg_s="0.00001",
                           absolute_wall_mass_flux_kg_s="0.00001",
                           heat_in_W="0.02", energy_J=str(.12*t))
        self.mutate_csv(directory/"monitors.csv", h1.MONITOR_COLUMNS, modify)
        report = h1.analyze_run(directory)
        self.assertLess(report["balances"]["max_mass_balance_error_kg"], 1e-16)
        self.assertLess(report["balances"]["energy_balance"]["max_error_J"], 1e-14)
        self.assertGreater(report["balances"]["max_absolute_wall_mass_flux_kg_s"], 0)
        # Balance can close with wrong fields; independent cross-check still detects it.
        self.assertAlmostEqual(report["analytical_errors"][-1]["field_minus_monitor_energy_J"], -.04)

    def test_wrong_source_and_nonzero_energy_defect_detected(self):
        directory = self.fixture()
        self.mutate_csv(directory/"monitors.csv", h1.MONITOR_COLUMNS,
                        lambda rows: rows[-1].update(source_W="0.3", energy_J="0.7"))
        energy = h1.analyze_run(directory)["balances"]["energy_balance"]
        self.assertAlmostEqual(energy["max_source_power_deviation_W"], .2)
        self.assertAlmostEqual(energy["final_error_J"], .4)

    def test_weighted_norms_detect_known_offsets(self):
        report = h1.analyze_run(self.fixture(case="H1-C", error=.25))
        for metric in ("L1_K", "L2_K", "Linf_K"):
            self.assertAlmostEqual(report["analytical_errors"][-1][metric], .25)

    def test_lid_skips_thermal_accuracy(self):
        directory = self.fixture(case="H1-D")
        report = h1.analyze_run(directory)
        self.assertIsNone(report["analytical_errors"])
        self.assertIsNone(report["balances"]["energy_balance"])
        self.mutate_csv(directory/"monitors.csv", h1.MONITOR_COLUMNS,
                        lambda rows: rows[0].update(energy_J="0"))
        with self.assertRaisesRegex(ValueError, "thermal columns"):
            h1.analyze_run(directory)

    def test_unequal_volume_error_weights(self):
        directory = self.fixture(case="H1-A")
        def modify(rows):
            for row in rows:
                if row["cell_id"] == "0":
                    row.update(x_min_m="0", x_max_m="0.025", volume_m3="0.00025", temperature_K="301")
                else:
                    row.update(x_min_m="0.025", x_max_m="0.1", volume_m3="0.00075", temperature_K="303")
        self.mutate_csv(directory/"fields.csv", h1.FIELD_COLUMNS, modify)
        errors = h1.analyze_run(directory)["analytical_errors"][-1]
        self.assertAlmostEqual(errors["L1_K"], 2.5)
        self.assertAlmostEqual(errors["L2_K"], math.sqrt(7))
        self.assertEqual(errors["Linf_K"], 3)

    def test_unknown_build_and_wrong_properties_rejected(self):
        directory = self.fixture()
        meta = json.loads((directory/"manifest.json").read_text())
        meta["solver_build"] = "unknown"
        self.write_meta(directory, meta)
        with self.assertRaisesRegex(ValueError, "unresolved"):
            h1.analyze_run(directory)
        meta["solver_build"] = "TEST_FIXTURE"
        meta["parameters"]["rho_kg_m3"] = 2
        self.write_meta(directory, meta)
        with self.assertRaisesRegex(ValueError, "approved"):
            h1.analyze_run(directory)

    def test_ragged_csv_rejected(self):
        directory = self.fixture()
        self.write_rows(directory/"fields.csv", h1.FIELD_COLUMNS, [[0, 1]])
        with self.assertRaisesRegex(ValueError, "field count"):
            h1.analyze_run(directory)

    def test_nonfinite_missing_and_negative_data_rejected(self):
        for i, value in enumerate(("NaN", "inf", "", "-1")):
            directory = self.fixture(str(i))
            self.mutate_csv(directory/"monitors.csv", h1.MONITOR_COLUMNS,
                            lambda rows: rows[1].update(mass_kg=value))
            with self.assertRaises(ValueError):
                h1.analyze_run(directory)

    def test_duplicate_or_missing_times_rejected(self):
        for i, action in enumerate((lambda rows: rows[1].update(time_s="0"), lambda rows: rows.pop())):
            directory = self.fixture(str(i))
            self.mutate_csv(directory/"monitors.csv", h1.MONITOR_COLUMNS, action)
            with self.assertRaisesRegex(ValueError, "every declared step"):
                h1.analyze_run(directory)

    def test_duplicate_cells_volume_and_geometry_rejected(self):
        actions = [lambda rows: rows[-1].update(cell_id="0"),
                   lambda rows: rows[-1].update(volume_m3="-1"),
                   lambda rows: rows[-1].update(volume_m3="0.5"),
                   lambda rows: rows[-1].update(x_min_m="0.06")]
        for i, action in enumerate(actions):
            directory = self.fixture(str(i))
            self.mutate_csv(directory/"fields.csv", h1.FIELD_COLUMNS, action)
            with self.assertRaises(ValueError):
                h1.analyze_run(directory)

    def test_missing_final_snapshot_rejected(self):
        directory = self.fixture()
        self.mutate_csv(directory/"fields.csv", h1.FIELD_COLUMNS, lambda rows: rows.__delitem__(slice(2,None)))
        with self.assertRaisesRegex(ValueError, "initial and final"):
            h1.analyze_run(directory)

    def test_mesh_and_time_known_error_slopes(self):
        mesh_reports = []
        for cells in (2, 16, 128):
            scale = (.001/cells)**(1/3)
            mesh_reports.append(h1.analyze_run(self.fixture(f"m{cells}", "H1-C", cells, error=scale**2)))
        for row in h1.convergence(mesh_reports, "mesh")["adjacent_error_slopes"]:
            self.assertAlmostEqual(row["error_slope"], 2, places=6)
        time_reports = [h1.analyze_run(self.fixture(f"t{dt}", "H1-C", dt=dt, error=dt**2))
                        for dt in (1., .5, .25)]
        for row in h1.convergence(time_reports, "time")["adjacent_error_slopes"]:
            self.assertAlmostEqual(row["error_slope"], 2)

    def test_convergence_rejects_mixed_controls_and_too_few(self):
        reports = [h1.analyze_run(self.fixture(str(i), "H1-C", dt=dt, error=dt))
                   for i, dt in enumerate((1., .5, .25))]
        with self.assertRaises(ValueError):
            h1.convergence(reports[:2], "time")
        reports[1]["manifest"]["processes"] = 8
        with self.assertRaisesRegex(ValueError, "controls"):
            h1.convergence(reports, "time")

    def test_zero_error_yields_no_fabricated_order(self):
        reports = [h1.analyze_run(self.fixture(str(i), "H1-C", dt=dt))
                   for i, dt in enumerate((1., .5, .25))]
        for report in reports:
            report["analytical_errors"][-1]["L2_K"] = 0.
        self.assertTrue(all(r["error_slope"] is None for r in h1.convergence(reports,"time")["adjacent_error_slopes"]))

    def test_nonconvergence_and_repeated_scales_are_not_hidden(self):
        reports = [h1.analyze_run(self.fixture(str(i), "H1-C", dt=dt, error=1/dt))
                   for i, dt in enumerate((1., .5, .25))]
        for row in h1.convergence(reports, "time")["adjacent_error_slopes"]:
            self.assertAlmostEqual(row["error_slope"], -1)
        reports[1]["manifest"]["dt_s"] = 1.
        with self.assertRaisesRegex(ValueError, "duplicate refinement"):
            h1.convergence(reports, "time")

    def test_cli_error_is_nonzero_and_has_no_result(self):
        with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(h1.main(["run", str(self.root/"missing")]), 1)
        self.assertEqual(out.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
