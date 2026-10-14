# Day 10 research log

Date: 2026-10-14 (Asia/Shanghai).
Baseline branch research/day-9-f7-mesh-readiness, commit
04aee3217fe9393db17ba86712a4d868892ecafb, matched against origin.
Initial worktree clean; new branch research/day-10-f7-physics-framework.
No merges.

## Completed framework work

Read all nine Day 9 deliverables plus Day 2 material/equation audits.
Confirmed that geometry/mesh readiness cannot be established from available
evidence. Prepared stage gates (0 geometry/mesh; 1 nonreactive flow/CHT;
2 sodium oxidation; 3 aerosol only after combustion validation).

Prepared 15 proposed model/continuum requirements, 27 pending property entries,
20 region/interface/boundary records and 16 monitor definitions. Numeric material
values and observed monitor results remain empty. No model is activated or
region assigned. Direct wall–pan contact is conditional; insulation–external
is a boundary, not an invented paired solid interface. Region aliases preserve
the earlier names without creating additional physical volumes.

Only reported operating quantities and explicit unit conversions appear in
the boundary framework. No arbitrary gas temperature/pressure/composition,
initial velocity, external heat-loss condition or reaction coefficient is
introduced. Source identities are not promoted into verified material properties.

No native CAD/mesh, continuum, BC, reaction, particle model, solver or result
plot was created. No new source retrieval is claimed. Exact 2402 capability/
license evidence and primary experimental reports remain pending. Existing
source records, corrected equations and H1 tooling are unchanged.

## Deliverables / review summary

1. [Physics framework report](Day_10_Physics_Framework_Report.md)
2. [Model selection assessment](STARCCM_2402_Physics_Model_Selection.md)
3. [Continuum requirements](../../data/day-10/F7_Physics_Continuum_Register.csv)
4. [Material properties](../../data/day-10/F7_Material_Property_Register.csv)
5. [Regions/interfaces](../../data/day-10/F7_Region_Interface_Definition.csv)
6. [Boundary framework](F7_Boundary_Condition_Framework.md)
7. [Transient solver strategy](F7_Solver_Strategy_Report.md)
8. [Reaction requirements](Sodium_Reaction_Model_Preparation.md)
9. [Future monitors](../../data/day-10/F7_Monitor_and_Report_Definition.csv)
10. This log.

Review decisions needed: evidence for geometry/mesh release, actual material
grades/correlations, initial/inlet/exterior conditions, contact topology/laws,
flow-regime and energy formulation, Stage 1 synthetic test specification,
and later conservative sodium closure definitions. No scientific validation
or complete CFD model is claimed.

## Tests

| Executed check | Outcome |
|---|---|
| `python3 -m unittest discover -s tests -v` | 54 passed, including 4 new Day 10 framework tests |
| `python3 tests/H1_Postprocessing_Tests.py -v` | 21 passed |
| `python3 scripts/check_day1_data.py` | PASS |
| `python3 scripts/day2_data.py --check` | PASS; 57 preserved + 25 added = 82 historical records |
| `git diff --check` | PASS |

All 75 tests passed without failures or skips. New tests check inactive
models/unverified capability status, missing property values, distinct region
aliases/contact types and empty future monitor results. Earlier H1 fixtures
remain software-only tests, not CFD runs. Software integrity tests are not
physical simulation or experimental validation.

All Day 10 relative links resolve. A baseline diff confirmed prior Days 1–9
documentation/data and scripts remain unchanged. No local solver or native
model test was possible or claimed.

## Stop / Day 11

Physics setup readiness BLOCKED by missing geometry/mesh/data/capability
evidence. First Day 11 operation is CAD/mesh approval evidence intake and
local reopening to reconcile the actual region inventory, not reaction setup.
Stop after this framework; no Stage 1/2/3 implementation begins.
