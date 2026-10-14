# Boundary and initial-condition framework — no assignments

Source L2023 is fully cited in the physics framework report. “Published”
means reported in that article, not recovered original F7 records. Unknown
values remain unset; model proposals are not experimental facts.

| Quantity / boundary | Value or proposed treatment | Classification / exact source | Current limitation |
|---|---|---|---|
| Air ventilation | Approximately 3.0 m³/min, steady | Published; p.2 Section 2, Day 7 V014 | Reference T/p/composition and port area absent |
| Same volume flow in SI | Approximately 0.05 m³/s | Derived unit conversion: 3.0/60; retains reference-state uncertainty | Not an inlet velocity or mass flow |
| Sodium feed, Stage 2 only | Average 3.3 g/s for 1500 s | Published; p.2 Section 2, V012/V013 | Inlet temperature, bore and detailed time history missing |
| Same mean mass rate in SI | 0.0033 kg/s, average | Derived: 3.3/1000 | Not a confirmed constant instantaneous flow history |
| Nozzle position F7-1 / F7-2 | 0.1 / 1.5 m above pan | Published geometry; p.2 Section 2/Fig.1 | Not a flow BC; x/y/bore/normal unknown |
| Air inlet thermal/composition/turbulence state | Pending | Unknown experimental inputs | No assumed 300 K, 21% O2 or turbulence intensity |
| Exhaust pressure and backflow state | Pending | Unknown experimental inputs | No invented 1 atm outlet; duct losses and reference unknown |
| Impermeable solid-wall momentum | Candidate stationary no-slip wall | Modeling assumption for later nonreactive flow | Confirm actual surfaces; not an imposed heat condition |
| Gas–solid heat transfer | Candidate conservative CHT | Model requirement; not a measured BC | Properties/contact topology incomplete |
| Direct wall–pan contact | Unassigned | Geometry/contact unknown | Do not fuse or create a thermal bridge by name |
| Pan–insulation / interlayer contact | Pending law/area/resistance | Two layers published p.2; contact law not reported | Perfect contact is not an experimental fact |
| Vessel/insulation external thermal boundary | Pending | Unknown environment/heat-loss data | No default adiabatic wall, fixed ambient or arbitrary heat-transfer coefficient |
| Initial gas temperature / absolute pressure | Pending | Not specified in inspected paper | H1 initial values do not apply |
| Initial gas velocity | Pending | Unknown initial ventilation state | Zero velocity is not an F7 measurement |
| Initial vessel/pan/layer temperature fields | Pending | Unknown experimental initial conditions | No uniform numerical field assigned |
| Initial pool/inventory / sodium temperature | Pending | Unknown; reaction Stage 2 reserved | Final measured area is not initial geometry |
| Pressure datum | Later numerical reference, distinct from absolute pressure | Numerical convention only | Must remain compatible with open-boundary/EOS pressure definitions |

If converting volume flow to mass flow, use the density at the source flow's
stated reference conditions: m_dot=rho_ref*Q_ref. If converting to velocity,
also require actual port area, profile and thermodynamic conversion to local
volume flow. The published flow alone is insufficient.

Stage 1 has no sodium reaction source. A future synthetic thermal test may use
a deliberately prescribed heater/thermal boundary, but its power, location and
initial state require a labelled benchmark specification and review; no F7
combustion measurement is used as a hidden heat-source input.

Initial and boundary conditions must be consistent: an established ventilated
initial field versus startup-from-rest represents a modeling choice with
transient implications. Recover source timing before choosing it.
Inlet_Region/Outlet_Region are optional resolved ducts, not prerequisites for
assigning inlet/outlet boundary surfaces after approval.

No local boundary object, initial field, material or interface has been assigned.
