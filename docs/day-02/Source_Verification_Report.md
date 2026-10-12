# Day 2 source verification report

Review date: 2026-10-13 (Asia/Shanghai). Baseline: commit
`f14ebf1ce7bd1a9e3991f31df5c74628e58dfe63`.

## Outcome and limits

The supplied Louie et al. (2023) paper is readable and has been re-examined.
The original F7 report and SAND2021-0136 have **not been retrieved or studied**:
official retrieval attempts were rejected by the environment's egress proxy.
This Day 2 package records completed source auditing and engineering planning;
the requested additional-source verification remains blocked. It is not evidence
that the reports are unavailable publicly or that the user lacks permission.

## Sources and exact evidence locations

| ID | Source | Evidence actually examined | Availability and admissible use |
|---|---|---|---|
| L2023 | Louie, Aoyagi, Uchibori, Takata and Luxat, *Nuclear Engineering and Design* 407 (2023) 112285; DOI 10.1016/j.nucengdes.2023.112285 | Full supplied five-page publisher PDF; p.2 §2, Fig.1, Table 1, Eq.1; p.3 Eqs.2–3, Fig.2, §§3.2–4; p.4 Figs.3–5, data availability; pp.4–5 references | Read; source of all newly verified factual entries |
| F1998 | Futagami et al., *Sodium Pool Combustion Test Run-F7 (Interim Report)*, PNC TN9410 98-074 (1998) | Citation only, L2023 p.4 references. The printed author/title line is awkwardly typeset; the full author list is not reconstructed here | Primary report not retrieved; no report page numbers, extra input values or raw series asserted |
| S2021 | Louie and Aoyagi, *Sodium Fire Collaborative Study Progress–CNWG Fiscal Year 2020*, SAND2021-0136 (2021); DOI 10.2172/1761299 | Citation only, L2023 p.5; L2023 pp.2–3 explicitly defer control-function details to it | Not retrieved; no claimed reading, coefficients, applicability ranges or report pagination |
| Y2001 | Yamaguchi, Takata and Okano (2001), *Nuclear Technology* 136, 315–330; DOI 10.13182/NT01-A3248 | Citation only, L2023 p.5; method summarized by L2023 p.3 §3.2 | Not retrieved; inspect original before claiming a complete SPHINCS formulation |
| F1995 | Candidate: Fink and Leibowitz, *Thermodynamic and Transport Properties of Sodium Liquid and Vapor*, ANL/RE-95/2 (1995), candidate DOI 10.2172/94649 | No source content retrieved; bibliographic candidate for verification, not a citation supporting any numerical correlation here | Identity and full text require confirmation at OSTI/Argonne; no coefficients adopted |
| SIEMENS | Siemens STAR-CCM+ product, support and release-documentation sites | No vendor content retrieved | Version-specific compatibility, entitlements and hardware requirements remain unverified |

PDF SHA-256: `bf55d2d991b0d1defc2e78486a1869b67b5888c48fc4826355493d667eb34afe`.
PDF page index and printed page coincide on pp.2–5; the title page is PDF p.1.
The uploaded PDF is excluded from Git; evidence locators and its checksum are
versioned. A later reviewer needs a lawful copy matching this checksum.

## Retrieval audit

All entries below were attempted on the review date using TLS verification.
No full text or metadata page was returned. `CONNECT 403` is a proxy refusal
before the HTTPS origin request, not a publisher HTTP response or paywall.
The initial OSTI attempt and the Siemens product attempt were each retried
with escalated execution; the result did not change. No automatic approval
rejection was observed.

| Destination attempted | Purpose | Observed result |
|---|---|---|
| https://www.osti.gov/biblio/1761299 | S2021 authoritative metadata | curl exit 56; CONNECT 403, including escalated retry |
| https://www.osti.gov/servlets/purl/1761299 | S2021 full text | curl exit 56; CONNECT 403 under escalated execution |
| https://doi.org/10.2172/1761299 | S2021 DOI resolution | curl exit 56; CONNECT 403 under escalated execution |
| https://jopss.jaea.go.jp/search/servlet/search?kw=PNC%20TN9410%2098-074 | F1998 official repository search by report number | curl exit 56; CONNECT 403; search results never examined |
| https://www.osti.gov/biblio/94649 | Verify candidate sodium property source | curl exit 56; CONNECT 403 under escalated execution |
| https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/ | Official product documentation entry point | CONNECT 403, including escalated retry |
| https://support.sw.siemens.com/en-US/ | Release-specific installation/physics documentation | CONNECT 403 |
| https://blogs.sw.siemens.com/simcenter/simcenter-star-ccm-2402-released/ | Candidate 2024 release announcement | CONNECT 403; page existence/content not verified |

## Consequences for the database

The 57 Day 1 records retain their original fields and provenance. New records
are limited to the accessible paper, documented corrections and explicitly
labeled dimensional interpretations. No newly verified numerical inputs are
attributed to F1998, S2021, F1995, Y2001 or Siemens. Missing-in-article records
mean absence in L2023, not absence in the unread reports.

The equation audit corrects the transcription of Eq.1 to `beta/nu^2`, and Eq.2
to `m^3` with `m` undefined by the adjacent prose. Their Day 1 forms must not
be used for implementation. A passing CSV checker cannot establish scientific
accuracy; the second visual review was necessary to detect these errors.

## Source recovery procedure for the next approved session

1. Obtain lawful PDFs of F1998 and S2021, either as attachments or through
   working official access. If environment network settings are changed, add
   only needed destinations (`www.osti.gov`, `doi.org`, `jopss.jaea.go.jp`,
   and the applicable Siemens sites), preserving existing network rules.
   No network configuration has been changed in this task.
2. Verify cover/title/report number, revision, author list, page count and
   SHA-256. Record both PDF and printed page numbers where they differ.
3. Extract experiment tables separately from code input recommendations,
   calibration constants, schematic simplifications and property correlations.
4. Record each new fact with exact report page/table/equation, units, temperature
   validity range where applicable, and a visual verification status. Do not
   infer missing initial temperatures or oxygen fractions from generic air.
5. Resolve the Day 2 correction records and full-reproduction gate before
   detailed geometry, meshing or physical-model construction.

No authors were contacted, no report contents were reconstructed from memory,
and no STAR-CCM+ installation was inspected.
