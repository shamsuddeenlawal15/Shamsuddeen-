# Updated Day 03 research log

Date: 2026-10-13 (Asia/Shanghai). Scope: computational-readiness documentation.
Baseline: `c09e453ab9b3cfe2abe42f4d14dd1f9e0d3d7c74`.
Branch: `research/day-3-computational-readiness`.

## Environment and input status

The first resume was blocked by a failed cloud environment. After the user
restarted it, readiness and a clean Day 2 baseline were confirmed. No solver
installation was sought in the cloud; the researcher's local PC is the planned
execution platform.

Recorded user-confirmed facts: Intel Core i9-14900HX, 24 cores / 32 threads,
32 GB RAM and a working STAR-CCM+ license. Exact release/build, operating
system, enabled physics and licensed process count remain unconfirmed. The
working-license confirmation is preserved and is not replaced by an assumption
that the license is absent.

## Six deliverables

1. [Updated_STARCCM_Computing_Profile.md](Updated_STARCCM_Computing_Profile.md)
2. [STARCCM_Version_and_License_Check.md](STARCCM_Version_and_License_Check.md)
3. [H1_Nonreactive_Benchmark_Plan.md](H1_Nonreactive_Benchmark_Plan.md)
4. [Initial_Mesh_and_Resource_Budget.md](Initial_Mesh_and_Resource_Budget.md)
5. [CFD_Verification_Checklist.md](CFD_Verification_Checklist.md)
6. This research log.

The benchmark is a synthetic sealed cube, not an exact F7 geometry. Its
constants and analytical expressions are explicitly proposed mathematical
inputs/references, not experimental data or numerical results. Four cases
cover constant-field preservation, imposed heating, transient diffusion and
mass accounting under internal flow. Version-dependent features/menu concepts
are labeled `[BUILD CHECK]`; the exact installed manual remains necessary.

Mesh stages 20,000–50,000, 50,000–150,000 and 150,000–400,000 cells are
provisional resource budgets. Four/eight processes are subject to entitlement
and actual resource measurements. None establishes mesh independence or
predicts performance on the supplied hardware.

## Continued source recovery

On this date both official destinations below were retried normally and with
escalated execution. Each returned curl exit 56, `CONNECT tunnel failed,
response 403`. This is a proxy-level refusal; no report content was received.

| Target | Exact attempted destination | Status |
|---|---|---|
| SAND2021-0136 / DOI 10.2172/1761299 | https://www.osti.gov/servlets/purl/1761299 | Not retrieved or studied |
| F7 report PNC TN9410 98-074 | https://jopss.jaea.go.jp/search/servlet/search?kw=PNC%20TN9410%2098-074 | Search response not retrieved; original report unread |

No network settings or credentials were changed. Recovery still requires lawful
PDF copies or functioning official access. On receipt, verify report identity,
revision, checksum and pagination, then extract exact parameter/equation pages
with units and calibration context. No missing F7 input was filled with a guess.

## Continued equation verification

The supplied Louie et al. (2023) PDF remains checksum-identical:
`bf55d2d991b0d1defc2e78486a1869b67b5888c48fc4826355493d667eb34afe`.
The saved enlarged images of its p.2 Eq.1 and p.3 Eq.2 were visually rechecked:
Eq.1 contains beta/nu²; Eq.2 prints undotted m³. The
[Day 2 audit](../day-02/Equation_Transcription_Audit.md) remains the current
correction record. Definition of m, C1/C2, oxide fraction basis, transfer
closure and implementation context still require the original model report.
These checks establish transcription only, not physical validity. Historical
parameter, equation and Day 1/2 review files remain unchanged.

## Validation actually executed

- `python3 scripts/check_day1_data.py`: PASS.
- `python3 scripts/day2_data.py --check`: PASS, 57 preserved + 25 added = 82
  historical Day 2 records; no new experimental data added on Day 3.
- `python3 -m unittest discover -s tests -v`: 22 passed, 0 failed/skipped.
- Original PDF SHA-256 matched the recorded identity.
- Repository diff review confirmed earlier evidence files were unchanged.
- Documentation check found all six requested files and resolved all ten
  relative document links; benchmark volume/power/slope and example mesh-count
  arithmetic were checked independently of a solver.
- Git whitespace/diff checks passed before commit.

These are repository/data checks, not solver verification. All benchmark
accuracy, conservation, mesh/time refinement and performance checks remain
PLANNED. No STAR-CCM+ launch, license checkout, geometry construction, meshing,
simulation, numerical result or local hardware measurement was performed.

## Review handoff

Review the synthetic benchmark definition, build-specific implementation route,
provisional process/memory budgets and numerical acceptance procedure. Supply
the exact release/build and OS before a local setup walkthrough. Obtain the
primary reports before closing F7 physical-model assumptions. The later
publication plan remains conditional; Q1 targeting requires current journal,
category, ranking source and year verification after a defensible contribution.

Documentation is to be committed locally and work stopped for review. No push,
pull-request creation or solver run is part of this Day 3 handoff.
