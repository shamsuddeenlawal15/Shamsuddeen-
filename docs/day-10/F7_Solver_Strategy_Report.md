# Transient solver strategy — pending implementation

No solver is configured or run. Geometry/mesh approval, local model capability,
properties and initial/boundary data are missing. Recommended controls here
are a review framework, not executable settings.

## Temporal formulation

Use transient analysis for eventual F7 evolution: finite sodium discharge,
pool spreading, oxide accumulation and thermal storage cannot be represented
by a single steady state. A future steady nonreactive precursor could only
initialize a justified ventilation state; it would not reproduce the fire
transient and is not executed now.

For later Stage 1, assess a pressure-based segregated transient approach with
conservative gas energy and solid conduction. Exact temporal/spatial schemes,
coupling, relaxation and inner iteration policies must be recorded from the
actual build. Do not silently take defaults or borrow H1's 0.1 s time step.

Choose initial dt from resolved cell lengths and relevant time scales:
advective time h/U, thermal diffusion time h²/alpha (alpha=k/(rho*cp)), source
variation times and, for future Stage 2/3, reaction/interface/particle scales.
Evaluate local Courant and Fourier measures with actual mesh/properties.
Implicit stability does not imply accuracy; no universal target or dt is
assigned while scales are unknown.

Perform a short authorized pilot only after prerequisites are satisfied, then
a separate dt, dt/2, dt/4 comparison at common physical times with fixed mesh/
models and controlled inner error. That later verification is not part of
Day 10. Event times such as discharge termination need adequate resolution;
1500 s is a source duration, not an authorization for a long run.

## Convergence and conservation

Record full continuity, momentum, energy and later species residual histories,
including normalization and inner iteration counts. Set observable-specific
absolute/relative tolerances before judging data. Require mass/energy balance,
stable monitored quantities and consistent fields, not residual reduction alone.
A constant-state verification case may start near zero residual.

For an open-domain mass audit use
R_M=M(t)-M(0)+integral(m_dot_out dt)-integral(S_mass dt),
where boundary mass flux is signed outward and S_mass is internal net addition.
Do not count a feed both as a boundary inflow and internal source. Reaction
conserves total mass across all represented phases but may transfer mass
between gas, liquid and deposited products.

For energy audit include gas and solid/optional liquid inventories, signed
advective energy fluxes, exterior heat, prescribed/chemical sources and any
work terms required by the selected formulation. Use consistent phase enthalpy
references and avoid counting reaction heat both via formation enthalpies and
an added heat source. Internal conjugate heat fluxes must cancel over paired
sides. Do not compare gas energy alone with whole-apparatus heat input.

Stage 1 verification priorities: constant field, zero/unforced flow as a
synthetic limit, prescribed open-flow mass balance, analytical conduction/
CHT heat balance and time/mesh sensitivity. Check interface equal/opposite heat
rates and thermal contact resistance limits with a documented test setup.

## Safety stops and resource policy

Stop a future pilot for invalid cells, nonfinite/unbounded fields, unexplained
mass/energy drift, interface leakage or exhausted memory. Do not relax accuracy
criteria to fit 32 GB. Start with four processes only if local entitlement
supports them; record actual ranks and measured resource use. Day 9 resource
numbers remain uncalibrated scenarios, not observed solver performance.

All actual dt, tolerances, relaxation values, iteration limits, process count,
runtime and convergence results remain unset. No sodium/oxygen reaction,
aerosol, radiation or long transient calculation is activated.
