# Missing data, proposed assumptions and review decisions

Day 1 document review is accepted. No new experimental default or modeling
assumption is accepted by this Day 2 package. All source-absence statements
below refer to the accessible L2023 article, not to the unread original reports.
Source IDs resolve through [Source_Verification_Report.md](Source_Verification_Report.md).

## Input gaps and consequences

| Priority / input | Evidence location and present knowledge | Consequence | Required closure |
|---|---|---|---|
| P0 original F7 procedures and data | L2023 p.4 cites F1998; p.4 says data on request | Full reproduction cannot be specified or statistically validated | Obtain F1998 and raw series/uncertainty with permission |
| P0 model equations/context | L2023 pp.2–3 Eqs.1–3; two Day 1 transcription errors corrected | Implementing the old forms gives an incorrect source model | Approve equation audit; read S2021; resolve m/C1/C2 and DAB mapping |
| P0 sodium inlet state | L2023 p.2 gives only average 3.3 g/s and 1500 s; no temperature/purity/nozzle bore | Sensible energy, jet momentum and impingement unknown | F1998 source temperature history, mass-flow history and nozzle drawing |
| P0 atmosphere and ventilation state | L2023 p.2 ~3.0 m³/min; no gas T/p/O2/humidity or volumetric reference state | Density, oxygen inventory and inlet velocity undetermined | Recover gas composition/state, flow reference and port area |
| P0 sodium/steel/insulation properties | L2023 pp.2–3 material classes/symbols only | Energy and spreading closures incomplete | Verified property sources with units, ranges and uncertainty |
| P1 vessel/head/pan geometry | L2023 p.2 Fig.1 vs p.3 Fig.2 | Heat areas cannot directly define all CFD volumes | Primary drawings; internal dimensions; pan planform, support and gap |
| P1 thermal structure materials | Carbon-steel pan p.2; stainless hatch p.3 | Heat storage/conduction could be assigned to wrong material | F1998 construction and S2021 input thermal structures |
| P1 insulation and contacts | Two 50 mm layers, L2023 p.2 | Thermal losses unidentified | Material grade, contact resistance, extent and external boundary conditions |
| P1 inlet/outlet loss and locations | Fig.1 schematic only, p.2 | Asymmetry, pressure and residence time uncertain | Port dimensions, elevations, exhaust loss and pressure boundary |
| P1 pan/solid initial temperatures | Absent from L2023 pp.2–3 | Transient heating may dominate early comparison | Initial fields and preheat protocol |
| P1 ignition and time zero | Discharge phase shown; no complete trigger protocol | Curves may be misaligned | Event definition, acquisition trigger, any heater history |
| P1 spreading state | Final areas 0.28/0.30 m², L2023 p.2 | Area history/contact/wetting not recoverable from final area | Time-resolved footprint, depth, residual inventory and model calibration basis |
| P1 oxidation/oxide coefficients | Table 1 p.2 and Eqs.1–3 pp.2–3 define symbols without values | Rate, product partition and feedback underdetermined | C1/C2, epsilon basis, Sh, delta/Delta_l, DAB/FNA2O/FNA2O2/FO2/FHEAT |
| P1 reaction enthalpy/radiation | No numbers in L2023 pp.2–4 | Energy source and heat losses cannot close | Phase-specific enthalpy, emissivity and radiation closure |
| P1 instrument locations | Fig.4 p.4 gives r=0.1/0.2/0.24 m | Radial coordinate alone does not define a probe | Height/depth/azimuth, sensor type, response, calibration and uncertainty |
| P1 aerosol measurement/model | Fig.5 p.4 gives vessel and exhaust observations in g-Na/m³ | Sodium-equivalent aerosol mass differs from oxide mass | Sampling locations, size distribution, composition, losses and processing |
| P1 solver and PC resources | User says availability exists; no specifications supplied | No runtime, cell budget or compatible setup can be promised | Exact release, OS, CPU, RAM, GPU, disk and entitlements |

P0 means it blocks credible full-test specification now. P1 does not mean an
optional input: these gaps also block full reproduction, though some can be
excluded deliberately from a narrower approved benchmark.

## Proposed reduced-model assumptions — all pending review

| Proposal | Why useful | Limitation / approval condition |
|---|---|---|
| Idealized vessel with prescribed heated/reacting patch | Establish heat/mass conservation at small cost | A benchmark; cannot claim exact F7 apparatus reproduction |
| Prescribed pool area or published terminal-area cap | Isolates transfer physics | Area supplied from experiment is a calibration/input; cannot validate predicted area independently |
| Prescribed mass/energy source before predictive chemistry | Tests coupling and units | Matching a curve supplied as an input is not validation of combustion |
| Initial use of a lumped pool instead of resolved liquid | Reduces stiffness and computational cost | Omits film/jet/impingement and spatial sodium temperature |
| Exclude falling-column oxidation in first reduced model | Focuses on pool equations | Nozzle-height difference then has no predictive mechanism; cannot explain F7-1/F7-2 differences merely by relabeling runs |
| Idealized symmetry where a benchmark permits it | Reduces cost | Side inlet/outlet and instrumentation asymmetry prevent asserting full apparatus symmetry |
| Scalar aerosol mass before size-resolved aerosol physics | Checks Na-equivalent conservation | No particle-size/deposition/agglomeration prediction; Fig.5 scope limited |
| Use source-backed property law with stated validity interval | Reproducible and auditable | No extrapolation, fixed room-temperature value or mixture law silently adopted |

No default atmospheric pressure, oxygen percentage, room temperature, steel
grade, sodium inlet temperature, empirical coefficient or measurement error has
been entered as an experimental input. The user has not supplied enough PC
details to select a resource tier.

## Decisions for scientific review

1. Accept the equation corrections, while retaining the missing definition of
   m and all calibration questions as unresolved.
2. Choose a first reduced benchmark from the model hierarchy and explicitly
   declare its assumptions and excluded validation claims.
3. Prioritize lawful acquisition of F1998/S2021 and an authoritative property
   source; approve any author contact separately if desired.
4. Define calibration versus held-out validation use. Because both F7 tests
   have already been inspected, a later F7-2 check is held-out in fitting only,
   not a genuinely blind prediction of unseen evidence.
5. Supply the installation/hardware facts and official documentation needed
   to close the version/license gate.

Detailed geometry, meshing and physical-model construction remain paused until
these remaining assumptions are reviewed. There are no CFD outputs in Day 2.
