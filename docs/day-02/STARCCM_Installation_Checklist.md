# STAR-CCM+ installation and PC requirements checklist

Status: **requirements identified; installation and entitlement not verified**.
There is no access to the user's personal computer or licensed STAR-CCM+
installation in this task. Cloud repository access is not evidence of a local
solver, an active license, or a supported operating system. All unchecked items
below remain pending; no smoke test or CFD run has been performed.

The user replied “yes i have” to the hardware/software availability question.
This is recorded as a general access self-report only. It supplies no exact
operating system, hardware specification, release/build, or license evidence;
the inventory fields below remain unreported rather than inferred.

## Authoritative documentation to obtain

Obtain the Installation Guide, Release Notes, supported-platform/system
requirements, licensing guide, model reference and relevant tutorials for the
**exact selected 2024-or-earlier release and build** from Siemens or the
institution's licensed distribution. Record document title, release, revision,
page/section and a local checksum when a downloadable file is available. Check
CPU/GPU and model compatibility against that release, not a current marketing
page or a newer manual.

The following official URLs were attempted on 13 October 2026 (Asia/Shanghai).
Each returned proxy `CONNECT` HTTP 403; the product endpoint was also retried
with escalated execution and failed in the same way. No vendor content was
retrieved. A blocked request does not establish that the
document is unavailable to the license holder. The release-page path below is
an attempted route, not a verified page title, publication, or release record.

| Attempted official location | Intended use | Evidence status |
|---|---|---|
| <https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/> | Product entry point | Request blocked; no capability claim derived |
| <https://support.sw.siemens.com/en-US/> | Licensed software/download/manual access | Request blocked; account and entitlement not tested |
| <https://blogs.sw.siemens.com/simcenter/simcenter-star-ccm-2402-released/> | Possible 2024 release information | Request blocked; URL content/existence not established |

No vendor-supported minimum RAM, core count, disk size, operating-system
version, graphics driver, GPU model, or compiler has been verified. Proposed
hardware budgets must be labeled project planning choices, not vendor minima.

## Inventory to collect from the user's PC

Record names and configuration only; do not commit license keys, server
credentials, host identifiers used as secrets, or private account screenshots.

| Item | Required record | Decision it supports | Current status |
|---|---|---|---|
| Software | Exact STAR-CCM+ product version/build, installed path, installation source; whether a 2024-or-earlier build is available under the license | Select matching manuals/examples and avoid newer-file/API assumptions | Unknown |
| Operating system | OS edition, release, architecture; native/virtual/remote use | Compare with supported-platform matrix for this build | Unknown |
| CPU | Model, physical cores, logical threads and instruction-set/platform compatibility | Supported execution and a measured parallel-process choice | Unknown |
| Memory | Installed RAM and RAM available under typical workload | Bound maximum resident model/process memory | Unknown |
| Storage | Available fast local storage, project/checkpoint location, quota and backup arrangement | Estimate input, transient results, checkpoint and export budget | Unknown |
| Graphics | GPU model, VRAM and driver; remote-display arrangement if applicable | Separate interactive display support from solver acceleration support | Unknown |
| License | License type/entitlement name, authorized user/use, validity, academic/publication restrictions if any | Confirm the research is licensed and relevant features can be checked out | Unknown |
| Parallel entitlement | Maximum authorized solver processes/cores and any required add-on entitlement | Avoid assuming all hardware threads are licensed | Unknown |
| License access | Whether a server or local licensing mechanism is required; reachability/status only | Identify connectivity/VPN/service prerequisites without exposing secrets | Unknown |
| Extension tools | Bundled Java/runtime expectations; supported compiler/API if compiled user code is required | Choose a maintainable source-coupling route | Unknown |
| Work budget | Available run hours, acceptable turnaround and concurrent desktop workload | Select H1–H4 scope from measured cost | Unknown |

## License and solver feature evidence

Do not infer a license bundle from a generic feature name. The precise
entitlement names, add-ons, parallel rights, and compatibility limits must come
from the selected release's licensing documents and the user's actual
entitlement. The list below specifies functions the research may need, not
separately purchasable module names.

- [ ] Base GUI/preprocessing, solver and postprocessing can be used under the
  user's license; batch execution is permitted if required.
- [ ] Transient flow, gravity, chosen gas-density treatment, and the selected
  laminar/turbulence approach are documented for the exact build.
- [ ] Solid conduction and fluid/solid heat-transfer interfaces support the
  intended pan, insulation and chamber treatment.
- [ ] Species transport and gas-mixture property/diffusion definitions support
  the chosen composition and temperature range.
- [ ] A supported boundary-flux, source-term, or surface-reaction interface can
  conserve mass, elements and energy for the proposed reduced pool model.
- [ ] Any required radiation approach supports the participating materials and
  intended coupling; property evidence is available separately.
- [ ] A selected evolving-area approach can update the wetted footprint and heat
  exchange conservatively, or the reduced coupling limitation is documented.
- [ ] Any later free-surface/volume-of-fluid model supports the intended material
  pair, thermal/species coupling, surface tension and wetting treatment.
- [ ] Any later particle/population treatment supports the required aerosol
  size range, source, deposition and agglomeration processes. A generic particle
  model is not sufficient evidence for sodium-aerosol validation.
- [ ] User expressions, tabular properties, macros or compiled user code are
  supported, licensed where applicable, documented and reproducible in the
  chosen build; serial and parallel source behavior is understood.
- [ ] Process count and any accelerator use comply with the license and the
  release-specific solver/model compatibility matrix.

Evidence for each check should include the manual section/page and, later, the
observed software result or license diagnostic with secrets removed. No item
can be marked passed solely from this document or the Day 1 feasibility note.

## Later installation verification procedure

These are instructions for a later authorized local check, not a report of
commands executed. Do not invent platform-specific flags. Use the installed
build's documented commands and examples.

1. Confirm installation origin, exact version/build and supported OS/CPU from
   the matching Siemens installation/release documents. Verify distribution
   integrity using the vendor's published method where provided.
2. Launch the application and record sanitized version and license status.
   Resolve license/service or platform errors before modifying research files.
3. Confirm that a vendor example matching the installed release can be opened;
   test save/reopen in an isolated project directory. Do not assume that a
   `.sim` file saved in a later release can be reopened by an older one.
4. After scientific review permits solver work, run a small documented vendor
   example with the relevant basic physics. Record its provenance, observed
   completion, process count, memory use and wall time. Passing establishes
   installation operation only, not validation of sodium-fire physics.
5. Verify the documented batch invocation and reports/export path if automation
   is needed. Check a conservative source-coupling example before reactive F7
   construction; collect elemental and energy balance evidence.
6. Use the measured resource procedure in `STARCCM_Model_Selection.md` before
   choosing simulation size, time resolution or sensitivity-run count.

This checklist deliberately does not prescribe a guessed installer command,
license-server variable, product activation procedure, or current entitlement
bundle. The license holder or institution should supply the relevant official
guide and entitlement information through their approved channel.

## Research prerequisites independent of installation

A working solver is necessary but does not close the source gaps. Louie et al.
(2023), pp. 2–3, define model parameters without the complete input deck or
property laws, and p. 4 supplies graphical comparisons without raw uncertainty
records. Complete the geometry, thermophysical-property, reaction, initial-state
and measurement reviews alongside software verification. The remaining
assumptions must be reviewed before detailed geometry, mesh, or physical-model
construction begins.
