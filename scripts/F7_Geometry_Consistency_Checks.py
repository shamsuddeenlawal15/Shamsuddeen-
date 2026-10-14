#!/usr/bin/env python3
"""F7 analytical checks and evidence-summary audit; NOT a CAD kernel or solver."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PARAMETERS = ROOT / 'data/day-07/F7_Verified_Geometry_Parameters.csv'
NAMES = ROOT / 'data/day-07/F7_Regions_Interfaces_and_Surface_Names.csv'
HEADER = ['id', 'day6_id', 'parameter', 'value', 'unit', 'qualifier',
          'source', 'location', 'status', 'use']
TOPOLOGY = {'closed_shell_open_edges': 0, 'overlapping_solid_pairs': 0,
            'fluid_components': 1, 'orientation_defects': 0, 'duplicate_surfaces': 0}
MEASUREMENTS = {'pan_area': ('m2', 'V004'), 'pan_thickness': ('m', 'V005'),
                'insulation1_thickness': ('m', 'V006'),
                'insulation2_thickness': ('m', 'V007'),
                'nozzle_height': ('m', None), 'gas_volume': ('m3', None),
                'vessel_enclosed_volume': ('m3', 'V003')}


def finite(value, positive=False):
    if isinstance(value, bool):
        raise ValueError('Boolean is not a measurement')
    result = float(value)
    if not math.isfinite(result) or (positive and result <= 0):
        raise ValueError('Finite positive measurement required' if positive else 'Nonfinite value')
    return result


def load_parameters(path=PARAMETERS):
    with Path(path).open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADER:
            raise ValueError('Unexpected verified-parameter header')
        rows = list(reader)
    result = {}
    for r in rows:
        if None in r or any(not v for v in r.values()) or r['id'] in result:
            raise ValueError('Malformed, empty or duplicate parameter')
        finite(r['value'], positive=True)
        if (r['status'] != 'verified_in_2023_article_only'
                or '10.1016/j.nucengdes.2023.112285' not in r['source']
                or not r['location'].startswith('p.')):
            raise ValueError('Missing inspected-source provenance')
        result[r['id']] = r
    if set(result) != {f'V{i:03d}' for i in range(1, 18)}:
        raise ValueError('Incomplete or unexpected source IDs')
    return result


def source_value(parameters, key, unit):
    row = parameters[key]
    value = finite(row['value'], positive=True)
    if row['unit'] == unit:
        return value
    if row['unit'] == 'mm' and unit == 'm':
        return value / 1000
    raise ValueError(f'Unsupported source units for {key}')


def analytical(parameters):
    h = source_value(parameters, 'V001', 'm')
    d = source_value(parameters, 'V002', 'm')
    capacity = source_value(parameters, 'V003', 'm3')
    area = math.pi * d * d / 4
    volume = area * h
    pan = source_value(parameters, 'V004', 'm2')
    return {
        'status': 'analytical_consistency_only_not_actual_CAD',
        'source_ids': ['V001', 'V002', 'V003', 'V004', 'V006', 'V007', 'V008', 'V009'],
        'ideal_cylinder_volume_m3': volume,
        'ideal_cylinder_cross_section_m2': area,
        'ideal_cylinder_lateral_area_m2': math.pi * d * h,
        'cylinder_minus_capacity_label_m3': volume - capacity,
        'relative_capacity_difference': (volume - capacity) / capacity,
        'pan_minus_cylinder_cross_section_m2': pan - area,
        'insulation_total_thickness_m': source_value(parameters, 'V006', 'm')
        + source_value(parameters, 'V007', 'm'),
        'nozzle_height_difference_m': source_value(parameters, 'V009', 'm')
        - source_value(parameters, 'V008', 'm'),
        'limitations': 'Ideal cylinder arithmetic is not measured volume, a head profile, '
        'or CAD approval. Source uncertainty is not quantified. No pan planform inferred.'}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def audit(data, parameters, base):
    if (not isinstance(data, dict) or type(data.get('schema_version')) is not int
            or data.get('schema_version') != 1):
        raise ValueError('Evidence object schema_version=1 required')
    if data.get('case') not in ('F7-1', 'F7-2'):
        raise ValueError('Explicit F7 case required')
    if data.get('evidence_kind') not in ('local_cad_report', 'synthetic_test'):
        raise ValueError('Explicit evidence origin required')
    for field in ('solver_build', 'operator', 'export_date', 'measurement_scope'):
        if (not isinstance(data.get(field), str) or not data[field].strip()
                or data[field].lower() in ('unknown', 'pending', 'todo')):
            raise ValueError(f'{field} evidence required')
    if data.get('coordinate_frame') != 'F7_PROJECT_CARTESIAN':
        raise ValueError('Measurements must use the documented project frame')
    artifacts = data.get('artifacts')
    if not isinstance(artifacts, list) or not artifacts:
        raise ValueError('Referenced local CAD/diagnostic artifacts required')
    for item in artifacts:
        digest = hashlib.sha256()
        with (Path(base) / item['path']).open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                digest.update(block)
        if digest.hexdigest() != item['sha256']:
            raise ValueError('Artifact checksum mismatch')
    result = {'status': 'reported_evidence_audit_not_CAD_approval',
              'case': data['case'], 'evidence_kind': data['evidence_kind'],
              'comparisons': {}, 'pending': [], 'topology': {}}

    def compare(name, value, unit, source_id):
        value = finite(value, positive=True)
        entry = {'reported_value': value, 'unit': unit, 'source_id': source_id}
        if source_id:
            source = source_value(parameters, source_id, unit)
            entry.update(source_value=source, difference=value-source,
                         relative_difference=(value-source)/source,
                         qualifier=parameters[source_id]['qualifier'],
                         location=parameters[source_id]['location'])
        entry['acceptance'] = 'not_determined'
        if name == 'vessel_enclosed_volume':
            entry['caution'] = 'Capacity label comparison only; volume definition unresolved'
        result['comparisons'][name] = entry

    bounds = data.get('bounds_m')
    if bounds is None:
        result['pending'].append('vessel bounding dimensions')
    else:
        if (data['measurement_scope'] != 'vessel_envelope_excluding_external_pipes'
                or not isinstance(bounds, dict) or set(bounds) != {'x', 'y', 'z'}):
            raise ValueError('Bounding scope/axes do not match comparison')
        for axis, source_id in [('x', 'V002'), ('y', 'V002'), ('z', 'V001')]:
            values = bounds[axis]
            if not isinstance(values, list) or len(values) != 2:
                raise ValueError('Each bounding axis needs min/max')
            low, high = map(finite, values)
            compare('vessel_span_' + axis, high-low, 'm', source_id)
    measurements = data.get('measurements', {})
    if not isinstance(measurements, dict) or set(measurements) - set(MEASUREMENTS):
        raise ValueError('Unknown measurement names')
    for key, (unit, source_id) in MEASUREMENTS.items():
        if key not in measurements:
            result['pending'].append(key)
            continue
        row = measurements[key]
        if row['unit'] != unit:
            raise ValueError(f'{key}: canonical {unit} required; no implicit conversion')
        if key == 'nozzle_height':
            source_id = 'V008' if data['case'] == 'F7-1' else 'V009'
        compare(key, row['value'], unit, source_id)
    topology = data.get('topology', {})
    if not isinstance(topology, dict) or set(topology) - set(TOPOLOGY):
        raise ValueError('Unknown topology diagnostic')
    for key, reference in TOPOLOGY.items():
        if key not in topology:
            result['pending'].append(key)
            continue
        count = topology[key]
        if type(count) is not int or count < 0:
            raise ValueError('Topology diagnostics require nonnegative integer counts')
        result['topology'][key] = {'reported_count': count,
                                  'review_reference': reference,
                                  'needs_review': count != reference}
    with NAMES.open(newline='', encoding='utf-8') as f:
        registry = list(csv.DictReader(f))
    allowed = {r['name'] for r in registry}
    allowed.update(n for r in registry for n in r['paired_surface_names'].split(';') if n)
    names = data.get('names')
    if names is None:
        result['pending'].append('names')
    else:
        if not isinstance(names, list) or any(not isinstance(n, str) or not n for n in names):
            raise ValueError('Names must be nonempty strings')
        required = {'F7_Gas', 'F7_Vessel', 'F7_Pan', 'F7_Insulation1', 'F7_Insulation2'}
        result['naming'] = {'duplicates': sorted({n for n in names if names.count(n) > 1}),
                            'unregistered': sorted(set(names)-allowed),
                            'missing_core': sorted(required-set(names))}
    result['limitations'] = ('Only checks supplied diagnostic summaries and artifact hashes; '
                             'does not parse CAD, detect geometric intersections, establish '
                             'report truth or decide source uncertainty/engineering tolerances. '
                             'Connectivity reference of one needs review for lower pockets.')
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('analytic', 'audit'))
    parser.add_argument('--evidence', type=Path)
    args = parser.parse_args(argv)
    try:
        parameters = load_parameters()
        if args.mode == 'analytic':
            if args.evidence:
                raise ValueError('Evidence is only used by audit mode')
            result = analytical(parameters)
        else:
            if not args.evidence:
                raise ValueError('audit requires --evidence; no CAD result inferred')
            with args.evidence.open(encoding='utf-8') as f:
                data = json.load(f, object_pairs_hook=unique_object)
            result = audit(data, parameters, args.evidence.parent)
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0
    except (ValueError, TypeError, KeyError, OSError, OverflowError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
