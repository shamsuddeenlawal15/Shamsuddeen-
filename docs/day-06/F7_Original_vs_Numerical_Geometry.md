# Original apparatus versus numerical chamber

Source: L2023 as fully cited in [the experimental review](F7_Experimental_Geometry_Review.md).
Figure 1, p.2, describes apparatus; Figure 2, p.3, describes MELCOR/SPHINCS
heat structures. No value from Fig.2 is promoted to an experimental dimension.

| Component | Apparatus: p.2 Section 2 / Fig.1 | Numerical representation: p.3 Fig.2 | Reconstruction disposition |
|---|---|---|---|
| Vessel side | About 2.2 m overall height / 1.3 m diameter; stainless steel | Cylindrical wall 9.0 m²; 8 mm | Height need not be cylindrical barrel length; 8 mm is numerical input only |
| Top head | Curved outline; penetrations; no dimensioned profile | Rectangular top heat structure; 1.3 m²; 8 mm | Do not build a rectangular or flat experimental roof from this |
| Bottom / pan | Lower curved vessel outline separate from pan; carbon-steel pan 1.0 m² and 6 mm | Rectangular bottom heat structure; 1.0 m²; 6 mm | Likely pan/floor heat path interpretation; not an established bottom-shell profile |
| Steel assignment | Stainless vessel and carbon-steel pan explicitly distinguished | Legend says stainless steel; same hatch at bottom | Retain experimental carbon steel for pan; resolve numerical legend conflict |
| Insulation | Two 50 mm layers attached to pan | 100 mm bottom insulation | Total agrees; layers/material/extent/contact still not defined |
| Nozzle and sodium pipe | Different exit heights 0.1 / 1.5 m | Not dimensioned or represented explicitly | Retain configuration distinction; recover bore/path |
| Vent / exhaust | Lower side supply / upper exhaust schematically | No port dimensions | Areas and coordinates cannot be inferred from heat structures |
| Gas volume | Vessel label 3.0 m³ | No explicit free-volume partition shown | Do not equate vessel label with CAD gas volume without internals |
| Pool | Final areas 0.28 / 0.30 m² | Spreading closures; SPHINCS input maximum area | Observable or declared prescribed input, never both independently |

Section 3.2 and Section 4 (p.3) describe a two-dimensional radial/depth floor
heat model in SPHINCS and under-pool/outside-pool zones in enhanced MELCOR.
These thermal partitions motivate spatial pan heat-transfer resolution; they
do not define pan planform, actual sensor depths or CFD mesh dimensions.

## Three strictly separate models

- H1: artificial 0.1 m cube, numerical verification only, archived Days 3–5.
- F7 source reconstruction: incomplete apparatus specification; no unsupported
  head, nozzle, port, pan or gas-domain shape is instantiated.
- P0 provisional alternative (NOT APPROVED): idealized cylindrical envelope
  using approximate 1.3 m diameter and 2.2 m height, flat closures as explicit
  assumptions, reduced pool heat/mass-transfer surface. Pan planform and port
  assumptions must be proposed and reviewed separately before building P0.
  It is not a complete CAD recipe and must not be called F7 reproduction.
  The cylinder-derived 2.92011 m³ must not be renamed the measured gas volume.

A reduced pool-only model can omit falling-column transport only with a stated
limitation: changing nozzle-height metadata alone would not model the physical
difference between F7-1 and F7-2. A column/impingement treatment or independently
supported condition at the pool is needed before claiming both are reproduced.
