# H1 mesh and resource configuration

Scope: preparation for a synthetic cube, not the F7 apparatus. No mesh exists.
All STAR-CCM+ mesher controls and diagnostics below are **[BUILD CHECK]** items
requiring the installed release's manual before execution.

## Proposed mesh family

Use one closed 0.1 m cube aligned with x/y/z. Prefer an orthogonal, uniform,
rectangular-hexahedral grid with matching subdivisions in all axes, if the
installed build provides a documented route. No prism layers are required
for the initial analytic conduction grid; this is not a wall-resolved F7 mesh.

| Grid | Requested subdivisions | Nominal cells | Nominal spacing | Budget |
|---|---|---|---|---|
| G1 | 32 x 32 x 32 | 32,768 | 0.1/32 m | Initial 20,000–50,000 |
| G2 | 48 x 48 x 48 | 110,592 | 0.1/48 m | Provisional 50,000–150,000 |
| G3 | 72 x 72 x 72 | 373,248 | 0.1/72 m | Provisional 150,000–400,000 |

These are requests, not measured counts. Record the actual grid, h and quality
after generation. A generic base-size control may not create these subdivisions.
If only trimmed/polyhedral/skewed cells are available, do not label them
orthogonal rectangular merely to satisfy the Python contract. First verify a
rectangular grid/export route or review a new analytical integration adapter.
No unverified macro is supplied to force a particular mesh.

**[BUILD CHECK]** Verify positive cell volumes, total volume 0.001 m³, six
boundary areas 0.01 m² each, normals, closure, connectivity, skewness,
nonorthogonality and size transitions using the build's documented diagnostics.
Adopt quality thresholds from that documentation with provenance rather than
an invented universal cutoff. Record boundary edge treatment for the moving
lid; velocity is discontinuous where it meets stationary walls.

## Initialization and refinement

H1-A/B/D initialize T=300 K, u=0. H1-C uses the cosine profile. Confirm the
solver's stored-field representation and initialization method. Exact cell
averages are preferred for a finite-volume error comparison. If the GUI only
initializes the field at centers, record that method and its initial error;
do not claim it was cell-average initialization. Match the declared reference
sampling and investigate representation error before asserting convergence.

Start thermal trials at dt=0.1 s, end time 10 s; compare 0.1/0.05/0.025 s on
one fixed mesh for time refinement. Use a separately controlled sufficiently
small time step for mesh refinement. Three increasing cell counts alone do
not establish independence. Inner-solve error must be controlled separately.
Record actual spatial/temporal orders and any limiter settings; do not infer
them from a tutorial for another release.

For H1-D inspect the actual Courant number and transient accuracy; its
advective time step may need to be smaller than the thermal trial. For thermal
cases record alpha*dt/h². Implicit stability is not proof of accuracy.

## Four/eight-process resource trials on the PC

Hardware is user-confirmed i9-14900HX, 24 cores/32 threads, 32 GB RAM. Working
license is confirmed; parallel entitlements, OS and exact build are not.

1. Confirm the allowed process count and log the actual four ranks at startup.
   Only compare eight if entitlement permits. Use the same mesh, physics,
   time step, inner convergence and clean starting state in both trials.
2. Record background load, power mode and cooling. Separate mesh/load time,
   solve time and export time. Time the same physical interval and number of
   steps, excluding a consistently defined warmup if used. Repeat trials to
   distinguish variability from scaling.
3. Record peak process and whole-system memory during mesh generation, load
   and solve. State whether the metric is working set, private memory or
   proportional memory. Sum-of-RSS may double-count shared pages.
4. Retain the Day 3 provisional 20 GB solver planning ceiling and at least
   4 GB available-memory reserve, using the smaller feasible allocation after
   measuring current availability. Record GB versus GiB. These are project
   safeguards, not vendor specifications or predicted consumption.
5. Pause growth for persistent paging, exhausted reserve, thermal throttling
   that invalidates a comparison, insufficient disk space or poor solver
   convergence. Do not relax correctness criteria to fit the machine.
6. Compare t4/t8 and relative efficiency (t4/t8)/2 only for equivalent timed
   work. Neither value exists until actual runs are recorded. Check solution
   consistency before interpreting speed. The convergence script intentionally
   rejects mixing process counts within a mesh/time series.

Record raw resource observations in the run log. This task creates no
performance records. No GPU path or Java API is assumed compatible.
