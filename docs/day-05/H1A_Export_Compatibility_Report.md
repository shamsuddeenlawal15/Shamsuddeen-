# H1-A export compatibility report

Status: UNVERIFIED — no native STAR-CCM+ CSV or local installation evidence
received. No adapter has been built or claimed tested. The existing canonical
processor remains unchanged.

## Required mapping

Populate observed headers, units/sign conversion and evidence from real files.
Do not infer values from this table's required meanings.

| Canonical column | Required meaning | Observed header | Conversion / report evidence |
|---|---|---|---|
| time_s | Physical seconds; t=0 and each completed step | | |
| mass_kg | Whole-region integral rho dV | | |
| mass_out_kg_s | Outward signed mass flux summed over six walls | | |
| absolute_wall_mass_flux_kg_s | Surface integral of absolute LOCAL mass flux | | |
| energy_J | Whole-region integral rho*c*(T-300) dV | | |
| heat_in_W | Conductive wall heat into fluid; inward positive | | |
| source_W | Volume integral of applied heat source | | |
| max_speed_m_s | Global maximum velocity magnitude | | |
| max_abs_divergence_s1 | Global maximum absolute velocity divergence | | |
| continuity_residual | Nonnegative residual with normalization documented | | |
| cell_id | Stable unique cell identifier within each snapshot | | |
| x_min_m / x_max_m | True rectangular cell bounds in metres | | |
| volume_m3 | Actual cell volume | | |
| temperature_K | Actual stored cell temperature, representation documented | | |

Exact ordered headers are in
[monitors.template.csv](../../data/day-04/templates/monitors.template.csv) and
[fields.template.csv](../../data/day-04/templates/fields.template.csv).
The latter also requires time_s. Retain temperature extrema, other residuals
and velocity/pressure exports separately; the canonical schema is minimal.

## Inspection and adapter acceptance gate

1. Preserve raw files and SHA-256 checksums. Record delimiter, encoding,
   decimal convention, comments, headers and whether multiple series are
   interleaved. Record export precision; insufficient digits can hide drift.
2. Inspect each report's definition, selected region/boundaries and units.
   Confirm physical time, not iteration number. Confirm all six walls and
   normal signs. Absolute net flux is NOT integral of absolute local flux.
   Neither a configured no-flux condition nor a missing column is a measurement.
3. Require strictly increasing monitor timestamps from 0 through stated final
   time at fixed dt. Do not interpolate, silently remove duplicate times or
   mix restarted attempts. Initial/final field snapshots must each contain
   the actual cell count with unique stable IDs and volume sum 0.001 m³.
4. Verify bounds using real mesh geometry/connectivity. Do not derive cell
   IDs or bounds from CSV row order or pretend centroid coordinates are bounds.
   This processor requires orthogonal rectangular cells; other grids require
   scientific review, even though H1-A's analytical temperature is constant.
5. Fill manifest from actual evidence: case H1-A; completed only for a completed
   stated interval; evidence_kind solver_export; actual build, OS, processes,
   cells, schemes, iteration policy, geometry/mesh IDs, initialization and
   reference sampling. q_vol_W_m3=0 and lid_speed_m_s=0 are configured inputs,
   not substituted measured columns. Keep all approved material constants.
6. If an adapter is needed, document each unit/sign transform and build tests
   using clearly labelled test fixtures, plus a hand-checked real-file subset.
   Tests must reject missing fields, ambiguous units, duplicate times, invalid
   numbers and truncated snapshots, and verify flux signs and energy reference.
   Compare integrated quantities before/after conversion. No silent zero fill.
   Review the adapter before using its results.
7. Run the approved processor only after mapping is verified. Preserve output,
   exit status, code commit and source checksums. Its file tolerances are
   consistency checks, not numerical accuracy criteria.

| Compatibility evidence | Observed value |
|---|---|
| Native filenames / hashes / build | |
| Geometry and report-scope identifiers | |
| Native delimiter / encoding / precision | |
| Mapping reviewer / date | |
| Adapter revision / test evidence if required | |
| Canonical processing exit status / output path | |

Status remains pending until actual files pass this process; no claim that the
real STAR-CCM+ exporter already matches the Day 4 schema is made.
