# H1 expected analytical results

These are mathematical references derived from the approved synthetic inputs,
not numerical outputs. No solver run or performance measurement exists.

Let L=0.1 m, rho=1 kg/m³, c=1000 J/(kg K), k=0.1 W/(m K), T0=300 K.
Then V=L³=0.001 m³, M=rho V=0.001 kg and alpha=k/(rho c)=0.0001 m²/s.
The quiescent thermal equation is rho c dT/dt=k Laplacian(T)+q_vol with
adiabatic walls. Its thermal storage is defined by that equation, not by a
compressible constant-volume ideal-gas assumption.

| Case | Reference | Limitation |
|---|---|---|
| H1-A | T=300 K, velocity zero, constant mass | Uniform preservation is a smoke check; it does not measure spatial order |
| H1-B | q_vol=100 W/m³; Q=0.1 W; T=300+0.1t K; E=0.1t J relative to T0 | At t=10 s the analytical temperature is 301 K and energy increment is 1 J; these are predicted reference values only |
| H1-C | T=300+cos(pi x/L) exp[-alpha(pi/L)²t] K | Spatially nonuniform diffusion mode; volume mean stays 300 K and net relative thermal inventory stays zero |
| H1-D | Re=rho U L/mu=10 for U=0.1 m/s and mu=0.001 Pa s | No asserted analytical velocity field; evaluate mass/local continuity and process consistency, not a temperature-error norm |

For a rectangular cell with x extent [a,b], replace cos(pi x/L) by
L[sin(pi b/L)-sin(pi a/L)]/[pi(b-a)] to form its exact volume average.
The y/z dimensions cancel because the reference is independent of y/z.
The postprocessor requires orthogonal rectangular cells; x extents do not
give an exact average for skewed/polyhedral cells. Its optional cell-center
reference evaluates x=(a+b)/2 and must be labeled as point sampling.
Cell-center versus cell-average error must not be mistaken for solver error.

## Conservation and norms

Use outward positive net mass flux F_out and inward positive wall heat Q_in:

```text
R_M(t) = M(t) - M(0) + integral_0^t F_out(s) ds
E(t) = integral_V rho*c*(T - T0) dV
R_E(t) = E(t) - E(0) - integral_0^t [Q_source(s) + Q_in(s)] ds
```

There is no volumetric mass source. The intended impermeable/adiabatic walls
give F_out=Q_in=0. Nonzero exported values remain in the ledger so a leak is
not concealed. Also inspect the integral of absolute wall mass flux to detect
cancellation between leaking faces. A constant-density fixed-volume mass
identity is insufficient by itself: use the nonzero-flow case's local
continuity/divergence, and inspect spatial solution diagnostics.

For cell errors e_i and volumes V_i:

```text
L1 = sum(V_i*abs(e_i))/sum(V_i)
L2 = sqrt(sum(V_i*e_i^2)/sum(V_i))
Linf = max(abs(e_i))
```

All temperature errors are in K. The processor cross-checks the energy
reconstructed from exported fields against the independent energy monitor.
It reports the discrepancy rather than assuming monitor and field agreement.
Temporal integration of monitor rates uses trapezoids at every declared step.
Under-sampled discontinuous sources would require a different recorded
quadrature strategy; the approved source is constant.

Relative mass error uses positive initial mass. Relative final energy error
uses integrated absolute source and heat input; when that scale is zero the
result is null (undefined), not a made-up zero percentage.

## Refinement interpretation

For a pair of positive analytical errors and refinement scales, the diagnostic
slope is log(E_coarse/E_fine)/log(s_coarse/s_fine). Use s=h=(V/N)^(1/3) for
mesh studies and s=dt for time studies. The software requires at least three
H1-C runs with matching non-refined controls and returns adjacent slopes.
Zero errors produce a null slope; increasing errors can produce negative
slopes. Neither is silently converted into convergence.

Observed slopes require review for sampling error, roundoff, iteration error,
temporal/spatial contamination and the asymptotic regime. The tool does not
compute unsupported GCI or declare mesh independence. Predeclare acceptance
tolerances and scales before examining real results; none has been inferred
from missing F7 experimental uncertainty.
