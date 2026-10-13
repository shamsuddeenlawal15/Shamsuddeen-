# H1-A model setup checklist

All boxes are pending local evidence. Each operation is BUILD CHECK; use the
installation evidence mapping before acting. Values below are approved synthetic
inputs, not experimental sodium/air properties or measured results.

- [ ] Record build, OS, operator, date, run ID and actual licensed rank count.
- [ ] Create cube [0,0.1] m on each axis, one sealed fluid region.
- [ ] Name six exterior surfaces X_MIN, X_MAX, Y_MIN, Y_MAX, Z_MIN, Z_MAX;
      confirm outward normals (-x,+x,-y,+y,-z,+z) and no internal interface.
- [ ] Assign all six as impermeable, stationary no-slip, adiabatic walls.
      No inlet, outlet, moving wall or imposed-temperature wall.
- [ ] Select 3D transient laminar constant-density flow with energy enabled.
      Do not disable energy: that would not test temperature preservation.
- [ ] Set rho=1 kg/m³, dynamic viscosity=0.001 Pa s, thermal conductivity
      k=0.1 W/(m K), heat capacity c=1000 J/(kg K), following the Day 4 input table.
      Implement rho*c*DT/Dt=k*laplacian(T), not an ideal-gas compressible model.
- [ ] Disable gravity/buoyancy, turbulence, radiation, reactions, species,
      sodium, aerosols and all volumetric heat/mass sources.
- [ ] Set pressure reference 0 Pa gauge using the documented closed-domain
      pressure constraint, not an artificial pressure outlet.
- [ ] Initialize every cell T=300 K, velocity=(0,0,0) m/s and consistent
      spatially uniform gauge pressure. Record the actual initialization method.
- [ ] Verify a uniform orthogonal 32×32×32 mesh and complete the mesh register.
- [ ] Record actual spatial/temporal schemes, precision, solver tolerances,
      inner iteration cap and stopping policy. Defaults must be documented.
- [ ] Plan dt=0.1 s, end time=10 s, 100 steps, monitors including t=0.
      These are approved trial controls, not proven accuracy settings.
- [ ] Configure independent whole-region mass and relative thermal-energy
      integrals, signed/absolute-local wall flux, heat/source power, global
      velocity/divergence maxima and full residual histories.
- [ ] Retain temperature extrema and all-cell initial/final temperatures;
      retain velocity/pressure diagnostics for spatial inspection.
- [ ] Check units and selected region/boundary scope in every report.
- [ ] Save configuration and initial-state evidence before execution.

Expected exact solution: T=300 K, u=0, mass=rho*V=0.001 kg and no wall
mass/heat transfer. Relative energy is integral rho*c*(T-300)dV=0 J.
These are mathematical references only. Boundary conditions must be verified
from the saved model; reports must not be filled with these reference values.

Source: approved [Day 4 input table](../../data/day-04/H1_Benchmark_Input_Parameters.csv),
[boundary table](../../data/day-04/H1_Boundary_Conditions.csv) and
[mesh protocol](../day-04/H1_Mesh_Configuration.md).
