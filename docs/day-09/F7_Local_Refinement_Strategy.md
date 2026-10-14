# Local refinement requirements — conceptual only

All candidate locations below are unapproved/unresolved geometry. Therefore
these are future design hypotheses, NOT local mesh-control instructions.
No numerical control is supplied for a missing bore, patch or head.
Priorities describe future review effort, not authorization.

Let h be a later reviewed bulk length, ell_grad a gradient length from
physical scale analysis or a future pilot, d a verified opening/bore diameter,
t a verified solid thickness and n a justified resolution count. Values of
ell_grad, d and n remain unset. The mesh-level table's equivalent h is a
budget arithmetic scale, not the h to enter in STAR-CCM+.

| Candidate location | Purpose | Proposed scale hypothesis after approval | Priority / present gate |
|---|---|---|---|
| Reduced sodium pool surface | Resolve spatial heat/mass flux and perimeter | Tangential h_pool <= h/2, also limited by ell_grad/n | High; footprint/closure not approved |
| Resolved sodium–air interface, only if later justified | Resolve interface geometry and transport | h_interface <= min(h/2, ell_interface/n) | High if included; no liquid model/film depth chosen |
| Nozzle/column/impingement | Resolve feed geometry and sharp gradients | h_feed <= min(h/2, d_nozzle/n_d) | High if included; bore/path unknown |
| Wall heat-transfer surfaces | Represent wall-normal gradients | delta_n determined from resolved gradient and future wall treatment; no numerical value | High; flow regime/properties unavailable |
| Pan/insulation/shell thickness | Resolve conjugate conduction and contacts | delta_n=t/n_t; lateral scale independently determined | High; n_t requires convergence evidence; actual shell thickness unknown |
| Air inlet/exhaust | Resolve opening shape, flow redistribution and shear | h_port <= min(h/2, d_port/n_d) for appropriate verified characteristic size | High; patches currently empty slots |
| Expected thermal plume/strong gradients | Avoid under-resolving concentrated gradients | h_thermal <= min(h/2, ell_grad/n) | Conditional; location/extent requires approved physical scales |

The factor 1/2 is an illustrative engineering refinement hypothesis, not a
Siemens recommendation, experimental value or selected control. Minimum sizes,
transition rates, contact matching, prism growth and total thickness remain
review items. Do not manufacture absolute local millimetre sizes from unknown
geometry. Record rationale and resulting cell distribution once controls exist.

Near-wall y+ is a future diagnostic tied to density, viscosity, shear and wall
treatment; no target or first-layer height is selected now. Mesh requirements
may inform later physics decisions without enabling a physics model today.

Keep the same refinement-region definitions and proportional changes across
future sensitivity meshes. Do not change a prescribed footprint to obtain
desired cell counts. A moving pool perimeter requires an approved strategy
covering possible motion, not a patch frozen to the measured final area.
