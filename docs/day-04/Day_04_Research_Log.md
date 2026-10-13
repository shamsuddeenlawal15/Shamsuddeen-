# Day 04 research log

Date: 2026-10-13 (Asia/Shanghai). Approved baseline: Day 3 commit `777fc5d`.
New branch: `research/day-4-h1-preparation`.

## Preparation delivered

| Requested deliverable | Location |
|---|---|
| Day_04_Implementation_Guide.md | This documentation directory |
| H1_Benchmark_Input_Parameters.csv | `data/day-04/` |
| H1_Boundary_Conditions.csv | `data/day-04/` |
| H1_Mesh_Configuration.md | This documentation directory |
| H1_Expected_Analytical_Results.md | This documentation directory |
| H1_Run_Log_Template.csv | `data/day-04/` |
| H1_Postprocessing.py | `scripts/` |
| H1_Postprocessing_Tests.py | `tests/` |
| Day_04_Research_Log.md | This file |

The [implementation guide](Day_04_Implementation_Guide.md) links these files
and includes the export schema, local run directory, software dependency
register, GUI steps, source-sign conventions and reproducible Python commands.
Additional header-only CSV and incomplete manifest templates are under
`data/day-04/templates/`. No run log contains fabricated rows.

The four approved cases and 0.1 m cube are preserved. The top lid is explicitly
Z_MAX and moves in +x for D only. All case-specific boundaries are recorded
in 24 rows. Parameter tables retain the approved constant-density surrogate,
heat source, conductivity and thermal-storage choices, distinct from F7 inputs.

## Implemented Python processing

- Strict CSV/manifest reading, finite numbers and exact required headers.
- Whole-interval every-step monitor coverage and initial/final field coverage.
- Mass balance with outward flux convention; independent leakage and rho*V checks.
- Prescribed thermal balance with inward heat convention and independent
  field/monitor energy comparison; undefined relative scales return null.
- Analytical A/B/C temperatures, exact rectangular-cell averages, optional
  explicitly declared center sampling and volume-weighted L1/L2/Linf errors.
- Mesh/time refinement diagnostics for at least three consistent H1-C runs;
  mixed controls, duplicate IDs/scales and unsupported geometry are rejected.
- No invented convergence order for zero errors; negative slopes remain visible.
- H1-D has no asserted analytical thermal result and requires blank thermal columns.
- Command-line errors return nonzero; valid JSON output makes no automatic
  scientific or numerical PASS claim.

Fixed constants are checked against the approved manifest values. Stored
operator metadata is not proof that a solver executed. Geometry coverage,
source export fidelity, field representation and numerical tolerances still
require scientific review and local evidence.

## Validation performed

| Executed command | Result |
|---|---|
| `python3 tests/H1_Postprocessing_Tests.py -v` | 21 tests passed |
| `python3 -m unittest discover -s tests -v` | 22 existing tests passed |
| `python3 scripts/check_day1_data.py` | PASS |
| `python3 scripts/day2_data.py --check` | PASS; 57 preserved + 25 added = 82 Day 2 records |
| `python3 scripts/H1_Postprocessing.py --help` | CLI loads successfully |
| Python compilation and document/schema audit | PASS; 12 local links resolve; 24 boundary rows and canonical CSV headers checked |
| Git diff/whitespace review | PASS before commit |

All 43 tests passed, with no skipped or failed tests. New tests use explicitly
labeled synthetic fixtures written only into temporary directories; they test
software calculations, sign conventions, unequal weighting, invalid-data
rejection and convergence diagnostics. They are not STAR-CCM+ numerical outputs.

## Release and source limits

The PC CPU/RAM and working-license confirmation remain user-provided facts.
Exact build and OS are unknown; no installed Java API, mesher, field-function,
source-term, report or export interface has been verified. No Java macro was
created under these conditions. Python is executable and tested; the GUI
workflow becomes release-specific only after the local dependency checks.

No source-recovery success is claimed on Day 4. SAND2021-0136 and the original
F7 report remain unread after the documented Day 3 proxy failures. Recovery
through lawful supplied copies or functioning official access is a separate
prerequisite for full F7 reproduction. Historical evidence files are preserved;
Day 2's Eq.1 beta/nu² and Eq.2 undotted m³ corrections remain authoritative for
transcription, while their physical implementation context remains unresolved.

## Stop and review

Commit and push this preparation branch for review. Exact-build mapping and
local export verification are required before claiming a release-compatible
solver implementation. No STAR-CCM+ run, physical mesh, performance result,
numerical accuracy result, F7 validation or original-research result was created.
Day 4 stops at preparation; the planned local workflow is not executed here.
