# Day 7 geometry review

Date: 2026-10-14 (Asia/Shanghai). Baseline verified locally and on origin:
research/day-6-f7-geometry-reconstruction at
74e35611ad63abf1226a3012ee2290acc243d5b6. Working tree was clean.
Day 7 branch is research/day-7-f7-geometry-verification; no merges performed.

## Review inventory and dispositions

Every Day 6 deliverable was read, together with its added tests and README update.

| Day 6 file | Day 7 finding / disposition |
|---|---|
| F7_Experimental_Geometry_Review.md | Published numbers agree with paper; derived cylinder arithmetic correct; clarify exit datum versus physical exit plane |
| F7_Geometry_Parameter_Register.csv | All 39 records reviewed; preserve numeric source records; N001–N007 generic bottom-conflict warning is overbroad |
| F7_Original_vs_Numerical_Geometry.md | Apparatus/numerical distinction correct; P0 remains unapproved |
| F7_1_Geometry_Specification.md | 0.1 m is supported; exit orientation/position remains unknown |
| F7_2_Geometry_Specification.md | 1.5 m and final area 0.30 m² supported; other unreported differences not assumed identical |
| F7_STARCCM_2402_Geometry_Workflow.md | Logical sequence usable; exact UI/API still unverified |
| F7_Regions_and_Boundaries.csv | Proposed mappings, not created regions; make pool–gas pair explicit and separate surfaces from BC assignments |
| F7_Geometry_Verification_Checklist.md | No observed CAD values; appropriate; closure needs operational definition for capped inlet/outlet patches |
| Missing_Geometry_Data.md | Essential gaps persist; source access checked again below |
| Revised_Day_By_Day_Research_Plan.md | Review gates retained; Day 8 is not automatically authorized |
| Day_06_Research_Log.md | Scope and test claims consistent; preserve historical date/results |
| tests/test_day6_geometry.py and README.md update | Data-integrity tests not CAD evidence; retain unchanged |

Corrections/clarifications are additive in Day 7, not silent edits to Day 6:

- Exit **reference elevation** above the pan is established; a horizontal nozzle
  exit surface is not. The project may use a horizontal height datum without
  claiming the nozzle exit lies in that plane across its full bore.
- Fig.2 bottom material conflict concerns the pan/bottom interpretation
  (N005–N006); it is not a demonstrated conflict for the wall/top/insulator.
  None of N001–N007 becomes experimental CAD input.
- “Reported” does not mean exact, uncertainty-free experimental measurement.
  The paper does not give measurement tolerances for the non-approximate values.
- Inlet/outlet surfaces close a fluid-domain shell geometrically but are not
  impermeable walls physically. Count unintentional open edges only after
  physical openings have named boundary patches.
- Pool–gas coupling is now explicitly listed; a reduced pool surface is not
  simultaneously an unnecessary liquid volume.

## Source verification

Primary inspected source L2023: Louie et al., “Validation study of sodium pool
fire modeling efforts in MELCOR and SPHINCS codes,” Nuclear Engineering and
Design 407 (2023), 112285, DOI 10.1016/j.nucengdes.2023.112285.
Original supplied PDF SHA-256:
bf55d2d991b0d1defc2e78486a1869b67b5888c48fc4826355493d667eb34afe.
Printed and PDF page numbering agree. Rechecked Section 2 and rendered
Figures 1–2, not OCR equations. Day 2 equation corrections remain authoritative.

The [verified register](../../data/day-07/F7_Verified_Geometry_Parameters.csv)
preserves 17 article-reported values/units with Day 6 IDs and exact locations.
About 2.2 m height, about 1.3 m diameter, 1.0 m² pan, 6 mm pan, two 50 mm
layers and 0.1/1.5 m nozzle heights are on p.2 Section 2 (Fig.1 corroborates
the vessel/pan/nozzle labels). The 3.0 m³ capacity label is in Fig.1 only.
Final areas 0.28/0.30 m² are p.2 Section 2 observations, not CAD drivers.
No original-1998-report verification is claimed.

| Quantity class | Interpretation |
|---|---|
| Approximate published | Preserve “about” / “approximately”; no invented ± tolerance |
| Reported numeric without approximation | Preserve printed precision; uncertainty unquantified, not exact truth |
| Figure label | Volume scope may differ from free gas volume |
| Derived | SI conversions and idealized consistency arithmetic only |
| Proposed | Project frame, names and implementation choices; not experimental facts |
| Unresolved | No numerical value and no hidden software default |

## Consistency checks

The independent script reproduces the Day 6 ideal-cylinder values:
2.92011037 m³ volume, 1.32732290 m² cross section, 8.98495499 m² lateral area.
Capacity-label difference=-0.07988963 m³ (about -2.663%); pan area minus
cross section=-0.32732290 m². These do not prove incompatible apparatus:
overall/inner dimensions, heads and approximation uncertainties are unknown.
Do not tune missing heads to erase these differences.

Two layers total 0.100 m thickness arithmetically; the nozzle elevation
difference is 1.4 m. Neither establishes stacking positions or pipe geometry.
No equivalent circular pan/nozzle/port is adopted.

## Additional source attempts, 2026-10-14

Read-only HEAD requests with redirects to all destinations below failed at
proxy CONNECT with HTTP 403 / curl exit 56; no source content was returned.

| Report / destination | Evidence status |
|---|---|
| PNC TN9410 98-074: https://jopss.jaea.go.jp/search/servlet/search?kw=PNC%20TN9410%2098-074 | Original unread; cited in L2023 p.4 |
| SAND2021-0136: https://www.osti.gov/servlets/purl/1761299 | Original unread; title/DOI cited in L2023 p.5 |
| SAND2021-15469: https://www.osti.gov/servlets/purl/1834703 | User-supplied report/DOI pair not independently verified |
| SAND2022-14235: https://www.osti.gov/servlets/purl/1892376 | User-supplied report/DOI pair not independently verified |
| Siemens documentation: https://docs.sw.siemens.com/ | No exact 2402 control/API confirmed |

This is an access limitation, not proof of origin unavailability. Request local
copies/installed help for review; no author message was sent. Newly recovered
values must include report title, page, figure/table, units and scope before
promotion into the source-derived design.

**Full F7 CAD readiness: BLOCKED.** Source claims reviewed here are supported
at article level, but heads, wall thickness, pan outline, nozzle/vent geometry
and local CAD capability evidence remain unresolved.
