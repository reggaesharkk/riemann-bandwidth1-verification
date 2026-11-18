# Reproducibility

Use Python 3.13 in a disposable checkout. Install the pinned third-party dependencies with `python -m pip install -r requirements.txt`. The following commands exercise five included finite verifiers; they are not the complete historical audit suite.

    python src/wp84_functional_band_delta80_gate.py
    python src/wp84_bounded_christoffel_consumer.py
    python src/wp84_r400_filtered_connected_kernel.py --certificate
    python src/wp84_fourier_reprojection_bridge.py --exact-only
    python src/wp84_direct_prime_field_scalar_gaussian_replay.py

The delta80 and bounded-consumer checkers require SymPy 1.14.0. The R400 interval certificate uses mpmath 1.3.0 and NumPy 2.5.3. The Gaussian and chunked C5 replays use Python standard-library exact arithmetic. Honor each dependency's license; packages are not vendored.

Some scripts write files. Run only in a disposable copy. Compare outputs with the included source certificate and hashes. A verifier PASS establishes only the exact checks it implements, not the open arithmetic theorem. This selected command set does not claim to rerun every historical experiment or reproduce all research inputs.

The exact C5 polytope verifier is split into 16 deterministic shards. Locally, run one shard with `python src/checkpointed_c5_certificate.py --shard-index 0 --shards 16 --output shard-0/result.json`; run indices 0 through 15, then aggregate with `python src/checkpointed_c5_certificate.py --aggregate-dir shards`. Every shard has a disjoint residue class of the 148,995 canonical hyperplane intersections. GitHub Actions runs the shards independently and uploads generated public mathematical certificate JSON files. All CI jobs have explicit timeouts below six hours, read-only repository permissions, and require no credentials.

Some historical source-matched replays need inputs not included in this release candidate. They are not silently represented as reproducible by the selected commands above.
