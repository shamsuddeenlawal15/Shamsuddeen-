# F7-1 parameter-driven geometry specification

Status: incomplete source-backed design; NOT authorization to construct CAD.
Shared definitions and proposed coordinates are in
[F7_Experimental_Geometry_Review.md](F7_Experimental_Geometry_Review.md).
Source L2023 p.2 Section 2 / Fig.1 unless otherwise stated.

| Parameter / role | F7-1 specification | Status |
|---|---|---|
| case_id | F7-1 | Project identifier |
| h_nozzle above pan reference plane | 0.1 m | Published |
| nominal overall vessel height / diameter | About 2.2 m / about 1.3 m | Published approximate; dimension conventions unresolved |
| vessel capacity label | 3.0 m³ | Published schematic; not free gas volume |
| pan area / thickness / material | 1.0 m² / 6 mm / carbon steel | Published; outline/rim/grade unknown |
| insulation_1 / insulation_2 thickness | 50 mm each | Published; extents/material unknown |
| final_pool_area_observed | 0.28 m² | Validation observable, not default CAD footprint |
| sodium delivery | Average 3.3 g/s over 1500 s | Published operating condition, not nozzle diameter/velocity |
| ventilation | Approximately 3.0 m³/min | Published; reference state/ports unresolved |
| x_nozzle / y_nozzle / bore / exit orientation | Unset | Needs source evidence |
| head profiles / pan outline / port geometry | Unset | Blocks definitive geometry |
| sodium inlet temperature / initial gas conditions | Unset | Blocks physical model |

## Dependency design (proposed; not a verified STAR-CCM+ API)

Store a shared source-parameter manifest and a separate case selector:
h_nozzle(case)=0.1 m for F7-1, 1.5 m for F7-2. Define the nozzle exit datum
relative to the pan upper reference plane, not the vessel bottom. CAD feature
dependencies should reference that datum and shared apparatus parameters,
so a height change does not require rebuilding the vessel/pan manually.
Pipe length and penetration compatibility must be rechecked when the nozzle
moves; their path is not yet known. Do not shift the entire inlet assembly
through a roof or assume common pipe routing without evidence.

Keep unknowns null/unset and block geometric generation rather than substituting
zeros. Keep final_pool_area_observed outside the CAD-driving parameter group.
A future prescribed-area case must be labelled F7-1_prescribed_area and declare
0.28 m² as input; it cannot validate predicted area independently.

CAD groups proposed: Apparatus/Vessel, Apparatus/Pan, Apparatus/Insulation_1,
Apparatus/Insulation_2, Apparatus/SodiumFeed, Apparatus/AirSystem and
Reference/Instrumentation. Use named datums, not numeric topology indices.
Resolved supports and heads are separate features. All global nozzle/sensor
coordinates remain source-gated.

Before signoff, verify z_exit-z_pan_top=0.1 m from actual CAD reports, all shared
constraints, surface integrity, gas/solid volume accounting and region materials.
The [verification checklist](F7_Geometry_Verification_Checklist.md) contains
blank CAD observations. No generated model or solver result is attached.
