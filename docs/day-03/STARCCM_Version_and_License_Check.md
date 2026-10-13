# Day 3 STAR-CCM+ version and license check

Status: working license confirmed by user; exact release, build, OS, enabled
physics and parallel allowance remain unknown. Instructions below are for the
researcher's local machine. No installation or license query was run in Codex.

**[BUILD CHECK]** marks a menu, interface or capability that must be confirmed
against the installed build's official documentation. No literal menu path or
command-line switch below is asserted to work in every 2024-or-earlier release.

## Identify the software before following a tutorial

1. Record the PC OS edition, version and architecture using its normal system
   information utility. If Windows is confirmed, its system About/information
   view and Task Manager are possible inventory routes; if Linux, distribution
   information and system-monitor utilities are alternatives. These are
   conditional OS suggestions, not observations of the user's machine.
2. Start the existing local STAR-CCM+ installation. **[BUILD CHECK]** Locate its
   application About/version dialog, commonly under a Help-related menu, and
   copy the complete release/version and build identifier exactly.
3. **[BUILD CHECK]** Cross-check the application startup/session log or launcher
   version information, recording executable path and exact build. Avoid
   relying solely on a desktop shortcut name.
4. **[BUILD CHECK]** Obtain the matching Installation Guide, Release Notes,
   Licensing Guide and physics/model reference from Siemens support or the
   licensed distribution. Record title, release, revision, page/section and
   checksum of downloaded manuals.
5. Confirm that the identified release is from 2024 or earlier. If only a newer
   installation is available, pause release-specific setup until an eligible
   build or an explicit change of scope is chosen. Do not downgrade software
   or assume backward compatibility of saved simulation files automatically.

## Check licensed physics and usable process count

A successful application launch does not prove entitlement to every model,
parallel count, user-code feature or accelerator mode.

| Check | Local procedure | Evidence to record |
|---|---|---|
| License identity/status | **[BUILD CHECK]** Read the application's licensing/status view or startup diagnostics; consult the administrator's entitlement statement if needed | Non-secret license type, validity and authorized research use |
| H1 physics availability | **[BUILD CHECK]** Inspect compatible model-selection options for transient 3-D constant-density flow, laminar viscosity, thermal energy, thermal boundaries and volume heat source | Exact model names, enabled/disabled states, manual sections; visibility alone is not a successful checkout |
| Extra future physics | **[BUILD CHECK]** Check solid conduction/interfaces, gas species, reaction/source coupling, radiation, multiphase and particle options separately | Available versus licensed versus successfully tested; none needed merely to run the initial constant-field check |
| Parallel entitlement | **[BUILD CHECK]** Consult the installed licensing guide and entitlement record or supported license diagnostic | Allowed solver processes and any token/core limits; 32 hardware threads is not the answer |
| Requested versus actual processes | **[BUILD CHECK]** Locate launcher parallel controls or documented batch options; later request four, then eight if entitled | Startup log showing actual ranks/processes and any checkout errors |
| Source and boundary conventions | **[BUILD CHECK]** Confirm whether heat-source entry is W/m³, W/kg or integrated W, and how wall heat flux and moving-wall velocity are defined | Manual page, units, sign and integration convention |
| Accelerator support | **[BUILD CHECK]** Read exact-build hardware/model compatibility matrix if GPU use is proposed later | CPU is the current planning baseline; no GPU performance assumed |

Do not use a guessed licensing command, server-variable name, token count or
parallel flag. A launch-time checkout error should be recorded and resolved
through the existing license arrangement, not by modifying research inputs.
Keep secrets, server credentials and license keys out of the repository.

## Local evidence form — all observations pending

- OS / architecture:
- Exact STAR-CCM+ release / build / installation path:
- Official manual titles / revisions / sections:
- License status evidence and authorized parallel count:
- Compatible H1 flow / energy / source / wall models:
- Requested process count / actual process count:
- Available RAM / free storage before launch:
- Date / operator / sanitized log location:
- Outstanding compatibility questions:

Documentation inspection may be completed locally before the next research
review. Benchmark geometry construction and solver execution await approval
of the plan. The version-specific setup sequence is in
[H1_Nonreactive_Benchmark_Plan.md](H1_Nonreactive_Benchmark_Plan.md).

Official documentation entry point: https://support.sw.siemens.com/en-US/
No matching manual has been retrieved or read for the still-unknown local build.
