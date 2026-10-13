# STAR-CCM+ installation evidence

No local installation has been accessed. User-confirmed hardware is Intel
Core i9-14900HX (24 cores / 32 threads), 32 GB RAM; a working license is
user-confirmed. These are not independently measured entitlement or capacity.

| Evidence item | Observed value | Status / required evidence |
|---|---|---|
| STAR-CCM+ release and full build | | Pending: version dialog and startup log |
| Operating system / edition / build / architecture | | Pending: OS inventory |
| License type and permitted parallel processes | | Pending: entitlement plus startup evidence |
| Actual active solver processes | | Pending: four-process launch log |
| Available physics models | | Pending: selection list and successful checkout |
| Available mesh methods | | Pending: mesher list and installed manual |
| Installed / available RAM with units | | Pending: dated local inventory |
| Free storage on project and temporary volumes | | Pending: dated local inventory |
| GPU / driver if relevant | | Unknown; no GPU solver path assumed |

## Researcher collection procedure

1. Start the local application normally. Find its version information using
   the installed Help/manual's version-information topic; a menu often called
   About is only a search hint, not a verified click path. Capture the entire
   release/build string, including patch suffix, and the startup log version.
   If they disagree, resolve which client/server builds are active.
2. On Windows, run winver and open System Information (msinfo32). Record OS
   edition/build, system type and CPU. In Task Manager's memory view record
   installed and currently available RAM with timestamp. Check free space on
   both the project drive and the actual solver temporary-file drive.
   On Linux run these read-only local commands:
   `uname -srm`, `cat /etc/os-release`, `lscpu`, `free -h`, and
   `df -h /actual/project/path /actual/temp/path` (replace paths).
   For another OS stop and check release support; none is presumed supported.
3. Consult the actual license entitlement or administrator for allowed
   concurrent solver processes. A working GUI license or 32 hardware threads
   is not proof of four licensed processes. Use the build's documented launch
   controls, then capture actual solver rank count and checkout success/warnings.
   Never publish license keys or server credentials. If four is unavailable,
   stop and review the protocol; do not mislabel a serial run as four-process.
4. In a new disposable local simulation, inspect the model-selection and
   mesh-operation lists using the installed manual. Capture labels, enabled/
   unavailable states and dependency explanations. Availability in a list is
   not proof of licensed execution. Record successful model/mesher checkout
   at setup and any errors at startup.
5. Verify supported OS and mesh/model capabilities against this exact release's
   installed help or Siemens documentation. Record document edition, topic/
   page, access date and evidence filename in the mapping table below.

| Intended operation (all BUILD CHECK) | Actual UI path/label | Exact-build reference | Local evidence |
|---|---|---|---|
| Version display / local server launch / rank selection | | | |
| Cube dimensions / units / surface naming | | | |
| Structured rectangular grid subdivisions | | | |
| Region assignment / boundary types | | | |
| Constant-density laminar flow / transient energy selection | | | |
| Material constants / gravity / pressure reference | | | |
| Adiabatic stationary wall / initialization | | | |
| Time step / inner iterations / stopping criteria | | | |
| Mesh diagnostics / reports / monitors / export | | | |

No release-specific menu name, Java API or launch command is verified in this
package. Execution is gated on completing these mappings locally. No cloud
configuration change or local solver installation is required for Python tests.
