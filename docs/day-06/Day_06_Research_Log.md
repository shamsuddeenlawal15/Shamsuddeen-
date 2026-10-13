# Day 6 research log

Date: 2026-10-13 UTC. Starting branch research/day-5-h1a-local-readiness,
commit ab09745c8981a85250446fa50e8fba6df4508547.
Branch: research/day-6-f7-geometry-reconstruction.

## Completed work and scope

Reread supplied L2023 PDF, visually reviewed Figures 1–2 and Fig.4 sensor
labels, reconciled Sections 2–4 and preserved the Day 2 equation audit.
Created nine Markdown deliverables and two CSV registers for the eleven
requested outputs. The [review](F7_Experimental_Geometry_Review.md) indexes
source-backed dimensions; [missing data](Missing_Geometry_Data.md) records
fresh recovery attempts and unresolved constraints.

The new user statement confirms STAR-CCM+ 2402 (2024.1), Windows 11, i9-14900HX,
32 GB RAM and working license. Patch/build, model/mesher capabilities and
parallel entitlement still need local evidence. No previous evidence record
was overwritten to imply those details were known earlier.

H1 was already labelled synthetic; it remains separate, preserved and unrun
in the available evidence. Its cube and properties are not adopted for F7.
This package reprioritizes the apparatus reconstruction, not a fictitious
correction to executed F7 simulations. No F7 CAD, mesh, Java macro, solver run
or numerical result is claimed.

## Primary-source outcome

Four requested report destinations and Siemens documentation failed with
proxy CONNECT 403 (curl exit 56). No new source contents were inspected from
those requests. The two newly requested SAND report/DOI pairs remain user-
supplied candidates, not verified citations supporting dimensions. No further
numeric experimental input was invented or imported.

## Integrity and verification

Existing parameter databases and equation records remain unchanged. The new
register separates published apparatus, published numerical, missing and
proposed entries. Missing numeric values stay empty, approximation qualifiers
and source pages are retained, final pool areas are observables, and CAD
observations remain blank.

| Executed check | Outcome |
|---|---|
| `python3 -m unittest discover -s tests -v` | 29 passed, including 7 new Day 6 integrity tests |
| `python3 tests/H1_Postprocessing_Tests.py -v` | 21 passed |
| `python3 scripts/check_day1_data.py` | PASS |
| `python3 scripts/day2_data.py --check` | PASS; 57 preserved + 25 added = 82 historical records |
| `git diff --check` | PASS |

All 50 software tests passed with no failures or skips. New checks cover the
39-row geometry register's component coverage, source pages, approximation
qualifiers, distinct nozzle heights, pool-observable classification and
rejection of guessed missing values/numerical-to-apparatus promotion. The
18 region/boundary mappings remain proposals with unresolved dependencies.
These tests do not validate a CAD model or demonstrate CFD accuracy.

Additional review verified Day 6 relative links and cylinder consistency
arithmetic, and confirmed the prior Days 1–5 documents, parameter data and
approved H1 processor are unchanged from ab09745.

## Deliverable index

1. [Experimental review](F7_Experimental_Geometry_Review.md)
2. [Geometry parameter register](../../data/day-06/F7_Geometry_Parameter_Register.csv)
3. [Original versus numerical geometry](F7_Original_vs_Numerical_Geometry.md)
4. [F7-1 specification](F7_1_Geometry_Specification.md)
5. [F7-2 specification](F7_2_Geometry_Specification.md)
6. [2402 workflow and capability gate](F7_STARCCM_2402_Geometry_Workflow.md)
7. [Regions and boundaries](../../data/day-06/F7_Regions_and_Boundaries.csv)
8. [Geometry verification checklist](F7_Geometry_Verification_Checklist.md)
9. [Missing geometry / source recovery](Missing_Geometry_Data.md)
10. [Revised plan](Revised_Day_By_Day_Research_Plan.md)
11. This research log.

## Review request and stop

Review origin/datum convention, source classification, unresolved pan/head/port
geometry, thermal-region requirements and prescribed-vs-predicted pool-area
policy. Obtain the primary reports/drawings and local installed 2402 help before
Day 8 construction. Day 7 is a proposed next review, not begun here.
Stop at the specification; no definitive STAR-CCM+ geometry is constructed.
