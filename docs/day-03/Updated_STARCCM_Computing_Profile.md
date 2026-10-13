# Day 3 computing environment register

Date: 2026-10-13 (Asia/Shanghai). Baseline: c09e453.
Evidence source: the user's supplied specifications in this conversation.
These are accepted user-confirmed facts; none was measured from the PC by Codex.

| Field | Recorded value | Verification status |
|---|---|---|
| CPU | Intel Core i9-14900HX | User confirmed |
| Cores / threads | 24 cores / 32 threads | User confirmed; exact scheduling/topology not inspected |
| Installed RAM | 32 GB | User confirmed; available memory and OS reporting units not measured |
| STAR-CCM+ license | Working | User confirmed; feature and parallel entitlements still to identify |
| Exact release/build | Not identified | Pending local evidence |
| Operating system / architecture | Not confirmed | Pending local evidence |
| GPU / VRAM / driver | Not reported | No acceleration assumption |
| Available disk / storage type | Not reported | Pending local evidence |
| Licensed parallel process count | Not established | Hardware threads do not establish entitlement |
| Available RAM under normal workload | Not measured | Needed for benchmark budget |
| Power/cooling conditions | Not reported | Record for repeatable laptop performance comparisons |

The actual solver runs will occur on the researcher's computer. There is no
claim that STAR-CCM+ is installed, licensed or tested in this cloud environment.
No local benchmark result, memory use, runtime or accuracy has been observed.

## Initial planning decision

Propose approximately 20,000–50,000 cells and four solver processes first.
An eight-process comparison is conditional on verified parallel entitlement,
available memory and the same physical/numerical problem. Neither all 24 cores
nor all 32 threads should be selected automatically. Hybrid-core scheduling,
background activity, cooling and power settings can affect scaling; record
these facts locally rather than inferring a particular core allocation.

The provisional later budgets are 50,000–150,000 and 150,000–400,000 cells.
They are affordability experiments, not mesh-independence evidence. See
[Initial_Mesh_and_Resource_Budget.md](Initial_Mesh_and_Resource_Budget.md).

## Research boundaries

The project aims at F7-1/F7-2 reproduction and validation, followed by an
original extension and a Q1-targeted manuscript. H1 establishes basic numerical
and resource readiness only. It cannot validate sodium oxidation or predict
an F7 result. Q1 status requires later verification for a named journal,
ranking database, subject category and year; no journal rank or acceptance
is established by this readiness plan.

The Day 2 evidence and parameter records remain unchanged. This register
supersedes their *unknown hardware* planning status only, not their unresolved
scientific inputs or software-version checks.
