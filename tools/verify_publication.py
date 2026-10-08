#!/usr/bin/env python3
"""Check the publication manifest and SHA256SUMS without network access."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    manifest = json.loads((ROOT / "PUBLICATION_MANIFEST.json").read_text(encoding="utf-8"))
    listed = {entry["path"]: entry["sha256"] for entry in manifest["files"]}
    sums: dict[str, str] = {}
    for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, relpath = line.split("  ", 1)
        if relpath in sums:
            raise SystemExit(f"duplicate checksum entry: {relpath}")
        sums[relpath] = digest
    if set(listed) | {"PUBLICATION_MANIFEST.json"} != set(sums):
        raise SystemExit("manifest and SHA256SUMS paths differ (manifest self-hash belongs only in SHA256SUMS)")
    for relpath, expected in listed.items():
        path = ROOT / relpath
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"missing or non-regular publication file: {relpath}")
        actual = sha256(path)
        if actual != expected or actual != sums[relpath]:
            raise SystemExit(f"SHA-256 mismatch: {relpath}")
    manifest_hash = sha256(ROOT / "PUBLICATION_MANIFEST.json")
    if manifest_hash != sums["PUBLICATION_MANIFEST.json"]:
        raise SystemExit("SHA-256 mismatch: PUBLICATION_MANIFEST.json")
    print(f"PASS: {len(listed)} listed files plus manifest self-hash match SHA256SUMS")


if __name__ == "__main__":
    main()
