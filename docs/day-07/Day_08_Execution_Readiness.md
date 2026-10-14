# Day 8 execution readiness — not started

## Final Day 7 assessment

| Operation / scope | Readiness | Reason |
|---|---|---|
| Project coordinate convention and mathematical pan reference datum | APPROVED for this narrowly defined design operation | A reference plane/triad is a project convention, not invented apparatus |
| Parameter bookkeeping and F7-1/F7-2 height selection | APPROVED as specification | Heights supported; does not create a nozzle body |
| Executing datum creation in local 2402 | CONDITIONAL | Verify actual build, documented controls and local license availability first |
| P0 idealized diagnostic envelope | CONDITIONAL, not execution-approved | Explicit assumptions need separate engineering review |
| Definitive vessel/pan/nozzle/vent CAD | BLOCKED | Essential shape, position and dimensions unknown |
| Full F7 geometry / mesh / physical simulation | BLOCKED | Source, CAD and later numerical/physics gates unresolved |

APPROVED here does not imply external scientific signoff or approval of all
F7 geometry. Day 8 must be separately authorized; no CAD operation ran on Day 7.

## Exact first construction step

After local release/control verification and authorization, create **one
nonphysical datum plane named Pan_Top_Reference at z=0 in
F7_PROJECT_CARTESIAN**, with right-handed X/Y horizontal and Z upward.
Origin is the vessel reference-axis intersection with that plane; no pan
centroid, outline or vessel floor position is asserted.

Required inputs: the approved project frame, metre units and confirmed local
datum-creation control. Expected result: a reference plane/triad only, zero
physical solid or fluid bodies. Capture the object tree, coordinate/units
display and plane properties; save/reopen F7_C1_datums.sim. Do not start with
an extruded 1 m² square pan or a closed 1.3×2.2 m cylinder.

Prior administrative sequence: launch installed 2402, capture version/OS,
create empty local simulation, create empty CAD container and save C0.
Those intended operations are not exact menu paths until mapped using the
matching installed documentation.

## Ordered local execution with stop gates

1. Collect full client/server build, local help topic/control screenshots,
   CAD entitlement, memory and project/temp disk availability.
2. Reconfirm Day 7 source and assumption dispositions. If still blocked,
   limit any authorized session to empty container/reference datums.
3. Perform the first datum step above; optionally add case height reference
   after control verification (0.1 or 1.5 m). Do not create bore/exit surface.
4. Before the first physical body, obtain dimensioned heads/barrel and actual
   wall thickness, dimension conventions and pan-to-vessel datum offsets.
5. Resolve pan outline/rim/position/supports; insulation extents/order/gaps;
   nozzle bore/OD/pose/feed path and air/exhaust opening geometry/locations.
   Create only source-backed or separately approved provisional features.
6. Inspect contacts, closure, overlap, regions and volume accounting. Preserve
   source-linked CAD diagnostics/checkpoints and reopen verification evidence.
7. Stop for review before meshing, reactions or simulation.

Unresolved gate register is
[F7_Parametric_CAD_Input_Register.csv](../../data/day-07/F7_Parametric_CAD_Input_Register.csv).
All 23 unresolved entries are explicit; actual free gas volume is a later
CAD-derived quantity requiring a resolved assembly, not a guessed input.
Thermocouple xyz and pool geometry also limit validation and region design.
Material properties, inlet temperature/composition, ventilation reference state,
external thermal boundaries and model coefficients block later physics even
after CAD is complete. H1 verification remains a separate required workstream.

Needed handoff: official primary report PDFs/drawings, actual 2402 help/version
evidence, and explicit scientific decisions on remaining assumptions. Do not
advance merely because a day number or approximate envelope is available.
