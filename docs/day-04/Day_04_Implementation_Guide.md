# Day 4 H1 implementation preparation

Baseline: approved Day 3 commit `777fc5d`. This package contains executable
standard-library Python postprocessing and a **version-gated local GUI
workflow**. It does not establish an executable STAR-CCM+ case for an unknown
build. No solver was launched and no Java macro was generated: no installed
release API has been verified. Do not label a guessed macro executable.

The researcher's PC is an i9-14900HX with 32 GB RAM and a user-confirmed
working license. OS, release/build, compatible model interfaces and parallel
entitlement remain unknown. The solver runs locally, not in this cloud task.

## Package entry points

- [Input parameters](../../data/day-04/H1_Benchmark_Input_Parameters.csv)
- [Boundary definitions](../../data/day-04/H1_Boundary_Conditions.csv)
- [Mesh/resource plan](H1_Mesh_Configuration.md)
- [Analytical references](H1_Expected_Analytical_Results.md)
- [Run ledger header](../../data/day-04/H1_Run_Log_Template.csv)
- [Python processor](../../scripts/H1_Postprocessing.py)
- [Python tests](../../tests/H1_Postprocessing_Tests.py)
- [Research log and review status](Day_04_Research_Log.md)

All input values are approved synthetic benchmark constants, not F7 facts.
Preserve four separate cases: A constant field, B volumetric heating, C thermal
diffusion, D isothermal moving lid. No sodium, chemistry, buoyancy, radiation,
solid region or aerosol model belongs in these cases.

## Build verification before local setup

Complete the [Day 3 release/license check](../day-03/STARCCM_Version_and_License_Check.md).
Record exact release/build and OS from local application/system evidence.
Verify a 2024-or-earlier build and obtain its model, meshing, licensing and
export reference. A visible option does not alone prove license checkout.

Every GUI route below is marked **[BUILD CHECK]**: the quoted labels identify
the intended function, not a verified literal menu path. Record the actual
tree location/control name and manual page for your build in local notes.
If a required operation cannot be mapped, stop that operation and resolve it;
do not silently substitute a different physical model.

## GUI setup sequence

1. **[BUILD CHECK — launcher/session]** Launch the known local installation
   with four authorized solver processes. Confirm the actual rank count and
   license status in the startup log. Save version/OS evidence. No generic
   command-line flag or license-server setting is assumed here.
2. **[BUILD CHECK — geometry/parts creation]** Create a block with origin
   (0,0,0) and extents (0.1,0.1,0.1) m through the supported primitive or CAD
   route. Name its six faces X_MIN/X_MAX/Y_MIN/Y_MAX/Z_MIN/Z_MAX and inspect
   normals. The top is Z_MAX. Verify volume and face areas analytically.
3. **[BUILD CHECK — region assignment]** Assign one fluid region with six
   distinct wall boundaries. Confirm all are closed/impermeable. Do not create
   an inlet, outlet, open pressure boundary or internal baffle.
4. **[BUILD CHECK — mesh operation]** Follow the documented rectangular-grid
   route for G1, nominally 32³ cells, using the mesh plan. Inspect actual cell
   shape/count and quality. Retain common topology controls for G2/G3.
5. **[BUILD CHECK — physics continuum/model selection]** Choose transient,
   three-dimensional, laminar, constant-density single-fluid flow and the
   compatible thermal equation for A/B/C. Enter rho=1, mu=0.001, c=1000,
   k=0.1 in SI units. Confirm energy reduces to the approved thermal equation;
   disable gravity, compressibility, additional work/dissipation heating and
   other unneeded models. Do not replace it with constant-volume ideal-gas
   heating while retaining the same analytical cp-like storage formula.
6. **[BUILD CHECK — wall and pressure controls]** Assign stationary no-slip,
   adiabatic walls to A/B/C. Use the supported sealed-domain pressure reference
   at 0 Pa gauge, without opening a pressure outlet. For D, disable thermal
   evolution and use the constant-property/isothermal surrogate; apply +x
   tangential speed 0.1 m/s only to Z_MAX. Keep normal velocity zero. Document
   lid-edge discontinuities and boundary resolution.
7. **[BUILD CHECK — initialization]** Initialize velocity zero and temperature
   300 K for A/B/D. For C, map 300+cos(pi*x/0.1) K to the build's supported
   coordinate/field-expression syntax. Symbols here are mathematics, not a
   paste-ready STAR expression. Verify the x coordinate units and initial
   exported field. For rectangular cells use a verified cell-average mapping
   if supported; otherwise document center sampling and its error. No assumed
   cell-extent API is supplied.
8. **[BUILD CHECK — energy source]** For B set uniform 100 W/m³ in the fluid
   energy equation, using the actual documented source interface. If the
   interface expects W/kg, supply q_vol/rho; if it expects integrated W, use
   q_vol*V. Check the independent integrated source report equals the intended
   0.1 W. A/C use zero source; D has no active energy equation.
9. **[BUILD CHECK — reports/monitors]** Create the reports in the export contract
   below using compatible integral, maximum and residual report functions.
   Confirm normal orientation and sign conventions by dimensional reasoning
   and a controlled check. Record the actual report definitions and units.
10. **[BUILD CHECK — transient controls]** Select documented spatial and
    temporal schemes and record their orders, limiters and inner convergence
    policy. Start the thermal pilot at dt=0.1 s to t=10 s, subject to the
    reviewed refinement plan. Export the initialized t=0 state before advancing.
    D needs its own Courant/accuracy check; do not infer its time step from C.
11. **[BUILD CHECK — cell export]** Export every cell at t=0 and the final time
    (optional additional snapshots) without interpolation, averaging onto a
    surface or dropping cells. Obtain stable cell IDs, true x extents, volumes
    and temperatures for A/B/C. If the GUI cannot export extents directly,
    derive them from verified structured-grid indexing/connectivity in a
    separately reviewed adapter. Do not set x_min=x_max=centroid or infer
    connectivity from row order. Without this evidence, the field-error
    processor is not ready for that mesh.
12. **[BUILD CHECK — save/export]** Save separate initialized and completed
    case files, raw logs and unmodified raw exports. Convert copies to the
    canonical CSV schema with a recorded column/unit/sign map. Check one
    original sample and an integrated quantity before processing. Do not
    assume the solver's native CSV headings already match this schema.

## Unknown software dependencies register

| Dependency | Required confirmation | Status |
|---|---|---|
| Release/build and OS | Local About/startup evidence and supported-platform guide | Unknown |
| Parallel license | Entitlement and actual four/eight-rank checkout | Working base license confirmed; count unknown |
| Rectangular mesh route | Exact mesher controls and cell shape evidence | Unverified |
| Constant-density thermal model | Governing equation and excluded source terms | Unverified |
| Closed-domain pressure constraint | Reference control without open boundary | Unverified |
| Source interface/units | W/m³ vs W/kg vs W and region application | Unverified |
| Initialization/coordinate syntax | Field representation and cell-average capability | Unverified |
| Moving-wall control | Tangential speed and isothermal configuration | Unverified |
| Reports/exports | Flux signs, independent energy, residual normalization, cell extents/IDs | Unverified |
| Java API | Installed-release classes/methods, compile and local test | Unverified; no macro supplied |

## Run directory and evidence discipline

Use one unique local directory per case/mesh/time step/process trial:

```text
runs/<run_id>/
  manifest.json            # completed observed metadata; template starts planned
  monitors.csv            # canonical every-step integral/diagnostic exports
  fields.csv              # canonical initial/final full-cell snapshots, A/B/C
  raw/                    # untouched solver logs and exports
  local/                  # .sim checkpoints, manual-version and license evidence
  reports/                # derived JSON summaries and comparison output
```

`runs/` is ignored by Git to avoid publishing binaries, license evidence or
large raw datasets accidentally. Keep validated small research outputs under
reviewed version control later. Nothing in this directory is populated by Day 4.
Tests create labeled synthetic fixtures only in temporary directories.

Copy [manifest.template.json](../../data/day-04/templates/manifest.template.json)
and header-only CSV templates into each directory. Fill all null metadata from
actual configuration/evidence; select the case and its source/lid inputs. Only
set run_status=completed after the exports cover the stated interval. Set
evidence_kind=solver_export for real exports; tests use synthetic_test. The
metadata is an operator declaration, not independent proof of solver execution.
The ledger template holds resource observations; leave them blank until measured.

## Canonical CSV schema and monitors

Comma delimiter, dot decimal, UTF-8, header exactly as in the templates; no
units embedded in numeric cells. Each numerical cell must be finite. No
interpolation/resampling is performed by the processor. Convert documented
units/signs once and retain raw originals.

| monitors.csv column | Quantity / requirement |
|---|---|
| time_s | t=0 and every completed fixed-dt step through end_time_s; strictly ordered |
| mass_kg | Independent integral of rho over the whole fluid volume |
| mass_out_kg_s | Sum of outward signed wall mass fluxes; no volumetric mass source |
| absolute_wall_mass_flux_kg_s | Integral of absolute local wall mass flux over all faces, not absolute net flux |
| energy_J | Integral rho*c*(T-300) dV; A/B/C only |
| heat_in_W | Integrated conductive wall heat entering fluid, positive inward; A/B/C only |
| source_W | Integrated applied volumetric energy source, positive heating; A/B/C only |
| max_speed_m_s | Global maximum speed; inspect spurious velocity in thermal cases |
| max_abs_divergence_s1 | Global maximum absolute velocity divergence (1/s) |
| continuity_residual | Nonnegative reported continuity residual; document normalization in iteration_policy |

For H1-D the three thermal columns must be empty, not fictitious zeros from
a disabled equation. Its mass and local-flow diagnostics remain required.
For A/B/C do not replace a missing wall report with an assumed zero. Save full
momentum/energy residual histories and extrema in raw logs as well; the minimal
canonical schema does not substitute for complete convergence review.

`fields.csv` columns are time_s, cell_id, x_min_m, x_max_m, volume_m3,
temperature_K. Every snapshot must contain exactly manifest.cells unique
stable IDs and sum to the cube volume. Cell shape must be orthogonal rectangular.
Record reference_sampling as cell_average (preferred) or cell_center (point
comparison with explicit representation-error limitations). D does not require
a thermal field file; retain velocity/pressure diagnostics separately.

## Python execution

Python 3.10 or newer, standard library only. From the repository root:

```bash
python3 tests/H1_Postprocessing_Tests.py -v
python3 -m unittest discover -s tests -v
python3 scripts/H1_Postprocessing.py --help
# After real local exports exist:
python3 scripts/H1_Postprocessing.py run runs/<run_id>
python3 scripts/H1_Postprocessing.py convergence --axis mesh runs/<G1> runs/<G2> runs/<G3>
python3 scripts/H1_Postprocessing.py convergence --axis time runs/<dt1> runs/<dt2> runs/<dt3>
```

Replace angle-bracket placeholders with actual paths; on Windows use the
installed Python invocation and shell path conventions. Commands print JSON
to stdout and errors to stderr with a nonzero exit status. Save stdout only
after successful execution. No supplied command launches STAR-CCM+.

The manifest requires: schema_version=1; case; run_id; run_status; evidence_kind;
solver_build; os; processes (4 or 8); cells; dt_s; end_time_s; physics_id;
spatial_scheme; temporal_scheme; iteration_policy; mesh_family; mesh_id;
geometry_id; initialization; reference_sampling; mesh_geometry; parameters.
Strings must describe the actual configuration, not pending placeholders.
The parameters object fixes the approved constants; a changed-physics study
requires a reviewed extension to this processor. End time must be an integer
number of time steps; a shortened pilot must declare its actual end time and
must not be described as a completed 10 s comparison.

Refinement processing is restricted to H1-C and at least three distinct run
IDs/scales. Mesh series hold dt and all other controls fixed; time series hold
mesh identity/count fixed. Both hold final time, schemes, processes, solver
build, initialization, geometry, evidence kind and iteration policy fixed.
Control identity relies on truthful manifest entries and review of raw inputs.
Outputs are diagnostics, never an automatic numerical PASS or an F7 result.
The processor's relative 1e-8 / absolute 1e-12 floating comparison is a file
consistency tolerance for times, constants and volume, not a CFD accuracy
criterion. The schema cannot prove complete geometric coverage or truthful
metadata; review the mesh, source logs and full-cell export independently.

## Full F7 source prerequisite and stop gate

SAND2021-0136 and PNC TN9410 98-074 remain unread after Day 3 proxy failures.
Their recovery is separate from H1 readiness; no F7 missing input is needed
or invented for this synthetic cube. Keep the Day 2 equation corrections
(Louie 2023 p.2 Eq.1 beta/nu²; p.3 Eq.2 undotted m³) and unresolved coefficients
on the F7 gate. The [source report](../day-02/Source_Verification_Report.md)
documents official destinations and recovery requirements.

Day 4 stops after preparation, tests, commit and push. Exact-release GUI mapping,
any Java API implementation and actual solver trials require local evidence.
