# F7 geometry verification checklist

All CAD observations below are intentionally blank: no definitive CAD exists.
Source: L2023 exact locations in the geometry register. Record actual CAD file
hash, build, coordinate transform, measurement definition and operator for each
future observation. Targets are source statements, not achieved dimensions.

| Check | Source target / requirement | CAD observation | Difference / uncertainty | Evidence / disposition |
|---|---|---|---|---|
| Vessel overall height | About 2.2 m; p.2 Section 2 / Fig.1 | | | |
| Vessel diameter | About 1.3 m; p.2 Section 2 / Fig.1 | | | |
| Vessel capacity / gas volume | 3.0 m³ schematic label; free volume unresolved | | | |
| Catch-pan area | 1.0 m²; p.2 Section 2 / Fig.1 | | | |
| Catch-pan thickness | 6 mm; p.2 Section 2 / Fig.1 | | | |
| Insulation layer 1 / layer 2 | 50 mm each; p.2 Section 2 | | | |
| F7-1 nozzle exit relative to pan | 0.1 m; p.2 Section 2 / Fig.1 | | | |
| F7-2 nozzle exit relative to pan | 1.5 m; p.2 Section 2 / Fig.1 | | | |
| Heads / ports / pan outline / supports | Match newly recovered dimensioned evidence | | | |
| Boundary connectivity | Closed shells except named physical openings | | | |
| Gas region integrity | Correct connected volumes; solids subtracted once | | | |
| Surface orientation | Consistent outward fluid normals / paired interfaces | | | |
| Missing / overlapping geometry | No unintended gaps/intersections/duplicate surfaces | | | |
| Material-region consistency | Stainless vessel; carbon-steel pan; layers distinct | | | |
| Interface area matching | Matching paired areas or documented transfer method | | | |
| Instrument coordinates | Full source-supported transform; radii alone insufficient | | | |
| Case switching | Correct nozzle height; preserved shared constraints | | | |

For a source quantity s and CAD measurement c record c-s and, where meaningful,
(c-s)/s. For approximate dimensions preserve the approximation qualifier and
record “published uncertainty not quantified”; do not choose an invented ± bound
or assert exact equivalence. Set engineering acceptance tolerances explicitly
during review, distinct from source uncertainty and CAD precision.

Compare gas volume to a documented volume-accounting model, not automatically
to the vessel capacity label. Record outer/inner dimensions and all excluded
solid/liquid volumes. Report numerical Fig.2 areas/thicknesses in a separate
code-representation comparison if used, not as apparatus acceptance criteria.

- [ ] All source/assumption dispositions approved and missing critical inputs resolved.
- [ ] Installed 2402 build and intended CAD operations verified locally.
- [ ] Every CAD feature mapped to source row or approved provisional assumption.
- [ ] Pan planform and heads are not inferred from area or schematic pixels.
- [ ] Final pool area explicitly classified as input or validation observable.
- [ ] Datum and case-change audits complete with no collisions.
- [ ] Dimensional/material/connectivity audits signed before meshing.

Reviewer / date / decision: unfilled pending review. Passing software integrity
tests does not satisfy any CAD acceptance box.
