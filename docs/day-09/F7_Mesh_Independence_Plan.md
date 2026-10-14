# Formal spatial sensitivity plan — analysis deferred

No simulation data exist; no mesh independence or accuracy is claimed.
The coarse/medium/fine budgets are planning hypotheses, not proof that a
three-grid sequence reaches an asymptotic regime. Medium is only a candidate
for future primary validation, not pre-approved for that purpose.

## Controlled future design

Run F7-1 and F7-2 as separate convergence studies on individually approved,
fixed geometry. Hold physics/closures, initial/boundary conditions, numerical
schemes, precision, source histories, physical endpoints, process configuration
and iterative tolerance policy fixed. No physics is selected in Day 9.
Control time-discretization and inner-iteration errors independently so that
they do not dominate spatial differences. Plan a separate time-step study later.

Refine all influential dimensions coherently, including contact surfaces,
solid thickness and high-gradient zones. Preserve feature topology and the same
sampling definitions. For a genuinely similar 3-D grid family a representative
h=(V/N)^(1/3) may characterize resolution; anisotropic layers/multi-region
meshes require region/direction-specific spacings too. A total cell-count ratio
alone is insufficient.

Choose actual levels and ratios after CAD and mesh quality review. The budget
endpoints scale N by three, suggesting h ratio 3^(1/3)≈1.442 only for ideal
self-similar volume refinement. Local changes or mismatched counts invalidate
automatic use of that ratio.

## Observables and common locations/times

| Observable | Future comparison definition | Current limitation |
|---|---|---|
| Maximum temperature | Same phase/region, time and physical interval; also compare field/integral measures | Maxima can shift between cells; avoid equating different locations |
| Pool temperature | Same approved pool surface average plus sensor locations | Only radii 0.10/0.20/0.24 m known; xyz/depth unresolved |
| Combustion variables | Integrated sodium consumption, oxygen consumption and heat release at common times and integrated interval | Reaction implementation not selected or executed |
| Pressure | Same physical point/region and gauge/reference; include meaningful pressure differences | Pressure reference and experimental probes unresolved |
| Velocity | Fixed source-justified physical samples and volume/section averages | No sampling point invented |
| Aerosol concentration | Same species/mass basis at documented vessel/exhaust sample locations and averaging times | Later physics only; source sampler geometry unresolved |

L2023 p.4 Figs.3–5 motivates combustion/temperature/aerosol quantities; Fig.4
radii are not full sensor coordinates. Numerical-only comparison samples may
be proposed separately but must not be labelled experimental instruments.
Compare at common physical times; if temporal interpolation is needed later,
document/test its error rather than silently resampling.

## Error measures and extrapolation conditions

For a selected scalar Q, report signed difference, absolute difference
|Q_f-Q_m| and normalized difference
|Q_f-Q_m| / max(|Q_f|, Q_scale), with a physically justified positive Q_scale
chosen before results. Units and normalization must be stated; near-zero gauge
pressure or zero concentration cannot support naive relative errors. Also
compare time-series norms and conserved inventories/flux balances.

For three systematically similar grids with h1<h2<h3, equal ratio
r=h2/h1=h3/h2>1, Q1 fine, Q2 medium, Q3 coarse:
p=ln(|(Q3-Q2)/(Q2-Q1)|)/ln(r),
Q_ext=Q1+(Q1-Q2)/(r^p-1).
Only evaluate when differences are nonzero, convergence is monotonic and p>0,
ratios are appropriate and asymptotic behavior is credible. Zero differences,
oscillation, negative/unstable p or dissimilar grids require investigation,
not a fabricated order or infinity. Unequal ratios need a separately verified
generalized method, not this equal-ratio formula.

If later reporting a Grid Convergence Index, state the adopted method,
safety factor and rationale explicitly; none is assigned here without review.
A single triplet or a small medium/fine difference is not automatically
“mesh independent.” Add/revise levels when trends are inconclusive.

## Acceptance before future calculations

Set observable-specific absolute/relative tolerances using the scientific
decision needs and available experimental uncertainty, not a universal guessed
percentage. Require iterative/time errors demonstrably below the spatial
comparison tolerance, valid mesh quality on all levels, preserved geometry/
conservation, and stable observed trends for all decision-critical observables.
Thresholds and sensor definitions remain unresolved and must be signed before
results are evaluated. No present PASS, error value or convergence order exists.

Do not use the H1 postprocessor's convergence command for F7: its constants,
schemas and case restrictions are benchmark-specific. F7 export/processing
requires a separately tested implementation after actual data are available.
