# Day 2 equation transcription audit

## Scope and preservation of the Day 1 record

Source: Louie et al. (2023), *Nuclear Engineering and Design* 407, 112285,
DOI [10.1016/j.nucengdes.2023.112285](https://doi.org/10.1016/j.nucengdes.2023.112285),
printed/PDF pp. 2–3, Eqs. (1)–(3). The supplied publisher PDF was visually
examined at enlarged resolution; automatic text extraction alone incorrectly
orders the nested fraction in Eq. (1). The archived Day 1 CSV and review remain
unchanged to preserve provenance. Their `verified` labels on EQ-001 and EQ-002
do **not** survive this Day 2 audit. Use the following corrections for future
implementation, subject to the unresolved definition checks below.

## EQ-001: oxygen-diffusion control function

The printed Eq. (1), p. 2, is:

```text
D_diff = [(Sh / L) * (D / (1 + delta / Delta_l))]
         / [0.14 * (g * Sc * (beta / nu^2) * abs(T_surf - T_g))^(1/3)]
```

The denominator contains `beta / nu^2`. Day 1 erroneously recorded
`nu * beta^2`. The PDF identifies `Sh` as Sherwood number, `L` as pool diameter,
`D` as gas diffusion coefficient, `delta` as oxide-layer thickness,
`Delta_l` as characteristic length scale, `g` as gravitational acceleration,
`Sc` as Schmidt number, `beta` as gas expansion coefficient, `nu` as kinematic
viscosity, and `T_surf` and `T_g` as pool-surface and gas temperatures
(p. 2, paragraph directly following Eq. (1)).

Dimensional cross-check, using SI dimensions and dimensionless `Sh` and `Sc`:
the numerator has units m/s; `g * beta * abs(Delta_T) / nu²` has units m⁻³;
its cube root has units m⁻¹; consequently `D_diff` has units m²/s. This supports
the visual transcription but does not validate the empirical model.

The article calls the improved MELCOR input `DAB`, while the printed equation
uses `D_diff` (p. 2, Section 3.1.2). Numerical evaluation still requires the
Sherwood correlation and regime, `D(T, composition)`, `nu`, `beta`, oxide
thickness/length-scale definitions, and treatment of `T_surf = T_g`. The
denominator tends to zero at equal temperatures; no regularization is
specified in this article. Do not invent a floor value or apply the equation
as a general-purpose CFD diffusivity without the underlying control-function
context in SAND2021-0136.

Status: **visual transcription corrected; implementation context incomplete**.

## EQ-002: pancake spreading relation

The printed Eq. (2), p. 3, is:

```text
R(t + Delta_t) = [R(t)^8 + C1 * g * m^3 * Delta_t
                 / (mu * pi^3 * rho^2)]^(1/8)
```

There is no dot over `m` in the supplied PDF. Day 1 changed it to `m_dot`
and defined that as liquid-sodium inflow rate; neither the dot nor that
definition is supported by this article. The prose immediately following the
equation defines `mu`, `rho`, and `C1` as sodium viscosity, density, and an
empirical constant. It does **not** define `m` explicitly. The earlier prose
describes radial spreading and defines `t` and `Delta_t`.

Dimensional cross-check: if `mu` is dynamic viscosity and `C1` is
dimensionless, `g / (mu * rho²)` has dimensions L⁸/(M³ T). Therefore
`m³ * Delta_t` must have dimensions M³ T, consistent with `m` being a mass.
Using a mass rate in kg/s would make the added term L⁸/T³, incompatible with
`R(t)^8`. This is evidence against the Day 1 mass-rate interpretation; it is
not sufficient to decide whether `m` is sodium mass, total sodium/oxide mass,
or another inventory. That definition and the adopted coefficient must be
checked in SAND2021-0136 or its cited spreading-model source before coding.

Status: **visual transcription corrected; mass basis and coefficient unresolved
in the 2023 article**. No experimental mass or reaction coefficient has been
inferred from this dimensional argument.

## EQ-003: oxide-enhanced viscosity

The printed Eq. (3), p. 3, agrees with the Day 1 transcription:

```text
mu = mu_0 * exp(2.5 * C2 * epsilon)
```

The text identifies `epsilon` as the fraction of sodium oxides, `mu_0` as the
liquid-sodium viscosity, and `C2` as empirical. It refers to a Ramacciotti
correlation used in corium modeling. It does not give a numerical `C2`, specify
mass versus volume fraction for `epsilon`, or state that a corium-derived
coefficient is experimentally established for the F7 sodium/oxide mixture.
The expression requires a dimensionless exponent; with a dimensionless
fraction, `C2` is dimensionless. A property-model applicability assessment
is still required even if a coefficient is found in the 2021 input model.

Status: **transcription confirmed; coefficient, fraction basis, and sodium
mixture applicability remain source-dependent**.

## EQ-004: SPHINCS oxide suppression

The unnumbered text in Section 3.2, p. 3, states that combustion rate is
multiplied by the liquid-sodium fraction of the total pool mass, including
oxide mass. Day 1 accurately preserved this as a qualitative relation. It
does not independently specify a surface oxide-thickness law, product split,
or aerosol partition model. A homogeneous pool mass fraction and an
interfacial diffusion resistance are different closures; neither should be
silently substituted for the other in a CFD implementation.

## Downstream actions

- Preserve Day 1 artifacts as historical records, but link to this audit from
  the Day 2 entry point and identify EQ-001/EQ-002 as superseded transcriptions.
- Store any adopted SAND2021-0136 coefficients with exact printed/PDF pages,
  model scope, and calibration status; model inputs are not F7 measurements.
- Before future implementation, test units, sodium/oxygen/product/energy
  conservation, oxide-free and oxide-rich limits, and zero-temperature-
  difference behavior. These are planned verification requirements, not
  simulations or tests executed during this literature review.
