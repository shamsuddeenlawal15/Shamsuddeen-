# Sodium Pool Fire STAR-CCM+ Research

Reproducible research workspace for assessing whether the F7-1 and F7-2 sodium
pool-fire experiments reported by Louie et al. (2023) can be modeled and
validated in STAR-CCM+.

## Current scope

The [Day 3 readiness plan](docs/day-03/Updated_Day_03_Research_Log.md) records
the user's i9-14900HX, 32 GB RAM and working-license confirmation. It proposes
local nonreactive benchmarks and resource/verification checks; the exact
STAR-CCM+ release and OS remain unknown. No benchmark has been executed.

Day 1 documentation review is accepted. The [Day 2 review package](docs/day-02/README.md)
is prepared with source-access limits, an additive parameter register and a
conditional PC modeling strategy. Original F7/Sandia reports and release-specific
Siemens documentation could not be retrieved through the environment proxy.
No STAR-CCM+ installation was accessed and no simulation has been executed.

**Equation corrections:** Day 2 visual review found two errors in the archived
Day 1 equations. Read [Equation_Transcription_Audit.md](docs/day-02/Equation_Transcription_Audit.md)
before implementation. The old files remain unchanged as historical records.

The paper was reviewed from the user-provided attachment. For future local
re-review it may be placed at `references/source/louie_2023_original.pdf` (the
file is intentionally excluded from Git). Run:

```bash
python3 scripts/check_day1_data.py
python3 scripts/day2_data.py --check
python3 -m unittest discover -s tests -v
```

Python 3.10 or newer and Git history containing the accepted Day 1 commit are
required for the Day 2 validator. It checks provenance constraints and historical
preservation; it cannot establish scientific accuracy.

Review Day 2's remaining assumptions before detailed geometry, meshing or
physical-model construction. The Day 1 documents retain their historical status.

## Repository layout

```text
data/                  Source-preserving tabular research data
docs/day-01/           Day 1 technical deliverables
docs/day-02/           Day 2 evidence audit, PC strategy and publication roadmap
docs/day-03/           Local computing readiness and proposed H1 verification plan
models/starccm/        Future simulation conventions; no model files yet
references/            Citation metadata and local source-file instructions
scripts/               Reproducible, standard-library data checks
tests/                 Automated checks for the research data contract
```

## Research integrity

- Use `published` only for values directly stated in the paper.
- Use `derived` only with an explicit equation and cited source inputs.
- Use `missing` for information required by the model but not published.
- Never place an assumed value in the published-parameter database.
- Keep the publisher PDF local unless redistribution rights are confirmed.
