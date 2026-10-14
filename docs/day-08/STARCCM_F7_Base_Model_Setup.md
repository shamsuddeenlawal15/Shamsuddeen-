# F7 base model — local construction specification

Target: STAR-CCM+ 2402 (2024.1), Windows 11; i9-14900HX / 32 GB and working
license are user-confirmed. Exact build and operation controls remain unverified.
This document specifies intended operations, not exact menu paths or API calls.
Use the matching installed help and record each actual control before execution.

## Intended organization (not an existing simulation tree)

```text
F7_Sodium_Pool_Fire_Base.sim
  01_Experimental_Apparatus
    Vessel
    Catch_Pan
    Insulation_Layer_1
      Insulation_1                    [body deferred]
    Insulation_Layer_2
      Insulation_2                    [body deferred]
    Sodium_Inlet
      Nozzle_F7_1_Position            [height reference only]
      Nozzle_F7_2_Position            [height reference only]
    Air_Inlet
      Air_Inlet_Provisional           [empty slot / annotation]
    Exhaust
      Exhaust_Provisional             [empty slot / annotation]
    Instrumentation                  [references only]
  Reference_Geometry
    F7_PROJECT_CARTESIAN
    Pan_Top_Reference
  Configuration_Definitions
    F7_1
    F7_2
```

These are semantic project labels. If the build does not support equivalent
folders/configuration objects, retain a local manifest and separately saved
case files with the same shared parameter table; do not invent a configuration
API. All requested component/surface labels and Day 7 correspondence are in
[the component register](../../data/day-08/F7_CAD_Component_Register.csv).
No CFD regions or interfaces are instantiated by this organizational tree.

## Operator sequence and evidence gates

1. Launch the installed 2402 shortcut. Capture full client/server build and
   local help topics for new simulation, CAD container, units/datums, naming,
   parameter expressions, body creation, inspection and saving. Redact license
   credentials. Do not assume menus from another release.
2. Create a new empty local simulation using the verified control; save as
   F7_Sodium_Pool_Fire_Base.sim in local ignored runs/F7_day08/attempt_ID/.
   No physics/mesh operation is added. Save an immutable C0 copy.
3. Create an empty CAD container and organizational labels above where
   supported. Record metre units explicitly. Do not create zero-sized solids
   just to populate component names.
4. Establish right-handed F7_PROJECT_CARTESIAN: Z vertical up; X/Y horizontal.
   Origin is vessel reference-axis intersection with the pan upper reference
   plane, NOT the vessel bottom. X azimuth is arbitrary project datum.
5. Create nonphysical Pan_Top_Reference at z=0. Do not set the physical pan's
   unknown centroid, rim or bottom position. Save C1 and capture the triad.
6. Define a shared symbolic h_nozzle with F7_1=0.1 m and F7_2=1.5 m.
   Create Nozzle_F7_1_Position and Nozzle_F7_2_Position as height reference
   planes/loci, not points with guessed x/y and not actual nozzle outlet faces.
   Keep the other reference visible only as a comparison if locally supported.
   Record case selection and save C2 plus F7_1/F7_2 copies.
7. Reserve Air_Inlet_Provisional and Exhaust_Provisional as empty named slots
   or explicit unresolved-location annotations. Lower-side/upper schematic
   descriptions do not locate finite patches. Create actual placeholder
   surfaces only after their assumed size/pose is explicitly reviewed.
8. STOP definitive body creation at unresolved inputs. Once evidence is supplied,
   construct vessel shell/head profiles from their actual geometry, distinguish
   inside/outside walls and name top/bottom; create pan from a resolved outline,
   constrain area=1 m² and thickness=0.006 m (6/1000), then place two separately
   defined 0.05 m layers (50/1000) with reviewed extents and contacts. Do not
   fuse pan to vessel bottom by assumption or infer uniform layer footprint.
9. Name physical faces only after actual faces exist: Vessel_Inner_Wall,
   Vessel_Outer_Wall, Vessel_Top, Vessel_Bottom, Gas_Domain_Surface;
   Catch_Pan_Top, Catch_Pan_Bottom, Catch_Pan_Wall. A reference enclosure
   cannot provide both inner and outer walls without shell thickness.
   Keep names reserved while missing. No boundary conditions or materials set.
10. Inspect actual CAD as in the screenshot and audit checklists; save C3 only
    if bodies are genuinely created. Preserve failures and unresolved items.
    Reopen the saved project and check units/names/case references. Stop for review.

Unknown dimensions must remain unset, not zero or the software default.
Exact controls and executed-step dates/evidence are recorded locally; none
has been verified here. No untested Java macro is supplied.

## P0 provisional envelope — separate from apparatus

The user permits a clearly labelled provisional head representation. The
following optional visualization design makes the assumptions explicit;
local execution still requires verified controls. It is not a complete F7 model.

| Assumption ID | P0-only choice | Limitation |
|---|---|---|
| P0-A1 | Right circular reference cylinder, nominal D=1.3 m and H=2.2 m | Uses approximate overall dimensions as straight-cylinder envelope |
| P0-A2 | Flat top and bottom caps, named Vessel_Top_Approximation and Vessel_Bottom_Approximation | Does not claim real head shapes |
| P0-A3 | Separate P0_LOCAL frame with reference-cylinder base z=0 | Not F7 pan-based frame; actual pan offset unknown |
| P0-A4 | Envelope surface/volume visualization only; no shell thickness | Cannot define true inside/outside wall or occupied gas volume |

If pursued locally, save as F7_P0_Provisional_Envelope.sim, not the source-backed
base project, and mark screenshots NOT EXPERIMENTAL GEOMETRY. Its calculated
volume pi*1.3²*2.2/4≈2.92011 m³ is only analytical expectation; never a measured
CAD result or forced 3.0 m³. Do not insert a guessed pan, ports or nozzle.
P0 has not been constructed in this task and is not eligible for F7 meshing.

## Local preservation and name mapping

Keep base and case checkpoints, raw diagnostics, screenshots, units/frame,
assumption IDs and checksums in runs/F7_day08/attempt_ID/. No .sim or image
placeholder files are committed. Report actual saves and reopen evidence only
after the operator performs them.

Day 8 labels are CAD-level names, not replacements for Day 7 future region
names. For later report mapping, preserve raw names and use the component
register's day7_reference column. A mapping does not create regions, convert
a placeholder to an actual surface, or satisfy the Day 7 core-region audit.
The old geometry utility remains unchanged; do not submit fabricated mapped
names or measurements to make it pass.
