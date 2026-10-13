# Day 6 — F7 experimental geometry review

Status: source reconciliation and reconstruction specification only. No CAD,
mesh or CFD run exists for this package. H1 is a separate synthetic numerical
verification workstream; its 0.1 m cube and artificial properties are not F7
inputs. Prior documents already identified that separation; this package makes
the F7 reconstruction the immediate research priority without rewriting history.

## Source and inspection

L2023: Louie, D. L. Y., Aoyagi, M., Uchibori, A., Takata, T., and Luxat, D. L.
(2023), “Validation study of sodium pool fire modeling efforts in MELCOR and
SPHINCS codes,” Nuclear Engineering and Design 407, 112285,
DOI https://doi.org/10.1016/j.nucengdes.2023.112285.
The original five-page supplied PDF was reread; Figures 1 and 2 were rendered
and inspected, and Figure 4 sensor labels checked visually. Printed pages
equal one-based PDF pages. SHA-256:
bf55d2d991b0d1defc2e78486a1869b67b5888c48fc4826355493d667eb34afe.

“Published” below means reported in the inspected 2023 article, not independent
confirmation from the unrecovered original 1998 experimental report.

| Apparatus quantity | Published value / qualifier | Exact location |
|---|---|---|
| Vessel material | Stainless steel; grade unspecified | p.2 Section 2 |
| Vessel height / diameter | About 2.2 m / about 1.3 m | p.2 Section 2; Fig.1 |
| Vessel capacity label | 3.0 m³; free gas volume not established | p.2 Fig.1 |
| Catch pan material | Carbon steel; grade unspecified | p.2 Section 2 |
| Catch pan area / thickness | 1.0 m² / 6 mm | p.2 Section 2; Fig.1 |
| Insulation | Two layers of 50 mm each | p.2 Section 2 |
| F7-1 / F7-2 nozzle exit above pan | 0.1 m / 1.5 m | p.2 Section 2; Fig.1 |
| Final pool area F7-1 / F7-2 | 0.28 m² / 0.30 m² | p.2 Section 2 |
| Sodium discharge | Average 3.3 g/s for 1500 s | p.2 Section 2 |
| Air ventilation | Steady approximately 3.0 m³/min | p.2 Section 2 |
| Pool-temperature measurement radii | 0.10 / 0.20 / 0.24 m from pool center | p.4 Fig.4 legends and caption |

The requested values agree with the inspected paper. Measurement uncertainties,
internal/external dimension conventions and the gas-flow reference state are
not supplied. “About” does not specify a numerical uncertainty interval.
Do not convert ventilation to velocity before port area and flow reference
conditions are established. Final pool areas are observations, not pan area.

## Apparatus versus computational interpretation

Figure 1 shows a curved upper outline, lower curved vessel region, pan,
insulation, sodium feed and lower side air supply / upper exhaust. It is not a
dimensioned manufacturing drawing. Do not scale unknown lengths from schematic
pixels, infer a hemispherical/ellipsoidal head, or assume rotational symmetry
of the openings.

Figure 2 (p.3) assigns areas and thicknesses to numerical heat structures.
Its rectangular top/bottom labels do not establish physical rectangular heads.
See [the comparison](F7_Original_vs_Numerical_Geometry.md). Section 3.2 (p.3)
describes SPHINCS lumped mass/1-D flow-network modeling with a flame sheet and
radial/depth floor conduction; Section 4 describes MELCOR's under-pool and
outside-pool thermal treatment. Neither is a complete three-dimensional CAD
specification.

Section 4 and Figures 3–5 (pp.3–4) relate combustion, pool temperature and
aerosol behavior to spreading/oxide treatment. Prescribing the final pool area
can constrain a reduced model, but then that area is not an independent
validation prediction. Do not infer missing geometry, initial temperature or
reaction constants by fitting these plots without a separate calibration plan.
No plot values were digitized or new numerical validation results claimed.

## Geometry consistency — derived checks, not CAD targets

Using the rounded approximate diameter and height as a plain cylinder:
V=pi*(1.3²/4)*2.2 ≈2.92011 m³; lateral area≈8.98495 m²;
cross section≈1.32732 m². Difference from the schematic 3.0 m³ is about
-0.07989 m³ (-2.66%). This arithmetic cannot establish actual free gas volume
or a tolerance for agreement. Heads, internals, wall conventions and approximate
dimensions remain unresolved. Do not force a cylinder to 3.0 m³ by silently
changing its dimensions.

Pan area 1.0 m² is not vessel cross-sectional area. The outline, rim, supports,
gaps and insulation extent require source recovery. Two 50 mm layers imply
100 mm total thickness arithmetically, but not a known material or contact law.

## Proposed coordinates, not a reported experimental convention

Use right-handed Cartesian axes, Z vertically upward, X/Y horizontal.
Proposed origin O is the intersection of the vessel reference axis with the
pan's upper reference plane. This does NOT assert that the pan centroid,
pool center or nozzle centerline coincides with that axis. X azimuth is an
arbitrary project datum until an apparatus drawing establishes orientation.
All instrument radii remain relative to the pool center; their global x/y/z
are unknown. Store the later experimentally justified coordinate transform.

Pan top is z=0 by definition. Nozzle exit reference plane is z=h_nozzle,
h_nozzle=0.1 m (F7-1) or 1.5 m (F7-2); x_nozzle and y_nozzle remain unset.
Head apex, vessel base and pan-to-base clearance cannot be assigned from the
overall height alone. Proposed coordinates do not supply missing dimensions.

Use the additive [geometry register](../../data/day-06/F7_Geometry_Parameter_Register.csv).
Earlier parameter records and the [Day 2 equation audit](../day-02/Equation_Transcription_Audit.md)
are preserved. Source-backed reconstruction is presently incomplete.
