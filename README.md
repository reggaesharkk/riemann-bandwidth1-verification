<p align="center"><a href="https://github.com/reggaesharkk/Reggae-shark-universe-"><img src="https://raw.githubusercontent.com/reggaesharkk/Reggae-shark-universe-/main/assets/universe_bar.svg" alt="Reggae Shark Universe — public research map" width="100%" /></a></p>

<p align="center"><a href="https://github.com/reggaesharkk/Reggae-shark-universe-">Public research map</a> &nbsp;·&nbsp; <a href="https://github.com/reggaesharkk?tab=repositories">All public repositories</a> &nbsp;·&nbsp; <a href="https://orcid.org/0009-0002-1170-4487">ORCID</a></p>

> I keep each project’s evidence, scope, and open questions alongside the work.

---

# Riemann Bandwidth-One Verification

**Prince Upadhyay · Independent Research**

What proportion of the nontrivial zeros of the Riemann zeta function lie on the critical line and have multiplicity one? I study this question through finite matrices built from primes and bandwidth-one Weil forms. **The target of strictly more than 79% simple critical-line zeros remains open.**

[WP84 milestones](#wp84-milestones) · [Project guide](#start-here) · [Mathematical status](#current-mathematical-status) · [Reproduction](#evidence-and-reproduction) · [Cite the archive](#cite-this-release)

**Current proof status.** See the [radius-9000 proof ledger](notes/WP84_R9000_PROOF_STATUS.md) for the matched Weil comparison, the paired contribution, and the remaining signed arithmetic inequality.

**Finite-radius model check.** I added an exact six-site replay of the paired sixth moment and a model error budget. The semi-connected term uses about 0.00112721 square units. A uniform paired estimate and verification of the connected mass remain open. [Model ledger and replay instructions](notes/WP84_R9000_PROOF_STATUS.md#finite-radius-model-audit)

## WP84 milestones

| Result | What the calculation establishes |
| --- | --- |
| Weighted truncation at radius 9,000 | For the specified Loewner matrices, keeping the displacement weights gives a smaller upper bound on the truncation error at radius **9,000** than the previous estimate at **12,000**. [Derivation, §9](notes/WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md#9-weighted-displacement-estimate-and-a-radius-9000-arithmetic-target) |
| Test of the relaxed sixth moment | At the relaxed reference moment vector, even the best cubic normalized at the threshold has mean square **635/6159 ≈ 0.103101**. This exceeds the fixed gate **K ≈ 0.102108**. Refitting that cubic alone cannot close the gap at this model endpoint. [Exact calculation, §10](notes/WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md#10-radius-9000-the-signed-arithmetic-moment-budget) |

**The next arithmetic step.** On the same radius-9,000 prime-matrix section, the required moment inequality can be written as $\limsup_{T\to\infty}(Q_T-\tfrac{100}{161}V_T)<\theta$, where $\theta\approx0.21560655$. Here $Q_T$ is the mean square of a cubic in the centered matrix, and $V_T$ is the variance of a quadratic in that matrix. The square completion is exact. An upper bound on this signed difference and the subsequent transfer to the zero count remain open. [Definitions and exact threshold, §11](notes/WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md#11-same-section-square-completion-and-the-remaining-prime-sum-estimate)

With the [repository dependencies](requirements.txt) installed, run the [exact checker](src/wp84_functional_band_delta80_gate.py) from the repository root:

```sh
python src/wp84_functional_band_delta80_gate.py
```

## Cite this release

- **Archived version (fixed v0.1.0 snapshot):** [DOI 10.5281/zenodo.23244818](https://doi.org/10.5281/zenodo.23244818)
- **All-versions Zenodo concept DOI:** [10.5281/zenodo.23244817](https://doi.org/10.5281/zenodo.23244817) — resolves to the latest Zenodo version, not a substitute for citing the fixed v0.1.0 archive.
- **Frozen GitHub source:** [v0.1.0 release](https://github.com/reggaesharkk/riemann-bandwidth1-verification/releases/tag/v0.1.0), commit `6d799bddd9a27ba79c4faf8c757f7985ceb6d4c2`.
- The DOI identifies the archived research software and its exact version. Later commits on `main` do not alter the frozen v0.1.0 tag or archived DOI snapshot. The 68.820273% calculation is conditional, 79.627% is a model frontier, and strict >79% remains unproved.


**Zenodo version-field clarification (9 October 2026):** the Zenodo landing page presently displays `Version v1`, whereas the uploaded ZIP is named `riemann-bandwidth1-verification-0.1.0.zip` and the source is the GitHub `v0.1.0` tag. This is a deposit metadata-label mismatch, not an additional code version. GitHub cannot edit the Zenodo record; the Zenodo owner may correct that metadata separately. The archival source and tag are not rewritten.

## Start here

- [Research status](RESEARCH_STATUS.md) — established, conditional, model-only, and open statements.
- [Bounded WP84 consumer candidate](notes/WP84_BOUNDED_CHRISTOFFEL_CONSUMER.md) — exact model-moment algebra; the arithmetic six-pole gate remains open.
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

The original R=6000 high-product route still requires a negative saving exceeding `0.002057354918974498...`, plus transfer payments and strict slack; no such signed saving has been proved. A separate bounded rational-consumer route gives the original model coefficient `671891/847351` (about 79.2931%). Applying Jensen’s inequality to the same six-pole function gives `336653/424383` (about 79.32764%) under the pinned moments. The arithmetic comparison remains open. Both routes still require matching prime-to-Weil/source normalization and the zero-side transfer. The high-product first-alias analysis found that existing norm/divisor bounds lose about `X^(1/10)` in the critical window; that is a limitation of those estimates, not a counterexample to the underlying arithmetic inequality. See the [bounded-consumer candidate](notes/WP84_BOUNDED_CHRISTOFFEL_CONSUMER.md) and [frontier audit](notes/WP84_RESEARCH_FRONTIER_PUBLICATION_STATUS.md) for their distinct proof gates.

The publication audit ranks: (1) curvature-controlled discrete Loewner band truncation; (2) interval-certified finite-filter fourth-cumulant sign counterexamples; (3) alias-uniform quadratic prime correlations and same-section moments; (4) simultaneous good-section endpoint selection and weighted reprojection; and (5) a finite-block Gaussian Loewner sixth-moment certificate. Their scoped statements, proof locations, verifications, literature comparisons and novelty limits are documented in notes/WP84_PUBLICATION_READINESS_AUDIT.md. Priority and novelty remain unresolved. Candidate 1 is a potential standalone paper topic, not a cleared novelty claim.

## Evidence and reproduction

This public tree contains five selected verifier programs and a chunked exact C5 certificate. GitHub Actions separates exact arithmetic, independent replay, manifest integrity, regression tests and 16 deterministic certificate shards. It uses public Ubuntu runners, commit-pinned actions, read-only repository permissions and explicit job timeouts below six hours. Uploaded artifacts are generated public certificate shards. No credentials are required. Each PASS establishes only the finite checks implemented; it does not prove the open arithmetic or zero-side claims. See REPRODUCIBILITY.md and VERIFICATION_SUMMARY.md. Several scripts write files; use a disposable checkout.

The dependency map and OPEN/CONDITIONAL boundaries are in [the frontier status](notes/WP84_RESEARCH_FRONTIER_PUBLICATION_STATUS.md). The manifest records selected source paths and SHA-256 hashes. Upstream Git history, attachment indexes, offline archives and unrelated source material are not included.

## Rights

LICENSE and RIGHTS_POLICY_2026_10_01.md reserve eligible author-owned original expression first publicly released in this repository. They do not claim rights in mathematical facts or third-party works. Prior express licenses remain in effect for the material they covered. See THIRD_PARTY_NOTICES.md and the per-file manifest. No unconditional >79, priority or Riemann Hypothesis claim is made.
