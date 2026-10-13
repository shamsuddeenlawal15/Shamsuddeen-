# CFD verification checklist

Status of every solver check: **planned, not executed**.
The documentation and data tests in this repository are not CFD tests.

## Four distinct claims

| Activity | Question | Required evidence | Day 3 status |
|---|---|---|---|
| Solver verification / solution verification | Does the configured discretization reproduce known equations, and is numerical error controlled? | Analytical H1 tests, balance audits, grid/time refinement and controlled iteration error | Planned; no results |
| Physical-model implementation verification | Are sodium/oxide/spreading equations and conservative couplings implemented as intended? | Authoritative equations/units; limiting cases; elemental/energy tests; source coupling audit | Source gaps remain; no implementation |
| Experimental validation | Does the reviewed model reproduce F7 observables within characterized uncertainty? | Raw/derived data provenance, sensor definitions, uncertainty, matching observables and held-out comparisons | Not started |
| Original research development | Does a new model or analysis establish a defensible contribution? | Reproduced baseline, novelty review, controlled hypothesis test and independent evidence | Future roadmap only |

Passing a subset of H1 is evidence about that configuration, not complete
verification of the commercial solver or sodium-fire physics.

## Required tests and recorded quantities

- [ ] **Constant-field preservation (H1-A):** record maximum temperature drift
  from T0, maximum spurious velocity, pressure behavior and inventory drift.
  Use absolute errors and declared scales because the reference velocity is zero.
- [ ] **Mass conservation (all cases, especially H1-D):** M(t) = integral rho dV.
  With outward wall mass flux F_out and volumetric mass source S_m, check
  R_M = M(t)-M(0) + integral(F_out)dt - integral(S_m)dVdt.
  Both source and net boundary flow are zero in these cases. Report absolute
  and M(0)-normalized imbalance, wall leakage and local continuity/divergence.
  Constant density in a closed fixed volume can make global mass trivial;
  H1-D's nonzero internal flow and local balance are needed to avoid treating
  that identity alone as a meaningful flow verification.
- [ ] **Prescribed heat balance (H1-B):** define E = integral rho*c*(T-T0)dV
  for this synthetic thermal equation. With Q_in positive into the domain,
  R_E = E(t)-E(0) - integral(Q_vol+Q_in)dt should be small.
  Here Q_in=0 and Q_vol=q_vol*V. Check the predicted uniform slope, spatial
  spread and full energy ledger; do not equate source-entry value to verified
  integrated power without a report. Normalize by integrated imposed heat
  for t>0; use absolute error at t=0.
- [ ] **Spatial refinement (H1-C):** compare at common physical times using
  volume-weighted L1/L2 and maximum temperature errors against the analytical
  cell-average solution. Keep temporal and iterative errors small enough to
  isolate spatial trends. Use at least three systematically refined meshes
  when estimating an order; record actual h and mesh differences.
- [ ] **Transient time-step refinement (H1-C):** on a fixed sufficiently
  resolved mesh use trial dt = 0.1, 0.05, 0.025 s, common final time 10 s and
  consistent scheme/inner convergence. If spatial/initialization errors mask
  time error, revise the experiment; do not claim a temporal order from a plateau.
- [ ] **Iteration-error separation:** tighten inner convergence or increase
  iterations per step on representative runs until the quantities/error trends
  of interest are insensitive at the declared tolerance.
- [ ] **Process-count consistency:** repeat the same case with four and eight
  ranks only if licensed; compare balances and errors within the predeclared
  floating-point/numerical tolerances, not necessarily bitwise equality.
- [ ] **Mesh validity:** attach actual diagnostic distributions and check
  counts from the exact build; resolve invalid cells before solving.

H1-B's uniform field may be integrated exceptionally accurately even on poor
meshes. Use H1-C's nonuniform diffusion mode for refinement evidence. A mass
or heat balance can close while the local solution is inaccurate; require both
balances and analytical field comparisons.

For constant refinement ratio r and errors E(h), an observed order can be
estimated as log(E_coarse/E_fine)/log(r) only when the error is above noise and
the asymptotic regime is supported. If differences oscillate or orders are
inconsistent, report them and investigate. Richardson extrapolation/GCI
requires its assumptions and adequate systematic data; cell-count bands alone
do not justify either.

## Acceptance decision before actual runs

Choose and record numerical tolerances, reference scales and the rationale
before inspecting final results. Consider precision, scheme order, the
analytical error budget and intended future accuracy. No experimental
uncertainty value exists here to justify a fabricated tolerance.

A test may be recorded as PASS/FAIL only after attaching the case inputs,
exact build, mesh, time-step sequence, raw monitor exports, calculation method
and error values. Until then its status stays PLANNED. Failed, aborted and
inconclusive cases must remain in the ledger.

## Equation and source gate carried forward

Use the Day 2 [equation audit](../day-02/Equation_Transcription_Audit.md),
not the archived Day 1 transcription. Louie et al. (2023), p.2 Eq.1 has
beta/nu²; p.3 Eq.2 prints undotted m³, with m undefined by the adjacent prose.
Eq.3 on p.3 has mu = mu0*exp(2.5*C2*epsilon), with coefficient and fraction
basis unresolved. C1/C2, Sherwood closure, oxide evolution, DAB mapping and
the physical meaning of m still require SAND2021-0136 and its cited sources.
No sodium equation is implemented by H1.
