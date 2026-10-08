# WP84 strict >79: hostile audit, balanced-pair reduction, and a necessary saving

2026-10-08. This publication copy omits private branch and commit references.
No packet alteration, push, main change, history rewrite, or PR merge.

**Result:** the preceding collision removal passes in its stated *unsplit*
scope. Its section transfer is a valid conditional implication, not an
unconditional sixth-norm estimate. New arithmetic and norm arguments reduce
the remaining signed gate to all-distinct words and one **balanced** pair
with distinct singleton slots. Inequality (12) remains OPEN. An exact lower
bound on its actual filtered pair main term proves that a null-residual
argument cannot reach its cap: a negative residual exceeding
`0.0020583781807554428...` is necessary. No such saving is proved here.

## A. Proof audit and unconditional new results

### A1. Source and normalization are kept intact

Write X=T/(2*pi), L=log X, N=floor(exp(L-sqrt L)), h=2*pi/L,
d=floor(TL/(2*pi)). Use the original coefficient
c_m=-Lambda(m)/(a_phi(T)*L*sqrt m), a_phi(T)->1, and every m=p^v<=N.
R=6000 throughout. The root section is I=[a,a+n-1], n/d->1. There is no
shortened prime pool, new row stencil, frequency mask, or replacement kernel.
The source-normalization hypothesis on a_phi is explicitly inherited.

For each closed ordered displacement word ell, |ell_j|<=R, sum ell_j=0,
q_0=0, q_j=sum_(t<=j)ell_t, put s_m=log(m)/L and

    rho=max(0,n-max(q)+min(q)), i_min=a-min(q),
    f_0^eps(s)=1-s,
    f_l^+(s)=(1-exp(2*pi*i*l*s))/(2*pi*i*l),
    f_l^-(s)=conjugate(f_l^+(s)), l!=0,
    lambda=sum_j eps_j log(m_j),
    W=prod_j c_(m_j) f_(ell_j)^(eps_j)(s_(m_j))
        *exp(2*pi*i*sum_j eps_j*q_(j-1)*s_(m_j)),
    K(lambda)=exp(i*T*lambda+i*h*i_min*lambda)/n
                  *sum_(r=0)^(rho-1) exp(i*h*r*lambda).

The compressed trace is exactly sum W*K. Boundary root restrictions stay in
rho and i_min for each original b-word even after slots are contracted.
If lambda=mL+delta, delta in [-L/2,L/2), the kernel is
exp(i*T*mL)*exp(i*(T+h*i_min)*delta)/n*sum_r exp(i*h*r*delta).
The carrier exp(i*T*mL) is never discarded. All periodic aliases and tails
are therefore present. Constants below may depend on fixed R and degree;
they are asymptotic estimates, not uniform numerical error payments at T.

### A2. Independent audit of the preceding global removals

For an equality block of multiplicity nu and signed charge e, its field is
Z(t)=sum_(p<=N) a_p exp(i*e*t*log p), |a_p|<=C_R |c_p|^nu.
The elementary coefficient estimates are

    sum |c_p|^2=O(1), sum |c_p|^nu=O(L^-nu) (nu>=3),
    sum |c_p|^4=O(L^-4).

For e!=0 the logarithmic frequency separation is at least |e|/(N+1).
Continuous Hilbert/mean-square estimation on the actual interval, followed
by cellwise |Z(grid)|^2 <= (2/h)*integral|Z|^2+2h*integral|Z'|^2, gives

    avg_rho |Z|^2 <= 2*(1+4*pi^2*e^2)
                 *(1+2*pi*(N+1)/(|e|*rho*h))*sum |a_p|^2.

Here rho*h~T, N/T->0; differentiation uses |e log p|<=|e|L.
This estimate treats the whole sampled correlation, including aliases.
Singleton fields have L2=O(1); unbalanced pair fields have L2=O(L^-2)
and supremum O(1); balanced pair fields are static O(1). A singleton's
signed mean is O(sqrt(N)/T), since log p stays away from 0 and the first
alias L by the natural cutoff. Derivatives of fixed-band coefficients
do not enter these time estimates: they are constant at each prime.

Thus multiplicity >=3 with at most two singleton blocks is o(1): bound
the heavy field absolutely and use Cauchy-Schwarz for two singleton fields.
Fifth-order two-pair-plus-singleton words are o(1): use an unbalanced
pair L2 and singleton L2, or two static pairs and the singleton mean.
Sixth three-pair words with a charged pair are o(1), by that pair's L2
and the other pairs' supremum bounds. All-balanced three-pair words give
the exact filtered main term; higher exact repeated blocks are o(1).
Restoring pairwise block-prime distinctness by partition inclusion-exclusion
only merges blocks into the already bounded populations. This verifies
the prior census: 1312 closed fifth classes, 7688 closed sixth classes
(including 200 previously closed lower exact classes), 120 sixth exact
three-pair classes, and respectively 352/5184 previously open classes.

**Scope limitation:** this is not a theorem for arbitrary frequency-masked
pieces. Splitting a positive/negative sum into near-alias windows before
factorization can destroy these estimates. No per-mask claim is used here.

### A3. New unconditional removal: balanced 2+2+1+1

Both pairs have charge zero, so their independently summed prime fields
are time-independent O(1). Keep the two remaining singleton primes distinct.
Their degree-two off-diagonal correlation is o(1), uniformly for the actual
bounded slot weights and original root kernel. Here is a direct proof that
includes the potentially dangerous first alias.

For opposite signs and p!=q, in |log(p/q)|<=1 the kernel bound is
C/(T*|log(p/q)|)<=C*sqrt(pq)/(T*|p-q|). Multiplying the coefficients
gives C/(T*|p-q|); summing over all integers up to N costs O(N log N/T).
Outside that window no alias is within distance 1: |log(p/q)|<=L-sqrt L.
The kernel is O(1/T) and the coefficient l1-product costs O(N), since
|c_p|<=C/sqrt p. This contributes O(N/T).

For same signs put u=pq. Unique factorization gives at most two ordered
representations of each u; coefficient size is C/sqrt u. The only possible
near nonzero alias is log u=L. In |log(u/X)|<=1 the contribution is bounded
by

    C/sqrt X * sum_(u integer, X/e<=u<=eX)
                         min(1, C*X/(T*|u-X|))
       = O(L/sqrt X).

The nearest integer, including an exact alias if X is an integer, is bounded
separately by 1; the rest form a harmonic sum. The zero alias is separated
by log 4, and the second by 2 sqrt L. Away from the first alias use O(1/T)
and total coefficient mass O(N). Therefore the bound is

    O_R(N log N/T + L/sqrt X)=o(1).                 (A)

No cancellation of exp(i*T*L) is assumed. Opposite-sign p=q is explicitly
excluded; it would be an exact pair main term. Restoring distinction from
the two paired primes creates either multiplicity >=3 with <=2 singleton
blocks, or a three-pair collision; the singleton-same-prime term was already
excluded. The remaining merges are covered by A2. Consequently the entire
balanced 2+2+1+1 population is unconditionally o(1), including aliases.
This closes 45*16=720 more raw ordered sign/equality classes.

### A4. Actual matrix bounds, without an unconditional sixth-norm assertion

For ordinary primes let Y be the real Hermitian hard-band source matrix.
With tau_i=T+h*i, its actual entries are

    alpha_i=Im sum_p c_p exp(i*tau_i*log p),
    beta_i=2 Re sum_p c_p*(1-log p/L)*exp(i*tau_i*log p),
    Y_ii=beta_i, Y_ij=(alpha_i-alpha_j)/(pi*(j-i)),
                          0<|j-i|<=6000.

For each slot, summing its two orientations gives exactly
Y_(i+q_(j-1),i+q_j). This is a source identity, not a free Gaussian field.
Put t=||Y||_(6,n). For each fixed slot and its allowed root range,

    avg_i |Y_(i+qprev,i+qnext)|^6 <= tau_n(Y^6)=t^6. (B)

Indeed |Y_uv|^2<=(Y^2)_uu, and spectral Jensen implies
(Y^2)_uu^3<=(Y^6)_uu. The row map is injective and remains in I.
Products of k slot entries therefore have L_(6/k) norm at most t^k.

An unbalanced pair, after summing its ++/-- orientations, has supremum O(1)
and L2=O(L^-2). Interpolation gives L3=O(L^-4/3). A triple block has
supremum O(L^-3). Holder on the original root range yields

    fifth unbalanced pair + 3 singletons: O(L^-2*t^3),
    sixth unbalanced pair + 4 singletons: O(L^-4/3*t^4),
    sixth two pairs, >=1 unbalanced + 2 singletons: O(L^-2*t^2),
    sixth triple + 3 singletons: O(L^-3*t^3).        (C)

For the third line use pair L_(3/2)<=L2, other pair L-infinity, and the
two-entry product L3. For the first/fourth use the three-entry product L2.
Prime-distinctness corrections are legitimate: merging a charged pair with
a singleton creates the controlled triple population; merging two singleton
blocks creates the controlled two-pair population; all subsequent merges
are A2. The original charged pair cannot become balanced unless it is
merged, in which case it belongs to those larger blocks. No uncontrolled
balanced-one-pair term is generated by these corrections.

These estimates require the **complete singleton orientation sum first**.
They do not bound each complex sign class separately. They also do not
assert t=O(1) without an arithmetic gate. This distinction matters.

## B. Noncircular gate reduction and good-section transfer

### B1. Self-bounding proves the additional removals for bounded gates

Let A=11501/12500, B=137641/250000 and
J_full=tau_n(BY^6-AY^5). Pointwise

    Bx^6-Ax^5 >= (B/2)|x|^6-C,
    C=(A/6)*(5A/(3B))^5.                           (D)

For x>=0 set z=x/(5A/(3B)); the difference divided by C is
5z^6-6z^5+1=(z-1)^2*(5z^4+4z^3+3z^2+2z+1)>=0.
For x<0 the assertion is immediate. Thus U=J_full+C>=0 and
t^6<=2U/B. Let J_red retain the exact pair main term, all-distinct fifth
and sixth words, and **balanced** one-pair words with 3/4 singletons.
A2, A3, C give

    |J_full-J_red| <= e_T*(1+U^(2/3)), e_T->0.       (E)

Lower powers of t are absorbed into 1+t^4. If J_red<=K for large T, then
U<=K+C+e_T+e_T*U^(2/3). The exact Young bound

    e*U^(2/3) <= U/2+16e^3/27                     (F)

follows by maximization, attained at U=(4e/3)^3. It implies
U<=2(K+C+e_T+16e_T^3/27), hence t=O(1) and E=o(1).
Conversely an upper bound on J_full gives t=O(1) directly by D and again
E=o(1). Therefore the original and reduced bounded strict signed gates are
equivalent. This is stronger than removing these populations by *assuming*
a sixth-moment estimate; it closes that apparent circular implication.

The resulting raw-class census is fifth 192 (32 all-distinct and 160
balanced-pair), sixth 544 (64 all-distinct and 480 balanced-pair).
These are labels of retained summands, not 736 independently estimated
near-alias correlations. New C removals operate on orientation groups.

Proper powers are not silently omitted. Their complete band matrix V has
||V||op=O_R(1), ||V||_(2,n)=O_R(L^-1), from the natural-cutoff power
coefficient sums and the same sampled linear estimate. Interpolation gives
||V||_(6,n)=O_R(L^-1/3). Telescoping trace powers and Schatten Holder
give o(1) between complete and ordinary-prime gates if either gate is bounded
above, by D and the triangle inequality. Combined with F, this remains a
valid bounded-gate equivalence. It is not disposal of every masked power
correlation individually.

### B2. A legitimate hidden-pair PNT reduction

For paired slots a,b on the original closed path define

    phi_ab(s)=2 Re[f_(ell_a)^+(s) f_(ell_b)^-(s)
                         *exp(2*pi*i*(q_(a-1)-q_(b-1))*s)],
    k_ab=integral_0^1 s*phi_ab(s) ds.               (G)

Both orientations of the balanced pair give exactly
sum_p c_p^2 phi_ab(log p/L), which tends to k_ab by the existing
prime-square PNT measure theorem. The natural upper endpoint
1-1/sqrt L tends to 1. These are the actual finite Fourier coefficients,
not sharp interval overlaps. Fixed R leaves finitely many bounded-variation
tests. Restoring/removing exclusions between this hidden prime and visible
singletons costs A2/C (a collision creates a triple).

The distinct-singleton 3/4-fold correlation has averaged absolute size
O_R(1+t^3) / O_R(1+t^4): use partition inclusion-exclusion, B for the
singleton product, supremum O(1) for paired contractions and O(L^-3) for
triple contractions. This proves that replacing the hidden-prime sum by G
costs delta_T*(1+t^4), delta_T->0; it fits the bootstrap E/F. PNT is used
only after this signed/product reduction. It cannot replace the remaining
weighted singleton correlation with an unweighted scalar moment.

This yields a source-exact reduced residual F_T: sum over the original fifth
and sixth closed paths/root kernels, with weights -A and B, of (i) the
all-distinct ordinary-prime word and (ii) for every chosen slot pair its
k_ab times the distinct 3/4-singleton correlation. Sum every singleton
orientation; retain original q, root range, f, carrier, and all aliases.
In a bounded gate,

    J_full = B*Pair6_6000 + Re F_T + o(1).          (H)

There are no fifth exact ordinary-prime closures. Unique factorization
forces all charges zero, impossible in odd total degree. Sixth exact
three-pair closures alone supply Pair6_6000; 4+2 and 6 are already o(1).

### B3. Section audit: a sufficient implication, not missing source data

For a canonical matrix Y_d and any deletion r=o(d), put Z=PYP embedded in
dimension d. Compression contracts every Schatten norm, rank(Y-Z)<=2r,
||Y-Z||_(6,d)<=2||Y||_(6,d). Telescoping b powers and Schatten Holder give

    |tau_d(Y^b-Z^b)| <= 2b ||Y||_(6,d)^b
                         *(2r/d)^((6-b)/6), 1<=b<=5.

The rank factor follows by converting the defect's sixth norm to its
6/(7-b) norm. For b=6 only tau_d Z^6<=tau_d Y^6 is required. Consequently

    J_(d-r)(Y_I) <= d/(d-r)*[J_d(Y)
                     +10A ||Y||_(6,d)^5*(2r/d)^(1/6)].

A bounded full gate supplies the norm by D, without assuming its strict
numerical cap. For the source r/d=O(L^-1/2), loss is O(L^-1/12)=o(1).
Endpoint scores may select any admissible common good section in those
quarantine windows. A uniquely specified historical determinant selector
is not required by this implication; none is invented. The aggregate
A-to-B reprojection error remains the existing good-section theorem.
No per-mask trace-compression claim or two-sided sixth stability is used.

The first unproved higher arithmetic step is an upper bound on Re F_T with
a strict negative saving. The current canonical norm/section implication
does not provide that bound. The inherited scalar third-moment aggregate,
source normalization and zero-side/full-to-band transfer assumptions remain
separate conditional consumers. In particular scalar mu3=o(1) does not
discharge all path-weighted three-singleton terms in G. No zero theorem is
promoted from a model coefficient or a determinant rank.

## C. Exact falsifiers and independent certificate

### C1. Source-matched obstruction to the null-residual route

The already reduced exact pair main term is the stationary Gaussian Wick
trace with Cov(alpha_i,alpha_j)=delta_ij/4,
Cov(beta_i,beta_j)=1/6 on the diagonal and -1/(2*pi^2*(i-j)^2) otherwise,
Cov(alpha_i,beta_j)=0, and W_ij=(alpha_i-alpha_j)/(pi*(j-i)) for band edges,
W_ii=beta_i. This represents only the exact paired contraction sum, not the
full law of the source matrix. The covariance is positive: it is the prime-
square integral of the original sine/cosine slot features. For example the
beta covariance is 2*integral_0^1 s*(1-s)^2*cos(2*pi*k*s) ds;
the alpha-beta sine integral vanishes by s->1-s symmetry.

Pinch this R=6000 matrix into consecutive blocks of nine sites. Schatten
sixth contraction, stationarity, and vanishing boundary fraction give
Pair6_6000 >= E tr(W_9^6)/9. All its off-diagonal block edges are included
because 8<=6000. This is a lower-bound calculation on the exact main term;
it neither changes R nor selects nine prime-source rows.

The 531441 closed vertex walks and their 15 Wick pairings give the exact
polynomial p(x), x=1/pi^2, with positive coefficients

    [5/72,
     288223/403200,
     3189863194981/663828480000,
     2749260640878247123/156132458496000000].

Using pi<22/7 therefore gives the strict lower bound

    Pair6_6000 > p((7/22)^2)
       = 31498340500050746323/150466924118016000000
       = 0.2093373057546228... .                    (I)

An independent exact replay uses recursive Wick contraction of 40191
distinct commuting edge multisets instead of the producer's direct 15
pairings. Rational alternating-series Machin bounds independently certify
333/106<pi<22/7. No floating-point integration is used. The nine-site
polynomial's upper enclosure is NOT an upper bound on Pair6_6000.

### C2. Hostile norm examples and limits of this audit

In dimension d=t^30 take a diagonal matrix with one eigenvalue t^5.
Its normalized sixth moment is 1, yet deleting one row changes that moment
by 1. Thus bounded sixth norm plus o(d) deletion does not imply two-sided
sixth stability. Its fifth loss t^-5 does vanish, agreeing with B3.
With eigenvalue t^6 instead, the fifth loss is 1 and sixth moment t^6:
rank deletion alone does not prove even fifth stability.

On t^2 sample sites let a pair field be 1 on one site and zero elsewhere,
and each of four singleton fields be t on that site and zero elsewhere.
The pair has L2=1/t and supremum 1; singleton L2 norms equal 1. Their
averaged product is t^2, not o(1). Small pair L2 plus only singleton L2
does not close the unbalanced sixth one-pair term. Bound C uses the actual
matrix sixth norm and F supplies a legal bounded-gate bootstrap.

These matrices/fields are explicit counterexamples to general proof steps,
not claimed prime-source counterexamples. The null-residual budget test
I/D below is source-matched. No synthetic row is used to prove H or the gate.
The independent tests also reject shortened cutoff, R=400, discarded
carrier/powers, per-sign promotion, and a claimed completed signed theorem.

## D. Smallest remaining joint inequality and exact margin

Preserve the original rational consumer:

    A=11501/12500, B=137641/250000,
    Jstar=64788151489666079/572357731837500000,
    frozen reference margin
       M=52897896569489/572357731837500000
        =0.00009242103954753147... .

The reduced, equivalent bounded-gate task is precisely

    limsup Re F_T <= Jstar-B*Pair6_6000-eta,
                         eta>0.                  (J)

This retains the joint fifth/sixth budget and the actual filtered pair main
term. The frozen 1/36,34/135 reference values remain budget references and
are not promoted to arithmetic moment identities. By I a necessary condition
for J is a negative residual of magnitude strictly exceeding

    g9=B*p((7/22)^2)-Jstar
       =43770221409581023769108432686241
          /21264421581420459982848000000000000
       =0.0020583781807554428...,

in addition to eta. The exact sufficient cap is still Jstar-B*Pair6_6000;
g9 is only a necessary minimum saving. If Re F_T=0+o(1), then the source
pair term alone exceeds the cap by at least g9. Thus disposing of every
nonexact word as negligible is a concrete failed method for this consumer.
The two retained sectors can have either sign; no positivity or Gaussian
cancellation is presumed. Current mean-value bounds give no negative signed
saving there, so the analytic attack stops at J rather than declaring >79.
Conditional on J and the independently inherited lower/source/zero-side
gates, the existing consumer yields .79+2eta-o(1). That conclusion remains
conditional; no new zero-proportion theorem is claimed.

## Reproduction

Run `src/wp84_strict79_balanced_pair_reduction.py` to produce the new JSON,
then `src/wp84_strict79_balanced_pair_replay.py`. Both use only the Python
standard library. The replay does not import the producer. The JSON pins
input source bytes and git blobs, preserves the preceding packet byte hashes,
records the orientation-group scope, and explicitly leaves inequality (12)
and strict >79 false as proof-status flags. Symbolic combinatorics and
constants are certified; the analytic arguments above are proofs to audit,
not numerical tests of the full natural-cutoff arithmetic object.
