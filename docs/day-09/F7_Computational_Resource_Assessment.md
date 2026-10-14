# Personal-computer resource assessment — scenario estimates only

User-confirmed: i9-14900HX, 24 cores/32 threads, 32 GB installed RAM, Windows 11,
STAR-CCM+ 2402 and working license. Installed RAM is not currently available RAM.
No actual runtime, peak memory, licensed rank count or mesh generation is known.

## Explicit planning assumptions, not measured performance

Use decimal GB (10^9 bytes) and kB (10^3 bytes). For a future total cell count N:
M_scenario = 2 GB + N*b/10^9 GB, b in [4000,16000] bytes/cell.
The 2 GB overhead and b range are deliberately broad analyst-selected scenarios,
NOT Siemens requirements, fitted measurements or validated bounds. They combine
a hypothetical process footprint; they are not multiplied by rank count.
Real mesher peaks, parallel duplication, faces, equation count and future
aerosol/chemistry fields can exceed them. Measure each phase separately.

| Level | Total cell budget | Equivalent volume scale | RAM scenario | Cell-work index |
|---|---|---|---|---|
| Coarse | 100,000–200,000 | 24.7–31.1 mm | 2.4–5.2 GB | 1 |
| Medium | 300,000–600,000 | 17.1–21.5 mm | 3.2–11.6 GB | 3 |
| Fine | 900,000–1,800,000 | 11.9–14.9 mm | 5.6–30.8 GB | 9 |

Equivalent scale=(3.0/N)^(1/3) m uses the schematic vessel label purely as a
reference-volume scenario (L2023 p.2 Fig.1 / Day 7 V003). It is NOT actual
gas volume, a predicted characteristic cell dimension of polyhedra, or a
base-size setting. Total N includes prospective solids/layers, so these
equivalent scales cannot size thin-solid meshes. Decimal precision in the CSV
is arithmetic precision, not experimental knowledge.

Cell-work indices assume identical work per cell/iteration and comparable
position within each budget; they do not predict wall time. Meshing overhead,
linear-solver conditioning, inner iterations, smaller stable/accurate time
steps and coupled fields may produce very different scaling. No seconds,
hours or speedup estimate is supported without a local pilot.

## Capacity decision and processes

Retain the provisional project safeguard: at most 20 GB solver/mesher process
budget and at least 4 GB available-system-memory reserve, using the smaller
feasible allocation once current background use is measured. These are project
safeguards, not vendor limits. Avoid paging; monitor system and process metrics.

At b=16000 bytes/cell and 2 GB overhead, 20 GB corresponds arithmetically to
N=1,125,000 cells, not a safe validated capacity. The fine upper scenario
30.8 GB exceeds both the process budget and practical 32 GB host headroom.
Mark it infeasible under that scenario; reduce scope with review or obtain
resources, not claim convergence by discarding necessary local resolution.

For a later authorized local pilot recommend four licensed processes first.
Verify actual ranks/checkout and measure aggregate/private memory and CPU load.
Eight processes are only a subsequent entitlement/resource comparison, never
inferred from 32 hardware threads. No solver runs are authorized in Day 9.
Record Windows power mode, cooling, background load and GB/GiB definitions.

## Storage and output management

No disk availability is supplied. Check both project and temporary volumes.
For planning let one retained state have hypothetical size
S=0.25 GB + N*b_disk/10^9 GB with b_disk=2000–8000 bytes/cell.
This is an uncalibrated storage scenario, not a native .sim compression estimate.
Reserve at least 3*S plus diagnostic exports per active run for working save,
checkpoint and temporary duplicate, then separately budget archives/backups
and future transient snapshots. At 1.8 million cells S is 3.85–14.65 GB;
three copies alone are 11.55–43.95 GB before diagnostics. Replace these scenarios
with actual measured file sizes before allocating a multi-run campaign.

Keep immutable CAD baselines and identified case/mesh attempts; save lightweight
statistics/monitors frequently and full fields only at scientifically selected
intervals after output review. Never delete the sole raw evidence to save disk.
Hash files, record build/settings and archive completed runs separately.
Commit only documentation/scripts/small reviewed manifests, not large .sim files
or credentials. Resource logs remain empty until real local evidence exists.
