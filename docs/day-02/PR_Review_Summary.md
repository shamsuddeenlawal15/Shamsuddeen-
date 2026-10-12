# Day 2: source audit, equation corrections and PC research requirements

The accepted Day 1 package did not close the experimental inputs or establish
release-specific STAR-CCM+ requirements. This change adds a Day 2 review package
and preserves the accepted evidence while correcting two equation transcriptions.

## Changes for review

- Add all nine requested deliverables: source verification, updated parameter
  database, geometry review, material-source register, model selection,
  missing-data decisions, installation checklist, publication roadmap and log.
- Preserve all 57 original parameter records; append 25 evidence/correction/gap
  records and explicit source-access metadata (82 total).
- Correct Eq.1 from `nu * beta^2` to `beta / nu^2`; record Eq.2's printed `m^3`
  without an unsupported mass-flow interpretation. Original Day 1 files are
  retained for provenance, with a prominent current-use audit notice.
- Distinguish experimental apparatus from numerical thermal structures,
  idealized PC benchmarks from full F7 reproduction, and candidate software
  features from verified release/license support.
- Extend the plan through controlled scientific contributions, manuscript
  preparation, journal selection and author-approved submission.

## Evidence and limits

The supplied Louie et al. 2023 PDF is the only primary document read during
Day 2. Official F7/Sandia/property/vendor requests were blocked by the network
proxy. SAND2021-0136 and PNC TN9410 98-074 remain unread; no new coefficients
or initial conditions were invented. Exact PC/software/license details remain
unreported. Source recovery and assumption review are required next.

No detailed geometry, mesh, physical model or STAR-CCM+ simulation was created.
Day 2 stops for scientific review. All later work in the roadmap is conditional.

## Validation

`python3 scripts/day2_data.py --build` and `--check` pass with 57 + 25 = 82
records. `python3 -m unittest discover -s tests -v`: 22 tests pass. The checks
test data integrity and historical preservation, not CFD accuracy or scientific
validity of historical strings.

Suggested PR base: `research/day-1-sodium-pool-fire` (accepted baseline).
Head: `research/day-2-source-verification`. This compares only Day 2 changes;
if the accepted Day 1 branch is later merged, retarget after checking the diff.
