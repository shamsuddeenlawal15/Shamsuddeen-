# Initial mesh and resource budget

All allocations below are provisional planning budgets for the user-confirmed
i9-14900HX (24 cores / 32 threads) and 32 GB RAM. No observed memory, elapsed
time, throughput, scalability, mesh quality or numerical accuracy is available.

## Stages and promotion rules

| Stage | Provisional cells | Solver processes | Condition to consider the next stage |
|---|---|---|---|
| R1 initial | 20,000–50,000 | Start at 4; compare 8 if entitled | Setup/quality checks and numerical balances pass; measured memory/time budget acceptable |
| R2 intermediate | 50,000–150,000 | Choose from measured 4/8 comparison | Same physics and mesh-family controls; reliable runtime/memory measurements and useful error comparison |
| R3 later | 150,000–400,000 | Reassess measured 4/8 cost | Only if earlier results justify it and actual available RAM supports it |

A possible uniform cube sequence is 32³ = 32,768, 48³ = 110,592,
72³ = 373,248 cells. It spans these budgets with nominal linear refinement
ratio 1.5. This is an example for the synthetic cube, not a mesh already built,
an F7 mesh recommendation or a mesh-independence criterion. A different actual
topology requires a documented comparable family and effective h = (V/N)^(1/3).

Grid convergence requires observed errors and asymptotic behavior, not reaching
400,000 cells. A coarse analytical test can reveal a coding/setup mistake; a
large grid can retain the same wrong boundary condition.

## Resource measurement protocol on the local computer

1. Record exact build, OS, licensed process allowance, physical/logical CPU
   inventory, available RAM and disk. Keep power mode, cooling conditions and
   competing workloads consistent; record throttling or background jobs.
2. Save a clean initialized case. Start R1 with four actual processes. Separate
   startup/mesh loading/initialization from solver-step and output timing.
3. Record peak memory during mesh generation, loading, initialization and
   solving. Observe both solver processes and whole-system memory/paging.
   On Linux use proportional memory where available; on Windows label working
   set/private-memory measurements. Summed process RSS can double-count shared
   pages and must not be reported as uniquely allocated RAM without explanation.
4. For a fixed physical case, step size and inner settings, record wall time for
   a stated steady workload window (for example 100 subsequent steps after
   startup), plus total physical time advanced, iterations/step and output cost.
   The suggested window is a protocol choice, not an observed timing.
5. Repeat the comparable timing window to characterize variation. Reset from
   the same initial/checkpoint state for each comparison. Verify conserved
   quantities and quantities of interest, not just speed.
6. If licensed, compare eight processes on the same case. Report S = t4/t8
   and relative scaling efficiency S/2, with timing scope stated. This is
   scaling relative to four processes, not a serial speedup.
7. Promote one resource stage at a time. Keep physics/numerics fixed when
   estimating memory scaling; separately repeat mesh/time-step accuracy checks.
   Parallel changes must not quietly change convergence settings or final time.

## Provisional safeguards, subject to actual OS measurements

Use an initial solver-memory planning ceiling of 20 GB, and also retain at
least 4 GB of measured available-memory reserve before additional allocation.
Use the smaller feasible budget; 32 GB installed is not 32 GB free. These are
conservative project choices, not Siemens minimums or a prediction of demand.
Use consistent GB/GiB units from the local monitoring tool.

Pause growth or stop safely if persistent paging occurs, available reserve is
exhausted, the OS becomes unresponsive, or disk/checkpoint capacity is inadequate.
Do not wait for an out-of-memory crash. Observe local thermal/power throttling
when interpreting timing. GPU use is outside this baseline.

If memory is excessive, first inspect duplicate loads, report/output frequency,
rank count and actual physics. Reduce the benchmark scope/count if needed;
do not hide poor conservation or relax accuracy requirements to fit a budget.

A planning fit M(N) = a + b*N can be estimated from two comparable measured
cases, but shared-memory, rank, mesher and solver overhead make it approximate.
Never extrapolate it to a new reacting/multiphase/aerosol model without a pilot.
Estimate transient cost from measured seconds/step and independently justified
time step; no runtime estimate is filled in before actual runs.

## Mesh quality and convergence evidence

**[BUILD CHECK]** Obtain the installed release's mesh validity and quality
diagnostics and document their definitions/recommended limits. Check positive
cell volumes, boundary closure, face orientation, connectivity, skewness,
nonorthogonality, size transitions and any boundary-layer treatment actually
used. No universal undocumented quality cutoff is adopted.

Residuals are recorded with normalization, equation, inner iterations and
time step. Require bounded fields, stable monitored quantities and closed
balances, and verify that tighter inner convergence no longer controls the
reported error. A falling residual alone is insufficient.

For the moving-lid case, inspect the actual convective Courant number and
accuracy at the trial time step; the thermal trial dt is not automatically
suitable for advective transients. For thermal cases record the Fourier number
alpha*dt/h². Implicit stability does not establish time accuracy, and explicit
schemes may require smaller steps for stability. Confirm scheme-specific limits
in the exact-build documentation before execution.

Use a run ledger with these columns, initially blank:
case ID; commit; build; OS; mesh ID/count/h/quality; actual processes;
time step; scheme orders; inner controls; simulated interval;
peak memory method/value; loading time; solve time; export time;
conservation metrics; analytical errors; warnings; operator/date.

See [CFD_Verification_Checklist.md](CFD_Verification_Checklist.md) for the
numerical checks. No row in the future run ledger is populated with fictitious
results by this plan.
