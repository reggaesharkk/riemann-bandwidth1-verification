# Riemann Bandwidth-One Verification

> Research status: strict >79% simple critical-line zeros remains OPEN. No unconditional theorem at this level is claimed.

**Prince Upadhyay · Independent Research**

This public repository studies bandwidth-one Weil-form certificates and finite-band prime-operator methods relevant to lower bounds on simple critical-line zeros of the Riemann zeta function. It is a clean, curated tree of selected research artifacts. It does not import the private repository's Git history, branches, pull requests, private working materials, audit archives, or upstream A1294 source.

> **The strict >79% simple-zero theorem is unproved and remains OPEN.** This repository makes no Riemann Hypothesis claim and no unconditional >79% claim.

## Start here

- [Research status](RESEARCH_STATUS.md) — established, conditional, model-only, and open statements.
- [Dependency map](DEPENDENCY_MAP.md) — theorem dependencies and proof gates.
- [Verification summary](VERIFICATION_SUMMARY.md) — what the included checks do and do not establish.
- [Reproducibility](REPRODUCIBILITY.md) — pinned local commands and CI scope.
- [Third-party notices](THIRD_PARTY_NOTICES.md) and [rights policy](RIGHTS_POLICY_2026_10_01.md).
- `notes/` — theorem statements, proofs, audit reports, and machine-readable certificates.
- `src/` — exact and interval-based verifier implementations.

## Current mathematical status

Exact collision, Fourier/path and root-sum identities, rational ledgers and their stated verifiers are established in their documented scopes. The deterministic curvature-controlled discrete Loewner band-truncation theorem has a complete finite-dimensional proof. Prime-side moment and selected-section reprojection results hold under their stated cutoff, normalization and section hypotheses. None by itself proves the zero-proportion target.

Conditional calculations retain their assumptions. The Gaussian/Wick Pair6 value is for a defined reference model; it has not been identified with the full actual zeta sixth moment. Values mu5=1/36 and mu6=34/135 are model bookkeeping, not proved same-section zeta moments.

The **historical 68.820273% route is conditional**, not an established zero-proportion result. Its R=400 consumer had a nominal margin, but the complete filtered-to-sharp quartic correction, all transfer payments, and the zero-side passage were not closed. In particular, the filtered overlaps cannot simply be replaced by sharp overlaps. See the R=400 filtered/sharp audit notes.

The **79.627% figure is a model frontier**, not a theorem for zeta zeros. It comes from a finite model/reference moment calculation; the proposed values `mu5=1/36` and `mu6=34/135` are not established as actual same-section zeta moments.

For the current strict >79 target, the remaining gate is the joint signed third/fifth/sixth prime-product residual at full R=6000, with the natural cutoff, original masks, aliases, carrier phases and actual Pair6 term retained. The sufficient frozen inequality requires a negative saving exceeding `0.002057354918974498...`, plus transfer payments and strict slack. No such signed saving has been proved. Prime-to-Weil/source normalization and the matching zero-side transfer also remain open. The high-product first-alias analysis found that existing norm/divisor bounds lose about `X^(1/10)` in the critical window; that is a limitation of those estimates, not a counterexample to the underlying arithmetic inequality. The exact residual and reopening criterion are in [the frontier audit](notes/WP84_RESEARCH_FRONTIER_PUBLICATION_STATUS.md).

## Standalone research candidates

The publication audit ranks: (1) curvature-controlled discrete Loewner band truncation; (2) interval-certified finite-filter fourth-cumulant sign counterexamples; (3) alias-uniform quadratic prime correlations and same-section moments; (4) simultaneous good-section endpoint selection and weighted reprojection; and (5) a finite-block Gaussian Loewner sixth-moment certificate. Their scoped statements, proof locations, verifications, literature comparisons and novelty limits are documented in notes/WP84_PUBLICATION_READINESS_AUDIT.md. Priority and novelty remain unresolved. Candidate 1 is a potential standalone paper topic, not a cleared novelty claim.

## Evidence and reproduction

The earlier internal audit reported 43 designated replays and four additional selected certificate checks passing; this public tree does not reproduce that full suite. It contains four selected verifier programs and a chunked exact C5 certificate. The GitHub Actions workflow separates exact arithmetic, independent replay, manifest integrity, regression tests and 16 deterministic certificate shards. It uses public Ubuntu runners, commit-pinned actions, read-only repository permissions and explicit job timeouts below six hours; the only uploaded artifacts are generated public certificate shards, retained for five days. No private inputs or secrets are required. A verifier PASS establishes only the finite checks it implements; it does not prove the open arithmetic or zero-side claims. See REPRODUCIBILITY.md and VERIFICATION_SUMMARY.md. Several scripts write files; use a disposable checkout.

The dependency map and OPEN/CONDITIONAL boundaries are in [the frontier status](notes/WP84_RESEARCH_FRONTIER_PUBLICATION_STATUS.md). The source research repository dates to 2026-10-03. This separate public repository has its own creation date and fresh history. The manifest records selected source filenames and public-file hashes, without exposing or carrying over private Git history. No private working materials, local attachment index, offline audit archive, or upstream A1294 source is included.

## Rights

LICENSE and RIGHTS_POLICY_2026_10_01.md reserve eligible author-owned original expression first publicly released in this repository. They do not claim rights in mathematical facts or third-party works. Prior express licenses remain in effect for the material they covered. See THIRD_PARTY_NOTICES.md and the per-file manifest. No unconditional >79, priority or Riemann Hypothesis claim is made.
