# STAR-CCM+ modeling feasibility assessment

## Preliminary decision

**Conditionally feasible; not yet model-ready.** STAR-CCM+ can generally
represent fluid flow, heat transfer, species transport, radiation, and user
sources, but quantitative F7 modeling depends on details omitted from the
article and on licensed model availability. No simulation has been created or
executed.

## Capability mapping

| Need | Candidate implementation | Principal risk | Day 1 disposition |
|---|---|---|---|
| Enclosure gas flow | 3-D finite-volume continuum | Initial gas state and vent geometry absent | Basic vessel envelope known; detailed report needed |
| Wall heat transfer | Solid regions or thermal boundaries | Grades/properties absent; Fig. 2 material ambiguity | Thickness/areas partly known; properties needed |
| Oxygen transport | Multicomponent species transport | Initial O2 and reaction-source consistency | Eq. 1 gives structure; constants/properties needed |
| Sodium pool burning | Surface mass/species/energy sources or custom model | No demonstrated native sodium-pool-fire model | Research required |
| Radiation | Participating-media/surface radiation candidate | No emissivity/optical data in article | Upstream source needed |
| Aerosol behavior | Particle/population model candidate | Chemistry, agglomeration, deposition complexity | Required only if Fig. 5 is in scope |
| Validation output | Reports, monitors, probes, tables | Axial sensor coordinates/raw data/uncertainty absent | Three pool radial locations known |

## Minimum model-enabling information

Facility and pan geometry; initial and boundary conditions; sodium inventory
and temperature; gas composition; wall thermal data; reaction stoichiometry,
kinetics, and heat release; radiation properties; sensor locations; time zero;
measured time histories; and uncertainty/acceptance criteria.

## Licensing and platform checks for Day 2

- Confirm STAR-CCM+ version, executable availability, license server access,
  and licensed physics modules without recording license secrets.
- Confirm whether Java macros and user code are allowed in the target runtime.
- Establish supported batch command and a minimal licensed smoke test.
- Do not build the physics model until the Day 1 source gate is approved.

## Risks

The dominant technical risk is the sodium oxidation submodel and its coupling
to heat release, oxygen depletion, and aerosols. Geometry and measurement gaps
could also make quantitative validation underdetermined. These risks must be
resolved with evidence rather than assumed inputs.
