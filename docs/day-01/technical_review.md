# Day 1 technical review

## Research question

Can a STAR-CCM+ model reproduce the published F7-1 and F7-2 sodium pool-fire
experimental observables with a transparent uncertainty and validation chain?

## Evidence reviewed

The original five-page article was checked using extracted text and rendered
pages. It is a concise validation paper, not a complete experiment
specification. It points to Futagami et al. (1998) for the F7 test report and
Louie and Aoyagi (2021) for detailed MELCOR control functions.

The article identifies a stainless-steel vessel (~2.2 m high, 1.3 m diameter,
3.0 m3 figure label), carbon-steel 1 m2 by 6 mm catch pan, two 50 mm insulation
layers, 3.3 g/s average sodium discharge for 1500 s, and ~3.0 m3/min steady air
ventilation. F7-1/F7-2 differ in nozzle height (0.1/1.5 m) and have final pool
areas of 0.28/0.30 m2. Atomic records are in `parameters.csv`.

## Extraction protocol

1. Verify title, authors, venue, DOI, version, and printed/PDF pagination.
2. Review the paper sequentially, including captions, footnotes, appendices,
   and cited sources explicitly adopted by the authors.
3. Enter one atomic fact per parameter row. Preserve the printed value and
   unit in `value_text`; use `value_numeric` only when lossless.
4. Record the PDF page and the printed page, if different, in `source_page`
   and explain the convention in `source_locator`.
5. Tag direct statements `published`; tag calculations `derived` and document
   their equation and inputs; tag required but absent information `missing`.
6. Conduct a second pass against every F7-1/F7-2 table, figure, and equation.

## Topics to extract

- Facility and containment geometry, coordinate system, pool/pan dimensions,
  sodium depth or inventory, freeboard, obstructions, vents, and boundaries.
- Initial gas composition, pressure, temperature, humidity, and flow state.
- Sodium initial state, composition/purity, temperature, and thermophysical
  properties or correlations.
- Ignition/heating method, test timing, boundary heat losses, and termination.
- Sensors, locations, sampling, calibration, uncertainty, and data reduction.
- Temperatures, pressure, oxygen concentration, sodium consumption, aerosol or
  combustion-product quantities, heat-release indicators, and time histories.
- MELCOR and SPHINCS versions, nodalization, correlations, coefficients,
  assumptions, sensitivity cases, and reported validation metrics.

## Validation finding

Figures 3-5 publish graphical comparisons for pool combustion rate, pool
temperature, and aerosol concentration. The paper says both codes capture the
thermal-hydraulic data well, while aerosol is underpredicted during discharge
and overpredicted afterward. It supplies no raw series, uncertainty, numeric
error metric, or acceptance threshold; data are available on request. No curve
values were digitized.

## Day 1 conclusion

The article supports a preliminary model architecture but is insufficient for
a defensible quantitative STAR-CCM+ input deck. Initial conditions, property
data, reaction constants, full sensor details, uncertainty, and raw validation
data require the cited reports or author-supplied data.
