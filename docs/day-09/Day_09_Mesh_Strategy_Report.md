# Day 9 — mesh readiness and strategy

Date: 2026-10-14 (Asia/Shanghai).
Baseline verified locally and on origin: research/day-8-starccm-f7-geometry,
cae95380be66c1b0b3f850db6914f26a4290e90c; initial working tree clean.
New branch: research/day-9-f7-mesh-readiness.

**Mesh readiness: BLOCKED.** Day 8 contains preparation only, not approved
physical CAD. No new local CAD/mesh evidence accompanies this request.
The phrase “approved geometry” does not override the recorded evidence gap.

## Day 8 review

Read the construction report, base setup, both case records, component register,
geometry audit, screenshot checklist and readiness report.

| Required verification | Evidence reviewed | Outcome |
|---|---|---|
| Closure / valid bodies | All CAD observations empty | Unverified; not passed |
| Region connectivity | No native geometry diagnostics | Unverified |
| Surface naming | 33 planned component/name entries; none created | Naming design only |
| Component separation | Planned pan/layers/vessel tree | No inspected solids |
| Case difference | Source heights 0.1/1.5 m; no case files | Parameter distinction only |
| Assumptions | P0 envelope, unknown pan/heads/nozzle/vents | Not a meshable experimental assembly |

The 37-row Day 8 audit retains source/unknown status, blank CAD values and
blank differences. Do not mesh its datums or empty vent slots. P0 is not F7;
no P0 mesh is authorized here.

## Conditional strategy recommendation, not method activation

The requested method names below are candidates/search terms. Exact 2402
availability, control labels, definitions and licenses still require installed
documentation/local evidence. No Java API, mesh command or specific menu is
claimed verified.

| Candidate | Physical/numerical purpose | Conditional assessment |
|---|---|---|
| Automated Mesh operation | Organize surface/volume generation and reproducible controls | Preferred orchestration concept after geometry approval; not a cell type |
| Surface remesher | Control surface tessellation, curvature, thin gaps and contact-face fidelity | Candidate preprocessing; must preserve approved dimensions/contacts |
| Polyhedral mesher | Flexible bulk gas cells around resolved curved/complex surfaces | Candidate gas baseline; RAM/quality measured before scaling; not intrinsically more accurate |
| Prism layer mesher | Resolve wall-normal gradients where later wall treatment requires them | Deferred; no layer height/count or y+ target without flow/property/model evidence |
| Thin mesher / directed-through-thickness alternative | Avoid unsuitable bulk cells across thin pan/layers/shell | Candidate only if exact-build support and valid topology confirmed; not automatic for every solid |

Provisional recommendation for a future approved assembly is surface-controlled
polyhedral bulk gas plus separately designed through-thickness solid meshes.
Add wall-normal layers only after their need and compatible future wall treatment
are established. A structured/directed alternative may suit simple solids but
is not selected merely because a mesher exists. No method is assigned to any
unapproved component today.

Thin 6 mm pan and 50 mm insulation layers (Louie et al. 2023 p.2 Section 2;
Day 7 V005–V007) cannot inherit a bulk gas cell size without a resolution review.
Actual vessel thickness is unknown: numerical Fig.2 8 mm is not an apparatus
input. Final pool areas 0.28/0.30 m² are observables, not refinement-patch shapes.

## Planning outputs

The [domain register](../../data/day-09/F7_Computational_Domain_Register.csv)
contains nine future domain/boundary candidates; none is included in a current
mesh. Air/exhaust are boundary surfaces unless resolved ducts are justified.
Reduced pool surfaces are not automatically liquid volume regions.

The [mesh-level table](../../data/day-09/F7_Mesh_Level_Definition.csv) defines
whole-model cell budgets only: 0.10–0.20, 0.30–0.60 and 0.90–1.80 million.
These are proposed planning scenarios, not validated mesh requirements,
mesher settings, observed counts or scientific independence criteria.
They do not inherit the H1 32³ grid.

See resource assessment for explicit RAM assumptions and refinement plan for
symbolic scales. The fine upper budget can exceed the provisional memory cap;
do not coarsen critical regions merely to claim completion on a PC.

Geometry verification, mesh verification, numerical/physical-model verification
and experimental validation are separate. No CAD, mesh, physics continuum,
simulation or validation calculation was performed.

## Exact first Day 10 operation

**Perform the geometry approval intake: obtain the actual local base/case
.sim files, record their hashes/build and a reviewer-signed geometry audit,
then reopen the identified files locally to confirm the approved part/surface
inventory.** If any is missing, remain at geometry recovery/review; do not create
a mesh operation or physics continuum. A day number is not approval.
