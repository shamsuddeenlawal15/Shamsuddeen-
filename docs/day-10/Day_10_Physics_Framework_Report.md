# Day 10 physics framework — documentation only

Date: 2026-10-14 (Asia/Shanghai).
Baseline verified locally and on origin: research/day-9-f7-mesh-readiness,
04aee3217fe9393db17ba86712a4d868892ecafb; initial worktree clean.
Branch: research/day-10-f7-physics-framework.

**Physics setup readiness: BLOCKED.** The framework is prepared for review,
not instantiated in STAR-CCM+. No geometry/mesh approval or local model evidence
has been supplied. All activation/assignment fields explicitly remain “no”.

## Day 9 review and prerequisite findings

Read all nine requested Day 9 deliverables, including both CSVs.

| Required confirmation | Finding |
|---|---|
| Geometry ready for assignment | Cannot confirm: actual head/wall/pan/nozzle/vent geometry and CAD approval missing |
| Computational regions defined | Nine candidates documented; no created/approved regions |
| Mesh supports physics | Only hypothetical budgets/strategy; no generated mesh, wall resolution or quality evidence |
| Uncertainties recorded | Geometry, material data, initial/boundary states, source closures and exact-build controls remain open |

The Day 9 equivalent length and RAM scenarios are not observed meshes or
physics-capacity guarantees. New chemistry/particle fields could increase memory.
No continuum is assigned merely to make a placeholder look complete.

## Staged scientific hierarchy

| Stage | Proposed scope | Gate to entry / exit |
|---|---|---|
| 0 | Geometry and mesh verification only; no physical simulation | Obtain real CAD/mesh, source/assumption signoff and native quality evidence |
| 1 | Nonreactive thermal-fluid and conjugate-interface verification | Stage 0 approved; documented synthetic test conditions or verified F7 nonreactive conditions; source-backed properties and local models checked |
| 2 | Sodium oxidation with consistent pool/feed/energy bookkeeping | Stage 1 verification accepted, mechanism/closure data reviewed, conservation/unit tests passed; no reaction enabled now |
| 3 | Aerosol generation/transport/deposition | Only after combustion behavior is validated; source/size/partition/measurement basis verified |

Stage 1 separates a deliberately synthetic verification problem from
experimental F7 reproduction. H1 remains its own earlier workstream; neither
H1 properties nor its zero-gravity/300 K initialization is an F7 fact.
A synthetic CHT test can later verify interface conservation without claiming
an experimental thermal result. Its temperatures/properties/sources require
an explicit test specification, not silent default values.

Stage 1 exit evidence should cover constant-state preservation, open-domain
mass balance, a prescribed heat balance and an analytical solid/contact
conduction case with transient and mesh refinement where appropriate. These
are planned tests, not simulations performed here.

## Architecture and scientific distinctions

Gas flow/energy and four material-specific solid conduction continua are
proposed. Coupling is an interface requirement, not an extra fluid material.
A reduced sodium pool may be a surface model rather than a liquid region.
Air inlet/exhaust may be boundaries rather than separate duct regions.

Wall–pan direct contact is not established: keep that interface conditional.
Insulation–external is an external boundary unless an actual second region is
documented. Do not equate contact naming with physical connectivity.

Geometry verification concerns source shapes/topology; mesh verification
concerns discrete representation; physical-model verification concerns equation/
closure implementation; experimental validation compares independently predicted
quantities with measurements and uncertainty. None is established by a framework.

## Source basis and preservation

L2023: Louie et al. (2023), “Validation study of sodium pool fire modeling
efforts in MELCOR and SPHINCS codes,” Nuclear Engineering and Design 407,
112285, DOI 10.1016/j.nucengdes.2023.112285. Section 2 p.2 identifies apparatus/
operating quantities; p.2 Table 1 and Eq.1, p.3 Eqs.2–3/Section 3.2, and
pp.3–4 Section 4/Figs.3–5 motivate future model requirements.
The Day 2 property register and corrected equation audit were reviewed.
No new primary-report retrieval or source-backed property correlation is claimed.

Preserve prior records and corrected equations. All 27 material-property entries
have empty numeric values/correlation fields pending sources; material families
alone do not determine properties. Availability and license requirements for all
15 model/requirement entries are unverified for the local patch/build.

Monitor definitions distinguish gas/pool/wall temperatures, flow, conservative
inventories/fluxes, future Na/O2 sinks and later aerosol concentration. L2023
p.4 Fig.5 uses g-Na/m³: converting to kg-Na/m³ divides by 1000, but converting
to oxide mass or particle number needs product/size information, not a unit
change alone. Fig.4 temperatures are in degrees C; future K exports require
documented comparison-unit conversion. No measurement values or plots are made.

## Exact first Day 11 operation

Perform the prerequisite evidence intake: obtain the actual local CAD and mesh
files/reports, hashes, full build and scientific geometry/mesh signoff; reopen
the identified model locally to reconcile the region inventory. If unavailable,
continue geometry/mesh/source recovery, not continuum or reaction activation.
Only after those gates and property/BC review may a later authorized Stage 1
setup proceed. No Day 11 work begins here.
