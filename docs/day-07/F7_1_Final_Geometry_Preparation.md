# F7-1 final Day 7 preparation — BLOCKED for definitive construction

“Final” names this review package, not an approved complete experimental model.
Use the shared [CAD register](../../data/day-07/F7_Parametric_CAD_Input_Register.csv)
and [project frame](F7_Coordinate_System_and_Origins.md).

Source-controlled constraints: vessel about 2.2 m high / about 1.3 m diameter;
capacity label 3.0 m³ (not free gas volume); carbon-steel pan area 1.0 m² and
thickness 0.006 m; two insulation thicknesses 0.05 m each. These come from
L2023 p.2 Section 2 / Fig.1 via V001–V007; SI thickness conversions are declared.

Select configuration F7-1: nozzle_height=0.1 m (V008), relative to the pan upper
reference. Nozzle x/y, normal, bore, OD and feed path remain unset. Keep the
0.28 m² final pool observation (V010) separate from geometry-driving inputs.
Shared recorded values do not prove that all missing experimental conditions
were identical in both runs.

## Dependency graph in words

Project frame → pan reference datum → case nozzle elevation reference.
Shared source constraints → reviewed vessel/pan/layer features only after
profiles/dimension conventions are recovered. Case elevation reference → nozzle
placement, then independently checked feed path/roof penetration. Region and
surface names are stable semantic identifiers, not changing face indices.

Unknown profile, bore, pose or thickness values block the affected feature.
Never pass zero/default dimensions to CAD. No top/bottom profile is selected.
A parameter switch alone must not move a vessel, pan or vent. Re-evaluate pipe
length, collision and bounds after changing nozzle height.

No source supports a prescribed 0.28 m² initial burning disk. A future
F7-1_prescribed_area variant must explicitly assign that area as an assumption/
input, describe temporal use, and exclude area from independent validation.
A reduced pool-only model cannot reproduce column-height effects just by
storing h_nozzle in metadata.

## Case acceptance evidence (currently absent)

Record actual datum offset, source-linked body dimensions, volume accounting,
named surfaces, material mapping and no-overlap/connectivity diagnostics.
Retain matching initial/final CAD files and the exact build. Do not mark
accepted based solely on analytical cylinder calculations.

Permitted next design action is the reference datum from the operator guide,
subject to local capability verification and Day 8 approval. Vessel and pan
solid generation remains blocked pending source evidence or a separately
approved provisional model.
