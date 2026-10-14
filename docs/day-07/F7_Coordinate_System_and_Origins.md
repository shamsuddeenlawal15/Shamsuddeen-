# F7 project coordinate and origin register

Status: APPROVED as a documented mathematical project convention for reference
datums; not an experimentally reported frame and not full CAD approval.
Implementation still requires local 2402 control verification.

Use right-handed F7_PROJECT_CARTESIAN: Z up, X/Y horizontal. Origin O=(0,0,0)
is the intersection of the chosen vessel reference axis with the catch-pan
upper reference plane. X azimuth is a project orientation, not “toward the
inlet” until its real azimuth is recovered. Record any later apparatus-to-project
rotation and translation; never rotate only some components.

| Component / reference | Position rule | Evidence class / unresolved fields |
|---|---|---|
| Vessel reference axis | x=y=0 | Convention; actual axis identification from drawing pending |
| Pan upper reference datum | z=0 | Convention; not a complete pan outline or tilted-surface measurement |
| Pan centroid / rim | x/y unset; physical shape unset | G023; do not force centroid to origin |
| Pan lower surface | Thickness constraint 0.006 m | Uniform flat plate interpretation needs review; not a bottom-head datum |
| Vessel top / bottom | Absolute z unset | About 2.2 m overall separation is not a pan-to-top height |
| F7-1 nozzle exit reference | z_ref-z_pan_ref=0.1 m | V008; x/y and exit normal unset |
| F7-2 nozzle exit reference | z_ref-z_pan_ref=1.5 m | V009; x/y and exit normal unset |
| Sodium pipe | Pose/path unset | No automatic translation of roof penetration with nozzle |
| Insulation 1 / 2 | Thickness 0.05 m each; positions unset | Identity, extent, gaps and contacts unresolved |
| Supports / lower cavity | Unset | Assembly and connectivity unknown |
| Air inlet / exhaust | x/y/z and normals unset | Lower/upper schematic placement is not xyz |
| Pool center / surface | x/y/z and shape unset | Do not force pool center onto vessel/nozzle axis |
| Temperature sensors | r=0.10, 0.20, 0.24 m from pool center | L2023 p.4 Fig.4; theta/depth and pool-center transform unknown |
| Aerosol sample sites | Vessel/exhaust labels only | L2023 p.4 Fig.5; no point coordinates |

A horizontal reference plane at z=h_nozzle is merely a height locus, not
proof that the physical exit face is horizontal. This clarifies Day 6 wording.

Future sensor mapping, once documented, may use x=x_pool+r*cos(theta),
y=y_pool+r*sin(theta), z=z_sensor. Do not fill theta=0 or z=0 as a convenience.
A radius-only locus may be plotted as a reference ring but not as a measured
sensor location or physical CAD solid.

The first geometry operation proposed for Day 8 is creation/naming of the
nonphysical pan reference datum at z=0 with this axis triad. It needs no nozzle
bore, vessel head or pan planform. It must create no occupied volume. Save the
datum-only checkpoint and stop if required body dimensions remain unresolved.
