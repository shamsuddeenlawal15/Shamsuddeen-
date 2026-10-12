# Day 2 experimental geometry review

## Evidence and pagination

Source: Louie, D. L. Y., Aoyagi, M., Uchibori, A., Takata, T., and Luxat,
D. L. (2023), “Validation study of sodium pool fire modeling efforts in
MELCOR and SPHINCS codes,” *Nuclear Engineering and Design* 407, 112285,
DOI [10.1016/j.nucengdes.2023.112285](https://doi.org/10.1016/j.nucengdes.2023.112285).
The supplied five-page publisher PDF was examined as rendered images as well
as extracted text. Its printed page numbers equal its one-based PDF page
numbers. Figure 1 is on p. 2; Figure 2 is on p. 3. Numerical labels below
were read directly from those figures and their accompanying prose. This
review does not establish the contents of an inaccessible original F7 report.

## Apparatus versus numerical representation

Figure 1 is an apparatus schematic. Figure 2 is explicitly captioned as the
MELCOR/SPHINCS representation of the chamber; it gives thermal-structure areas,
thicknesses, and shape labels. The numerical heat structures are insufficient
to define a watertight three-dimensional experimental chamber.

| Feature | Experimental evidence: Fig. 1 / Section 2, p. 2 | Numerical evidence: Fig. 2 / Sections 3.2–4, p. 3 | Day 2 disposition |
|---|---|---|---|
| Vessel | Stainless steel; approximately 2.2 m high, 1.3 m diameter; Fig. 1 labels 3.0 m³ | Cylindrical wall: area 9.0 m², thickness 8 mm | Retain experimental overall dimensions and numerical wall thickness as different evidence classes. Interior diameter, usable gas volume, and head profiles are not defined completely. |
| Top | Curved upper outline with sodium entry and exhaust in schematic | “Top head (rectangular)”: area 1.3 m², thickness 8 mm | “Rectangular” is a numerical-structure label; it does not establish a physically rectangular roof or a square chamber. |
| Catch pan / bottom | Carbon-steel catch pan; surface area 1.0 m², thickness 6.0 mm | “Bottom head (rectangular)”: area 1.0 m², thickness 6 mm, insulation 100 mm | Matching area and thickness suggest that the bottom thermal structure represents the pan/floor heat path; this correspondence is an interpretation, not a dimensioned experimental drawing. |
| Steel material | Vessel stainless steel; pan carbon steel explicitly in Section 2 | Legend identifies the diagonal hatch as “Stainless steel”; bottom head has the same hatch | Material conflict remains: do not replace the experimental carbon-steel pan with stainless steel from the numerical legend. Obtain the F7 report or code input deck. |
| Insulation | Two 50 mm layers attached to the pan | 100 mm under bottom head | Total thickness agrees. Material, density, conductivity, heat capacity, layer contact resistance, and extent are absent from the article. |
| Sodium nozzle | Height above pan: F7-1 0.1 m; F7-2 1.5 m; falling sodium described as a column | No nozzle represented in Fig. 2 | Reproducing only Fig. 2 omits the geometric distinction between the experiments. Nozzle bore, wall thickness, orientation, outlet temperature, and exact centerline position require further evidence. |
| Air supply | Schematic air line enters the lower right side above the pan; approximately 3.0 m³/min steady ventilation | No inlet or exhaust dimensions shown | A schematic position is not a measured coordinate. Port area is needed before converting volume flow to inlet velocity. The reference state for volume flow is not supplied. |
| Exhaust | Upper-right schematic outlet | Not specified | Outlet area, loss coefficients, pressure boundary, elevation, and downstream system remain unknown. |
| Pool footprint | Final areas: F7-1 0.28 m²; F7-2 0.30 m² | MELCOR spreading includes viscosity/oxide effects; SPHINCS halts spreading at an input maximum area | Final measured footprint is an observable. If used to prescribe a maximum model area, it cannot also be treated as an independent validation prediction. |
| Floor thermal treatment | Pan and insulation shown; spatial temperature measurements plotted in Fig. 4, p. 4 | SPHINCS uses radial/depth ring mesh; enhanced MELCOR divides pan into under-pool and outside-pool regions | A single uniform pan temperature cannot represent these treatments without a stated approximation. The description does not supply mesh counts or thermal contact data. |

## Geometric consistency calculations — derived checks only

The following arithmetic uses the approximate published height and diameter;
it is not an extraction of new measurements, and it does not define the model
to be built after scientific review.

- Cylinder side area: `pi * 1.3 * 2.2 = 8.99 m²`, consistent with the rounded
  numerical wall area of 9.0 m².
- Circular cross-sectional area: `pi * 1.3² / 4 = 1.327 m²`, consistent with
  the rounded numerical top-head area of 1.3 m².
- Plain-cylinder volume: `pi * 1.3² * 2.2 / 4 = 2.92 m³`, close to the
  schematic 3.0 m³. This does not determine head volumes or whether the height
  is an internal cylindrical height.
- The bottom thermal-structure area (1.0 m²) is smaller than the circular
  vessel cross section (approximately 1.327 m²). Forcing both to be the same
  physical face would change one of the reported quantities. The catch-pan
  shape, supports, surrounding gap, and gas/solid volume accounting must be
  established separately.

An equivalent circular pan diameter or equivalent final pool radius may be
calculated for a future idealized benchmark, but the article does not establish
a circular pan, an exactly circular pool, or square pan side lengths. No such
derived value has been entered as an experimental fact.

## Instrumentation and initial conditions

Figure 4 (p. 4) labels pool-temperature radial distances of 0.10, 0.20, and
0.24 m from the pool center. These are radial coordinates only. Sensor depth,
azimuth, junction construction, whether the junction measures pan or sodium
locally, response time, and calibration are not specified in the article.
Figures 3–5 provide plotted observables, not machine-readable raw time series
or measurement uncertainty. Figure 1 does not provide a dimensioned sensor map.

The article does not specify the initial gas pressure, gas temperature,
oxygen fraction, humidity, sodium inlet temperature, initial pan/insulation
temperature distribution, nozzle bore, or sodium composition. Existing Day 1
missing-data rows mean “not found in Louie et al. (2023)”; any Day 2 evidence
from another source must be recorded additively with its own scope and page.

## Review decisions required before geometry construction

1. Select either an idealized heat/mass-transfer benchmark or full F7
   reproduction. A cylinder with the published rounded dimensions and a
   prescribed burning patch is a benchmark assumption until ports, heads,
   pan, and nozzle are resolved.
2. Resolve the carbon-steel pan versus the stainless-steel Fig. 2 legend;
   preserve the primary apparatus statement in the meantime.
3. Establish whether 3.0 m³ is vessel capacity or the modeled free gas volume,
   and obtain the gas/solid region boundaries and pan planform.
4. Obtain inlet/outlet/nozzle dimensions, pressure/flow reference conditions,
   and experiment-specific sensor coordinates.
5. Specify whether falling-column oxidation and impingement are excluded from
   a reduced model and how that limits comparison of the two nozzle heights.
6. Resolve which spreading inputs are calibrated to final area before claiming
   independent validation of area or combustion peaks.

No detailed geometry, mesh, STAR-CCM+ model, or CFD output was created during
this review. The equation issues found while rereading pp. 2–3 are recorded
separately in [Equation_Transcription_Audit.md](Equation_Transcription_Audit.md).
