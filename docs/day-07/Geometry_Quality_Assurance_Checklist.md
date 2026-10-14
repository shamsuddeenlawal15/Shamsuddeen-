# Geometry QA and independent checks

No CAD file or native diagnostic report has been supplied. All geometry QA
observations are pending. Analytical checks are reproducible calculations,
not actual CAD validation.

## Commands (Python 3.10+, standard library)

From the repository root on the cloud or local PC:

```text
python3 scripts/F7_Geometry_Consistency_Checks.py analytic
python3 -m unittest discover -s tests -v
python3 tests/H1_Postprocessing_Tests.py -v
```

On Windows use the locally verified Python invocation (for example py -3 if
installed). Analytical mode reads the Day 7 verified register, converts only
declared mm-to-m units, calculates ideal-cylinder consistency, layer total and
nozzle-height difference. It does not open STAR-CCM+, create a shape or adopt
a cylinder as F7. Console precision is computational, not measurement precision.

After real local CAD reports exist, prepare the documented audit JSON and run:

```text
python3 scripts/F7_Geometry_Consistency_Checks.py audit --evidence runs/ACTUAL_CASE/cad_audit.json
```

Replace the path with actual evidence. No real-CAD audit was run in Day 7.
Unit tests use explicitly labelled synthetic_test fixtures in temporary folders.

## Evidence JSON contract (not native STAR-CCM+ export)

A manually reviewed mapping is required from actual reports; no unobserved
native-export format is assumed. No populated example is committed as a result.

| Key | Required content |
|---|---|
| schema_version | Integer 1 |
| case | F7-1 or F7-2 |
| evidence_kind | local_cad_report for genuine data; synthetic_test reserved for tests |
| solver_build / operator / export_date | Actual non-placeholder strings |
| coordinate_frame | F7_PROJECT_CARTESIAN |
| measurement_scope | For bounds: vessel_envelope_excluding_external_pipes |
| artifacts | Nonempty list of objects with path (relative to JSON or absolute) and sha256; files must exist and hashes match |
| bounds_m | Optional x/y/z pairs [minimum,maximum] in metres; actual aligned vessel envelope including heads, excluding external ducts |
| measurements | Optional entries below: each object has value and unit |
| topology | Optional nonnegative integer diagnostic counts below |
| names | Optional list of actual semantic part/region/surface names mapped to registry |

Measurement keys/units: pan_area (m2), pan_thickness (m),
insulation1_thickness (m), insulation2_thickness (m), nozzle_height (m),
gas_volume (m3), vessel_enclosed_volume (m3).
Nozzle height is a measured relative datum difference, not absolute global z
from an arbitrary export. Export actual thickness diagnostics, not requested
CAD input values; retain location/range if thickness varies. Only supplied
scalar summaries are compared; full distributions still require manual review.

Topology keys: closed_shell_open_edges, overlapping_solid_pairs,
fluid_components, orientation_defects, duplicate_surfaces. Counts must come
from real diagnostics with the inspected geometry/selection scope retained
in the referenced artifacts. Close intended inlet/outlet boundaries with
geometric patches for shell inspection; that does not assign wall BCs.
A connectivity reference of one is a review expectation, not permission to
remove a real lower cavity or ignore its source-dependent communication.

Missing observations remain pending. JSON duplicate keys, ambiguous units,
nonfinite/invalid measurements, malformed bounds, unknown metric names and
checksum mismatches are rejected. Named surfaces are checked against the
register; unknown/duplicate names and missing core regions are reported.
The name check does not demand creation of CFD regions during CAD-only work.

Audit returns differences against source constraints, not acceptance decisions.
Vessel volume compared to 3.0 m³ is labelled a capacity comparison, not free-
volume verification. Gas volume has no verified target and is reported without
a fabricated difference. Engineering tolerances must be reviewed separately
from unquantified experimental uncertainty.

The utility is NOT a CAD kernel. It does not detect intersections, determine
closure/connectivity or check normals from a geometric file. It checks the
reported counts and names, and hashes referenced evidence. A hash confirms
file identity, not authenticity or correct diagnostic selections. Zero counts
alone therefore never produce “CAD approved”; inspect native reports/files.

## Actual geometry review sheet

| Check | Required basis | Actual observation / evidence | Reviewer disposition |
|---|---|---|---|
| Vessel bounds / diameter | V001–V002 and resolved dimension conventions | | |
| Vessel enclosed / free gas volume | Distinguish capacity, head and occupied volumes | | |
| Pan area / thickness | V004–V005; resolved planform and rim | | |
| Two insulation thicknesses | V006–V007; resolved extents/contact | | |
| Nozzle height | V008 or V009; correct pan datum | | |
| Closure | Named patches; no unintended open edges | | |
| Solid overlaps | All intended bodies checked; contact not interpenetration | | |
| Fluid connectivity | Include reviewed lower cavities and openings | | |
| Normals / duplicate faces | Paired orientations and consistent region sides | | |
| Names / material mapping | Semantic register; carbon-steel pan distinguished | | |
| Source-to-CAD agreement | Measured minus source; uncertainty and assumptions explicit | | |

All rows remain unfilled. Human source/geometry review is required before
meshing; a successful script exit only means the requested processing completed.
