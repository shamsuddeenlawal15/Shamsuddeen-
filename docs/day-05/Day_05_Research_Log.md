# Day 5 research log

Date: 2026-10-13. Baseline: approved Day 4 commit
eeb1b99e9ee02d4fdd99b7648fb87468f34a6c67.
Scope: H1-A local operator preparation only; user authorized execution-pending
fallback when local solver access is unavailable.

## Deliverables and evidence status

- Local setup guide: evidence-gated workflow and run directory convention.
- Installation evidence: user-confirmed hardware/license separated from
  unknown build, OS, rank entitlement, physics/mesher availability and capacity.
- Model checklist: approved synthetic cube, constants and sealed-wall setup.
- Mesh quality CSV: expected geometry targets with all observed values blank.
- Solver execution log: local procedure and blank performance observations.
- Export compatibility report: canonical mapping and adapter acceptance gate.
- Verification results: analytical references, blank results, no pass claim.

No local installation, native solver exports, mesh or execution evidence was
provided. No executable release-specific GUI paths, macros or adapter were
invented. The Python processor and historical parameter databases are unchanged.
No STAR-CCM+ simulation, numerical accuracy or performance measurement is
claimed. Repository tests exercise software fixtures, not CFD.

## Repository validation

Executed in the cloud checkout on 2026-10-13:

| Command | Outcome |
|---|---|
| `python3 tests/H1_Postprocessing_Tests.py -v` | 21 tests passed |
| `python3 -m unittest discover -s tests -v` | 22 tests passed |
| `python3 scripts/check_day1_data.py` | PASS |
| `python3 scripts/day2_data.py --check` | PASS: 57 preserved + 25 added = 82 records |
| `python3 scripts/H1_Postprocessing.py --help` | Exit 0 |
| `git diff --check` | PASS |

All 43 software tests passed, with no failures or skips. Existing unit tests
include clearly labelled synthetic fixtures for other H1 cases; running those
regression tests does not execute or advance their CFD studies. No real-run
postprocessing was attempted. Tests validate tooling, not local solver accuracy.

Additional documentation review checked all Day 5 relative links, the 25-row
mesh CSV structure, blank observed/evidence fields and pending statuses, and
the analytical structured-grid face counts. All passed. These are document
integrity checks, not actual mesh diagnostics.

Cloud setup uses the existing Python standard library and accepted Git history;
no dependency installation or environment configuration changes are necessary.

## Separate unresolved F7 source prerequisites

H1-A does not resolve or use missing F7 inputs. Carry forward, without upgrading
verification status:

- Futagami et al. (1998), PNC TN9410 98-074: original F7 report not recovered/read.
- Louie and Aoyagi (2021), SAND2021-0136, DOI 10.2172/1761299:
  original report not recovered/read.
- Missing inlet dimensions/vent details, initial gas state and composition,
  instrumentation coordinates, material correlations and reaction/oxide
  coefficients remain subject to primary-source verification.
- Preserve the Day 2 equation transcription audit and apparatus/numerical-
  chamber distinction; no guessed coefficient or F7 input is adopted.

See [Source_Verification_Report.md](../day-02/Source_Verification_Report.md)
and [Equation_Transcription_Audit.md](../day-02/Equation_Transcription_Audit.md).
Earlier proxy access failures are historical evidence, not proof the reports
are unavailable publicly. No new literature retrieval is claimed on Day 5.

## Review handoff / stop

Researcher must supply exact build/OS evidence, four-process entitlement and
locally verified menu/report mappings before setup execution; then mesh
diagnostics, native initial/final field and step-monitor exports, solver and
resource logs for result review. No local numerical result is filled in here.
Stop after this Day 5 package. No H1-B/C/D or reactive sodium work has begun.
