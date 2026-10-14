# Day 7 research log

Date: 2026-10-14 (Asia/Shanghai).
Verified baseline branch research/day-6-f7-geometry-reconstruction,
commit 74e35611ad63abf1226a3012ee2290acc243d5b6, matching origin.
Clean initial working tree; no merges. New branch:
research/day-7-f7-geometry-verification.

## Work completed

All eleven Day 6 deliverables plus its tests and README change reviewed.
Article dimensions rechecked; no new experimental numeric values recovered.
Corrections are additive: nozzle height datum does not prove exit-plane
orientation; Fig.2 bottom-material conflict is localized; intended openings
must have geometric closure patches without implying wall BCs; pool–gas
coupling now has an explicit proposed mapping.

Prepared 17 verified article parameter records, 37 CAD input/reference entries
(including 23 unresolved entries) and 21 proposed region/surface/interface
records. No prior data/equation/document record is overwritten. H1 remains
separate. Day 2 equation corrections retain authority.

The geometry utility provides independent analytical consistency calculations
and an evidence-summary audit for future local CAD reports. It is not a CAD
kernel or STAR-CCM+ interface. No CAD/mesh/solver execution or real-CAD audit
was performed; numerical test fixtures are explicitly synthetic.

## Source/software access

Five new source/documentation HEAD attempts failed at proxy CONNECT 403,
curl exit 56, as documented in the review report. No primary report or Siemens
manual recovered. User-confirmed 2402/Windows 11 is retained; exact build/
capabilities remain local-evidence gates. No unverified macro/menu command added.

## Deliverables

1. [Review report](Day_07_Geometry_Review_Report.md)
2. [Verified geometry parameters](../../data/day-07/F7_Verified_Geometry_Parameters.csv)
3. [Geometry consistency utility](../../scripts/F7_Geometry_Consistency_Checks.py)
4. [Coordinates and origins](F7_Coordinate_System_and_Origins.md)
5. [Parametric CAD input register](../../data/day-07/F7_Parametric_CAD_Input_Register.csv)
6. [F7-1 preparation](F7_1_Final_Geometry_Preparation.md)
7. [F7-2 preparation](F7_2_Final_Geometry_Preparation.md)
8. [Regions/interfaces/surface names](../../data/day-07/F7_Regions_Interfaces_and_Surface_Names.csv)
9. [2402 construction guide](STARCCM_2402_CAD_Construction_Guide.md)
10. [Geometry QA checklist](Geometry_Quality_Assurance_Checklist.md)
11. [Day 8 readiness](Day_08_Execution_Readiness.md)
12. This log.

## Validation

Executed checks:

| Command | Outcome |
|---|---|
| `python3 -m unittest discover -s tests -v` | 42 passed, including 13 new Day 7 tests |
| `python3 tests/H1_Postprocessing_Tests.py -v` | 21 passed |
| `python3 scripts/check_day1_data.py` | PASS |
| `python3 scripts/day2_data.py --check` | PASS; 57 preserved + 25 added = 82 records |
| `python3 scripts/F7_Geometry_Consistency_Checks.py analytic` | Exit 0; analytical-only values match independently checked arithmetic |
| `git diff --check` | PASS |

All 63 tests passed, no failures/skips. Tests cover conversions, case heights,
source preservation, explicit unknowns, names/interfaces, missing evidence,
nonfinite data, invalid bounds, wrong units, topology defects, artifact hashes,
duplicate JSON keys and CLI failure status. The only audit fixtures used were
synthetic unit-test data, not local CAD evidence. Code tests validate data
handling and arithmetic, never experimental fidelity or actual CAD quality.

Additional checks confirmed all Day 7 relative links resolve, all three CSVs
are well formed, and prior Days 1–6 documentation/data, Day 6 tests and the H1
processor are unchanged from 74e3561. The [PR description](PR_Description.md)
is prepared for review against the Day 6 branch; no PR creation is claimed.

## Stop

Full F7 geometry is BLOCKED. Reference-datum specification is APPROVED only in
the limited mathematical sense; local creation is CONDITIONAL on verified
controls and explicit Day 8 authorization. No Day 8 work started.
