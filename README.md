# Sodium Pool Fire STAR-CCM+ Research

Reproducible research workspace for assessing whether the F7-1 and F7-2 sodium
pool-fire experiments reported by Louie et al. (2023) can be modeled and
validated in STAR-CCM+.

## Current scope

Day 1 is complete and awaiting review. No STAR-CCM+ simulation has been
executed and no experimental or numerical result is asserted without a
page-level source.

The paper was reviewed from the user-provided attachment. For future local
re-review it may be placed at `references/source/louie_2023_original.pdf` (the
file is intentionally excluded from Git). Run:

```bash
python3 scripts/check_day1_data.py
python3 -m unittest discover -s tests -v
```

See [`docs/day-01/README.md`](docs/day-01/README.md) for the Day 1 status and
review gate.

## Repository layout

```text
data/                  Source-preserving tabular research data
docs/day-01/           Day 1 technical deliverables
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
