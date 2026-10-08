# WP84 — actual filtered fourth row-cumulant kernel

Date: 2026-10-07. Filtered connected-kernel audit.
Fixed band R=400. This historical route remains conditional.

**CLOSED:** exact definition and coefficient measure for the actual filtered
connected fourth trace; its full 26-term cumulant; exact reduction to the
non-pair trace up to o(1) for the retained prime operator; interval-certified
positive and indefinite-kernel witnesses.

**FALSIFIED as a geometric shortcut:** negative Gram sign for this actual
kernel, and identification of its sharp version with the public double-overlap
Phi4 by an O(1/R) geometric error. A literal two-tail-coefficient necessity
also fails for the actual combined cumulant.

**OPEN:** the signed coefficient-weighted bound Delta400, the corrected consumer
margin, and unconditional R400 promotion. The route is NOT falsified. The
kernel witnesses are not arithmetic lower bounds: exact ordinary-prime
non-pair closures are impossible, and their proper-power representations have
negligible normalized mass. Near products and near aliases remain essential.

## 1. Define the connected quantity from the actual band matrix

Use the same infinite hard-band prime operator S_T,R and selected section I
as the parent repair. Write m=|I|, and let E_I mean the UNIFORM average over
the starting Fourier row k in I, not expectation over random primes.

For a closed lag path r=(r1,r2,r3,r4), |rj|<=R, sum rj=0, put
q0=0 and qj=sum_(a<=j) ra. Define four complex row variables

    X_j(k) = (S_T,R)_(k+q_(j-1), k+q_j).

The actual single-compression fourth trace is exactly

    B4,T,R = sum_(closed lag paths r) E_I[X1 X2 X3 X4].

The trace involves 342615201 closed lag paths at R400. That count is not used
as an unweighted error multiplier. The selected-section reprojection theorem
already gives A4,T,R=B4,T,R+o_T(1) for fixed R on the common good section.

Define the ACTUAL connected part by the classical joint row cumulant:

    Connected4,row(T,R,I) = sum_r cum_I(X1,X2,X3,X4).

This is a deterministic empirical cumulant of the actual matrix entries. No
continuum overlap, Gaussian assumption, or cumulant formula from the public
candidate is used in its definition.

## 2. The full 26-term combination, derived before any sharp substitution

For a subset B of labels {0,1,2,3}, put M_B=E_I product_(j in B) X_(j+1).
The cumulant is exactly

    M0123
      - M0 M123 - M1 M023 - M2 M013 - M3 M012
      - M01 M23 - M02 M13 - M03 M12
      + 2 M0 M1 M23 + 2 M0 M2 M13 + 2 M0 M3 M12
      + 2 M1 M2 M03 + 2 M1 M3 M02 + 2 M2 M3 M01
      - 6 M0 M1 M2 M3.

The combined coefficients 2 and -6 are the sums of anchored block orders.
Uncombining them gives exactly 26 terms: 1 term with one block, 7 with two,
12 with three and 6 with four. For each set partition pi, anchor the block
containing label 0, order the other blocks, and assign each order coefficient
(-1)^(|pi|-1). The verifier reuses the complete block ledger from the parent
exact script and checks both the counts and signs.

Crucially the block factors are products of EMPIRICAL MOMENTS. They are not
nested subset-path overlaps. Cumulant symmetry combines block orders into
the coefficients above; it does not generate a second physical interval.

## 3. Exact tuple kernel and exact arithmetic coefficient measure

Use c_n=-Lambda(n)/(a_phi L sqrt(n)), signed shifts
v_j=epsilon_j log(n_j)/L and S=sum_j v_j. Define J_v, V_v,R, and the
filtered external overlap exactly as in the parent note:

    Omega4,R(v) = integral_0^1 product_(j=0)^3
                  (F_R 1_Jvj)(x+p_j) dx,
    p0=0, p_j=sum_(a<j) v_a.

Let

    D_m(u) = m^(-1) sum_(k=0)^(m-1) exp(2pi i k u),
    kappa_m(v) = sum_(anchored ordered partitions pi)
                (-1)^(|pi|-1) product_(B in pi) D_m(sum_(j in B) v_j).

This is the same complete 26-term expression of §2 with
M_B=D_m(sum_(j in B)v_j). Define the unambiguous actual filtered kernel

    Phi4,R,m(v) = Omega4,R(v) kappa_m(v).

It depends on the row count m as well as R. Removing m without proving a
weighted arithmetic limit would lose the 1/m-scale resonance windows.

Define the complex atomic arithmetic measure

    mu_T,I = sum_(n_0,...,n_3<=N; epsilon_0,...,epsilon_3=+,-)
             (product_j c_nj)
             exp(i T L S) exp(2pi i k_- S) delta_(v_0,...,v_3).

Then, at FINITE T and FINITE R, exactly

    Connected4,row(T,R,I) = integral Phi4,R,m(v) dmu_T,I(v).

Proof: cumulants are multilinear. In the lag-path entry expansion each
variable contains exp(2pi i k v_j) times a k-independent prime coefficient,
carrier and fixed-lag phase. Block moments therefore supply D_m of the block
sum. Every partition carries the same exp(2pi i k_- S) and exp(iTLS).
Summing the four external Fourier coefficients over sum rj=0 gives Omega4,R.
No merged translation or second physical overlap is introduced. All sums are
finite, so the rearrangements are algebraic.

For nonclosed v the kernel can be complex. A useful REAL convention absorbs
the common midpoint phase into the measure:

    d_m(u) = sin(pi m u)/(m sin(pi u)), with its continuous integer limits,
    kappa_m(v) = exp(pi i(m-1)S) kappa_m^0(v),
    kappa_m^0(v) = sum_pi sign(pi) product_B d_m(sum_B v_j),
    Phi4,R,m^0 = Omega4,R kappa_m^0,
    dmu_T,I^0 = exp(pi i(m-1)S) dmu_T,I.

On S=0 both conventions agree and are real. The measure remains complex;
pointwise kernel positivity is not a lower bound on its arithmetic integral.

## 4. Exact relation to the non-pair fourth trace: singleton terms are o(1)

Rearranging §2 gives the exact identity, path by path,

    E_I product_j X_j
      = cum_I(X1,X2,X3,X4)
        + M01 M23 + M02 M13 + M03 M12
        + sum_(four 1+3 splits) M_single M_triple
        - 2 sum_(six 1+1+2 splits) M_single M_single M_pair
        + 6 product_j M_single.

The retained cutoff N<=exp(L-sqrt(L)) is used here. For each fixed-R edge
field, elementary coefficient summation gives

    sup_k |X_j(k)| = O_R(sqrt(N)).

The exact geometric sum for one signed prime-power frequency, using
log 2<=log n<=L-W and W->infinity, gives

    |E_I X_j| = O_R(sqrt(N)/T).

Indeed |D_m(log n/L)|<=C/[T min(log n,L-log n)]<=C/T; the fixed-lag
interval coefficient is bounded, and sum |c_n|=O(sqrt(N)) even from the
crude Lambda(n)<=log n bound. Phase factors have modulus one. This estimate
is uniform over the admissible selected section.

Linear-polynomial mean square and discrete sampling give

    E_I |X_j|^2 = O_R(1),

because N/T->0, h log N=O(1), and the coefficient square mass is bounded.
Thus Cauchy--Schwarz gives |M_triple|=O_R(sqrt(N)) and |M_pair|=O_R(1).
The summed singleton remainder, with fixed R FIRST, is consequently

    O_R(N/T + N/T^2 + N^2/T^4) = o_T(1).

It follows that

    B4,T,R = Pair4,T,R + Connected4,row(T,R,I) + o_T(1),
    Pair4,T,R = sum_r [M01 M23 + M02 M13 + M03 M12].

The fixed-lag second-covariance/PNT theorem reduces this exact pair expression
to Pair_R. Only second moments are transferred at this step. The existing
finite-lag formula and rational certificate remain

    Pair400 < 0.266329.

Combining with selected-section reprojection gives, for the retained prime
operator in this normalization,

    A4,T,400 = Pair400 + integral Phi4,400,m dmu_T,I + o_T(1).

This closes the DEFINITION/IDENTIFICATION gap for an actual empirical kernel.
It does not identify this integral with a fixed continuum connected model,
nor prove that it is nonpositive or below the consumer allowance. Corrected
Weil/prime identification is a separate source obligation.

## 5. The actual kernel does not preserve the sharp Brownian Gram sign

If v has rational denominator q dividing m, then exactly

    D_m(sum_B v_j) = 1 if sum_B v_j is an integer, 0 otherwise.

Consider the balanced closed vector

    v = (1/5, -2/5, 3/5, -2/5), S=0.

No proper nonempty block sum is an integer. Therefore the FULL COMBINED
26-term actual cumulant is kappa_m(v)=1, for every m divisible by 5. This
does not approximate or discard any partition term.

The interval-certified actual filtered kernel values are:

| R | Certified Phi4,R,m(v) enclosure |
| --- | --- |
| 10 | [0.39100467639596503, 0.39100467639596505] |
| 20 | [0.39530546591821454, 0.39530546591821456] |
| 50 | [0.39805030463291987, 0.39805030463291989] |
| 100 | [0.39900912356790413, 0.39900912356790415] |
| 200 | [0.39949975594800223, 0.39949975594800225] |
| 400 | [0.39974848084713831, 0.39974848084713832] |

These are positive witnesses, NOT supremum upper certificates. Among balanced
interior closed rational vectors on a common denominator grid, denominator 5
is the first possible positive non-pair cumulant: exhaustive exact enumeration
of the grids q=2,3,4 rules out smaller ones. In ALL sign populations a smaller
denominator-4 witness is (1/4,1/4,1/4,-3/4), with cumulant 1. The certificate
also checks its R400 filtered overlap is positive. No claim about the smallest
description among arbitrary real displacements is made.

The minimum-denominator statements concern positive ROW CUMULANTS on these
grids, not a global minimum-denominator theorem for the filtered kernel:
a negative cumulant times a negative overlap would need a separate check.
The displayed denominator-4 and denominator-5 positive kernel witnesses are
rigorously certified without that stronger minimality claim.

For the fixed-scale Gram test, define C_R,m(P,Q) by summing all six balanced
interleavings of Phi and AVERAGING over the two internal orderings of each
factor pair (equivalently one quarter of the 24 labeled orders). This is a
Hermitian pair kernel by trace-adjoint symmetry. The arithmetic coefficient
sum already ranges over ordered pairs, so replacing the kernel by its internal
ordering average does not multiply that sum by four. Filtered translations
need not commute; the sharp identity C24=4 C6 is not assumed here. At
product scale 4/5, choose

    P=(1/5,3/5), Q=(2/5,2/5).

The diagonal cumulants are exactly 0 for (P,-P) and -1 for (Q,-Q). The cross
cumulant is 1. The R400 cross kernel is certified in

    [1.59849868969065119, 1.59849868969065120].

Hence the two-state connected kernel has the form

    [[0, c], [c, h]], c>0,

and determinant -c^2<0, independently of h. It is indefinite. All four
internal ordering combinations are retained by the interval certificate.

The SAME test fails in the SUPERCRITICAL domain of
WP84_FIXED_SCALE_CONNECTED_KERNEL. Take

    P=(2/5,4/5), Q=(3/5,3/5), s=6/5.

Again the diagonal cumulants are 0 and -1 and the cross cumulant is 1.
The R400 six-word cross entry is certified in

    [0.39950281400985174, 0.39950281400985176],

with determinant in

    [-0.15960249840179020, -0.15960249840179019].

Thus negative semidefiniteness of the actual filtered cumulant matrix fails
even after all six interleavings are combined. No representation of its
negative as a covariance kernel with nonnegative spectral coefficients can
hold on this full displacement domain. The sharp Brownian depth covariance
is not a stationary convolution in s-t in the first place; Fourier banding
the matrix entries is not truncating a spectral expansion of that depth
covariance.

The witnesses persist as m->infinity without restricting m to multiples of
5, since each noninteger proper block average tends to zero. They therefore
are not an artifact of a small Fourier section.

These exact displacements admit proper-power realizations (for example use
log p/L=1/5), not distinct ordinary-prime non-pair equalities. Unique
factorization prevents the latter. The witness disproves a geometric sign
theorem, not the signed arithmetic upper bound or the R400 consumer route.

## 6. Reconnaissance over the displacement cube and its boundary regimes

The script searches R=10,20,50,100,200,400, with seed 7962400 and m=1000000.
For each R the recorded run tested 671 closed points: random points over the
whole closed cube |v_j|<1 (all sign populations), plus structured equal-scale
chambers, subcritical/supercritical slices, nearly zero steps and boundary
depths. It also tested 1012 nonclosed points: random cube points and explicit
windows S=integer+delta/m, including near aliases and physical detuning.

Floating positive maxima FOUND on the closed samples were respectively

    0.9829792970, 0.9854860416, 0.9910135495,
    0.9945663469, 0.9939788370, 0.9945147374.

These are reconnaissance lower observations, not rigorous supremum values
or exhaustive coverage of a continuous domain. The interval certificates in
§5 are the rigorous sign decisions. The nonclosed search uses the real
midpoint-phase convention; the omitted carrier remains in mu_T,I^0 and may
change the arithmetic sign.

An analytic observation explains the near-one values. At every fixed R,
take v=(1/q,-2/q,3/q,-2/q), m a multiple of q, and q->infinity. All proper
block averages vanish for q>4, so kappa_m=1. Each filtered interval tends
uniformly to the full indicator because R is fixed, hence Omega4,R->1.
Therefore the supremum of the positive actual kernel over the full family
of admissible row counts and closed displacements is at least 1, for EVERY
R. Positive actual cumulants are not a small O(1/R) perturbation of a
pointwise nonpositive model.

## 7. Tail cancellation: separate the correct sharp limit from the model

The sharp limit of the ACTUAL row kernel is

    Phi4,infinity,m(v) = O_A(v) kappa_m(v).

It is not the public connected kernel O_A(v) B4_nc(v). At the denominator-5
subcritical witness above, the first is exactly 2/5 while the second is
zero. The actual filtered values tend to 2/5 as R->infinity. Consequently

    Phi4,R,m - Phi4_public_sharp

cannot obey a uniformly vanishing C/R or C log(R)/R bound on this domain.
The discrepancy remains nonzero even without filtering. It is an arithmetic
model-identification issue, not an interval Fourier tail.

For comparison to the CORRECT actual sharp kernel, expand each external
interval Fourier series. The frequency tuple

    (401, -399, -2, 0)

has total Fourier displacement zero and exactly ONE coefficient beyond R400.
At v=(1/5,-2/5,3/5,-2/5) all four interval coefficients are nonzero; the
combined 26-term cumulant multiplying this Fourier monomial is exactly 1.
Thus connected Möbius cancellation does not force every retained error term
to contain two literal |n|>R tail coefficients. A second large comparable
frequency may occur below the cutoff; that is a different statement.

This refutes the proposed necessity, not every possible improved O(1/R)
estimate. No sharp coefficient-weighted O(1/R) or O(log R/R) bound is proved
here. The old uniform word-convergence result does show the correct external
filtered overlap tends to O_A for fixed displacements. It cannot identify the
different arithmetic cumulant with B4_nc.

A rigorous combined-cumulant scalar envelope, avoiding an unweighted 26-word
bound, is available. For unit-modulus row variables Z_j, put mu_j=E Z_j.
One has

    E|Z_j-mu_j|^4 <= 1+2|mu_j|^2-3|mu_j|^4 <= 4/3.

Holder bounds the centered four-product by 4/3; the three covariance products
are each at most one in modulus. Thus |kappa_m|<=13/3. For an interval
filter, ||f_R||_infinity<=G_R=1+2H_R/pi and
||f_R||_2^2<=|J|. Holder therefore gives

    |Phi4,R,m| <= (13/3) G_R^2 product_j |J_vj|^(1/4).

This is a uniform scalar envelope, not the least possible supremum and not
a practical consumer bound. It is NOT inserted as Delta400.

## 8. Cross-scale anchor and endpoint commutator

The old sharp decomposition is Csharp=-Gsharp+Esharp, with
|Esharp|<=dist(s-t,Z) and Esharp(s,s)=0. It cannot be reused for the actual
row-cumulant kernel. At the supercritical witness s=t=6/5,

    Gsharp(P,Q)=2(1/5) min(1/5,2/5)=2/25=0.08,
    Cactual,R400(P,Q) in [0.39950281400985174,0.39950281400985176].

Adding the old anchor produces an actual residual in

    [0.47950281400985174,0.47950281400985176],

despite zero product-scale detuning. It is not bounded by torus detuning.
With z_i=exp(2pi i s_i), the entry (z_i-z_j) is zero here, so no bounded
divided difference H can represent this nonzero residual as
H o [Z,K]. The rank-two commutator identity for K itself remains exact; its
application to THIS residual fails at the identification/divisibility step.

This already disposes of the proposed inherited detuning decomposition before
any cross-scale optimization. A different decomposition exploiting the signed
prime measure might still work. The existing sharp endpoint charge is not
added to a second copy of this residual. Bounded endpoint-row deletion and
reprojection remain separate o(1) operations.

## 9. What degree four closes arithmetically, and what still does not

Degree four is simpler than five/six for exact sectors: ordinary-prime exact
equalities are pairings, and only second-covariance/PNT transfer is needed
for their Wick contribution. Singleton terms in the row cumulant decomposition
are negligible by §4. This is a genuine degree-four simplification.

It does not shorten the remaining balanced product length: its two sides
reach N^2. At N=exp(L-sqrt(L)), N^2/T diverges. Weighted Hilbert/mean-square
control of a quadratic product polynomial does not become o(1) merely because
the degree is four. Near-alias products also survive the available generic
bound. The sign-balance theorem gives a single-word spacing estimate, not a
complete aggregate estimate. Current-prime carrier closure in bounded
resolvents does not supply an upper bound on this raw quartic cumulant.

The exact coefficient measure in §3 is not the PNT product measure
product s ds. Its total variation, on the complete tuple sum, is

    ||mu_T,I||_TV = (2 sum_(n<=N) |c_n|)^4
                  ~ 256 N^2/(a_phi^4 L^4).

Thus neither the scalar supremum in §6 nor the scalar envelope in §7 can be
multiplied by an O(1) prime-square mass to produce Delta400. The phase and
product correlations in this actual complex measure must be used.

The exact-kernel identity is CLOSED. A transfer to, or upper bound by, a
fixed filtered continuum model remains OPEN. The narrowest required theorem
now has no ambiguity about which kernel or measure it means:

    Re integral Phi4,400,m(v) dmu_T,I(v) <= Delta400 + o_T(1),
    with certified Delta400 < 3675673694911/148250000000000,

uniformly on one admissible common selected section, with all proper-power,
unbalanced, and alias contributions included unless separately bounded.
Proving this single signed upper bound would suffice; a full model moment
asymptotic is not needed.

## 10. Consumer insertion and remaining source obligations

No coefficient-weighted Delta400 is certified in this note. The scalar
witnesses greater than 0.35 or near 1 cannot be treated as lower bounds for
Delta400. Therefore they do NOT establish margin exhaustion.

If the theorem in §9 closes and the old first/third, variance, band and
normalization gates remain valid, the exact consumer insertion is

    w400 <= 0.266329 + Delta400 + o(1),
    quartic <= 0.1504665485 + (593/2000)Delta400 + o(1),
    full-to-band charge = 2.1728342265/400 = 0.00543208556625,
    defect <= 0.15589863406625 + (593/2000)Delta400 + o(1),
    record ceiling = 0.163249981456072,
    margin >= 0.007351347389822 - (593/2000)Delta400 + o(1),
    conditional simple coefficient >= 0.6882027318675
                                        - (593/1000)Delta400 - o(1).

These use the same frozen displayed ledger inputs as the parent note; an
analytic rounding correction to Cmatch belongs in the separate band debt.
No corrected numerical percentage or surviving theorem margin is asserted.
The route remains OPEN, rather than classified as numerically exhausted.

Separate obligations retained:

1. covariance normalization and corrected Weil/prime identification;
2. integrated second mass of any NEW actual endpoint-feature representation;
3. certified full-to-band resolvent tail with the matched consumer constant;
4. zero-side block, interval and tail-Weyl transfer for the same full matrix;
5. selected-section first/third moment gates used by the centered quartic.

The prior source audit's zero-side results and normalization correction are
preserved, not independently re-proved here. Positive kernel witnesses cannot
promote or refute the zero-side theorem. No unconditional percentage claim
is made.

## 11. Independently replayable verification

Run:

    python src/wp84_r400_filtered_connected_kernel.py --certificate
    python src/wp84_r400_filtered_connected_kernel.py --search --samples 400 --seed 7962400

The certificate uses mpmath interval arithmetic at 35 decimal digits. The
interval FFT is an explicitly implemented radix-two inverse DFT with interval
trigonometric roots and interval butterfly operations. The quadrature grid has
M>4R, so its average is EXACTLY the constant coefficient of each four-factor
trigonometric polynomial. There is no unresolved quadrature remainder or
floating-grid supremum claim. Acceptance requires strict positive interval
bounds and negative determinants; failure raises an exception.
The recorded runtime used mpmath 1.3.0 and NumPy 2.5.3. Optimized Python
(`-O`) is explicitly rejected before certificate execution so assertions
cannot be silently disabled; that failure path was checked.

The rational Möbius checks and minimum-grid-denominator checks use Fraction.
An independent finite band-entry cumulant calculation checks the tuple kernel
identity numerically (R1, five rows, two signed frequency pairs); its observed
discrepancy is about 2.6e-18. This diagnostic supplements the exact algebra
in §3, not the interval certificate. The search is explicitly labeled floating
reconnaissance and never supplies a supremum acceptance test.

Expected certificate status:

    RESULT: ACTUAL_ROW_CUMULANT_SIGN_COUNTEREXAMPLE_CERTIFIED; WEIGHTED_DELTA400_OPEN

All parent audit commits and both parent repair files remain unchanged. Only
this note and the new verifier are added. No push, merge, rebase, or modification
of main or Downloads is performed.
