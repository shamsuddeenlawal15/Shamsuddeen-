# H1-A verification results

**Execution pending; no numerical result or pass/fail determination exists.**
Blank observed cells mean not measured, never zero. References below are
analytical expectations, not solver outputs.

| Diagnostic | Analytical reference | Observed result | Predeclared tolerance / rationale | Evidence |
|---|---|---|---|---|
| Temperature L1 / L2 / Linf error | 0 K | | | |
| Temperature spread / extrema | 0 K / 300 K | | | |
| Maximum speed | 0 m/s | | | |
| Maximum absolute divergence | 0 1/s | | | |
| Mass / deviation from rho V | 0.001 kg / 0 kg | | | |
| Integrated mass balance error | 0 kg | | | |
| Absolute local wall mass flux integral | 0 kg/s | | | |
| Relative thermal energy / balance error | 0 J / 0 J | | | |
| Conductive wall heat / source power | 0 W / 0 W | | | |
| Field-minus-monitor energy | 0 J | | | |
| Continuity / momentum / energy residual histories | Stable near-zero state expected | | | |
| Numerical stability / finite fields | No nonfinite values or growth | | | |

## Review method after receiving evidence

Use scripts/H1_Postprocessing.py, unchanged from approved Day 4. The processor
calculates mass balance M(t)-M(0)+integral(mass_out dt) and energy balance
E(t)-E(0)-integral(heat_in+source dt), using trapezoidal integration of sampled
rates. Inspect intermediate steps, not only endpoint cancellation. Relative
mass residual is normalized by initial mass; zero-source relative energy error
can be undefined, so report absolute joules instead.

Field errors use volume-weighted L1 and L2 and maximum absolute Linf against
300 K; compare the initial and final snapshots and the independent monitor
energy. Review output field names against the script, retaining its full JSON.
The processor reports processed_not_automatically_passed. Its 1e-8 relative /
1e-12 absolute file-consistency tolerances are NOT CFD acceptance thresholds.

Before execution, the reviewer should record absolute temperature, speed,
mass-balance and energy-balance tolerances, considering solver precision,
export precision, inner iteration policy and intended use. Do not choose
thresholds after seeing errors merely to obtain a pass. If tolerances are
not agreed, report diagnostics as unevaluated rather than passed.

Constant density on a fixed mesh makes total mass an insensitive test by
itself: also examine local divergence, spurious speed and absolute local wall
flux. Residuals can begin zero; inspect raw time/inner-iteration histories for
growth rather than demanding an arbitrary residual reduction. A maximum
residual from the Python output does not replace that history review.

| Review decision | Entry |
|---|---|
| Actual run ID / processed output / evidence hashes | |
| Reviewer / date | |
| Accepted tolerances recorded before run | |
| Findings / deviations / disposition | |

H1-A assesses discrete constant-state preservation and implementation only.
It does not prove solution accuracy for nonconstant fields, mesh independence,
time-step independence, sodium physical-model validity, F7 experimental
validation or original scientific novelty. Those are separate later stages.
Do not start H1-B/C/D or reactive modeling on the basis of this preparation.
