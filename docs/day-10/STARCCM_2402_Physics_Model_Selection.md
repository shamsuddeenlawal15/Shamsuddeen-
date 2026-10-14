# STAR-CCM+ 2402 physics selection assessment

Target release/OS are user-confirmed: 2402 (2024.1), Windows 11. Working license
does not establish specific physics modules, process count or API availability.
No local installation, screenshots or matching manual has been inspected.
All method names below are conceptual candidates/search terms, not verified
exact menu instructions or activated models.

| Requirement / candidate | Rationale and decision | Availability / license evidence |
|---|---|---|
| Three-dimensional gas | Full apparatus ports/thermal fields are not established axisymmetric; preferred eventual representation | Pending installed build/model list and entitlement |
| Transient segregated flow | Candidate pressure-based starting approach for a future low-Mach regime; no Mach/Re estimate possible yet | Verify actual flow formulation/dependencies and checkout |
| Gas energy | Required for thermal storage/advection/conduction and consistent CHT | Verify energy variable, pressure work and enthalpy reference |
| Density model | Temperature-dependent density/ideal-gas candidate for heated ventilation; constant-density/Boussinesq only under justified limited variation | Verify supported EOS and compatible energy/buoyancy model; gas state/composition pending |
| Turbulence | No F7 closure selected without inlet scales/properties and Re/Ra assessment | Verify candidate RANS/wall treatment if later required; no license assumption |
| Laminar | Appropriate only for a separately justified controlled benchmark; not proof F7 is laminar | Local capability and test specification pending |
| Solid conduction | Separate vessel, pan and two layers to retain material/contact distinctions | Verify solid-energy models and material-law support |
| Conjugate heat transfer | Conservative gas-solid and solid-solid heat paths; contact resistance needs evidence | Verify paired-interface capability and supported contact treatment |
| Gravity/buoyancy | Assess for thermally driven circulation; project Z is up, eventual g vector down | Magnitude/implementation and state coupling pending; do not inherit H1 g=0 |
| Species / pool reaction | Stage 2 only; requires conservative mass/energy closure and verified surface or volume implementation | Exact modules, dependencies and license pending |
| Radiation | Later relevance assessment for high-temperature case, not an initial assumed default | Optical/emissivity data and supported model pending |
| Aerosol transport | Stage 3 only after combustion validation; selection follows size/loading/transport regime | Particle/sectional/moment capabilities and license pending |

A segregated formulation is a recommendation to evaluate, not a guarantee of
convergence or a conclusion that compressibility is negligible. Coupled-flow
alternatives require a justified change and re-verification if later evidence
demands them. No turbulence coefficients or wall-function constants are set.

## Local verification procedure before implementation

After geometry/mesh approval, record full client/server patch/build, matching
installed help topic/page for each candidate, model-selection dependencies,
enabled/disabled availability, license entitlement and checkout warnings.
A selectable item alone does not prove a working licensed configuration.
Keep keys/server credentials out of Git. Do not invent Java methods or
release-specific menu paths. No exact GUI activation sequence is issued now.

Gas_Stage1 is the proposed gas continuum. Vessel_Conduction, Pan_Conduction,
Insulation1_Conduction and Insulation2_Conduction are distinct material-role
continua until real grades/properties establish whether any safe sharing exists.
Thermal_Coupling is a requirement, not a literal extra material continuum.
Gas_Stage2_Extension denotes later extension of the gas equations, not a
duplicate overlapping gas region. Sodium_Reserved and Aerosol_Reserved stay
inactive and need not create any local objects.

The 6 mm pan / 50 mm layers require justified thermal resolution; Day 9 bulk
budgets cannot establish it. Turbulent wall treatment would require compatible
near-wall mesh and later y+ evidence. Physics decisions and mesh design must be
reviewed together without pretending either is already verified.

## Material acceptance

Use [the material register](../../data/day-10/F7_Material_Property_Register.csv).
For each future value/law record exact source/page/equation, phase/grade/
composition, units, temperature and pressure range, uncertainty, interpolation/
extrapolation rule and conversion. Check against source values at multiple
in-range temperatures and verify continuity/positivity where applicable.
No such property tests can run without recovered correlations.

For an ideal-mixture candidate rho=p_abs*M_mix/(R_u*T), require absolute pressure,
temperature and mixture molar mass with consistent units. This is a proposed
thermodynamic form, not an adopted air correlation or experimental measurement.
Specific heat, conductivity and dynamic viscosity remain pending; do not insert
library defaults as published F7 values. Insulation materials/anisotropy and
contact resistances also remain unknown.
