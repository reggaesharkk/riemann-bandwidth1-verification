# Verification coverage

An earlier internal audit reported 43 named replay suites and four additional selected certificates passing. Those historical runs are not reproduced in full by this public repository, and their machine logs and private source-history inventory are not included.

This public repository includes five selected verifier commands plus a chunked exact C5 certificate described in REPRODUCIBILITY.md. It does not include all scripts or historical inputs, so it does not reproduce the full internal audit. File hashes and source filenames are in PUBLICATION_MANIFEST.json; private Git object identifiers are omitted.

Finite checks verify finite expressions and certificates within their stated scope. They do not prove the joint high-product arithmetic saving, actual zeta moments, prime-to-Weil transfer, zero-side transfer, or strict >79% theorem. Analytic statements are supported by written proofs and assumptions in the linked notes, not by numeric replay alone.


## Added bounded-consumer candidate

The regression workflow now runs the exact SymPy checker and its two targeted tests for the fixed-parameter (F_{61}) model-moment candidate. These checks cover its rational identities and reported finite model bound. They do not verify the weighted six-pole comparison for arithmetic matrices, identify the model moments with zeta-prime data, or close prime-to-Weil or zero-side transfers. Numerical pole locations and residue norms remain diagnostics.
