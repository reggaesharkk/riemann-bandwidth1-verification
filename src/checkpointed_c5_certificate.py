#!/usr/bin/env python3
"""Deterministically shard and aggregate the exact 5-cycle certificate.

Each shard visits a disjoint residue class of the canonical ordered
148,995 four-hyperplane intersections. Shard JSON files contain rational
vertices and counters only. Aggregation checks complete coverage, exact
vertex deduplication, each claimed inequality, and the recorded extrema.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wp84_c5_pointwise_supercritical_sign import (  # noqa: E402
    F,
    OUTER,
    arrangement,
    c5,
    dot,
    half_l1,
    solve4,
)

TOTAL_INTERSECTIONS = 148_995
SHARD_COUNT = 16
EXPECTED_VERTICES = 151


def encode_vertex(vertex: tuple[Fraction, ...]) -> list[str]:
    return [str(F(value)) for value in vertex]


def decode_vertex(data: list[str]) -> tuple[Fraction, ...]:
    if len(data) != 4:
        raise ValueError("vertex must have four coordinates")
    return tuple(F(value) for value in data)


def relevant_vertex(vertex: tuple[Fraction, ...]) -> bool:
    values = [dot(a, vertex) for a in OUTER]
    return max(values) - min(values) <= 1


def verify_vertices(vertices: set[tuple[Fraction, ...]]) -> tuple[Fraction, Fraction]:
    minimum: Fraction | None = None
    maximum: Fraction | None = None
    for vertex in vertices:
        if not relevant_vertex(vertex):
            raise ValueError(f"reported point lies outside the closed support: {vertex}")
        value = c5(vertex)
        s = half_l1(vertex)
        if value < 0 or value > max(F(0), s - 1):
            raise ValueError(f"pointwise inequality fails at {vertex}: C5={value}, s={s}")
        minimum = value if minimum is None else min(minimum, value)
        maximum = value if maximum is None else max(maximum, value)
    if minimum is None or maximum is None:
        raise ValueError("no support vertices were aggregated")
    return minimum, maximum


def shard(index: int, shards: int, destination: Path) -> None:
    if shards < 1 or not 0 <= index < shards:
        raise ValueError("shard index must lie in [0, shards)")
    hyperplanes = arrangement()
    vertices: set[tuple[Fraction, ...]] = set()
    tested = 0
    rank_deficient = 0
    for global_index, rows in enumerate(combinations(hyperplanes, 4)):
        if global_index % shards != index:
            continue
        tested += 1
        point = solve4(rows)
        if point is None:
            rank_deficient += 1
        elif relevant_vertex(point):
            vertices.add(point)
    encoded = sorted(encode_vertex(vertex) for vertex in vertices)
    canonical = json.dumps(encoded, separators=(",", ":"), ensure_ascii=True).encode()
    payload = {
        "schema": "wp84-c5-exact-shard-v1",
        "shard_index": index,
        "shards": shards,
        "canonical_total_intersections": TOTAL_INTERSECTIONS,
        "tested_intersections": tested,
        "rank_deficient_intersections": rank_deficient,
        "support_vertices": encoded,
        "support_vertices_sha256": hashlib.sha256(canonical).hexdigest(),
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"shard {index}/{shards}: tested={tested}, vertices={len(vertices)} -> {destination}")


def aggregate(directory: Path) -> None:
    files = sorted(directory.glob("**/result.json"))
    payloads = [json.loads(path.read_text(encoding="utf-8")) for path in files]
    if len(payloads) != SHARD_COUNT:
        raise ValueError(f"expected {SHARD_COUNT} shard files, found {len(payloads)}")
    by_index: dict[int, dict] = {}
    all_vertices: set[tuple[Fraction, ...]] = set()
    tested_total = 0
    deficient_total = 0
    for payload in payloads:
        if payload.get("schema") != "wp84-c5-exact-shard-v1" or payload.get("shards") != SHARD_COUNT:
            raise ValueError("unexpected shard schema or partition size")
        index = payload["shard_index"]
        if index in by_index or not 0 <= index < SHARD_COUNT:
            raise ValueError("duplicate or invalid shard index")
        by_index[index] = payload
        vertices_data = payload["support_vertices"]
        canonical = json.dumps(vertices_data, separators=(",", ":"), ensure_ascii=True).encode()
        if hashlib.sha256(canonical).hexdigest() != payload["support_vertices_sha256"]:
            raise ValueError(f"vertex payload hash mismatch in shard {index}")
        vertices = {decode_vertex(data) for data in vertices_data}
        if len(vertices) != len(vertices_data):
            raise ValueError(f"duplicate vertices within shard {index}")
        all_vertices.update(vertices)
        tested_total += payload["tested_intersections"]
        deficient_total += payload["rank_deficient_intersections"]
    if set(by_index) != set(range(SHARD_COUNT)):
        raise ValueError("partition does not contain every shard index")
    if tested_total != TOTAL_INTERSECTIONS:
        raise ValueError(f"incomplete intersection coverage: {tested_total} != {TOTAL_INTERSECTIONS}")
    if len(all_vertices) != EXPECTED_VERTICES:
        raise ValueError(f"support vertex count mismatch: {len(all_vertices)} != {EXPECTED_VERTICES}")
    minimum, maximum = verify_vertices(all_vertices)
    if minimum != 0 or maximum != F(1, 2):
        raise ValueError(f"extremum mismatch: min={minimum}, max={maximum}")
    result = {
        "schema": "wp84-c5-exact-aggregate-v1",
        "shards": SHARD_COUNT,
        "tested_intersections": tested_total,
        "rank_deficient_intersections": deficient_total,
        "support_vertices": len(all_vertices),
        "minimum_C5": str(minimum),
        "maximum_C5": str(maximum),
        "result": "PASS_WITHIN_DECLARED_FINITE_CERTIFICATE_SCOPE",
        "warning": "This finite polytope certificate does not prove the open arithmetic or zero-proportion theorem.",
    }
    target = directory / "aggregate-result.json"
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-index", type=int)
    parser.add_argument("--shards", type=int, default=SHARD_COUNT)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--aggregate-dir", type=Path)
    args = parser.parse_args()
    if args.aggregate_dir is not None:
        aggregate(args.aggregate_dir)
    elif args.shard_index is not None and args.output is not None:
        shard(args.shard_index, args.shards, args.output)
    else:
        parser.error("choose --aggregate-dir or both --shard-index and --output")


if __name__ == "__main__":
    main()
