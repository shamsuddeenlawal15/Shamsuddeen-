# STAR-CCM+ model selection for a personal computer

Day 2 decision: begin with a reduced, conservation-tested pool model after the
scientific review gate. Full F7 reproduction remains conditional on source
closure, release-specific solver documentation, a suitable license, and a
measured computer resource budget. No STAR-CCM+ installation was accessed and no
model, mesh, or simulation was created or executed during Day 2.

## Evidence and compatibility boundary

The physical requirements below come from the supplied Louie et al. (2023)
paper, DOI `10.1016/j.nucengdes.2023.112285`:

- PDF/printed p. 2, Section 2 and Fig. 1: ventilated vessel, falling sodium
  column, pan, insulation, and different nozzle heights in F7-1/F7-2.
- P. 2, Table 1 and Eq. (1): oxygen transfer, oxide retention, product split,
  heat partition, and oxide resistance require explicit definitions.
- P. 3, Eqs. (2)–(3) and Section 3.2: changing pool area, oxide-modified
  viscosity, SPHINCS flame-sheet conservation, and radial/depth pan conduction.
- Pp. 3–4, Section 4 and Figs. 3–5: combustion-rate, pool-temperature, and
  aerosol comparisons; post-discharge oxide effects remain unresolved.

These are evidence for what must be represented, not evidence that a particular
STAR-CCM+ release implements it. Official Siemens product, support, and release
page requests failed with proxy `CONNECT` HTTP 403, including escalated retries.
No vendor page body or release manual was retrieved. See the installation
checklist for the exact attempted URLs and the required vendor-document checks.
All STAR-CCM+ implementation choices here are **engineering candidates**, with
compatibility and license entitlement **unverified for 2024 or earlier**.

Use one exact installed version/build dated 2024 or earlier for any later work.
Do not assume a model, expression interface, user-code API, example, or macro
documented for a newer version exists in that build. General product capability
and an enabled feature in the user's license are separate questions.

## Candidate physics and required evidence

| Physical requirement | Candidate implementation to check in the selected release | Data and technical conditions | Day 2 disposition |
|---|---|---|---|
| Ventilation and buoyant gas flow | Transient finite-volume gas flow, gravity, temperature-dependent mixture density; evaluate laminar and Reynolds-averaged closures | Inlet/exhaust dimensions and direction, reference state of volumetric flow, gas temperature/pressure/composition; justify turbulence treatment after obtaining properties and dimensions | Conceptual approach only; geometry and initial states incomplete |
| Pan, wall, and insulation heat transfer | Fluid/solid conjugate heat transfer with interfaces, or a documented thin-solid/thermal-resistance approximation where defensible | Resolve physical pan versus numerical bottom head; steel grades, conductivity, heat capacity, density, contact resistance, external losses | Pan radial/depth conduction is supported by p. 3; release-specific solid/interface controls unverified |
| Oxygen and sodium-related transport | Multicomponent gas species and consistent diffusive fluxes; include sodium vapor only when demanded by the selected flame model | Gas species set, mixture property rules, diffusion correlation, pressure dependence and reference states | Species transport is required by the physical problem; no bundled sodium material/reaction mechanism established |
| Sodium oxidation at a pool | Coupled surface mass/energy fluxes or a verified heterogeneous reaction interface; otherwise conservative source coupling to a reduced pool balance | Oxygen-limited transfer/kinetics, oxide resistance, product split and reaction enthalpy; surface/volumetric units, signs, and sink/source pairing must be demonstrated | Native sodium-pool-fire capability is not established; no executable reaction model selected |
| Pool temperature and retained inventory | External or in-solver reduced mass/energy balance coupled to surface fluxes and pan conduction | Inflow enthalpy, reacted/retained/airborne sodium, pool-to-gas heat split and heat losses | Proposed first reactive implementation if supported coupling can be verified |
| Spreading pool | First prescribe area as a sensitivity scenario, then consider a reviewed reduced spreading law; free-surface multiphase flow only at a later gate | Time-dependent experimental area, wetting/contact-angle data, surface tension, viscosity, oxide rheology, inflow geometry | Final area alone does not determine area history. Eq. (2) transcription/dimensions and coefficients require resolution before implementation |
| Radiation | Surface radiation initially; participating-media treatment only with justified gas/aerosol optical properties and a compatible release model | Sodium/oxide/steel emissivity and its evolution, optical path and aerosol size/composition | Do not silently omit radiation from an F7 energy balance; an omission is an explicit approximation requiring assessment |
| Aerosol generation and transport | Begin with a transported aerosol-mass surrogate; progress to a verified particle/sectional or moment method only if needed and supported | Source composition and release fraction, particle size/distribution, agglomeration, settling, wall deposition, exhaust sampling response | Mass surrogate can test conservation but cannot establish size-dependent deposition or full Fig. 5 validation |
| Falling sodium stream | Reduced delivery condition for initial pool studies; multiphase jet/droplet treatment only if justified by evidence | Nozzle bore, flow history, temperature, stream breakup/oxidation, impact location and momentum | F7-1/F7-2 nozzle heights differ; omitting stream effects prevents claiming complete experimental reproduction |

An interface that can display a spatial field does not necessarily permit
time-dependent conservative source coupling or a moving wet footprint. Verify
the selected release's field-function, table, macro, and compiled-user-code
interfaces against the required update frequency and parallel behavior. A Java
macro that edits setup is not by itself a reaction solver. Do not represent
condensed sodium oxides as ideal-gas species simply to use a gas chemistry tool.

## Resource-gated model hierarchy

Every tier below is a proposal for later reviewed work. None has been run.

| Tier | Intended question and scope | Why it is useful on a PC | What it cannot establish | Promotion gate |
|---|---|---|---|---|
| H0: zero-dimensional balance and property checks | Verify units, stoichiometry, elemental balances, heat accounting, source limits, and property ranges with a small reproducible utility | Separates closure mistakes from CFD cost; no mesh required | Chamber flow, spatial temperatures, or F7 validation | Authoritative property/chemistry evidence and all limiting-case checks pass |
| H1: nonreactive thermal/flow benchmarks | Later use an analytical conduction case and a prescribed thermal source/ventilation case to test solver coupling and reports | Small transient runs can measure memory and runtime before adding uncertain chemistry | Sodium burning, measured aerosol concentration, or reproduction of F7 | Installed-version tutorial/example and conservation checks pass; PC pilot budget accepted |
| H2: fixed-area pool surrogate | Couple oxygen supply, simplified pool inventory/temperature, and pan heat transfer at a declared fixed area | Avoids resolving a moving liquid surface; isolates transfer and heat partition | Early spreading, stream combustion, oxide dynamics, or a full F7 history | Boundary/initial inputs reviewed; source coupling verified; numerical error assessed |
| H3: reduced F7 reproduction candidate | Add reviewed evolving area and oxide closures, documented chamber/vents, pan conduction, and an aerosol mass balance where warranted | Concentrates computing on gas/solid fields while keeping thin pool dynamics reduced | Resolved wetting, stream breakup, particle size distributions, or unsupported deposition physics | F7 input gaps resolved or bounded; calibration/validation split fixed; model-form limitations explicitly accepted |
| H4: high-detail experimental reproduction candidate | Consider resolved free surface/stream, coupled oxide evolution, radiation and size-dependent aerosols only for a specific unresolved observation | May be attempted only if incremental benefit and measured resource cost justify it | Automatic predictive validity; more detail alone supplies no missing experimental data | Authoritative closure data, installed capability, numerical verification and PC runtime all demonstrated |

H1 is a **solver benchmark**, H2 is a **reduced sodium-fire study**, and H3/H4
are only **candidates for F7 reproduction**. A sector or axisymmetric gas model
may be a preliminary benchmark if its symmetry is explicitly imposed; the
schematic ventilation/stream arrangement must not be declared axisymmetric from
the vessel outline alone. A radially reduced pan model also does not prove that
the surrounding gas flow is axisymmetric.

Fixed final areas from p. 2 (0.28 m² and 0.30 m²) may define declared surrogate
cases; they must not be relabeled as measured initial areas or time histories.
Prescribing each test's measured final area makes that part of the calculation
data-informed, not an independent prediction of spreading. The plotted
0–3600 s range in Figs. 3–5 is a figure range, not a separately verified test
termination or a mandated simulation duration.

## Conservation and comparison contract

Before a reactive CFD run, define a single sodium inventory ledger: inlet,
unreacted pool, retained oxide, airborne oxide, deposited oxide, and exhaust.
Track sodium elements and oxygen elements independently of oxide compound
mass. Pair gas oxygen sinks with oxide production and heat release exactly once;
define whether released reaction energy is handled by species enthalpies or an
explicit heat source to prevent double counting. Pool/gas heat partition must
sum consistently with the total reaction and sensible-enthalpy accounting.

Fig. 5 reports `g-Na/m³`, not total sodium-oxide compound mass per volume
(Louie et al., 2023, p. 4). A later model must convert each oxide mass to its
sodium-equivalent mass using its chemical composition before comparing with
that figure. Document whether reported aerosol concentration is vessel average,
probe value, or exhaust-duct sample; those observables are distinct. Particle
deposition requires a receiving surface inventory if conservation is claimed.

Define later verification cases for zero sodium supply, zero oxygen supply,
closed inventory, imposed heat input, and mesh/time-step refinement. Numerical
residual convergence alone is insufficient. Select conservation and numerical
uncertainty tolerances before result inspection and justify them relative to
available experimental uncertainty; no measured error or tolerance is supplied
by this Day 2 document. Missing property ranges, reaction constants, and
measurement uncertainties remain explicit gates.

## PC execution decision

The first practical target is H0 followed by an approved H1 pilot. Use CPU
execution as the planning baseline until the exact release, physics combination,
hardware, and license establish accelerator support. Do not assume a GPU is
required or that it accelerates sodium chemistry, multiphase flow, or particles.

Measure peak process memory and wall time on the user's actual machine after
the review gate. For two comparable pilot mesh sizes, an empirical incremental
memory estimate is `b = (M2 - M1) / (N2 - N1)` bytes/cell, with intercept
`a = M1 - b*N1`; `M(N) = a + b*N` is a planning approximation only for the
same physics and process count. Particle, radiation, interface and solver
storage can invalidate the estimate. Budget operating-system memory, output
storage and checkpoint copies separately and retain a measured reserve.

Estimate transient runtime from measured step cost, required physical duration,
and the independently justified time step; a smaller computer does not justify
a physically inadequate step. Reduce model scope or use sequential sensitivity
cases when the budget fails. H4 may be impractical on the eventual PC, but no
hardware inventory or pilot evidence currently establishes that conclusion.

## Required next review

Approve the reduced-model scope, the source/data gap dispositions, and the
version/license evidence before selecting detailed geometry, meshing, reaction
implementation, or free-surface construction. Day 2 ends at that review gate.
