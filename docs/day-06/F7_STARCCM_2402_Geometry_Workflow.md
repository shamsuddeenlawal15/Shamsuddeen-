# F7 geometry workflow — STAR-CCM+ 2402 / Windows 11

User-confirmed target: Siemens Simcenter STAR-CCM+ 2402 (2024.1), Windows 11,
Intel Core i9-14900HX, 32 GB RAM, working license. This supersedes the current
unknown release/OS in the historical Day 5 record without changing that record.
Exact patch/build, licensed process count, module checkout, available RAM/disk
and local screenshots remain unverified.

## Capability gate

No release-specific manual/API was accessible in this task; the Siemens
documentation endpoint was blocked by the proxy. Consequently no particular
CAD, mesher, interface or physics control is asserted as verified for 2402.
The table is a requirements/verification queue, not executable GUI instructions.
No Java macro is supplied. Source incompleteness independently blocks CAD.

On the local PC, identify the full version string from the installed version
display/startup log, OS build through winver, RAM via Task Manager and free
space on project/temp drives. Open installed documentation matching that build.
For each row record actual GUI path, manual topic/page and screenshot; confirm
license checkout rather than assuming a visible model is usable. Do not
publish license keys or server credentials.

| Intended operation | Verification needed before use | Actual 2402 topic/path/evidence |
|---|---|---|
| Parametric CAD / neutral CAD import | Supported geometry route and parameter units | |
| Named datums and surface groups | Stable naming on regeneration | |
| Fluid extraction / boolean operations | Watertight region extraction and retained solids | |
| Region and boundary creation | Part-to-region assignment semantics | |
| Conjugate interfaces | Supported contact/conduction coupling and normals | |
| Solid material properties | Units and temperature-dependent property assignment | |
| Volume meshing / near-wall layers | Available meshers and quality diagnostics | |
| Gas energy / species / buoyancy | Dependency and license checks | |
| Surface heat/mass/species coupling | Conservative supported implementation | |
| Transient reports / exports / save | Actual definitions and data schema | |

## Review-gated local workflow

1. **Preserve and organize.** Keep H1 under models/starccm/H1/ and F7 design
   evidence under models/starccm/F7/ when these are later created. Store local
   run/model binaries outside tracked sources (runs/ is ignored). Label every
   F7 variant source_reconstruction or provisional_P0. Use SI dimensions.
2. **Resolve geometry.** Complete Day 7 source and assumption review. Use named
   parameters from the Day 6 register and F7-1/2 specifications. Do not convert
   the numerical Fig.2 structures into apparatus heads. No CAD operation is
   allowed to fill an unset source parameter automatically.
3. **Create approved CAD only on Day 8.** After capability verification, use
   the verified local creation/import route to construct separately named vessel
   barrel, heads, pan, each insulation layer and documented feed/vent parts.
   Preserve source reference and datum association for each feature.
4. **Inspect before regions/mesh.** Measure source-linked dimensions and record
   deviations. Check head/port joins, gaps, overlaps, self-intersections, normals
   and material volumes. Audit gas volume after subtracting occupied solids
   and modeled sodium. Account explicitly for connected/unconnected under-pan
   space; do not delete it merely to match the 3.0 m³ label.
5. **Define regions after approval (Day 9).** Use
   [F7_Regions_and_Boundaries.csv](../../data/day-06/F7_Regions_and_Boundaries.csv).
   These are proposed semantic names, not vendor menu labels. Audit every
   boundary and interface pair for one intended role.
6. **Mesh after geometry approval (Day 10).** Choose a locally verified method
   appropriate for resolved heads/ports/thin solids. Refine near feed/vent,
   pool perimeter and thermal gradients. Resolve through-thickness conduction
   or review a supported thin-wall alternative; no arbitrary universal cell
   count/layer count is mandated. Do not transplant H1's 32³ grid or its resource
   budgets as F7 accuracy criteria. Log mesh quality and hardware feasibility.
7. **Physics requirements, not model activation.** Future reproduction needs gas
   flow/energy and oxygen transport with supported heat/mass exchange, pan/
   insulation/vessel heat paths, properties and boundary/initial conditions.
   Select turbulence, radiation, pool transport, oxidation and aerosol closures
   only after relevance/source/license review. Do not assign H1 rho, viscosity,
   heat capacity or conductivity to F7. Conjugate thermal coupling at pool–pan,
   pan–insulation, layer–layer and gas–solid interfaces must be resolved or
   represented by explicitly justified reduced boundary laws. Thermal contact
   resistance and external heat transfer remain unknown.
8. **Plan reports.** Geometry: volumes, areas, thicknesses, height offsets and
   interface pairing. Future physics: total mass/species/energy, inlet/outlet
   budgets, pool inventory/area, combustion rate, temperature at justified
   sensor positions, and vessel/exhaust aerosol concentration if a validated
   aerosol model exists. Retain definitions/units and region selections.
   A radius-only measurement is not an established Cartesian sensor point.
9. **Preserve and export.** Save CAD/source parameters, initial .sim, neutral
   geometry export if locally supported, semantic surface list, region/interface
   assignments, screenshots and version metadata. Hash artifacts and record
   units, coordinate frame, source IDs, assumptions, operator and date.
   Reopen locally and compare dimensions/names before meshing. Public Git
   contains specifications/manifests, not proprietary software or license data.

No workflow step above is a claim of a locally verified capability or completed
operation. Four-process entitlement/resource checks and H1 verification remain
required before physical runs. There is no licensed cloud solver evidence.
