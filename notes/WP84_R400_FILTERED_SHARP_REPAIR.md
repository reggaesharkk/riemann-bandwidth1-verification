# WP84 — R400 filtered/sharp repair and first arithmetic obstruction

Date: 2026-10-07. Filtered-versus-sharp audit.
R is fixed at **400** throughout. This historical route remains conditional.

**Status: exact consumer tolerance and degree-four Fourier diagnostics CLOSED;
the actual coefficient-weighted correction Delta400 remains OPEN. The margin
is not proved exhausted, and the 68.82027318675% route is not proved repaired.**

The first obstruction is before numerical optimization: the six audited notes
do not derive an identity from the actual filtered non-pair prime trace to a
specified 26-term connected measure/kernel, nor an estimate in the weighted
quadratic-form norm needed to pay its replacement. A supremum bound on a
continuum kernel, even a very small one, cannot supply that missing identity
or norm estimate. This note does not assign a model number to Delta400.

The exact allowable fourth-moment increase, conditional on the other old
inputs retaining their stated bounds, is

    Delta400 < 3675673694911 / 148250000000000
             = 0.02479375173633052276559865092748...

The accompanying verifier performs exact rational summation and rational pi
enclosure. It prints the complete 26-term ledger with `--terms`. Its final
status explicitly leaves the actual R400 theorem open. All existing commits
and source notes are preserved. No push, merge, rebase, or main/Downloads
change is part of this repair.

## 1. The actual object and the two different closure conditions

Use the normalized prime coefficients and selected Fourier section already
audited in `WP84_FIXED_BAND_WEIGHTED_REPROJECTION`:

    L = log(T/(2pi)),  h = 2pi/L,
    d = floor(TL/(2pi)), I = [k_-,k_+], d' = |I|,
    N = floor(exp(L-W)), W = sqrt(L) (or the stated o(L) quarantine),
    c_n = -Lambda(n)/(a_phi L sqrt(n)), a_phi -> 1.

On the unit circle, let J_v be the admissible interval for the sharp partial
translation U_v; for |v|>1 it is empty. Define

    V_v,R = M_(F_R 1_Jv) T_v,
    S_T,R = sum_(n<=N,epsilon=+,-) c_n exp(i epsilon T log n) V_(epsilon log n/L,R),
    A4 = d'^(-1) tr((P_I S_T,R P_I)^4),
    B4 = d'^(-1) tr(P_I S_T,R^4 P_I).

The centered prime fourth moment is A4, subject separately to the corrected
Weil/prime normalization and scalar/ramp reductions. Reprojection gives B4,
not a sharp word. The selected-section proof with b0=6 also applies to b=4:

    |A4-B4| <= 16 R K_R^4/d' = o_T(1),

where K_R=O_R(1) is the local edge norm from the linear-field endpoint score.
This is the same proof for a smaller word degree; no original-endpoint raw
quartic stability is inferred.

For a tuple v_j=epsilon_j log(n_j)/L, put p_0=0,
p_j=sum_(a<=j) v_a and S=p_4. The exact filtered overlap is

    Omega4,R(v) = integral_0^1 product_(j=1)^4
                           (F_R 1_Jvj)(x+p_(j-1)) dx.

Then

    B4 = sum_(n_1,...,n_4,epsilon_1,...,epsilon_4)
         (product_j c_nj) K_I(S) Omega4,R(v),
    K_I(S) = exp(i T L S) exp(2pi i k_- S) D_d'(S).

Every tuple has coefficient exactly `product_j c_nj`, before the consumer
coefficient 593/2000. There is no 26-term cumulant in this exact expansion.

For a_r(v)=integral_Jv exp(-2pi i r x) dx, the finite Fourier identity is

    Omega4,R(v) = sum_(|r_j|<=R, sum r_j=0)
                 product_j a_rj(v_j)
                 exp(2pi i sum_j r_j p_(j-1)).

Here a_0(v)=1-|v| for |v|<=1 and |a_r(v)|<=1/(pi |r|).
At R400 the number of closed displacement paths is exactly

    binom(1603,3)-4 binom(802,3) = 342615201.

**sum r_j=0 is Fourier matrix-index closure. S=0 is physical/log-product
closure. They are independent conditions.** In particular the former cannot
remove nonexact multiplicative products or periodic aliases. The physical
alias condition is S in Z, with near-alias windows |S-m|=O(1/(TL)).

## 2. Load-bearing audit of the six requested sources

Let Csharp(v)=O_A(v) B4_nc(v), where O_A is the sharp walk overlap and
B4_nc is the signed 26-term nested-subset overlap sum. This is the object
computed by the geometric certificates, including for nonclosed v. It is
not an algebraic consequence of expanding the linear prime operator above.

| Source and use | Actual quantity requiring a bound | Sharp quantity substituted | Exact coefficient / status |
| --- | --- | --- | --- |
| FIXED_SCALE_CONNECTED_KERNEL §§1–3 | No arithmetic object in these sections; standalone sharp kernel | C6,s(x,y)=-2(s-1)[min(r_x,r_y)-(s-1)] | Six interleavings each +1; geometric identity CLOSED |
| Same §§4–6 | Actual balanced filtered prime remainder after finite-lag pair subtraction | c* (C6 o K_I) c, signed by the Brownian Gram factorization | Ordered-pair coefficient c_p c_q against c_r c_s, each interleaving +1; the identification is OPEN |
| CROSS_SCALE_SHARP_DETUNING §§1–4 | All six filtered interleavings, including four nonalternating words | Four zero amplitudes plus A1 and A2 below | Each word coefficient +1 times the prime product; sharp-only vanishing cannot delete the filtered words |
| Same §§4–7 | Filtered unequal-product-scale residual in the same weighted trace | C6=-G+E, G=2c min(b,(a-delta)_+), -dist(s-t,Z)<=E<=0 | Reference coefficient -1 and residual +1; the 2 is inside G, not an extra orientation multiplier |
| DETUNING_COMMUTATOR_ENDPOINT §§1–2 | K_I and [Z,K_I] | The same exact Gram kernel | SAFE algebra; each of two endpoint carriers has coefficient +1/d' or -1/d' |
| Same §3 and sharp-constant update | Actual filtered residual, if represented as E_R o K_I | E o K_I = H o [Z,K_I], H=E/(z_i-z_j), |H|<=1/4 | Identification OPEN; no corresponding E_R or H_R was derived |
| GOOD_ENDPOINT_TRIMMING §§1–2 | Bounded consumer before quartic application | Bounded rank comparison | Rank charge O(r/d)=o(1); no fixed-R overlap replacement is used here |
| Same §§3–6 | Correct weighted filtered endpoint families, if they exist | Sharp threshold-feature Dirichlet families, followed by the endpoint 1/d' factor | Feature signs inherited from E; mean-square argument CONDITIONAL on exact representation and second mass |
| Same §7 | Actual w400 on the selected section | Pair400 + sharp connected contribution <=0+o(1) | Pair coefficient +1; non-pair coefficient +1; missing weighted filtered identification |
| R400_COMPLETE_WORD_LEDGER_REPLAY §6 | Finite-lag pair contractions | Pair400=2 t_adj(400)+t_opp(400) | Coefficients exactly 2 and 1; already filtered, so NO sharp-pair tail charge is added |
| Same §7 | Non-pair arithmetic residual of A4 or B4 | Sharp negative Brownian part plus sharp endpoint residual | Coefficient +1; model -1/60 is NOT consumed numerically |
| Same §§8–9 and FIRST_RECORD_ASSEMBLY §§2–5 | Full centered quartic trace | w400<=0.266329, v400<=1/3, first/third moments o(1) | Fourth 593/2000; variance 213/1000; see complete polynomial below |

The two surviving sharp alternating amplitudes in the chamber
1<=s<=t<=2, c=s-1, d=t-1, delta=d-c,
0<=a<=(1-c)/2, 0<=b<=(1-d)/2 are

    A1 = -min(c+a,d) [min(a,b,1-d-a)]_+,
    A2 = -c min(b,(a-delta)_+),
    C6 = A1+A2, G=2c min(b,(a-delta)_+), E=C6+G.

Thus the Brownian bulk and endpoint term are a decomposition of ONE sharp
connected contribution. They are not independent errors to be charged twice.
Likewise C24=4 C6=C8 is a sharp orientation reconciliation, not permission
to multiply an already ordered-pair arithmetic ledger by four again. At fixed
R the assertion C24=C8 requires a new check because the four nonalternating
filtered overlaps need not vanish.

## 3. The exact 26 coefficients and the finite-R definition gap

An ordered partition is anchored by the block containing label 0. For each
ordered list of blocks B1,...,Bm its coefficient is (-1)^(m-1). Its second
sharp overlap uses the positions 0, sum_(j in B1)v_j, ...,
sum_(j in B1 union ... union B_(m-1))v_j, S. All 26 terms share O_A.
Each coefficient below becomes its sign times 593/2000 at the consumer,
with any normalized arithmetic measure still needing derivation.

| Term | Sign | Ordered blocks |
| --- | --- | --- |
| 1 | +1 | 0123 |
| 2 | -1 | 0 / 123 |
| 3 | -1 | 01 / 23 |
| 4 | -1 | 023 / 1 |
| 5 | +1 | 0 / 1 / 23 |
| 6 | +1 | 0 / 23 / 1 |
| 7 | -1 | 012 / 3 |
| 8 | -1 | 03 / 12 |
| 9 | +1 | 0 / 12 / 3 |
| 10 | +1 | 0 / 3 / 12 |
| 11 | -1 | 02 / 13 |
| 12 | -1 | 013 / 2 |
| 13 | +1 | 0 / 2 / 13 |
| 14 | +1 | 0 / 13 / 2 |
| 15 | +1 | 01 / 2 / 3 |
| 16 | +1 | 01 / 3 / 2 |
| 17 | +1 | 02 / 1 / 3 |
| 18 | +1 | 02 / 3 / 1 |
| 19 | +1 | 03 / 1 / 2 |
| 20 | +1 | 03 / 2 / 1 |
| 21 | -1 | 0 / 1 / 2 / 3 |
| 22 | -1 | 0 / 1 / 3 / 2 |
| 23 | -1 | 0 / 2 / 1 / 3 |
| 24 | -1 | 0 / 2 / 3 / 1 |
| 25 | -1 | 0 / 3 / 1 / 2 |
| 26 | -1 | 0 / 3 / 2 / 1 |

Counts by m are 1,7,12,6; signs count 13 positive and 13 negative.
The signs cancel on constants but this alone says nothing about the filtered
arithmetic trace.

There are at least three inequivalent finite-R candidate constructions:

1. Filter only the four external translations, retaining the sharp B4 bracket.
2. Filter external translations and every MERGED translation in the bracket.
3. Keep products of the INDIVIDUALLY filtered translations inside each block.

Filtering is linear and not multiplicative. For v0=v1=1/2,

    V_(1,R)=0,
    integral (F_R 1_[0,1/2])(x) (F_R 1_[0,1/2])(x+1/2) dx = g_R >0.

Thus filtering a merged block 01 differs from multiplying its filtered leaves.
For term 3 at v=(1/2,1/2,-1/2,-1/2), construction 2 has a zero second
overlap, while construction 3 has the strictly positive mixed fourth overlap
computed below. These are EXACT finite-R distinctions.

The actual arithmetic expansion specifies four external filters; it supplies
no rule introducing a second, independent overlap and its ordered partitions.
Until that derivation is given, selecting a finite-R cumulant construction is
a model definition, not a theorem. This is the first source-level obstruction.

## 4. Certified degree-four calculation: no generic b-word estimate used

This calculation uses an actual closed four-step operator word, exact Fourier
coefficients, zero total Fourier displacement, and the pair structure. It
also computes all cancellations in construction 2 at this witness. It is NOT
a uniform kernel bound, a weighted arithmetic bound, or a Delta400 certificate.
Repeated half-step prime tuples themselves have negligible diagonal prime
mass; the witness establishes operator distinctions, not a surviving prime
contribution.

Let f=F_R 1_[0,1/2], u=f-1/2. For even R,

    f(x+1/2)=1-f(x),
    u_hat(r)=1/(pi i r) for nonzero odd |r|<=R; zero otherwise,
    A = integral u^2 = (2/pi^2) sum_(odd 1<=r<=R) 1/r^2,
    B = integral u^4 = Eodd4/pi^4.

For M=399 and positive even r<=798, put

    s0 = -2 sum_(positive odd j<=M) 1/j^2,
    s_r = (2/r) sum_(odd max(-M,r-M)<=j<=min(M,r+M)) 1/j,
    Eodd4 = s0^2 + 2 sum_(positive even r<=798) s_r^2.

Partial fractions prove the s_r formula directly from the convolution; all
sums are rational. The fourth moments are EXACTLY

    Qalt = integral f^4 = 1/16 + (3/2) A + B,
    Qmix = integral f^2(1-f)^2 = 1/16 - (1/2) A + B.

The two alternating balanced words have Qalt. The four nonalternating words
have Qmix. Their sharp overlaps are respectively 1/2 and zero. At R400:

    g400 = 1/4-A
      in [0.00025330243139596370, 0.00025330243139596371],
    Qalt
      in [0.49962004619250208674, 0.49962004619250208676],
    Qmix
      in [0.00012665105529401415, 0.00012665105529401416].

The alternating error is approximately -0.00037995380749791325, not -g400.
After all six outer words are summed,

    Kouter = 2 Qalt+4 Qmix = 3/8 + A + 6 B,
    Kouter-1
      in [-0.00025330339381976990, -0.00025330339381976989].

Even this six-word error is not exactly -g400.

For the explicitly labeled MERGED-FILTER DIAGNOSTIC cumulant, the full
26-term cancellation gives

    B4,merged,R = -1 + 4 integral f^2 - 2 Qalt - 4 Qmix
                = -3/8 + 3 A - 6 B.

The net coefficients of the inner paths are: constant -1, pair +4,
alternating fourth -2, mixed fourth -4. The sharp bracket is zero here.
Consequently the six-word diagnostic connected value is

    C6,merged,R = (3/8+A+6B)(-3/8+3A-6B)
      in [-0.00075971384491126395, -0.00075971384491126393].

Construction 1 instead gives zero at this same tuple because its sharp
bracket is zero. Thus even after exploiting all 26 signs, finite-R candidate
definitions disagree. The negative diagnostic value above is not evidence
of uniform Gram negativity of the actual filtered arithmetic remainder.

Machin's identity pi=16 arctan(1/5)-4 arctan(1/239), with alternating rational
remainders (28 and 9 terms), certifies every displayed interval. The verifier
also checks selected convolution coefficients directly, independently of the
partial-fraction shortcut. Interval decimal endpoints are rounded outwards.

## 5. Why a small kernel error is not the coefficient-weighted correction

The sharp connected gate is consumed as a semiprime quadratic form. If a
derived filtered kernel were Csharp+J_R, its additional contribution would be

    sum_(p,q,r,s) c_p c_q c_r c_s
       J_R(p,q;r,s) K_I(log(pq/rs)/L).

The ordered two-prime coefficient second mass is bounded, and collapsing
ordinary semiprimes incurs at most multiplicity two. This controls ||c||_2,
not the operator norm of J_R o K_I or the variation of the four-prime measure.

The finite Dirichlet Gram kernel is positive semidefinite with diagonal one,
but its operator norm need not be bounded independently of the number of
product states. A scalar entrywise estimate |J_R|<=epsilon does NOT give
`|c*(J_R o K_I)c| <= epsilon ||c||_2^2`.

Exact counterexample to that inference: K=11*, J_R=epsilon 11*, and
c=1/sqrt(M) times the all-ones vector. Then ||c||_2^2=1 while the quadratic
error is epsilon M. With epsilon=1/4000 and M=400 it is 1/10, already larger
than the entire allowed fourth-moment correction. This is a counterexample
to the abstract norm inference, NOT a counterexample to the actual prime
theorem. Equal or clustered phases explain the issue; a theorem exploiting
actual prime support and signs could still close it.

Likewise pointwise negative entries do not establish negative semidefiniteness.
The sharp Brownian min-kernel has a proven Gram representation. No analogous
Gram decomposition of the filtered remainder is supplied by these notes.

There is therefore no justified step multiplying g400, the half-word
fourth error, or a 26-term scalar supremum by the one-prime square mass and
calling the result Delta400. No positive lower bound proving margin
exhaustion follows either. The unknown weighted correction is the obstruction.

## 6. Arithmetic reduction at degree four: exact sectors versus nonexact ones

The exact filtered B4 expression in §1 can be collapsed, for each finite lag
path and sign population r versus 4-r, into

    sum_(u<=N^r, v<=N^(4-r)) a_r(u) conjugate(a_(4-r)(v))
        K_I(log(u/v)/L).

The coefficients include all fixed-lag Fourier factors and their phases.
The effective lengths are

| Sign populations | Lengths | Pooled length | Generic weighted Hilbert scale |
| --- | --- | --- | --- |
| 0 versus 4; 4 versus 0 | 1, N^4 | N^4 | N^2/T |
| 1 versus 3; 3 versus 1 | N, N^3 | N^3 | N^2/T |
| 2 versus 2 | N^2, N^2 | N^2 | N^2/T |

At N=exp(L-sqrt(L))=T^(1-o(1)), N^2/T diverges. The absolute central-cell
grouped estimate has an additional O(1+L) factor. The discrete alias estimate
in the fixed-R arithmetic-transfer note specializes to

    O_R((1+L)^5 [exp(-L/2)+N^2/T]).

These estimates do not close the long-scale residual. The exact nonzero alias
piece alone is negligible; approximate aliases are not closed by this bound.
An estimate that fails to vanish does not prove the contribution diverges.

Ordinary-prime exact equalities u=v occur only in the 2-versus-2 sector with
the same prime multiset. Distinct bases give the three pairings with opposite
orientations. Repeated bases have vanishing squared-pair mass. Exact closures
with proper powers are lower order by the prime-base valuation argument.
After this exact reduction the fixed-lag PNT/BV transfer gives the filtered
pair layer. Its existing finite-R formula is retained:

    Pair400 in
    [0.26632812189892278065, 0.26632812189892278067]
    < 266329/1000000.

This is not replaced by 4/15 and is not charged an extra g400.
The exact-pair reduction does not identify nonexact four-prime correlations
with a double-overlap cumulant. No use of prime-square PNT before that signed
reduction can justify the missing identification.

The old same-sign and 3-versus-1 gates also need their summed, filtered
versions. A uniformly small SINGLE-word trace is not a bound on the complete
weighted sum. Proper-power second mass similarly does not alone dispose of
all nonexact raw quartic products. They may be included in the single residual
theorem below rather than separately assumed away.

## 7. Complete quartic consumer ledger, with all errors exposed

Exact expansion about H=1+P gives

    P4(1+P) = 1/2000 + (9/1000)P + (213/1000)P^2
              - (51/100)P^3 + (593/2000)P^4.

Thus the commonly displayed three-term identity also consumes the first- and
third-moment gates. They are not automatically implied by the fourth bound.
Let |tau P|<=eta1, |tau P^3|<=eta3, tau P^2<=1/3+Delta2,
tau P^4<=0.266329+Delta4, and let etaBand be any ADDITIONAL charge beyond
the quoted full-to-band constant, etaRank any bounded-section charge. Then

    defect <= 0.15589863406625
               + (593/2000) Delta4 + (213/1000) Delta2
               + (9/1000) eta1 + (51/100) eta3
               + etaBand + etaRank + o(1).

For the frozen displayed ledger inputs Cmatch=2.1728342265 and
Erec=0.163249981456072, exact rational algebra gives

    old_defect = 124718907253/800000000000,
    old_margin = 3675673694911/500000000000000,
    old_simple = 275281092747/400000000000.

Treating displayed decimals as rational ledger inputs is not a new analytic
certificate of the full-to-band constant. Any rounding/certification correction
to that constant belongs to etaBand.

If Delta2, eta1, eta3, etaBand, etaRank are o(1), a certified Delta400 would
produce

    defect <= 0.15589863406625 + (593/2000)Delta400 + o(1),
    margin >= 0.007351347389822 - (593/2000)Delta400 + o(1),
    simple >= 0.6882027318675 - (593/1000)Delta400 - o(1).

The strict record test is exactly Delta400<3675673694911/148250000000000.
Equivalently the full fourth ceiling is 0.29112275173633052276...
under those same conditional inputs. This is a tolerance, not a certified
Delta400. No new simple-zero coefficient or surviving theorem margin can
be reported until the weighted correction is bounded.

## 8. Separate transport debts; no double charging

| Debt | Quantity | Current disposition |
| --- | --- | --- |
| Reprojection A to B | Repeated finite-band compression versus one compression of the infinite filtered fourth power | o_T(1) on the common good section by the b<=6 edge proof; NOT a sharp-filter error |
| Filtered arithmetic | Exact weighted B4 tuple correlations minus its exact-pair part and any DERIVED filtered connected ledger | OPEN at the retained long cutoff; includes nonexact products and near aliases |
| Filtered-to-sharp geometry | Difference of a SPECIFIED filtered connected ledger from the sharp Brownian/detuning ledger in its weighted norm | OPEN for the actual arithmetic state; §4 supplies certified operator/model diagnostics only |
| Endpoint trimming | Bounded rank deletion and, separately, endpoint feature mean-square error | Rank deletion o(1) CLOSED; sharp-feature endpoint estimate CONDITIONAL on representation and integrated norm |

One may either prove the arithmetic and geometry debts separately and add
them once, or bound their combined non-pair residual directly. One cannot
put the same residual in both columns and pay it twice. Nor can one assume
the arithmetic column vanishes because geometry is smooth.

The existing endpoint argument has consistent scaling once the claimed
feature representation is granted: U~T/sqrt(L), product length <=T^2,
integrated coefficient second mass O(1), sampled average O(T sqrt(L)),
then division by d'~TL yields O(L^(-1/2)). It does not construct the correct
filtered features. The original feature note exposes E's threshold factors,
while the commutator requires H=E/(z_i-z_j). A termwise representation of H
with the asserted summable multiplier and integrated second mass still needs
to be supplied; bounded entries of H are not such a representation.

## 9. Narrowest remaining theorem and promotion status

Define Pair4,T,R by the finite-lag pair contractions in the SAME convention as
B4, and put

    Residual4,T,400 = B4 - Pair4,T,400.

This is an unambiguous arithmetic definition, not a choice of cumulant
model. Its expansion includes every sign population, nonexact proper-power
term and alias after exact-pair subtraction. The narrowest sufficient primary
theorem, avoiding all unnecessary sharp cumulant identifications, is:

    On one admissible common selected section, prove
    limsup_(T->infinity) Residual4,T,400 <= Delta400
    for one certified Delta400 < 3675673694911/148250000000000,

with Pair4,T,400 <=0.266329+o(1), the first/third moment gates, and the
separate normalized consumer/zero-side assumptions in force. If targeting
only the balanced contribution, its bound must reserve explicit room for
all other unresolved sign/power/alias contributions. This formulation asks
for one upper bound, not a full fourth-moment asymptotic or the model -1/60.

The requested hostile promotion audit is conditional on first surviving the
finite-R repair. Survival has not been proved, so none of these four source
obligations is marked newly CLOSED:

| Obligation | Current boundary |
| --- | --- |
| Covariance normalization | Exact fixed-lag resonant covariance algebra and the rational pair formula checked; identification with the normalized selected Weil/prime matrix still required |
| Endpoint-feature second mass | Bounded individually specified pair features have O(1) mass; the actual filtered divided-difference family and its integrated norm are not derived |
| Full-to-band resolvent tail | The old quoted Cmatch/R input remains conditional here; this audit certifies the consumer algebra, not that analytic constant |
| Zero-side block and tail-Weyl transfer | Prior source audit reports these for the paper's Weil/Gabor matrix and corrects feature normalization; this note does not re-prove the source or its full prime-side match |

**Conclusion: OPEN at the first arithmetic/weighted-kernel interface, before
the margin-exhaustion decision.** The degree-four Fourier errors are real,
quantitatively certified and different from g400. They do not constitute
the actual coefficient-weighted connected correction. Neither an exhausted
margin nor a repaired unconditional 68.82% theorem is established.

## 10. Verification and preserved evidence

Run:

    python src/wp84_r400_filtered_sharp_repair.py --terms

Expected status:

    RESULT: EXACT_SCALAR_AND_DEGREE_FOUR_DIAGNOSTICS_PASS; ACTUAL_R400_REPAIR_OPEN

The verifier uses only Python's standard library and the existing exact
pair-layer helper. No prime data fitting, floating-point acceptance, crude
general b-word estimate, or public-candidate theorem is used. Its exact
assertions cover the polynomial coefficients, ledger fractions, pair bound,
26-term signs and classification, Fourier path count, selected independent
convolution checks, half-word moments and the abstract Gram norm obstruction.

The prior commits `908f6c2`, `d629e53`, `8ff09bc`, and `be7eee7` remain
ancestors on the same isolated branch. The six historical notes are preserved
as audit evidence; their old internal-closure headings are not new theorem
endorsements. This repair creates only this note and its verifier.
