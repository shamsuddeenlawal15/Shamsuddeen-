# Updated research and publication roadmap

Day 1 is accepted. Day 2 establishes source status, remaining input gaps and a
conditional PC modeling strategy. This roadmap extends the original 90-day
plan to original scientific contributions, manuscript preparation and journal
submission. Days are work-package targets, not evidence that a gate has passed
or a guarantee of elapsed time. Source access, experimental uncertainty and
measured computing cost control the schedule.

No scientific contribution, accuracy improvement, STAR-CCM+ result or
publication acceptance is claimed. Day 2 ends before detailed geometry,
meshing, or physical-model construction; later rows below require scientific
review approval.

## Scientific position and hypotheses

The paper already introduces oxygen-transfer/oxide resistance and spreading
enhancements in MELCOR (Louie et al., 2023, p. 2, Eq. (1); p. 3,
Eqs. (2)–(3)). It also describes SPHINCS flame-sheet physics and radially/depth
resolved pan conduction (p. 3, Section 3.2). Simply repeating these ingredients
in STAR-CCM+ is not automatically an original contribution.

The paper identifies remaining post-discharge combustion and aerosol
discrepancies and possible oxide-model improvements (p. 3, Section 4; p. 4,
Figs. 3–5 and conclusion). These motivate the following **candidate questions**,
subject to a broader literature review and adequate data:

| Candidate contribution | Falsifiable comparison to preregister after source closure | Evidence needed to support a manuscript claim |
|---|---|---|
| Oxide accumulation and transport limitation | Does a time-dependent retained-oxide closure improve post-discharge predictions compared with a declared constant-retention baseline while preserving pre-discharge agreement? | Authoritative closure equations and property bounds; independent observable(s), numerical/experimental uncertainty, parameter identifiability; demonstrate that any improvement is not hidden retuning |
| Pool-spreading/thermal coupling | Does coupling evolving area to local pan conduction explain differences in combustion-rate peak shape better than a fixed-area or area-capped baseline? | Area history or credible independent bounds, thermocouple definitions and uncertainties, verified coupling and conservation, declared model-form comparison |
| Model fidelity per desktop computing cost | What reduced model retains useful predictive skill for F7 observables at lower measured cost? | Common input/validation definitions, convergence studies at each tier, measured wall time/memory on disclosed hardware, reproducible comparison rather than invented scaling estimates |
| Robustness and identifiability | Which uncertain inputs can F7-1/F7-2 actually constrain, and which uncertainty dominates the prediction? | Source-based priors/bounds, sensitivity/identifiability analysis, separation of input and numerical uncertainty, transparent reporting of non-identifiable parameters |

Select one primary contribution and at most a small number of supporting
questions after reproduction. Do not promise that an oxide-layer mechanism can
be identified from pool temperature and bulk aerosol alone. Failure to
discriminate models is a reportable result, not grounds to invent measurements.

## Schedule and review gates

| Target days | Work package | Reviewable artifact and exit condition |
|---|---|---|
| 1 | Original-paper foundation | Accepted Day 1 archive, subject to the two equation transcription corrections identified in Day 2 |
| 2 | Source availability and feasibility | Day 2 deliverables; unresolved assumptions explicitly reviewed before any model construction |
| 3–5, conditional | Obtain detailed F7 report, SAND2021-0136, property and uncertainty evidence; reconcile apparatus and numerical representation | Approved input register with source pages, units, conflicts, admissible assumptions and claims limited to accessible evidence |
| 6–10, conditional | Verify exact PC installation/license; review matching manuals; source/property unit checks and small solver example | Sanitized installation evidence, conservation test specification and measured resource budget; no F7 accuracy claim |
| 11–18, conditional | Geometry and mesh strategy for the approved reduced target | Source-traceable geometry decisions, symmetry justification, mesh families, sensor mapping and numerical-error plan |
| 19–28, conditional | Nonreactive flow/conjugate-heat-transfer and species benchmarks | Verified balances and reports; radiation/transport approximations documented |
| 29–38, conditional | Reviewed sodium/pool/oxide source implementation | Independently checked closure equations, stoichiometry, energy accounting, limiting cases and parallel behavior |
| 39–45, conditional | Experimental comparison protocol and pilot | Preregistered observables, time-zero treatment, digitization/measurement uncertainty, error metrics and calibration/validation split; computing budget updated |
| 46–55, conditional | F7-1 numerical verification | Mesh/time-step and conservation study; quantified numerical uncertainty |
| 56–65, conditional | F7-1 baseline assessment and any declared calibration | Transparent baseline comparison, parameter provenance and fitted-parameter list; no accidental claim of independent validation for calibrated outputs |
| 66–73, conditional | F7-2 prediction using frozen transferable choices | Archived configuration and predicted outputs before comparisons; test-specific documented inputs may differ |
| 74–80, conditional | Cross-test validation | Observable-specific errors, uncertainty and limitations; investigate failures without concealing post hoc adjustments |
| 81–85, conditional | Prioritized sensitivity and feasibility of a new contribution | Uncertainty ranking; decide which candidate question is identifiable and affordable |
| 86–90, conditional | Reproduction report and publication study design | Reproducible baseline archive, independent review and literature novelty check; select an original contribution or explicitly retain a reproduction-only scope |
| 91–110, conditional | Original contribution study | Locked comparison protocol, controlled model changes, additional verified runs and uncertainty-aware analysis; retain unsuccessful cases |
| 111–120, conditional | Manuscript drafting and artifact audit | Full methods/results/discussion draft, figures with actual provenance, source/data/code availability statements, limitations and replication instructions |
| 121–130, conditional | Scientific coauthor/reviewer checks and journal fit | Resolve comments, repeat only checks affected by corrections, agree authorship and target journal; verify current submission requirements |
| 131 onward, conditional | Submit and manage review | Final author-approved manuscript, verified journal policy compliance, submission record and tracked response-to-reviewers; revision schedule depends on actual editor/reviewer decisions |

If source access remains blocked, continue source-independent literature
organization and protocol work only. Do not start a purported experimental
reproduction using guessed inputs. A reduced idealized study is a different
scientific scope and requires explicit review of that scope change. No later
task in this table is authorized by the Day 2 work alone.

## Validation design and data discipline

Propose F7-1 as development/calibration and F7-2 as a held-out prediction case,
subject to review once data independence and test details are known. Record
every calibrated quantity and freeze it before F7-2 comparison. The tests are
closely related and share apparatus; successful F7-2 transfer alone does not
prove general validity across sodium-fire regimes. If measured F7-2 final area
is prescribed, declare that conditioning and do not report it as predicted.
Both tests' published curves have already been inspected, so held-out here
means excluded from parameter fitting, not unseen evidence or a genuinely
blind prediction. Declare this limitation in any manuscript.

Use separate comparisons for combustion rate, pool temperature at the actual
measurement locations, and vessel/exhaust aerosol concentration (Louie et al.,
2023, p. 4, Figs. 3–5). Preserve sodium-equivalent aerosol units. Document time
alignment and compare like averaging/sampling operations. Avoid fitting time
shifts after inspecting error unless that procedure is declared and its effect
reported.

Predeclare error metrics, numerical convergence requirements and uncertainty
treatment after learning the measurement resolution. Report absolute and
normalized errors with a physically justified normalization; relative error
near zero can be misleading. Graph digitization, if later approved, yields
derived estimates with digitization uncertainty, not raw measured records.
Separate publication figures' axis ranges from measured data values.

Maintain an immutable source snapshot/provenance register, approved input
manifest, exact software build, case configuration, code version, mesh/time-step
metadata, run logs, failed-run ledger, and scripts that reproduce every reported
table/figure. Retain license-protected files and copyrighted reports locally
unless redistribution rights are confirmed. Obtain permission for reused
publisher figures or generate original plots from lawfully available data with
clear attribution; do not copy a paper's graphical series as new measurements.

## Manuscript plan

1. **Introduction:** precise unresolved question and a dated review of prior
   sodium-fire/oxide/spreading studies; distinguish replication from novelty.
2. **Experiment and evidence:** test apparatus, F7-1/F7-2 differences, source
   access limits, sensor definitions and uncertainty; list unresolved inputs.
3. **Methods:** conservation equations, closure origins/ranges, numerical
   implementation, PC/software/license-independent reproducibility metadata,
   and model hierarchy.
4. **Verification and baseline validation:** numerical error, conservation,
   calibration choices and held-out results, with limitations.
5. **Original study:** one preregistered model comparison or uncertainty question
   supported by actual verified runs.
6. **Discussion and conclusions:** mechanism evidence, competing explanations,
   bounds of validity, computing tradeoffs and unresolved experimental needs.
7. **Availability and supplementary material:** accessible processed data and
   scripts, source provenance, case manifest and restrictions described honestly.

Do not populate Results with placeholder numerical conclusions. A negative or
inconclusive finding should be retained when the protocol and uncertainty make
it scientifically informative. Submission is conditional on coauthor approval
and a defensible result, not arrival at a scheduled day.

## Provisional journal shortlist

This is a fit hypothesis for later editorial review. Current scopes, article
types, fees, open-access policies, data policies, formatting and submission
rules have not been retrieved or verified in Day 2. No impact-factor, acceptance
probability, review-time or fee claim is made.

| Candidate journal | Why investigate it | Evidence required before selection |
|---|---|---|
| *Nuclear Engineering and Design* | The original F7 comparison was published here: Louie et al. (2023), vol. 407, 112285, PDF p. 1 | Current aims/scope and author guide; articulate the advance beyond the published comparison |
| *Nuclear Technology* | The supplied paper cites sodium-fire methodology in this journal: Yamaguchi et al. (2001), reference list on PDF p. 5 | Retrieve cited methodology and current journal requirements; assess relevance to nuclear-safety model validation |
| *Fire Safety Journal* | Candidate if the central contribution becomes fire/oxidation mechanisms and validated fire modeling | Verify current scope, recent comparable papers and author policies; no fit claim based on title alone |
| *Annals of Nuclear Energy* | Candidate if the outcome centers on nuclear-system modeling and uncertainty | Verify current scope and comparable validated modeling work, then confirm article/data policies |

Select a target after the contribution and evidence are clear. Keep a second
choice to avoid restructuring methods around unverified journal assumptions.
At submission record the exact author-guide version/date, availability
statements, funding/conflicts, authorship approval and artifact release decision.

## Day 2 stop condition

The next action is scientific review of the remaining assumptions and source
gaps. This roadmap schedules future work; it does not start Day 3, detailed
geometry, meshing, reaction construction, simulations, or submission.
