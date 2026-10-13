# F7-2 parameter-driven geometry specification

Status: incomplete source-backed design; NOT authorization to construct CAD.
Use the shared parameters, dependency design and unset-field gates in
[F7_1_Geometry_Specification.md](F7_1_Geometry_Specification.md), with the
following source-supported case entries (L2023 p.2 Section 2 / Fig.1):

| Parameter | F7-2 | Difference from F7-1 |
|---|---|---|
| case_id | F7-2 | Identifier |
| h_nozzle above pan | 1.5 m | Published; F7-1 is 0.1 m |
| final_pool_area_observed | 0.30 m² | Published outcome; F7-1 is 0.28 m² |

Shared reported vessel dimensions remain about 2.2 m high and 1.3 m diameter,
schematic capacity 3.0 m³; pan carbon steel, 1.0 m² and 6 mm; insulation two
50 mm layers. The reported average sodium rate 3.3 g/s, duration 1500 s and
approximately 3.0 m³/min air ventilation are shared in the article. Their
detailed time histories and case-specific uncertainty are not supplied.

Set z_exit=z_pan_top+1.5 m in the proposed coordinate system, retaining unknown
x/y, bore and exit orientation. Do not assume all unreported conditions are
identical merely because the article highlights nozzle height as the key
difference. Recover case-specific feed/vent/initial-condition records.

Keep 0.30 m² outside CAD drivers unless a separately reviewed
F7-2_prescribed_area model deliberately uses it as an input. Neither a nozzle
height change in a pool-only metadata file nor different prescribed final areas
alone reproduces falling-column transport or predicts spreading.

Future switch test: preserve vessel/pan/insulation source parameters, regenerate
the nozzle datum for each case, check changed feed geometry for collisions,
verify both nozzle-to-pan heights and compare the configuration manifests.
A shared coordinate convention does not establish identical pool centerlines.

No source-backed nozzle bore, head profile, port geometry, pan planform, support
geometry or instrument depth has been recovered. These block definitive CAD
for F7-2 just as for F7-1. No executable macro or geometry has been produced.
