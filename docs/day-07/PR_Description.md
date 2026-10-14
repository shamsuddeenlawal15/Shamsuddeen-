# Day 7: F7 geometry verification and conditional CAD readiness

Base: research/day-6-f7-geometry-reconstruction at 74e3561.
Head: research/day-7-f7-geometry-verification.

## Summary

- Review all Day 6 files; preserve previous source records and equation audit.
- Add 17 source-verified article records, 37 CAD inputs/references with 23
  explicit unknowns, and 21 proposed region/surface/interface names.
- Clarify nozzle-height datum versus exit orientation, bottom-only Fig.2
  material conflict, physical openings versus numerical BCs and pool–gas coupling.
- Add independent analytical consistency calculations and an evidence-summary
  audit utility, with 13 meaningful new tests; no CAD kernel or solver claims.
- Provide twelve requested deliverables, local operator gates, QA contract
  and exact first reference-datum step for a separately authorized Day 8.

## Verification

42 discovered tests + 21 H1 tests = 63 passing; no failures/skips.
Day 1 and Day 2 data checks pass. Analytical utility exits 0.
Historical sources and H1 implementation remain unchanged.

## Scientific review required

Full F7 construction remains BLOCKED: no verified head/barrel dimensions,
actual shell thickness, pan planform, nozzle bore/pose or vent sizes/locations.
Four primary-report destinations and Siemens documentation still fail through
the cloud proxy. Exact 2402 controls/API remain unverified; no macro supplied.

APPROVED scope is only the mathematical project datum convention and supported
parameter bookkeeping. Local execution remains conditional; P0 assumptions
need separate approval. No CAD, mesh, CFD or real-CAD validation has occurred.
Do not merge as an approval of full F7 reproduction or start Day 8 automatically.

This is a prepared PR description; no GitHub PR creation is claimed.
