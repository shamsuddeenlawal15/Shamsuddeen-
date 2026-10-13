# Missing geometry and primary-source recovery

Status: blocked for definitive F7 CAD. Missing means not established in the
inspected 2023 article, not proof the information does not exist elsewhere.

| Missing item | Why it matters | Required evidence / disposition |
|---|---|---|
| Internal vs external height/diameter; barrel length | Gas volume and wall solids | Dimensioned apparatus drawing |
| Top/bottom head shapes and junctions | Envelope and thermal area | Head profiles/radii; no hemisphere assumption |
| Vessel actual wall/head thickness and grade | Heat capacity/conduction | Experimental specification; Fig.2 8 mm remains numerical |
| Pan planform, rim, centroid, clearances | Pool extent and gas topology | Pan drawing; 1 m² alone does not imply square/circle |
| Supports and lower volume communication | Heat leakage and gas connectivity | Assembly sections and material/contact data |
| Nozzle bore/OD/orientation/x-y; pipe path | Falling column and displacement | Feed-system drawing for each case |
| Sodium inlet temperature/state/time history | Enthalpy and oxidation | Experimental operating record |
| Vent/exhaust areas/positions/path/pressure losses | Flow boundary conditions | Vent drawing and flow reference state |
| Insulation materials/extents/properties/contact | Pan heat loss | Layer specification and thermal boundary data |
| Initial gas/pan/wall temperature and pressure/composition | Transients and reaction | Case-specific initial-condition records |
| Sensor depths/azimuths/response; aerosol locations | Comparable validation outputs | Instrument map/calibration and raw data |
| Pool shape/center/thickness histories | Spreading model validation | Images/measurement definitions and uncertainties |

## Sources and fresh access checks, 2026-10-13 UTC

All five read-only curl HEAD requests with redirects failed at proxy CONNECT
with HTTP 403, curl exit 56, before document content was returned. No PDF or
vendor manual was recovered. This is cloud access failure, not origin-server
unavailability or an authentication diagnosis.

| Source / evidence basis | Attempted destination | Recovery status |
|---|---|---|
| Futagami et al. 1998, PNC TN9410 98-074; cited L2023 p.4 | https://jopss.jaea.go.jp/search/servlet/search?kw=PNC%20TN9410%2098-074 | Original unread; no new page evidence |
| Louie and Aoyagi 2021, SAND2021-0136; L2023 p.5; DOI 10.2172/1761299 | https://www.osti.gov/servlets/purl/1761299 | Original unread |
| SAND2021-15469; user-supplied DOI 10.2172/1834703 | https://www.osti.gov/servlets/purl/1834703 | Identity/content not independently verified |
| SAND2022-14235; user-supplied DOI 10.2172/1892376 | https://www.osti.gov/servlets/purl/1892376 | Identity/content not independently verified |
| Siemens release documentation | https://docs.sw.siemens.com/ | No 2402 capability/API verification obtained |

Use the local browser/library access to retrieve official PDFs, or supply copies
for review. The 2023 paper says data available on request (p.4); an author/JAEA
request for apparatus drawings, input decks and instrument records is a possible
next action, not a message sent by this task. No secrets are requested.

On receipt record title/authors/report ID/DOI, checksum and both printed/PDF
page numbers; inspect provenance and distinguish experimental facts from code
inputs. Reconcile contradictions additively. Do not import a figure or value
until its identity, page and applicability to F7-1/F7-2 are established.

## Provisional alternatives — separate and unapproved

P0 idealized envelope/reduced-pool concept is defined separately in
[F7_Original_vs_Numerical_Geometry.md](F7_Original_vs_Numerical_Geometry.md).
Do not execute it as a substitute for source recovery. Decisions on flat
closures, pan shape, equivalent openings, thermal contact or prescribed pool
area each need a labelled assumption, sensitivity plan and approval. No
numerical placeholder diameter, vent size or head shape enters the source table.

Keep the [Day 2 equation audit](../day-02/Equation_Transcription_Audit.md)
authoritative: Eq.1 beta/nu²; Eq.2 undotted m³ with mass definition/C1 unresolved;
Eq.3 C2 and oxide fraction basis unresolved. No guessed reaction coefficient
or viscosity correction is adopted.
