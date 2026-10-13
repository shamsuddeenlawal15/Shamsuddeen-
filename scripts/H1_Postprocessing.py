#!/usr/bin/env python3
"""Process local H1 exports. No STAR-CCM+ API or third-party dependency is used."""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
import sys

L = 0.1
RHO = 1.0
C = 1000.0
K = 0.1
T0 = 300.0
VOLUME = L ** 3
CASES = {"H1-A", "H1-B", "H1-C", "H1-D"}
MONITOR_COLUMNS = [
    "time_s", "mass_kg", "mass_out_kg_s", "absolute_wall_mass_flux_kg_s",
    "energy_J", "heat_in_W", "source_W", "max_speed_m_s",
    "max_abs_divergence_s1", "continuity_residual",
]
FIELD_COLUMNS = [
    "time_s", "cell_id", "x_min_m", "x_max_m", "volume_m3", "temperature_K",
]
META_TEXT = [
    "run_id", "solver_build", "os", "physics_id", "spatial_scheme",
    "temporal_scheme", "iteration_policy", "mesh_family", "mesh_id",
    "geometry_id", "initialization", "reference_sampling", "mesh_geometry",
]


def number(value, name, *, positive=False, nonnegative=False):
    if isinstance(value, bool):
        raise ValueError(f"{name}: boolean is not a number")
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name}: finite number required") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name}: finite number required")
    if positive and result <= 0 or nonnegative and result < 0:
        raise ValueError(f"{name}: invalid sign")
    return result


def close(a, b):
    return math.isclose(a, b, rel_tol=1e-8, abs_tol=1e-12)


def read_csv(path, columns):
    with Path(path).open(newline="", encoding="utf-8-sig") as stream:
        records = list(csv.reader(stream, strict=True))
    if not records or records[0] != columns:
        raise ValueError(f"{path}: exact header required: {','.join(columns)}")
    if len(records) < 2:
        raise ValueError(f"{path}: no exported rows")
    result = []
    for index, record in enumerate(records[1:], 2):
        if len(record) != len(columns):
            raise ValueError(f"{path}:{index}: wrong field count")
        result.append(dict(zip(columns, record)))
    return result


def read_manifest(path):
    with Path(path).open(encoding="utf-8") as stream:
        meta = json.load(stream)
    if not isinstance(meta, dict) or meta.get("schema_version") != 1:
        raise ValueError("manifest: schema_version must be 1")
    if meta.get("case") not in CASES or meta.get("run_status") != "completed":
        raise ValueError("manifest: valid case and completed run required")
    if meta.get("evidence_kind") not in {"solver_export", "synthetic_test"}:
        raise ValueError("manifest: evidence_kind must explicitly identify origin")
    for key in META_TEXT:
        if not isinstance(meta.get(key), str) or not meta[key].strip():
            raise ValueError(f"manifest: {key} required")
        if meta[key].strip().lower() in {"unknown", "pending", "todo"}:
            raise ValueError(f"manifest: {key} still unresolved")
    for key in ("cells", "processes"):
        if type(meta.get(key)) is not int or meta[key] <= 0:
            raise ValueError(f"manifest: {key} must be a positive integer")
    if meta["processes"] not in (4, 8):
        raise ValueError("manifest: this protocol supports 4 or 8 processes")
    for key in ("dt_s", "end_time_s"):
        meta[key] = number(meta.get(key), key, positive=True)
    steps = meta["end_time_s"] / meta["dt_s"]
    if not close(steps, round(steps)):
        raise ValueError("manifest: end_time_s must be a whole number of steps")
    if meta["reference_sampling"] not in {"cell_average", "cell_center"}:
        raise ValueError("manifest: invalid reference_sampling")
    if meta["mesh_geometry"] != "orthogonal_rectangular":
        raise ValueError("manifest: exact cell reference requires orthogonal rectangular cells")
    required_parameters = {"L_m": L, "rho_kg_m3": RHO, "c_J_kgK": C,
                           "k_W_mK": K, "mu_Pa_s": 0.001, "T0_K": T0,
                           "q_vol_W_m3": 100.0 if meta["case"] == "H1-B" else 0.0,
                           "lid_speed_m_s": 0.1 if meta["case"] == "H1-D" else 0.0}
    if not isinstance(meta.get("parameters"), dict):
        raise ValueError("manifest: approved parameters required")
    for key, expected in required_parameters.items():
        actual = number(meta["parameters"].get(key), key)
        if not close(actual, expected):
            raise ValueError(f"manifest: {key} differs from the approved synthetic benchmark")
    return meta


def analytical_temperature(case, time_s, a, b, sampling="cell_average"):
    t = number(time_s, "time_s", nonnegative=True)
    a, b = number(a, "x_min_m"), number(b, "x_max_m")
    if not 0 <= a < b <= L:
        raise ValueError("cell x interval must lie inside the cube")
    if sampling not in {"cell_average", "cell_center"}:
        raise ValueError("unknown analytical sampling")
    if case == "H1-A":
        return T0
    if case == "H1-B":
        return T0 + 100.0 * t / (RHO * C)
    if case != "H1-C":
        raise ValueError("no analytical temperature-error test for H1-D")
    if sampling == "cell_average":
        phase = L * (math.sin(math.pi*b/L) - math.sin(math.pi*a/L)) / (math.pi*(b-a))
    else:
        phase = math.cos(math.pi*(a+b)/(2*L))
    return T0 + phase * math.exp(-(K/(RHO*C))*(math.pi/L)**2*t)


def trapezoids(times, values):
    if len(times) != len(values) or not times:
        raise ValueError("integration requires matching nonempty series")
    times = [number(t, "integration time") for t in times]
    values = [number(v, "integration value") for v in values]
    integral = [0.0]
    for i in range(1, len(times)):
        if times[i] <= times[i-1]:
            raise ValueError("integration times must strictly increase")
        integral.append(integral[-1] + (times[i]-times[i-1])*(values[i]+values[i-1])/2)
    return integral


def monitor_metrics(rows, meta):
    thermal = meta["case"] != "H1-D"
    parsed = []
    for row in rows:
        parsed_row = {}
        for key in MONITOR_COLUMNS:
            if key in {"energy_J", "heat_in_W", "source_W"} and not thermal:
                if row[key] != "":
                    raise ValueError("H1-D thermal columns must be blank; energy is disabled")
                continue
            parsed_row[key] = number(row[key], key)
        for key in ("time_s", "absolute_wall_mass_flux_kg_s", "max_speed_m_s",
                    "max_abs_divergence_s1", "continuity_residual"):
            if parsed_row[key] < 0:
                raise ValueError(f"{key}: negative value")
        if parsed_row["mass_kg"] <= 0:
            raise ValueError("mass must be positive")
        if parsed_row["absolute_wall_mass_flux_kg_s"] + 1e-14 < abs(parsed_row["mass_out_kg_s"]):
            raise ValueError("absolute wall mass flux is smaller than net flux")
        parsed.append(parsed_row)
    times = [r["time_s"] for r in parsed]
    count = round(meta["end_time_s"]/meta["dt_s"]) + 1
    if len(times) != count or any(not close(t, i*meta["dt_s"]) for i, t in enumerate(times)):
        raise ValueError("monitors must cover t=0 through end_time_s at every declared step")
    outward = trapezoids(times, [r["mass_out_kg_s"] for r in parsed])
    mass0 = parsed[0]["mass_kg"]
    mass_residual = [r["mass_kg"]-mass0+flow for r, flow in zip(parsed, outward)]
    result = {
        "max_mass_balance_error_kg": max(map(abs, mass_residual)),
        "max_relative_mass_balance_error": max(map(abs, mass_residual))/mass0,
        "max_mass_deviation_from_rhoV_kg": max(abs(r["mass_kg"]-RHO*VOLUME) for r in parsed),
        "max_absolute_wall_mass_flux_kg_s": max(r["absolute_wall_mass_flux_kg_s"] for r in parsed),
        "max_speed_m_s": max(r["max_speed_m_s"] for r in parsed),
        "max_abs_divergence_s1": max(r["max_abs_divergence_s1"] for r in parsed),
        "max_continuity_residual": max(r["continuity_residual"] for r in parsed),
        "energy_balance": None,
    }
    if thermal:
        powers = [r["source_W"]+r["heat_in_W"] for r in parsed]
        energy_input = trapezoids(times, powers)
        residual = [r["energy_J"]-parsed[0]["energy_J"]-q for r, q in zip(parsed, energy_input)]
        intended_power = 0.1 if meta["case"] == "H1-B" else 0.0
        scale = trapezoids(times, [abs(r["source_W"])+abs(r["heat_in_W"]) for r in parsed])[-1]
        result["energy_balance"] = {
            "max_error_J": max(map(abs, residual)),
            "final_error_J": residual[-1],
            "relative_final_error": residual[-1]/scale if scale > 0 else None,
            "max_source_power_deviation_W": max(abs(r["source_W"]-intended_power) for r in parsed),
            "max_adiabatic_wall_heat_leak_W": max(abs(r["heat_in_W"]) for r in parsed),
        }
    return result, parsed


def field_metrics(rows, meta, monitors):
    groups = {}
    for row in rows:
        t = number(row["time_s"], "field time", nonnegative=True)
        if not row["cell_id"].strip():
            raise ValueError("empty cell_id")
        groups.setdefault(t, []).append(row)
    if not any(close(t, 0) for t in groups) or not any(close(t, meta["end_time_s"]) for t in groups):
        raise ValueError("fields need initial and final snapshots")
    results, baseline_geometry = [], None
    for t, cells in sorted(groups.items()):
        monitor = next((m for m in monitors if close(t, m["time_s"])), None)
        if monitor is None:
            raise ValueError("field time has no matching monitor")
        if len(cells) != meta["cells"] or len({c["cell_id"] for c in cells}) != len(cells):
            raise ValueError("incomplete snapshot or duplicate cell_id")
        geometry, errors, volumes, temperatures = {}, [], [], []
        for cell in cells:
            a, b = number(cell["x_min_m"], "x_min_m"), number(cell["x_max_m"], "x_max_m")
            v = number(cell["volume_m3"], "volume_m3", positive=True)
            value = number(cell["temperature_K"], "temperature_K", positive=True)
            exact = analytical_temperature(meta["case"], t, a, b, meta["reference_sampling"])
            geometry[cell["cell_id"]] = (a, b, v)
            errors.append(value-exact)
            volumes.append(v)
            temperatures.append(value)
        volume = math.fsum(volumes)
        if not close(volume, VOLUME):
            raise ValueError("snapshot cell volumes do not sum to the cube volume")
        if baseline_geometry is None:
            baseline_geometry = geometry
        elif geometry != baseline_geometry:
            raise ValueError("cell geometry/IDs changed between snapshots")
        energy = RHO*C*math.fsum(v*(temp-T0) for v, temp in zip(volumes, temperatures))
        results.append({
            "time_s": t,
            "L1_K": math.fsum(v*abs(e) for v, e in zip(volumes, errors))/volume,
            "L2_K": math.sqrt(math.fsum(v*e*e for v, e in zip(volumes, errors))/volume),
            "Linf_K": max(map(abs, errors)),
            "temperature_spread_K": max(temperatures)-min(temperatures),
            "field_minus_monitor_energy_J": energy-monitor["energy_J"],
        })
    return results


def analyze_run(directory):
    directory = Path(directory)
    meta = read_manifest(directory / "manifest.json")
    balances, monitors = monitor_metrics(read_csv(directory / "monitors.csv", MONITOR_COLUMNS), meta)
    fields = None
    if meta["case"] != "H1-D":
        fields = field_metrics(read_csv(directory / "fields.csv", FIELD_COLUMNS), meta, monitors)
    return {
        "status": "processed_not_automatically_passed", "manifest": meta,
        "constants": {"L_m": L, "rho_kg_m3": RHO, "c_J_kgK": C, "k_W_mK": K, "T0_K": T0},
        "balances": balances, "analytical_errors": fields,
        "limitations": [
            "Manifest is operator-declared evidence, not independent proof of a solver run.",
            "Rates integrated by trapezoids; under-sampling can conceal balance defects.",
            "Cell-center references include sampling error; cell averages require rectangular cells.",
            "No universal accuracy threshold, F7 validation or mesh independence is inferred.",
        ],
    }


def convergence(reports, axis):
    if axis not in {"mesh", "time"} or len(reports) < 3:
        raise ValueError("convergence needs mesh/time axis and at least three runs")
    shared = ["case", "solver_build", "os", "physics_id", "geometry_id", "spatial_scheme",
              "temporal_scheme", "iteration_policy", "initialization", "reference_sampling",
              "mesh_geometry", "end_time_s", "processes", "evidence_kind"]
    shared += ["dt_s", "mesh_family"] if axis == "mesh" else ["cells", "mesh_id", "mesh_family"]
    first = reports[0]["manifest"]
    if first["case"] != "H1-C":
        raise ValueError("analytical convergence protocol is defined only for H1-C")
    ids = [r["manifest"]["run_id"] for r in reports]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate run_id in refinement series")
    for r in reports:
        if any(r["manifest"][key] != first[key] for key in shared):
            raise ValueError("refinement series changes non-refined controls")
    rows = []
    for r in reports:
        meta = r["manifest"]
        scale = (VOLUME/meta["cells"])**(1/3) if axis == "mesh" else meta["dt_s"]
        rows.append({"run_id": meta["run_id"], "scale": scale,
                     "L2_K": r["analytical_errors"][-1]["L2_K"]})
    rows.sort(key=lambda row: row["scale"], reverse=True)
    if len({row["scale"] for row in rows}) != len(rows):
        raise ValueError("duplicate refinement scales")
    slopes = []
    for coarse, fine in zip(rows, rows[1:]):
        ec, ef = coarse["L2_K"], fine["L2_K"]
        slope = math.log(ec/ef)/math.log(coarse["scale"]/fine["scale"]) if ec > 0 and ef > 0 else None
        slopes.append({"coarse": coarse["run_id"], "fine": fine["run_id"], "error_slope": slope,
                       "note": "inspect noise, temporal/spatial contamination and asymptotic regime"
                       if slope is not None else "zero error: order undefined"})
    return {"axis": axis, "runs": rows, "adjacent_error_slopes": slopes,
            "claim": "Diagnostic error slopes only; no automatic GCI, asymptotic-order or mesh-independence claim."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("directory", type=Path)
    study = sub.add_parser("convergence")
    study.add_argument("--axis", choices=["mesh", "time"], required=True)
    study.add_argument("directories", nargs="+", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_run(args.directory) if args.command == "run" else convergence(
            [analyze_run(p) for p in args.directories], args.axis)
        print(json.dumps(result, indent=2, allow_nan=False))
    except (OSError, ValueError, KeyError, TypeError, csv.Error, OverflowError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
