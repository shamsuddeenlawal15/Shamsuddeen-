# Day 5 — local H1-A operator guide

Status: preparation complete; local execution pending. Based on approved Day 4
commit eeb1b99. No STAR-CCM+ installation or native exports were available to
this cloud task. This is a synthetic solver-verification cube, not F7 geometry.

## Evidence gates and sequence

1. Collect [installation evidence](STARCCM_Installation_Evidence.md) on the
   researcher's PC. Confirm exact release/build, OS and four-process entitlement.
2. Use the installed build's documentation to map each operation in the
   [model checklist](H1A_Model_Setup_Checklist.md) to its actual UI control.
   Retain manual section/page or help topic and screenshots. All STAR-CCM+
   operations below are **BUILD CHECK** requirements, not verified menu paths.
   Do not execute a macro or borrow another release's menu/API names.
3. Create the cube and models only after those mappings are verified. Save a
   pre-mesh simulation and the configuration evidence locally.
4. Generate the requested uniform rectangular 32³ grid using a documented
   structured/mapped route. A base-size setting alone does not guarantee it.
   If the release offers no verified route, stop and request mesh-method review;
   do not relabel trimmed/polyhedral cells as structured.
5. Populate the [mesh register](../../data/day-05/H1A_Mesh_Quality_Register.csv)
   from real diagnostics; resolve failed closure/connectivity/quality checks.
6. Configure all reports and exports before initialization. Inspect a native
   initial export against the [compatibility report](H1A_Export_Compatibility_Report.md).
   Missing report definitions or cell bounds are blockers, not implicit zeros.
7. Initialize, save the initial state, and conduct H1-A using the
   [execution log](H1A_Solver_Execution_Log.md). Inspect the first step before
   completing the planned 10 s interval. Preserve evidence even for a failed run.
8. Validate real exports, run the approved processor and complete
   [results review](H1A_Verification_Results.md). Stop for scientific review.
   Do not advance to H1-B/C/D, mesh-refinement trials or sodium modeling.

## Local file organization

Use a unique run ID, for example H1A_G1_P4_YYYYMMDD_attempt01 (an identifier,
not a claim of an existing run). Keep under the local ignored runs/ directory:

- raw/: untouched native CSVs, solver log, mesh diagnostics, residual histories.
- evidence/: build/manual mapping, model settings, resource samples, screenshots.
- manifest.json, monitors.csv, fields.csv: verified canonical data.
- processed/: successful postprocessing output and review notes.
- simulation/: initial and final solver files, with timestamps.

Copy the Day 4 templates from data/day-04/templates locally; they are not
valid results until populated from evidence. Record file checksums using the
OS's SHA-256 utility, export time and operator. Keep licensing keys, server
credentials and personal machine identifiers out of public Git commits.
Do not commit large solver files or fabricate sample solver datasets.

## Processing after real data exist

Python 3.10+ and Git history are the existing cloud/local data-tool requirements;
only the Python standard library is needed. From the repository root:

```bash
python3 scripts/H1_Postprocessing.py run runs/ACTUAL_RUN_ID
```

Replace ACTUAL_RUN_ID with the real directory; use the verified installed
Python invocation on Windows. This command processes files, not STAR-CCM+.
Retain stdout only on exit status 0, plus stderr and the script commit ID.
A processed result is not an automatic pass. No adapter is supplied because
no native export format has yet been observed.

F7 recovery remains independent; see the separate prerequisite section in
[the research log](Day_05_Research_Log.md).
