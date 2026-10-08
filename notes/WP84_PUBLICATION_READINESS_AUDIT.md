# WP84 standalone contribution, proof and novelty audit

Research publication-readiness assessment, 2026-10-08.
This is not a new >79 proof. The public proposal does not include the
private repository's commit history or internal audit inventory.
The concise frontier and exact reopening gate are in
[WP84_RESEARCH_FRONTIER_PUBLICATION_STATUS.md](WP84_RESEARCH_FRONTIER_PUBLICATION_STATUS.md).
All source statements below use the frozen input versions; old artifacts
are not edited. Relative links resolve within this repository.

## Scope, verification and novelty boundary

The underlying private research was reviewed broadly, but its history
inventory, internal file hashes and run logs are intentionally not part of
this public proposal. The internal audit reported 43 named replay suites
and four additional selected certificate runs passing on isolated copies.
These historical checks do not reproduce in full from the selected public
tree and are not represented as such. The included finite rank checks
verify only their finite matrices; they do not recover source-selected rows
or prove rank of the actual source family. Proof and novelty conclusions
were evaluated for the five ranked candidates and the dependency chain,
rather than inferred from file names or script PASS messages.

The proposed release manifest records hashes of the files actually included
here. Historical external-source programs are not vendored, and their
presence in earlier private audit records is not a proof of the arithmetic
claims under review. SymPy, mpmath and NumPy are runtime dependencies only;
they are not vendored. Other historical replays requiring inputs outside
this public tree are excluded from the reproducibility claim.

The literature search consulted primary papers, author-hosted manuscripts
and original lecture notes. It establishes the comparisons stated here,
not exhaustive priority clearance. Failure to find an identical formula
does not prove originality. None of the five is presently cleared as a
new publishable theorem with established priority.

## 1. Deterministic curvature-controlled full-to-band trace bound

**Statement.** Let H be an n-by-n real symmetric matrix with arbitrary real
diagonal and H_ij=(alpha_i-alpha_j)/(pi(j-i)) for i!=j. Let H_R keep the
diagonal and entries with |i-j|<=R, R>=1. Put q=||alpha||_2^2/n and
tau=tr/n. For every real C^2 function f with M=||f''||_infinity finite,

    |tau f(H)-tau f(H_R)| <=12 q M/(pi^2 R).

No spectral bound, prime input, moment model or open arithmetic gate is
needed. Boundedness of f itself is unnecessary for finite matrices.

**Complete proof.** [Functional band theorem](WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md),
Sections 1--4, independently derived again in
[referee foundations](WP84_INDEPENDENT_REFEREE_RESPONSE_FOUNDATIONS_AND_GUE.md),
Section 5. Set E=H-H_R and D=diag(0,...,n-1). Direct entry sums give
tau E^2<=8q/(pi^2 R) and ||[D,H_R]||_F^2/n<=8Rq/pi^2.
The trace Taylor remainder is at most (M/2)tau E^2. In the eigenbasis of
H_R, divided differences give
||[D,f'(H_R)]||_F<=M||[D,H_R]||_F. Since E has only distant entries,
the linear trace costs at most ||E||_F||[D,f'(H_R)]||_F/(nR).
The charges 4 and 8 sum to 12. The proof handles repeated eigenvalues by
the derivative limit. **Unconditional deterministic theorem.** The WP84
specialization q=1/4+o(1) additionally uses the prime-matrix variance theorem.

**Verification.** Referee foundations independently replay the rational
curvature certificate 137721/5000 and both exact Sturm chains. The older
delta80 gate rerun verifies its different curvature bound 72. These verify
special consumer constants; the general matrix theorem is established by
the analytic proof, not by finite numerical tests.

**Literature comparison.** Gesztesy--Pushnitski--Simon,
[On the Koplienko spectral shift function, I](https://arxiv.org/pdf/0705.3629),
Theorem 4.1 and Proposition 4.2, give the classical Lipschitz
Hilbert--Schmidt bound. Their Theorem 3.4 gives the second-order trace
remainder mass (one-half the squared Hilbert--Schmidt perturbation norm).
The commutator version used here follows directly from the same divided
differences. Thus those ingredients and the C^2 trace remainder are KNOWN.
The discrete Loewner tail/commutator combination and explicit constant 12
are the specialized statement to compare; this audit found no directly
matching cited theorem, but does not establish its priority or sharpness.

**Classification:** potentially new specialized contribution; classical
proof ingredients. **Publication work:** present the theorem without zeta
claims, give the entry sums and finite-dimensional C^2 justification in one
place, document the arbitrary diagonal, and obtain expert literature
clearance. Do not market 12 as optimal or claim operator-norm Lipschitzness.

## 2. Explicit failure of filtered fourth-cumulant sign and Gram shortcuts

**Statement.** On the uniform m-row Fourier grid let
D_m(u)=m^(-1)sum_(k=0)^(m-1)exp(2pi i k u), and let

    kappa_m(v)=sum_(partitions pi) (-1)^(|pi|-1)(|pi|-1)!
                                product_(B in pi)D_m(sum_(j in B)v_j).

This is equivalently the 26 anchored ordered terms in the source.
Let Phi_(R,m)(v)=Omega_(4,R)(v) kappa_m(v), where Omega is the SAME
closed four-increment filtered interval overlap defined in the source.
For v=(1/5,-2/5,3/5,-2/5) and 5|m, kappa_m(v)=1 and

    0.39974848084713831 < Phi_(400,m)(v) <0.39974848084713832.

Furthermore the internally order-averaged six-interleaving pair kernel at
P=(2/5,4/5), Q=(3/5,3/5) has zero first diagonal and cross entry c in
(0.39950281400985174,0.39950281400985176). Its 2-by-2 principal determinant
is -c^2<0. The connected kernel is not negative semidefinite even at
supercritical scale 6/5. These are geometric/empirical counterexamples,
NOT counterexamples to the source-weighted prime inequality.

**Complete proof and assumptions.** [Actual filtered fourth kernel](WP84_R400_FILTERED_CONNECTED_KERNEL.md),
Sections 2--5. Every proper block sum of v is nonintegral; exact finite
Fourier orthogonality kills every proper partition, leaving cumulant 1.
The pair diagonals have cumulants 0 and -1. The cross value is evaluated
by outward-rounded interval arithmetic: the four finite trigonometric
factors have degree at most 4R, so a grid with M>4R exactly extracts their
constant coefficient. The script sums ALL internal orderings and six
interleavings. The determinant sign is independent of the second diagonal.
The witnesses persist in the m->infinity limit. **Unconditional for these
defined kernels**, not for actual ordinary-prime realization of the rational
displacements. Exact ordinary-prime non-pair closures cannot realize them.

**Verification.** `src/wp84_r400_filtered_connected_kernel.py --certificate`
was rerun, including its finite algebra checks and interval FFT. It produces
narrower enclosures within the quoted bounds. This is a validated rerun of
the existing interval algorithm; unlike the nine-site Wick calculation it
does not have a wholly different second interval implementation. No random
search, supremum certification or new experiment was used.

**Literature comparison.** [Speed (1983), Cumulants and partition lattices](https://doi.org/10.1111/j.1467-842X.1983.tb00391.x)
derives the classical partition/Mobius cumulant algebra. Its fourth-order
specialization is the identity above, not new mathematics. The explicit
filtered-overlap/sign witnesses are the possible new corrective contribution;
neither general cumulants nor cumulant matrices are automatically positive
or negative semidefinite. The relevant novelty question is the precise
proposed filtered partial-translation kernel, not a universal fact about
cumulants. No matching published sign theorem is claimed to have been
disproved by this private audit.

**Classification:** potentially new explicit counterexamples with interval
certificates. **Publication work:** state the exact overlap coefficients and
the challenged geometric implication without referring to unpublished
private claims; package the certificate and an independent interval replay;
explain why these displacements need not occur as distinct-prime closures.

## 3. Alias-uniform quadratic prime correlation and same-section moments

**Statement.** Put X=T/(2pi), L=log X, N=floor(exp(L-sqrt L)), h=2pi/L.
For any original fixed-band closed path use its exact root kernel

    K(lambda)=exp(i(T+h i_min)lambda)/n
                         sum_(j=0)^(rho-1)exp(i h j lambda),
    n/d->1, d=floor(XL), rho=n-O_R(1).

Uniformly in the initial row and weights |a_p|,|b_p|<=C/sqrt p supported
on the unchanged prime cutoff, the opposite-sign off-diagonal p!=q and
same-sign quadratic sums are bounded in absolute value by

    O_(C,R)(N log N/T + L/sqrt X)=o(1).

All exact and approximate aliases in these sums are included. Consequently
the two-singleton part of a globally balanced 2+2+1+1 collision is o(1),
with original distinctness restored by the already bounded merged blocks.
It is not the three-balanced-pair Pair6 main term.

For the actual ordinary-prime Loewner matrix Y with alpha/beta in the
source normalization a_phi->1, this also gives, uniformly over the same
contiguous n/d->1 sections,

    tau Y=o(1),
    tau Y^2=1/6+sum_(r=1)^R 1/r^2/pi^2+o(1),
    average alpha_i^2=1/4+o(1).

Proper powers change the first/second moments by o(1). This does NOT transfer
these moments to a different Weil matrix without a matched representation.

**Complete proofs.** [Balanced-pair audit](WP84_STRICT79_HOSTILE_AUDIT_AND_BALANCED_PAIR_REDUCTION.md),
A2--A3, and [same-section variance](WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md),
Section 3. Near the ratio zero, integer harmonic summation costs
O(N log N/T). A same-sign product has at most two ordered prime
representations; near u=X its kernel is bounded by min(1,C/|u-X|), and its
coefficient by C/sqrt X. Isolate the nearest integer then sum the harmonic
tail to obtain O(L/sqrt X), uniformly for real X. The natural cutoff
separates all other relevant aliases; away from the unit windows the
coefficient l1-product costs O(N/T). The diagonal is evaluated by classical
prime-square PNT. The proofs give UNCONDITIONAL results for the explicitly
defined prime matrix under their scalar normalization/cutoff assumptions,
not an unconditional zeta identification.

**Verification.** Balanced-pair replay independently checks the 14,656-class
census, merge corrections and hostile scope mutations. Third-aware replay
checks all 6000-displacement variance sums, exact payment credit and sign
falsifiers. Those finite tests support the coefficient/partition arithmetic;
the asymptotic bound is proved by the preceding summed majorants.

**Literature comparison.** [Montgomery--Vaughan (1974), Hilbert's Inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf),
Theorem 2 and Corollary 2, already give real-frequency mean-square control
by minimum spacing. Fixed charges e log p retain spacing |e|/(N+1), even
when a block carries p^2. The sampled-cell step and explicit alias harmonic
count are elementary source adaptations, not a new large-sieve theorem.
[Alpoge--Furman v2](https://arxiv.org/html/2608.13637v2), Sections 5.1--5.4,
already evaluates an unconditional bandwidth-one prime-side second moment
for its smooth Weil/Gabor test family. WP84's fixed-R, same-section formula
is a different specialization and is not a new discovery of the second
moment or a new record for zeros. A publication would need to show the
usefulness of this explicit discrete/alias-uniform corollary.

**Classification:** known techniques with a source-specific proof/application;
possible new explicit reduction, priority unresolved. **Publication work:**
make the constant dependencies and endpoint uniformity explicit, separate
the elementary quadratic lemma from PNT/normalization, and state precisely
which complete collision populations follow. Never extend the unsplit
collision result to arbitrary frequency-masked pieces by assertion.

## 4. Simultaneous endpoint selection and weighted band reprojection

**Statement.** For the linear alpha/beta prime-power fields with coefficient
square mass M=O(1), log-frequency support <=L, fixed R and b0=6, let
q=floor(d/sqrt L), q/d->0, and N/(qh)->0. There exists ONE contiguous
section I with d'=|I|>=d-2q, whose endpoint neighborhoods control all
degrees b<=6. If K is the local band operator-norm bound at those endpoints,

    |d'^(-1)tr((P_I A_R P_I)^b-P_I A_R^b P_I)|
                                <=4 b R K^b/d'=O_R(1/d').

A_R is the explicitly defined infinite hard-band alpha/beta matrix and
its local powers; the finite-band entries and prime powers are retained.
This is an existential section theorem, not a unique historical selector
for determinant evaluations or a raw-moment transfer from the full matrix.

**Complete proof.** [Weighted reprojection](WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md),
Sections 3--5. MV mean-square plus disjoint-cell sampling bounds the linear
fields in each candidate endpoint window. Average the sum of finitely many
neighboring scores to select left/right endpoints simultaneously. The
local row sum gives K<=sqrt(F)(1+4H_R/pi), F=O_R(1). At most 2bR roots
have paths crossing an endpoint; each of the two local matrix-power
diagonals is bounded by K^b. No coefficient l1 sum or sixth global moment
is used. **Unconditional implication under these explicit finite-support,
second-mass and scale assumptions**. These assumptions hold for the
defined retained prime field; its relation to the original smoothed Weil
form is an additional application obligation.

**Verification.** The Fourier reprojection program rerun checks exact finite
compression identities and coefficient integrals, plus numerical diagnostic
instances. The foundation replay independently checks the disjoint-cell
constant. These do not enumerate all T or prove the asymptotic statement
computationally; the averaging/boundary proof supplies it.

**Literature comparison.** The same MV theorem above supplies the only
non-elementary mean-square ingredient. Finite bandwidth makes only bR
boundary roots exceptional, the usual finite-section mechanism. The
coefficient-preserving simultaneous endpoint application is the specialized
result, not a new Fourier convergence or spectral distribution theorem.
No priority claim is warranted by this literature search.

**Classification:** classical argument with a source-specific application,
potential auxiliary proposition. **Publication work:** provide all score
definitions and boundary neighborhoods in a standalone statement, and
make the distinction between section existence and source-authentic
determinant row data explicit. This theorem needs no determinant selector.

## 5. Exact finite-block Gaussian Loewner sixth-moment certificate

**Statement.** Define independent centered stationary real Gaussian fields
with E alpha_i alpha_j=delta_ij/4, E alpha_i beta_j=0, and beta covariance
1/6 at zero and -1/(2pi^2(i-j)^2) otherwise. Let W_(n,R) have diagonal
beta and off-diagonal (alpha_i-alpha_j)/(pi(j-i)) within band R. Define
Pair6_R=lim_(n->infinity)E tr(W_(n,R)^6)/n. For R>=8,

    Pair6_R >= E tr(W_9^6)/9
       =5/72+(288223/403200)x
          +(3189863194981/663828480000)x^2
          +(2749260640878247123/156132458496000000)x^3,
    x=1/pi^2,
    Pair6_R >31498340500050746323/150466924118016000000.

The beta covariance is positive semidefinite via its spectral density
s(1-s) on the unit circle. Thus the process exists independently of zeta.
**Unconditional for this defined Gaussian reference.** Its equality with
the source's exact three-pair contribution additionally uses the correctly
normalized prime-square PNT feature transfer. It is NOT a lower bound for
the entire actual sixth moment, which has a signed non-pair residual.

**Complete proof.** [Referee foundations](WP84_INDEPENDENT_REFEREE_RESPONSE_FOUNDATIONS_AND_GUE.md),
Section 4; [balanced-pair audit](WP84_STRICT79_HOSTILE_AUDIT_AND_BALANCED_PAIR_REDUCTION.md),
finite-block certificate. Wick-expand the nine-site matrix, average the
trace, then pinch a large W_(n,R) into consecutive nine-site blocks.
Pinching contracts Schatten six; complete blocks have law W_9, and the
leftover contributes nonnegatively. Fixed-R boundary walk fractions are
O_R(1/n). Positive polynomial coefficients and pi<22/7 give the rational
strict lower bound. No independence between consecutive blocks is needed.

**Verification.** Two existing algorithms enumerate 531441 walks and
40191 edge multisets using explicit matchings versus recursive Wick
pairing. Both were rerun in the corresponding independent suites; the exact
polynomial and rational pi enclosure pass. This is stronger than matching
two decimal simulations but remains a certificate for a specified model.

**Literature comparison.** [Isserlis (1918)](https://doi.org/10.1093/biomet/12.1-2.134)
is the classical Gaussian product-moment pairing theorem. For pinching,
[Tropp, Matrix Analysis, pinching exercise, PDF p. 208](https://tropp.caltech.edu/notes/Tro22-Matrix-Analysis-LN.pdf)
records singular-value weak majorization under block pinching, which gives
Schatten norm contraction. Neither Wick's theorem nor pinching is new.
The explicitly certified W_9 polynomial and resulting bound are the
candidate contribution. Their novelty alone does not ensure mathematical
publication significance.

**Classification:** new computational certificate for a defined model;
classical theorem application. **Publication work:** include the two compact
exact enumerators and pinned data, define the model without a GUE dictionary,
and explain a use independent of a still-open prime high-moment conjecture.

## Excluded promotions and historical proof dependencies

| Historical claim/application | Defensible present interpretation | First missing input |
|---|---|---|
| Frozen >79 or earlier 68.820273 assembly | Exact conditional consumer ledger | Actual signed arithmetic gate; R400 also unpaid filtered/sharp fourth correction |
| Same-section centered mu3=o(1) | Linear mean and repeated-base/low-product cubic pieces close | Aggregate surviving third aliases/tails; no scalar-third assumption imported |
| Scalar C_ab -> k_ab inside high moments | Valid complete bounded-gate bootstrap/PNT replacement | Upper bounded complete signed gate supplies sixth control; no unrestricted masked substitution |
| All charged-pair/triple higher removals | Valid bounded-gate equivalence, with grouped orientations | Not independently negligible in every sign/window absent sixth control |
| Arbitrary o(d) row deletion preserves high moments | b<=5 transfer with sixth bound; one-sided sixth compression | Uniform sixth norm supplied by a bounded gate, not by rank deletion |
| Fixed-R filtered overlaps equal sharp overlaps | False already for pair Fourier tails and fourth witnesses | Actual quantitative finite-R replacement error, not just R->infinity |
| Source-normalized prime moments equal Weil/zero moments | Prime-matrix lower moments proved | Same-section taper/background/normalization representation and bounded transfer |
| Zero-side block/index/tail argument | External theorem for the exact smooth Weil/Gabor matrix | Match WP84 test family, smoothing, normalization, thresholds and interval count |
| Gaussian/GUE or model mu5=1/36, mu6=34/135 | Model/reference values only | Actual arithmetic derivation and admissibility; the GUE dictionary was not established |
| Formal fifth ranks, 73->9->K and 453 functionals | Exact diagnostic identities; genuine-source K undetermined | Source-selected evaluation rows/masks/intertwining, auxiliary to the direct signed gate |
| Fourier-completion zero mode supplies a main term/sign | Exact basis-dependent identity; residual phase remains | Complete coupled prime-product correlation estimate |

These flags do not contradict legitimate conditional theorems. The
self-bounding coercivity and Young inequality prove an equivalence without
circularly asserting that its antecedent holds. The historical compression
counterexamples correctly refute rank-only inference, not the prime target.
The covariance-only mismatch compares two models and must not be described
as a contradiction with proved actual zeta moments.

The external [Alpoge--Furman v2, Sections 3--4](https://arxiv.org/html/2608.13637v2)
contains the pull-back inertia, on-line rank blocks, tail-Weyl and interval
count arguments. Remark 4.4 requires C^2 smoothing for the tail proof;
sharp-cutoff replacement cannot inherit it automatically. The WP84 source
matching obligation remains visible despite those external theorems.
WP84 must not claim this zero-side mechanism as a new local contribution.

Other historical branches were considered but rank below the five above:
Fourier word convergence is a standard Parseval/telescoping estimate;
Brownian/min-kernel Gram identities are familiar indicator-Gram mechanisms;
Gaussian heat/characteristic and Stein/Mehler identities are known identities
with unpaid source/tail transfers; model SOS/consumer optimizations and
formal determinants are computational/conditional results. None supplies
an independently proved new zero proportion.

## Publication recommendation and reopening rule

Prepare one standalone mathematical note on **curvature-controlled band
truncation for discrete Loewner matrices**, with the simultaneous endpoint
proposition as a source application. It has a complete target-independent
proof and can be written without the speculative moments, rank routes or
zero percentages. This is a supported writing topic, not a declaration of
originality or acceptance readiness. Before submission, an operator-theory
referee should determine whether the explicit specialization warrants a
research note or is best presented as an application/expository proposition.
No current >79 manuscript is publication-ready as a theorem paper.

Keep >79 frozen. The weakest sufficient target for its EXISTING consumer
is the complete same-section aggregate signed bound in the frontier report,
with actual Pair6, strictly positive gap, and paid transfer errors. It does
not require historical-selector recovery, separate fifth/sixth model limits
or mu3=o(1). A partial source-weighted strip theorem merits reopening only
when its exact normalized improvement and remaining global budget are
explicit; an o(1) removal alone is not the necessary negative constant.
Do not reopen on a favorable coefficient sign, norm bound for surrogate
weights or a nonzero-mode-only estimate. No new search was launched here.
