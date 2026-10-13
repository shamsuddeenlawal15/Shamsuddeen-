# H1 nonreactive benchmark plan

Status: design only; no geometry file, mesh, solver case or simulation exists.
This synthetic box is not the F7 vessel or a reconstruction of Fig. 1/2.
Every numerical input below is a proposed researcher-selected benchmark
constant, not an experimental sodium/fire/material value.

## Controlled mathematical problem

Use a sealed cube 0.1 m on each side, with Cartesian coordinates from 0 to
L = 0.1 m. It contains a single incompressible, constant-density, nonreactive
gas surrogate. There is no gravity, turbulence, radiation, sodium, phase
change, aerosol, species chemistry or buoyancy in H1.

| Synthetic parameter | Proposed value | Purpose |
|---|---|---|
| Density rho | 1 kg/m³ | Fixed mathematical density |
| Dynamic viscosity mu | 0.001 Pa·s | Laminar momentum benchmark |
| Heat capacity c | 1000 J/(kg·K) | Thermal storage coefficient in the equation below |
| Thermal conductivity k | 0.1 W/(m·K) | Constant thermal diffusivity alpha = 0.0001 m²/s |
| Initial reference temperature T0 | 300 K | Synthetic reference state |
| Initial velocity | Zero | Quiescent thermal cases |
| Gauge pressure reference | 0 Pa at the documented reference constraint | Pressure null-space constraint, not a measured absolute atmosphere |
| Initial trial time step / final time | 0.1 s / 10 s | Proposed baseline; refinement required |

The thermal equation to reproduce is
`rho*c*(dT/dt + u·grad(T)) = k*Laplacian(T) + q_vol`.
**[BUILD CHECK]** Verify that the selected constant-density thermal model
reduces to this equation for the quiescent tests, with no additional work,
radiation or dissipation source. Here c is the specified thermal-storage
coefficient. Do not switch to a closed ideal-gas heating problem and apply the
same heat-capacity formula: a compressible constant-volume system requires
internal-energy/cv accounting and pressure evolution. If the selected build
cannot realize this surrogate as specified, revise the benchmark before running.

All walls are impermeable. Thermal tests use stationary no-slip walls and
zero normal heat flux on all six faces. No pressure outlet belongs in this
sealed case. **[BUILD CHECK]** Set the solver's supported closed-domain
pressure reference without opening a boundary.

## Four separate cases

| Case | Initialization and forcing | Reference/check | What it tests |
|---|---|---|---|
| H1-A constant field | T = 300 K, u = 0, q_vol = 0; adiabatic stationary walls | T remains constant, velocity remains zero, mass remains rho*V | Basic field preservation and setup consistency |
| H1-B prescribed heating | Same start; uniform q_vol = 100 W/m³ | Uniform T(t) = 300 + 0.1*t K; total imposed power = 0.1 W | Source units/sign, thermal storage and energy accounting |
| H1-C diffusion decay | T(x,0) = 300 + 1*cos(pi*x/L) K; u = 0; q_vol = 0; adiabatic walls | T(x,t) = 300 + cos(pi*x/L)*exp[-alpha*(pi/L)²*t] K | Nontrivial spatial and temporal discretization accuracy |
| H1-D moving lid | Isothermal 300 K; top wall moves tangentially in +x at 0.1 m/s; others stationary; no normal mass flow | Global inventory plus local divergence/continuity and rank-to-rank consistency; Re = rho*U*L/mu = 10 | Mass accounting under nonzero internal transport and resource timing |

H1-D is a separate synthetic lid-driven cavity, with edge velocity
discontinuities documented. It has no asserted analytical velocity reference.
It must not be presented as a validated cavity-flow solution solely because
global mass remains constant. **[BUILD CHECK]** Confirm tangential moving-wall
support and energy-off/isothermal configuration. Thermal accuracy claims come
from H1-C, not this flow case. Stationary-wall H1-A/B/C do not assess advection
accuracy; a later advection benchmark would be needed if that is claimed.

For finite-volume cells, compare H1-C with analytical **cell averages** where
possible, including initialization, rather than mixing cell-center references
with volume-average stored unknowns. For a rectangular x interval [a,b], the
average cosine is `L*(sin(pi*b/L)-sin(pi*a/L))/(pi*(b-a))`.
For general cells, use adequate quadrature and quantify its error. Do not let
analytical sampling error dominate a claimed convergence trend.

The expressions and numbers above are analytical predictions and input design,
not calculated CFD outputs or measured accuracy.

## Version-dependent setup sequence (2024 or earlier target)

Each numbered step is **[BUILD CHECK]**: exact feature names, availability,
menu paths, API and file behavior require the installed release manual.

1. Create an isolated local benchmark project and record the exact build and
   software/license evidence from the version checklist. Use SI units.
2. Define the synthetic box, one fluid region and six named boundaries. Verify
   volume, face areas and normals. No F7 geometry file is to be imported.
3. Select a supported structured or comparable hexahedral mesh route. Begin
   within 20,000–50,000 cells; capture actual cell count and quality statistics.
   Preserve a systematic mesh family for H1-C; do not use unrelated mesher
   settings solely to hit a count.
4. Select 3-D transient laminar constant-density flow with the stated material
   constants. Enable the compatible thermal equation for A/B/C; disable
   buoyancy and all unneeded physics. Document pressure reference and solver
   coupling, gradient/reconstruction and temporal/spatial orders.
5. Set stationary impermeable adiabatic walls for A/B/C; establish H1-D in a
   separate saved case using the documented moving-wall control.
6. Enter initial temperature fields through the supported initialization/field
   expression route. Check units and, for C, cell-average consistency.
7. Enter B's heat source using the documented energy-source interface. If it
   expects W/kg, convert q_vol/rho explicitly; verify the volume integral.
8. Create supported integral reports/monitors for volume, mass, wall mass flux,
   thermal inventory, imposed power, boundary heat flow, extrema, residuals
   and local continuity measures. Export time and units with all reports.
9. Configure transient stepping and inner convergence controls. Start with
   dt = 0.1 s only as a trial; compare 0.1/0.05/0.025 s on a fixed mesh and
   perform the separate mesh series with sufficiently controlled temporal error.
10. Request four processes first, confirm actual count in the startup log, and
    later compare eight only if entitled. Save a clean initial state for every
    comparable trial; preserve build, mesh, input and run-log identifiers.

Do not infer that a field-function display automatically supplies a conservative
source term. No guessed Java macro or release-specific batch command is supplied.
Use the exact build's supported export, source, initialization and report paths.

## Relationship to F7

Louie et al. (2023), p.2 §2/Fig.1 and p.3 Fig.2, describe a ventilated
sodium-fire apparatus and numerical heat structures. H1 is sealed and nonreactive.
Their final pool areas, nozzle heights and combustion curves are not benchmark
inputs. Passing H1 only permits discussion of the next reviewed readiness stage.
It cannot close initial-condition, property, oxide, reaction or sensor gaps.
