# Day 2 additive evidence database

`Updated_Parameter_Database.csv` is generated from the unchanged Day 1
`../parameters.csv` plus `Parameter_Additions.csv`. Original row order and all
14 original fields are preserved. Source metadata and Day 2 interpretation
fields are appended; new rows never overwrite accepted historical records.

- `day_added`: 1 for copied history, 2 for this review.
- `source_id`: joins `references/day-02/sources.json`.
- `source_access_status`: `read` or `not_retrieved`, agreeing with that register.
- `evidence_kind`: legacy record, published statement/equation, article gap,
  derived interpretation, or `source_unavailable`. Source-availability rows
  use `blocked`; they are not claims about unread report contents.
- `supersedes`: optional reference to another parameter ID. Equation fixes
  reference a different legacy CSV and are therefore mapped separately below.
- `derivation`: explicit reasoning/inputs for derived interpretations.
- `verification_basis`: what was actually checked, not a claim that a model
  has been experimentally validated.

`verified` is transcription/absence verification, never proof of experimental
accuracy or implementation readiness. A copied missing-data row still means
missing in the 2023 paper, even when its inherited status says verified.

## Equation corrections

| Archived equation (in `../equations.csv`) | Current Day 2 record | Change |
|---|---|---|
| EQ-001 | D2-EQ-001 | Denominator uses beta/nu² |
| EQ-002 | D2-EQ-002 | Printed m³ has no dot; definition unresolved |
| EQ-003 | D2-EQ-003 | Transcription confirmed; coefficient/basis unresolved |

Read the [equation audit](../../../docs/day-02/Equation_Transcription_Audit.md)
before using either historical CSV. No equations were implemented or evaluated
as a sodium-fire simulation.

## Reproduce and check

From the repository root, using Python 3.10 or newer (standard library only):

```bash
python3 scripts/day2_data.py --build
python3 scripts/day2_data.py --check
python3 scripts/check_day1_data.py
python3 -m unittest discover -s tests -v
```

The checker requires the accepted baseline commit in local Git history; a
shallow clone must include it. It checks provenance constraints and preservation,
not scientific correctness. The CSV source-document page fields refer to the
document actually read. Blank pages on blocked source-availability records are
intentional; unknown report pages are never invented.
