# Mesh quality acceptance design — all observations pending

No mesh exists in available evidence. Candidate STAR-CCM+ diagnostic terms
below must be matched to the actual 2402 manual/UI with units and definitions.
Names are search labels, not verified exact menus or universal thresholds.

| Diagnostic / intended concept | Acceptance rule to establish | Native definition / threshold evidence | Actual result |
|---|---|---|---|
| Cell Quality | Review minimum and distribution; numeric limit unset until build/manual and discretization relevance established | | |
| Volume Change / Volume Change Ratio | Inspect abrupt neighboring-cell size jumps; definition and numeric limit unresolved | | |
| Skewness / Skewness Angle | Determine which metric and normalization the build reports; no borrowed cutoff | | |
| Non-orthogonality | Record face-normal/center-line relation per native definition; threshold unset | | |
| Face Validity if available | Verify exact-build meaning and acceptable range before use | | |
| Prism quality if later used | No inverted/collapsed layers; inspect achieved count, thickness, termination, aspect ratios and growth; numerical limits pending | | |
| Surface leakage / open edges | No unintended leak/open edge after intended openings receive proper geometric patches | | |
| Negative / zero cell volume | Zero negative or zero-volume cells; all retained volume cells strictly positive | | |
| Region connectivity | Match approved topology; no unintended islands or bridges | | |
| Interface integrity | No duplicate occupied volume; paired area/orientation/coverage audited | | |
| Mesh-to-CAD dimensions/volume | Differences within separately approved geometric tolerances; retain source approximation qualifiers | | |

Strictly positive volume and absence of unintended leaks are mathematical/
topological requirements, not attributed vendor numerical thresholds. They are
necessary, not sufficient, for accuracy. No arbitrary cell-quality, skewness,
growth-rate or non-orthogonality number has been adopted.

## Release criteria for an actual future mesh

- Source-backed geometry and all approved assumptions are traceable to file hash.
- Metric definitions, scopes and engineering thresholds are written before
  inspecting pass/fail outcomes, with manual references or explicit rationale.
- Full distributions and counts beyond thresholds are retained, not just means.
- Boundary layers, thin solids and small features are actually represented.
- Native diagnostics and orthogonal sections are reviewed for all regions.
- F7-1/F7-2 changes do not introduce collapsed features or unintended topology.
- Warnings and deviations are resolved or explicitly rejected for progression.
- Reviewer/date/disposition are recorded separately from software-test results.

Physical air/exhaust boundaries must not be converted into impermeable walls
just to eliminate an “open” diagnostic. Empty surface slots are not closed
patches and must never be meshed. Volume/count reconciliation must distinguish
gas, solids and any later liquid region.

Geometry verification checks shapes/topology; mesh verification checks their
discrete representation and quality; physical-model verification checks closure
implementation; experimental validation compares model predictions with data.
Passing one does not establish the next. Actual quality status is UNASSESSED.
