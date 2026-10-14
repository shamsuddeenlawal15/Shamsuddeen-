# Sodium reaction requirements — no mechanism implemented

Stage 2 is reserved until Stage 1 verification is accepted and missing chemistry/
property/geometry evidence is reviewed. Stage 3 aerosol transport additionally
requires validated combustion behavior. No rate coefficient, equilibrium law,
reaction module or user code is activated.

## Literature actually supporting the requirements

L2023: Louie et al. (2023), Nuclear Engineering and Design 407, 112285,
DOI 10.1016/j.nucengdes.2023.112285. The retained Day 2
[material-source register](../day-02/Material_Property_Source_Register.md) and
[equation audit](../day-02/Equation_Transcription_Audit.md) remain authoritative.

| Requirement | Exact inspected evidence | Still needed |
|---|---|---|
| Oxygen supply / transfer limitation | p.2 Section 3.1.2 Eq.1 and definitions | Sh closure, molecular D, gas properties, delta/Delta_l, operating range and implementation context |
| Product/retention/heat partition | p.2 Table 1: DAB, FNA2O, FNA2O2, FO2, FHEAT definitions | Coefficients/functions, basis, calibration and consistent gas/pool allocation |
| Pool spreading | p.3 Eq.2 | Meaning of undotted m, C1, inventory/units, boundary treatment |
| Oxide-enhanced viscosity | p.3 Eq.3 | C2, oxide fraction basis, sodium-mixture applicability |
| Flame-sheet transfer model | p.3 Section 3.2 | Sodium-vapor/O2 flux balances, transport laws, enthalpies and solution method |
| Oxide suppression | p.3 Section 3.2 | Liquid-sodium fraction of total pool mass including oxides; full inventory accounting |
| Aerosol generation/retention behavior | p.3 Section 4 and p.4 Fig.5 | Size distribution, retained/released products, deposition/optics, uncertainty and sampling basis |

Futagami PNC TN9410 98-074 and Louie/Aoyagi SAND2021-0136
(DOI 10.2172/1761299) remain unrecovered originals; L2023 references them
on pp.4 and 5 respectively. The additional SAND2021-15469 / SAND2022-14235
report/DOI pairs remain previously recorded search leads, not inspected sources.
No new retrieval or coefficient verification is claimed.

## Species and conservative bookkeeping

Candidate inventory includes liquid Na, Na vapor if a vapor/flame-sheet
representation requires it, O2, specified inert carrier gas, and Na2O/Na2O2
with explicit condensed/aerosol phases. N2 may represent a documented air
carrier, but mixture fractions/humidity are unresolved. Additional water/
hydroxide/carbonate chemistry must be assessed from actual atmosphere/source
evidence, not silently assumed included or absent.

Researcher-written atom balances, NOT transcribed elementary mechanisms:
- 4 Na + O2 -> 2 Na2O
- 2 Na + O2 -> Na2O2

These relations establish only Na/O stoichiometric accounting. They provide no
kinetics, phase choice, heat of reaction or proof of sodium-fire model validity.
Product splits must preserve both elements and total mass; do not interpret
an unspecified FO2 fraction as a product mass fraction without its definition.

Required thermodynamic data: phase-specific formation/sensible enthalpies,
heat capacities, phase transitions/latent heat, vapor pressure and transport
properties over the applicable temperature range. Required closure evidence:
surface versus gas-phase mechanism, diffusion/kinetic limitation, transfer
coefficients, oxide permeability/thickness evolution, wetting/spreading,
product retention and heat partition. No numeric property law is adopted.

## Corrected equations and implementation holds

Eq.1 denominator contains beta/nu², not nu*beta². Its equal-temperature limit
requires documented treatment; do not invent a regularization or apply a
MELCOR control-function coefficient as generic CFD molecular diffusivity.
Eq.2 contains undotted m³, not mass-flow rate cubed; inventory meaning/C1 remain
unknown. Eq.3 mu=mu0*exp(2.5*C2*epsilon) leaves C2 and fraction basis unresolved.
SPHINCS pool mass-fraction suppression is not identical to an interfacial oxide
diffusion resistance. Copying either without its domain of validity is unsafe
scientifically.

Before later coding: recover full source definitions; verify units and phase
bases; test atom/mass/energy conservation, oxide-free/oxide-rich and zero-source
limits, thermal equilibrium behavior and implementation timestep sensitivity.
Separate calibration observables from independent validation. Prescribed final
pool area cannot also be a predicted-area validation result.

## STAR-CCM+ requirements

Determine from exact-build documentation/local evidence whether the chosen
conservative surface-source, species, energy and optional liquid/particle
formulation is supported and licensed. General combustion module availability
does not establish a sodium mechanism or correct heterogeneous oxidation.
No API, Java macro, kinetic parameters or vendor reaction-model support is
claimed verified here. The reaction framework remains BLOCKED for activation.
