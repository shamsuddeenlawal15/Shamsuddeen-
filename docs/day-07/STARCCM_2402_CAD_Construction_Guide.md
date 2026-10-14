# Windows 11 / STAR-CCM+ 2402 operator guide

Scope: a detailed operation sequence and evidence requirements, NOT exact
verified menu commands. User confirms 2402 (2024.1), Windows 11, i9-14900HX,
32 GB and a working license. Patch/build, CAD controls and entitlement remain
unverified. Siemens documentation retrieval failed; no menu/API is invented
and no Java macro is supplied. No STAR-CCM+ execution occurred in Codex.

## Local identification and instruction-verification gate

Launch the researcher's installed STAR-CCM+ 2402 shortcut from Windows Start
or the existing desktop shortcut. Do not use an executable path guessed here.
Record the complete client/server version string from the local version display
and startup log, Windows build via winver, available RAM and disk. Save evidence
with keys/server credentials redacted.

Open the matching installed help. For each intended operation below locate the
manual topic and actual UI action; record the edition/build, topic/page and
screenshot. If a capability is absent/unlicensed or documentation differs,
stop that operation and submit the evidence for revised instructions. UI names
such as “new simulation” and “3D-CAD” below are intended operations/search terms,
not a claimed click path.

| Step / intended action | Required inputs and control verification | Expected result / checkpoint |
|---|---|---|
| 1 Create new local simulation | Verify new-simulation control and local server settings; no solver processes assumed licensed | Empty project; screenshot of version and object tree; C0 save |
| 2 Create empty 3D-CAD model/container | Verify supported model-creation action and license availability | Empty named F7_Source_Reconstruction container; no solids |
| 3 Establish units/coordinates | Confirm length units m and right-handed XYZ; inspect unit display rather than unitless entry | F7_PROJECT_CARTESIAN reference with Z up |
| 4 Create first reference datum | Verify plane/datum action; use z=0 and name Pan_Top_Reference | Nonphysical reference only; axis/plane screenshot; C1 save |
| 5 Add case height reference | Verify parameter/unit expression controls; h=0.1 m F7-1 or 1.5 m F7-2 | Nozzle_Exit_Height_Reference; not a nozzle face; offset screenshot |
| 6 Create primary vessel body | STOP until barrel length, heads, shell thickness, inner/outer basis and origin offsets are resolved; verify appropriate profile/body operation | Approved envelope and separate wall body, not arbitrary closed cylinder; C2 save |
| 7 Represent pan | STOP until planform/rim/position resolved; verify profile/thickness operation | Carbon-steel pan feature with 1 m² constraint and 0.006 m thickness; not a guessed square |
| 8 Create insulation structures | STOP until extents/order/gaps confirmed; verify separate-body operation | Distinct project-labelled 0.05 m layers without assumed materials; C3 save |
| 9 Place nozzle/feed | STOP until bore/OD/pose/route confirmed; reference case height without moving roof penetration arbitrarily | Separate feed feature; two case checks; C4 save |
| 10 Prepare vents/exhaust | STOP until opening size/pose/path known; verify supported cutting/imprinting operation | Named openings, not inferred velocities or pressure outlets |
| 11 Separate/name surfaces | Verify surface splitting/naming operations and persistence after update | Names from Day 7 register; physical surface vs BC role kept distinct |
| 12 Create parts from approved CAD | Verify supported part-generation/update action and unit preservation | Separate solid parts and reviewed gas-domain extraction; C5 save |
| 13 Inspect geometry | Verify bounds/area/volume, closure/intersection/connectivity diagnostics | Export reports, selection scopes, screenshots; no automatic pass |
| 14 Save/reopen/export | Verify save-as and supported neutral export; preserve source CAD | Reopened dimensions/names agree; hashes and audit; C6 save |

Steps 6–12 are blocked now. Do not execute a detailed meshing operation, enable
sodium reactions, create extra regions just because a model offers them, or
start a numerical run. Physical inlet/outlet patches close the geometry shell
but receive numerical BC types only during a later approved stage.

## Naming, audit and preservation

Use separate groups for vessel barrel/heads, pan, each insulation layer, feed,
air system and nonphysical references. Names/paired faces are proposed in
[F7_Regions_Interfaces_and_Surface_Names.csv](../../data/day-07/F7_Regions_Interfaces_and_Surface_Names.csv);
they are not software API identifiers. Keep gas extraction separate from solids,
subtract occupied volumes once, inspect lower-cavity connectivity and retain
thin heat paths intentionally. A reduced pool is a surface coupling unless
a liquid-region model is separately justified.

Use local ignored runs/F7_day08/<case>/<attempt>/ with CAD/, evidence/,
exports/ and checkpoints/. Suggested checkpoint filenames are
F7_C0_empty.sim, F7_C1_datums.sim and case-qualified later saves.
Do not overwrite a source-backed case with P0. No such files are created here.

Every checkpoint records build, case, units, coordinate frame, source-register
revision, assumption IDs, source/observed measurement distinction and SHA-256.
Retain screenshots of the feature tree, triad/datums, case offsets, orthogonal
views, section views, contacts and diagnostic scopes. On reopen verify part/
surface naming and unit scale before further operations.

## Provisional engineering option

P0 is CONDITIONAL, not approved for execution: a diagnostic cylinder envelope
using approximate dimensions with explicitly flat closures could demonstrate
CAD controls, but is not F7. It must live in a different model/project and
exclude claims about real free volume, pan shape, nozzle or vents. No body is
generated here. Reviewer approval of each assumption and its intended use is
needed before entering such dimensions in a construction operation.
