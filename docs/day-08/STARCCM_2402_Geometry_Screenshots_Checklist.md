# Local geometry screenshot and QA checklist

Status: no screenshots received or generated. Do not substitute a diagram,
rendered paper figure or AI-generated image for actual local STAR-CCM+ evidence.
Reference-only or P0 views must be labelled accordingly.

| Required image | Content and diagnostic scope | Actual filename / hash | Review |
|---|---|---|---|
| 1 Full apparatus view | Both case identity and all actual components; show omissions/placeholders | | |
| 2 Vessel cross-section | Actual inner/outer/head geometry with dimensions; P0 cannot prove shell geometry | | |
| 3 Catch pan view | Actual outline, top/bottom/wall, 1 m² constraint and measured thickness | | |
| 4 Nozzle position comparison | Pan datum and 0.1 / 1.5 m reference offsets; no invented bore | | |
| 5 Component tree | Requested eight component labels; distinguish empty names from bodies | | |
| Supplemental build / units / frame | Complete build, metre units, right-handed Z-up triad | | |
| Supplemental contacts / diagnostics | Closure, overlap, normals and connectivity selection scopes | | |
| Supplemental reopen | Same saved file, configuration and checksum-linked evidence | | |

For the current datum-only stage images 1–3 cannot demonstrate completed
apparatus. Mark unavailable components pending, not passed or silently omitted.
A screenshot alone does not establish watertight geometry or absence of overlaps.

## Before the operator saves a construction checkpoint

- Verify actual body bounds/areas/thicknesses using native CAD diagnostics.
- Check each solid is closed and valid, with no unintended intersections or
  duplicate faces. Intended contacts are not overlapping volumes.
- Once a fluid enclosure exists, check connectivity including lower cavities;
  cover real openings with named geometric patches for the closure check.
  Such patches are not assigned impermeable wall BCs.
- Confirm outward orientations and intended contact pairings.
- Check names and project/component/configuration identity against the register.
- Check F7_1/F7_2 relative nozzle heights; do not infer their existence from
  parameter values alone.
- Preserve diagnostic text/selection scopes alongside images and CAD files.

Reference planes, empty surface slots and annotations are not closed solids
and must not be counted as such. Actual gas/solid topology is pending. There
is no geometry QA PASS in this preparation package.

Save local files with timestamp, build, operator, source revision and assumptions;
calculate SHA-256 using the local OS tool. Redact personal/license information.
Record audit CAD values only from actual measurements; convert units explicitly
to the audit row's unit, then compute CAD_value-source_value. Approximate
source values keep their qualifiers and unquantified uncertainty.

The Day 7 Python tool may check analytical calculations and future mapped
diagnostic summaries; it is not a CAD kernel and cannot validate these images
or intersections directly. No real-CAD processing was performed here.
