# Verification coverage

This summary covers the finite checks reproduced by the public verification set. It does not claim to reproduce every historical experiment or research audit.

The public repository includes five selected verifier commands plus a chunked exact C5 certificate described in REPRODUCIBILITY.md. It does not include every historical script or input. File paths and hashes are recorded in PUBLICATION_MANIFEST.json.

Finite checks verify finite expressions and certificates within their stated scope. They do not prove the joint high-product arithmetic saving, actual zeta moments, prime-to-Weil transfer, zero-side transfer, or strict >79% theorem. Analytic statements are supported by written proofs and assumptions in the linked notes, not by numeric replay alone.


## Added bounded-consumer candidate

The regression workflow now runs the exact SymPy checker and its two targeted tests for the fixed-parameter (F_{61}) model-moment candidate. These checks cover its rational identities and reported finite model bound. They do not verify the weighted six-pole comparison for arithmetic matrices, identify the model moments with zeta-prime data, or close prime-to-Weil or zero-side transfers. Numerical pole locations and residue norms remain diagnostics.
