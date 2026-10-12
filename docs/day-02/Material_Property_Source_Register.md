# Material property and reaction source register

Status: source identification and evidence audit completed; additional-source
correlations remain unverified because retrieval failed. Source IDs and access
evidence are in [Source_Verification_Report.md](Source_Verification_Report.md).
No numerical property law has been approved for a STAR-CCM+ model.

## Properties required

| Quantity / material | Accessible evidence and exact location | Preferred next evidence | Current disposition |
|---|---|---|---|
| Liquid sodium density rho(T), viscosity mu_0(T) | L2023 p.3, text under Eqs.2–3 defines symbols without values | S2021 implementation; independently confirm candidate F1995 Argonne reference | Coefficients, units and temperature ranges missing |
| Sodium heat capacity, conductivity, enthalpy, vapor pressure, latent heat | No quantitative laws in L2023 pp.2–4 | Verified sodium property reference, reconciled with S2021 | Required before energy/vapor-source closure |
| Sodium surface tension | L2023 p.3 §3.2 identifies surface tension/gravity in SPHINCS spreading | Y2001 and S2021; primary property source | No correlation, contact-angle or wetting data in article |
| Gas density, heat capacity, viscosity and conductivity | L2023 p.2 defines gas expansion beta and kinematic viscosity nu in Eq.1 | Documented mixture law and source for each species | Gas composition and state must first be recovered |
| Oxygen diffusivity D and Schmidt number Sc | L2023 p.2 Eq.1 and definitions | S2021 / originating model reference | Formula inputs and applicable state range not given |
| Carbon-steel catch pan | L2023 p.2 §2; thickness 6 mm, area 1 m² | F1998 steel grade and temperature-dependent properties | Material identity known only to class; no property table |
| Stainless-steel vessel and model structures | L2023 p.2 §2; p.3 Fig.2 | F1998 and S2021 construction/model specifications | Grade and thermal data absent; bottom material conflict unresolved |
| Insulation | L2023 p.2 two 50 mm layers; p.3 Fig.2 total 100 mm | F1998 and S2021 | Composition, density, heat capacity, conductivity and contacts missing |
| Oxide density, heat capacity, conductivity and layer permeability | L2023 pp.2–3 only discusses oxide effects | S2021 and original oxide transport literature | Required for a resolved oxide layer; values absent |
| Surface emissivity and aerosol/gas optical properties | No values in L2023 pp.2–4 | Material-specific data and documented radiation closure | No default is an experimental fact |

The candidate Fink–Leibowitz report (F1995) is a search lead, not a verified
source of adopted coefficients. No remembered sodium-property formula is
entered into the parameter database. Once obtained, check its exact units,
liquid/vapor branch, pressure dependence, temperature range, fit uncertainty
and continuity at any piecewise boundary before adoption.

## Oxidation and oxide-layer evidence

| Mechanism | Evidence actually read | Information still required |
|---|---|---|
| Oxygen transfer to pool | L2023 p.2 Eq.1 uses Sherwood number, pool diameter, gas diffusivity and `1 + delta/Delta_l` oxide resistance | Sh closure; delta evolution; Delta_l; DAB/D_diff implementation mapping |
| Product/heat partition | L2023 p.2 Table 1 defines DAB, FNA2O, FNA2O2, FO2 and FHEAT | Numerical values, dependencies, calibration origin and mass/energy accounting |
| Oxide-enhanced spreading viscosity | L2023 p.3 Eq.3: `mu = mu_0 exp(2.5 C2 epsilon)` | C2, epsilon mass/volume basis, oxide phases and valid range |
| MELCOR spreading | L2023 p.3 Eq.2 prints `m^3`; Eq.3 slows spreading as oxide fraction increases | Definition of m, C1, implementation history and terminal-area treatment |
| SPHINCS flame sheet | L2023 p.3 §3.2 describes sodium-vapor/O2 molar flux and energy balances at a zero-thickness sheet | Full algebra, transfer laws, enthalpies and solution procedure in Y2001/S2021 |
| SPHINCS suppression | L2023 p.3 §3.2 multiplies combustion rate by liquid-sodium mass / total pool mass including oxides | Exact species accounting and coefficient/input history |
| Aerosol feedback | L2023 p.3 §4 attributes post-discharge errors to oxide behavior; retained aerosol fraction treated as constant | Generation, retention, deposition, particle sizes, optical data and uncertainty |

The named Ramacciotti correlation in L2023 p.3 is used by analogy with corium;
this does not establish sodium-specific calibration or permit importing an
unverified C2. It is a model-form uncertainty, not an experimentally measured
material property.

As a future conservation audit only, atom balance gives `4 Na + O2 -> 2 Na2O`
and `2 Na + O2 -> Na2O2`. These are researcher-written balanced reactions,
not transcribed reaction mechanisms from the article. They supply neither a
rate law nor an enthalpy. A selected reaction model must close Na/O inventory,
phase-specific enthalpy and heat partition consistently; bulk combustion
modules cannot be assumed to supply validated sodium chemistry.

## Experimental benchmark evidence

L2023 p.4 Fig.3 contains combustion-rate curves, Fig.4 pool-temperature curves
at r = 0.1, 0.2 and 0.24 m, and Fig.5 vessel/exhaust aerosol observations.
L2023 p.2 §2 supplies terminal pool areas. None constitutes a raw numerical
dataset with uncertainty. L2023 p.4 says data are available on request; no
data request was sent. F1998 is the priority source for instrumentation and
test procedures. Future digitization would require its own record of image
calibration, curve identity, resolution and digitization uncertainty and must
not be labeled raw experimental data.

## Property acceptance contract

For each future correlation record author/report/revision, exact page and
equation, material phase/composition, input/output units, admissible temperature
and pressure, uncertainty, extrapolation policy, and conversion derivation.
Verify numerical values at at least three in-range temperatures against the
source, then inspect dimensions and limiting behavior. These are planned
acceptance tests; none has run without a retrieved correlation.
