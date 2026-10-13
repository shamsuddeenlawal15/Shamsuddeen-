# H1-A solver execution log

Status: NOT RUN. No STAR-CCM+ process was launched by this cloud task.
Populate observations only from the local researcher run.

| Run metadata | Observed value |
|---|---|
| Run ID / operator / date / timezone | |
| Build / OS / evidence filenames | |
| Model and mesh IDs / checksums | |
| Licensed / actual process count | |
| Schemes / precision / inner iteration policy | |
| Actual dt / final time / completed steps | |
| CPU power mode / background load / cooling | |
| Available RAM / disk before run (units) | |

## Local execution protocol (BUILD CHECK)

1. Complete installation, model, mesh and export gates. Predeclare review
   tolerances in the results sheet before inspecting results.
2. Start with four licensed solver processes; verify actual ranks in the log.
   Save timestamps from launch request to ready initialized server (startup).
   Record loading, mesh generation and initialization times separately where
   possible. Do not include them in timed solver work.
3. Export initial t=0 reports and full cell fields. Inspect extrema, volume,
   mass, wall flux and stored fields before stepping.
4. Advance one dt=0.1 s step using the verified build controls; inspect logs,
   continuity/momentum/energy residuals, temperature and velocity. Stop on
   NaN/Inf, divergence, invalid mesh, unexpected leakage or license errors.
5. If stable, continue the same state to 10 s; record every completed step
   and final full cell fields. A constant-field problem can start with zero
   residual: a prescribed multi-order residual drop is not required.
   Inspect all inner-iteration histories, not just a final residual.
6. Record wall-clock solve time from first advancement to last completed
   step, excluding subsequent export. Log pauses/interventions explicitly.
   Preserve warnings verbatim, including a verified absence if reviewed.
7. Save final simulation, raw exports and logs. Validate compatibility, then
   postprocess. Do not label an aborted run completed. A shorter pilot must
   declare its actual endpoint and is not the full 10 s trial.

## Resource measurement

Use the OS monitoring tool appropriate to the verified OS (Windows Task
Manager/Performance Monitor or Linux top/pidstat if installed). Sample at a
declared interval, provisionally 1 s, throughout startup and solve. Record
sampler/tool version, timestamps, all solver rank PIDs and client inclusion.
State whether CPU 100% means one logical CPU or the whole machine. Retain
the time series and summarize mean/peak; a screenshot is not a full peak trace.

Record memory metric explicitly (working set, RSS, private or proportional
memory). Sum-of-RSS may double-count shared pages; report that limitation.
Monitor whole-system available RAM and paging as well as solver memory.
Report sampled peak as sampled, not an exact lifetime peak. Record disk
growth and warn/stop on paging, exhausted storage or thermal throttling.
The existing 20 GB solver ceiling and 4 GB available-memory reserve are
provisional safeguards, not measured consumption; use the smaller feasible
budget given background use. Record GB versus GiB. No eight-process trial
or speedup claim is part of this Day 5 run.

| Measurement | Value | Unit / definition | Evidence |
|---|---|---|---|
| Startup duration | | s | |
| Mesh / initialization duration | | s | |
| Solver runtime | | s | |
| Export duration | | s | |
| Mean / peak CPU utilization | | basis required | |
| Sampled peak solver memory | | metric and units required | |
| Minimum available system RAM | | units required | |
| Free disk after run / disk growth | | units required | |
| Sampling interval / coverage | | s | |
| Warnings / stability observations | | | |
