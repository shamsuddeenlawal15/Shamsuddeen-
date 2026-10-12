# Governing equations review

The atomic transcription is in `data/processed/equations.csv`. Equations below
use plain-text notation transcribed from printed pages 2-3; the PDF remains the
authority for typography.

## Published MELCOR enhancements

1. Oxygen-diffusion model, printed Eq. (1):

   `D_diff = [(Sh/L)(D/(1 + delta/Delta_l))] /
   {0.14[g Sc nu beta^2 |T_surf - T_g|]^(1/3)}`

   The article defines all symbols. It calls this an improvement to `DAB`,
   while the printed left-hand symbol is `D_diff`; that notation mapping needs
   confirmation from Louie and Aoyagi (2021).

2. Pancake radial spreading, printed Eq. (2):

   `R(t + Delta_t) = [R(t)^8 + C1 g m_dot^3 Delta_t /
   (mu pi^3 rho^2)]^(1/8)`

   `C1` is empirical; no value is published. The model represents viscous and
   gravitational effects.

3. Oxide-enhanced viscosity, printed Eq. (3):

   `mu = mu_0 exp(2.5 C2 epsilon)`

   `epsilon` is oxide fraction, `C2` is empirical, and `mu_0` is liquid-sodium
   viscosity. No `C2` or property correlation is published.

All three were implemented through MELCOR input control functions rather than
source-code changes.

## Published SPHINCS formulation

SPHINCS is described as a lumped-mass/1-D flow-network thermal-hydraulics code
with a zero-thickness flame sheet. It solves mass and energy conservation for
sodium-vapor and oxygen molar fluxes and heat transfer among pool, flame sheet,
and atmosphere. Combustion rate is multiplied by the liquid-sodium fraction of
total pool mass including oxide. Spreading balances surface tension and
gravity, stops at an input maximum area, then increases pool height. Floor heat
transfer uses a 2-D ring mesh in radial and depth directions. The article does
not print these conservation equations or coefficients.

## STAR-CCM+ equation set required

The eventual model needs gas mass/momentum/energy and species conservation,
sodium inventory and spreading, oxygen-consistent surface reaction sources,
reaction heat partition, conjugate wall heat transfer, radiation, and—if kept
in validation scope—aerosol generation/transport/deposition. The paper does not
fully close any of these inputs for STAR-CCM+.

## Verification requirements

- Demonstrate sodium, oxygen, reaction-product, and energy conservation.
- Unit-test source terms and limiting cases outside the full CFD model.
- Separate numerical (mesh/timestep) and model-form uncertainty.
- Do not use curve-fit coefficients until their provenance and calibration
  relationship to F7-1/F7-2 are documented.
