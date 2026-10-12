# Detailed 90-day research plan

## Stage gates

| Days | Work package | Deliverables | Exit criteria |
|---|---|---|---|
| 1 | Evidence foundation | Paper extraction, equation review, validation matrix, feasibility decision | Page-level second-pass review complete; gaps accepted or resolved |
| 2–5 | Source closure | Obtain cited facility/property sources; resolve geometry, properties, sensors, uncertainties | Model-enabling input register approved |
| 6–10 | STAR-CCM+ readiness | Version/license smoke test, units/conventions, baseline automation skeleton | Documented batch smoke test passes; no physics result claimed |
| 11–18 | Geometry and mesh strategy | Parametric geometry, regions/interfaces, mesh families, quality criteria | Dimensions trace to sources; mesh QA passes |
| 19–28 | Baseline physics | Flow, conjugate heat transfer, species, radiation baseline | Conservation checks close to predefined tolerances |
| 29–38 | Sodium combustion implementation | Reviewed reaction/source implementation and unit tests | Standalone source tests and limiting cases pass |
| 39–45 | Instrument mapping | Probe definitions, time alignment, output pipeline | Simulation observables match experimental definitions |
| 46–55 | F7-1 verification | Mesh/time-step study and solver diagnostics | Numerical uncertainty characterized |
| 56–65 | F7-1 validation | Blind comparison, residual/error analysis | Results reviewed against acceptance criteria |
| 66–73 | F7-2 prediction | Locked-model F7-2 run and diagnostics | Run completes with conservation/quality checks |
| 74–80 | Cross-test validation | F7-1/F7-2 comparison and model-form assessment | Discrepancies quantified without retuning concealment |
| 81–85 | Sensitivity/uncertainty | Prioritized parameter sensitivities and uncertainty propagation | Dominant uncertainties ranked |
| 86–90 | Synthesis | Reproducible archive, report, limitations, next-study backlog | Independent reproduction/review checklist passes |

## Day-by-day near-term plan

- Day 1: primary-source evidence and feasibility gate only.
- Day 2: resolve missing references and tool/license availability.
- Day 3: geometry/sensor reconstruction with uncertainty bounds.
- Day 4: material-property and reaction-model evidence review.
- Day 5: approve the model-input register and validation observables.
- Days 6–7: establish STAR-CCM+ execution conventions and smoke test.
- Days 8–10: design automation, provenance, and QA workflows.

## Governance

Each gate requires source traceability, reproducible scripts, clean version
control, and review. Experimental values remain immutable; model calibration
and validation subsets must be declared before result inspection. Failed or
inconclusive runs are retained and explained, not silently discarded.
