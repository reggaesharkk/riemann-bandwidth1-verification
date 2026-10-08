# Direct deterministic-prime scalar-field state law

Research-route note. Historical Git references are intentionally omitted from
this clean publication copy.

**Decision D — DIRECT PRIME-STATE ROUTE BLOCKED at the dependent-phase
smooth comparison, with a favorable Gaussian consumer value also uncertified.**
This is a proof obstruction, not a counterexample to convergence. The new
finite-lag theorem below CLOSES the nonlocal approximation gate. Consequently
C is not the decision. B would overstate the result: a CLT alone, without a
certified favorable Gaussian value, does not establish the consumer ledger.
The master/characteristic route is permanently circular and is not used.

## 0. Frozen target, constants, and surviving reductions

Let c=3142/2415, a=131/200, z=c+ia, eta=(c^2+a^2)^(3/2), and

    P(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3,
    Q_cons(A)=eta P(A)(A-zI)^(-3),
    f(x)=eta^2 P(x)^2/((x-c)^2+a^2)^3.

Exactly Q_cons* Q_cons=f(A), 0<=f<=E_inf, and f(x)>=1 for x<=0.
The positive factor has displacement rank at most six; it is NOT itself
a rank-six matrix. The frozen constants are

    E_inf=7761139416076220170204368647089/
          1680256283972002400160000000000,
    w0=1415/13891,
    epsilon=21/200-w0=8711/2778200.

The unprojected finite-noise energy is E_u=E tau f(A+sqrt(u)W).
Its one-sided tail cap costs nothing additional. The telescope uses its
Hermite energies S_32(U)-S_32(delta), rather than asserting their equality
to the unprojected energy difference. For delta=1/100000, the exact lower
Mehler witness O=lambda0 I+sum lambda_j T_rho_j and upper witness I give

    F_T = lambda0 B_(U,1)+sum_j lambda_j B_(U,rho_j)-B_(delta,1)
          <= S_32(U)-S_32(delta),
    B_(u,rho)=Re E tau(Q_cons(A+sqrt(u)W1)^* Q_cons(A+sqrt(u)W2)).

The pair covariance is [[C_ref,rho C_ref],[rho C_ref,C_ref]]. The eight
rho points and all nine signed rational coefficients are copied verbatim
into the certificate. No equality of the weak-dual lower bound and projected
energy is claimed. U is some FIXED finite parameter, not a certified tuple.

CLOSED reductions surviving circularity: scalar-background trace-norm
replacement at fixed poles; exact sharp scalar/displacement representation;
cubic rational consumer and positive-energy support/cap certificates;
rank-two resolvent and rank-six consumer identities; coupled three-wedge
and K2 Gram identities; grouped prime-base cube remainder and its
leave-one-out/common-state bookkeeping; current-prime resonant PNT/BV and
fast-channel covariance substitutions in their established scopes; fixed-dual
Gaussian noise-covariance transfer; all-n Mehler weak dual; exact
adjoint/flux telescope; paid initial layer; frozen zero-side bounded-consumer
transfers. None of these is a deterministic-prime nonlinear state law.
The source-level scope and qualifications in the cited predecessor notes
remain in force. The synthetic geometric benchmark is not theorem evidence.

## 1. Scalar-field-only target

Use the authoritative scale from WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER:

    L=log(T/(2pi)), X=e^L, N=floor(X exp(-sqrt(L))),
    d=floor(TL/(2pi)), tau_k=T+2pi k/L,
    c_n=-Lambda(n)/(a_phi L sqrt(n)), n=p^v<=N,
    Q_T(tau)=sum_n c_n exp(i tau log n),
    xi_k=Q_T(tau_k), chi_k=Q_T'(tau_k)/L.

Keep all retained powers in the deterministic mean. Define directly

    a_k=Im xi_k, beta_k=2Re xi_k-2Im chi_k,
    J_ij=1/(pi(j-i)) (i!=j), J_ii=0,
    M(xi,chi;alpha,h)=s0(T)I+diag(beta+h)+[diag(a+alpha),J],
    C(xi,chi;alpha,h)=eta P(M)(M-zI)^(-3).

Thus B_(u,rho)=Re E d^(-1)tr(C1* C2), with noises sqrt(u)(alpha,h)
having the stated joint covariance. This specifies F_T entirely in terms
of Q_T, Q_T'/L, J and fixed consumer/noise parameters. The noise covariance is

    C_alpha,alpha(r)=1_(r=0)/(4 a_phi^2),
    C_alpha,h(r)=0,
    C_h,h(0)=1/(6 a_phi^2),
    C_h,h(r)=-1/(2 a_phi^2 pi^2 r^2), r!=0.

Its finite restrictions are positive semidefinite spectral Grams. s0(T)->1
and a_phi->1. Their already-paid transfers are not counted again.

## 2. Exact cancellations before localization

For a real symmetric scalar Loewner sample, D=diag(k), R_z=(M-zI)^(-1),
u_j=R_z^j 1 and v_j=R_z^j(a+alpha), the source law gives

    [D,R_z^k]=-pi^(-1) sum_(j=1)^k
                     (u_j v_(k+1-j)^T-v_j u_(k+1-j)^T).

Polynomial division gives Q_cons=eta sum_(k=0)^3 b_k R_z^k, with
b0=p3, b1=p2+3zp3, b2=p1+2zp2+3z^2p3, b3=P(z).
The triangular Hankel matrix with rows (b1,b2,b3),(b2,b3,0),(b3,0,0)
couples the three wedge pairs. Do not bound these pairs separately.
For W_k=-pi[D,R_z^k], the exact K2 contraction is

    sum_(i!=j) conj(W_k,ij) W_l,ij/(i-j)^2
       =pi^2 sum_(i!=j) conj(R_z^k,ij) R_z^l,ij.

The analogous mixed-copy identity holds. The diagonal contribution completes
the full signed bilinear trace. We use that completed trace for localization,
not a separately truncated wedge estimate.

| Kernel / occurrence after reduction | Decay and qualification |
|---|---|
| J in the source | signed 1/r; bounded l2 operator, not absolutely summed |
| Positive wedge reconstruction | K2=1/r^2; squared-generator statistic |
| Gram after K2 cancellation | off-diagonal resolvent products; still nonlocal |
| D1 mixed-word cross displacement | S2, coefficients 1/r^2 |
| D2 two-generator reconstruction | S4, coefficients 1/r^4 |
| Diagonal statistic | zero lag but depends on a full inverse |
| Localized block consumer below | finite support in input lags |

Here S2(theta)=pi^2/3-pi theta+theta^2/2 on [0,2pi];
S4(theta)=pi^4/45-pi^2 theta^2/6+pi theta^3/6-theta^4/24.
The D1/D2 kernels describe the predecessor response reduction, not extra
terms to add to F_T. No non-summable absolute 1/|r| coefficient survives in
the error estimate below. Summable explicit generator kernels alone would
not have localized their propagated resolvent vectors.

## 3. CLOSED finite-lag theorem by translated block cuts

Set m=R+1. For each t=0,...,m-1, partition the integer lattice into intervals
on which floor((k-t)/m) is constant, intersected with [0,d-1]. Keep the two
possibly short edge blocks. Only NOW replace the two completed consumer
samples by their block diagonal restrictions. Do not pretruncate J or redo
the displacement identities for the cut matrices.

For i,j in the original section the exact probability of a cut, averaged
over t, is p_m(i-j)=min(1,|i-j|/m). The diagonal is untouched. For any real
scalar sequence v, write M_v=d^(-1)sum v_i^2. Then

    average_t ||cut_t[diag(v),J]||_(2,tau)^2
      =1/(pi^2 d) sum_(i!=j) p_m(i-j)(v_i-v_j)^2/(i-j)^2
      <=4 M_v/pi^2 sum_(r!=0) p_m(r)/r^2
      <=8 M_v (H_m+1)/(pi^2 m).                         (L1)

The last inequality uses sum_(r>m)r^(-2)<=1/m; H_m=sum_(r<=m)1/r.
This is a finite-matrix inequality, including edge blocks and all offsets.
It uses no pointwise bound on the prime field or its derivative.

The existing circular large-sieve proof gives

    M_a<=d^(-1)sum |Q_T(tau_i)|^2
       <=(1+O(N/T)) sum |c_n|^2=O(1),

uniformly in carriers and prime subsets. Since sum |c_n|^2->1/2, one can
take M_a<=2 eventually, with a_phi near one. If an all-admissible-T supremum
is desired, use C_*=sup_T M_a<infinity, absorbing any finite initial range;
no numerical height T0 or small-height cutoff prescription is claimed.

For noise amplitude u, E M_(a+sqrt(u)alpha)=M_a+u/(4a_phi^2).
The frozen bounds ||Q_cons||op<=C0=43/20 and Schatten-2 Lipschitz constant
C1=10 follow by the same finite resolvent/Cayley telescoping as their
operator bounds. Thus a bilinear trace changes by at most
C0 C1 times the sum of the two normalized HS sample errors.
Let Lambda_U=|lambda0|+sum |lambda_j| and

    h_m=8(H_m+1)/(pi^2 m).

The EXACT edge-aware, shift-averaged block functional F_(T,R) therefore satisfies

    |F_T-F_(T,R)|<=e_loc,prime(R),
    e_loc,prime=43 sqrt(h_m)
       [Lambda_U sqrt(C_*+U/(4a_phi^2))
                         +sqrt(C_*+delta/(4a_phi^2))].     (L2)

For a uniform-in-T constant replace a_phi in this envelope by any positive
lower bound a_min on the admissible height range (eventually a_min=1/2
suffices). This is uniform in T and O_(U,dual)(sqrt(log(R+1)/(R+1))). It is weaker
than O(1/R) but tends to zero and proves the requested localization property.
It pays the ACTUAL completed consumer, with all dual weights. It does not
assert that a four-cycle error equals a pair tail. Noise cross correlations
do not change (L1), which needs only the individual marginal masses.
For the infinite stationary Gaussian reference, the identical proof applies
with C_*=1/4 and a_phi=1, giving e_loc,Gauss. Both errors must be paid if a
finite-R reference is compared to a full Gaussian observable.

## 4. Explicit bounded smooth cylinder

Take K_T uniform on {0,...,d-1}, and

    X_(T,R)=(Re xi_(K+r),Im xi_(K+r),
             Re chi_(K+r),Im chi_(K+r))_(r=-R,...,R).

The prime formula defines exterior samples at every integer. They are NOT
wrapped modulo d. For j=0,...,m-1 use the m-site window [-j,R-j] around K;
its central site is j. Construct M_j and C_j from section 1 on that window,
freezing s0=1 and a_phi=1 in the cylinder definition,
with J restricted to those sites and stationary Gaussian covariance restricted
to the same window. Define explicitly

    b_(u,rho,j)(x)=Re E_noise (C_(j,1)(x)^* C_(j,2)(x))_(j,j),
    Phi_R(x)=1/m sum_(j=0)^R [lambda0 b_(U,1,j)(x)
                 +sum_l lambda_l b_(U,rho_l,j)(x)-b_(delta,1,j)(x)].  (P1)

This is one function of 4(2R+1) real coordinates. It retains useful independent
Gaussian noise. Summing central columns over each block recovers its trace.
The exact edge-aware Phi_(T,R,k) uses the corresponding short restriction
when a window hits a physical edge. For d>2R,

    F_(T,R)=E_K Phi_R(X_(T,R))+e_edge+o_T(1),
    |e_edge|<=4 Lambda_total E_inf R/d,
    Lambda_total=Lambda_U+1.                               (P2)

The o_T(1) here is only the fixed-R scalar/covariance parameter freezing:
the uniform consumer derivative bounds pay s0(T)-1, and finite-block
order-two Gaussian covariance interpolation pays a_phi^(-2)-1. It is not
an arithmetic comparison. Use 2 Lambda_total E_inf as the edge bound if d<=2R. Edge-aware localization (L2)
is genuinely uniform; replacing it by one T-independent cylinder (P1)
adds (P2), which vanishes at FIXED R as T->infinity. Do not claim that
sup_T R/d tends to zero. This distinguishes the two requested quantifiers.

The scalar-to-sample linear map has operator norm at most 6 from Euclidean
input coordinates: ||J||op<=1, ||diag beta||op<=2sqrt(2)||x||2 and
||[diag alpha,J]||op<=2||x||2. The bound also holds for every subwindow.
Let C_n bound the nth multilinear consumer derivative, with C0=43/20.
The certificate derives C1,...,C4 from exact outward Cayley bounds. For
n=1,...,4, uniformly in x,R,U,noise and dimension,

    ||Phi_R||infinity<=Lambda_total E_inf,
    ||D^n Phi_R||<=6^n Lambda_total
                         sum_(j=0)^n binom(n,j) C_j C_(n-j). (P3)

The gradient/Hessian bounds are n=1,2; prime Taylor comparison needs n=3.
The n=4 bound is recorded for possible smoothing, not silently required
by the existing Gaussian covariance transfer. Differentiation under the
Gaussian integral is justified by these deterministic envelopes.

## 5. Exact covariance of the random-index vector

Define I_j(r)=int_0^1 s^j exp(i2pi r s) ds. The candidate circular limit has

    E xi_i conj(xi_j)=I1(i-j),
    E chi_i conj(xi_j)=i I2(i-j),
    E xi_i conj(chi_j)=-i I2(i-j),
    E chi_i conj(chi_j)=I3(i-j),
    E xi_i xi_j=E xi_i chi_j=E chi_i chi_j=0.             (C1)

Divide all entries by a_phi^2 before its limit. At r=0,
I1=1/2,I2=1/3,I3=1/4. For r!=0 and t=2pi r,

    I1=-i/t, I2=-i/t+2/t^2,
    I3=-i/t+3/t^2+6i/t^3.                               (C2)

For complex U,V with zero pseudocovariance and C=E U conj(V), the real blocks
are Cov(ReU,ReV)=Cov(ImU,ImV)=ReC/2,
Cov(ImU,ReV)=ImC/2 and Cov(ReU,ImV)=-ImC/2.
These specify EVERY real covariance entry and derivative cross entry.
The spectral Gram construction establishes finite-dimensional PSD; the
one-site (xi,chi) complex Gram determinant is 1/72.
The resulting alpha=Im xi and beta=2Re xi-2Im chi exactly reproduce
C_alpha,alpha=delta/4, C_alpha,beta=0, and C_beta,beta=delta/6-K2/(2pi^2).
The circular symbol is s, or s/a_phi^2 at prelimit normalization.

These are also the deterministic random-index SECOND-MOMENT limits, not
only the covariance of independently randomized primes. For Hermitian
covariance, polarize the discrete large sieve: circular separation of
log n/L is >=const/(NL), so its Gram differs from identity in operator
norm by O(NL/d). Multipliers exp(i2pi r log n/L) and (log n)/L are bounded;
PNT gives the diagonal terms (C1). Means tend to zero by the finite
geometric sum bound, since retained frequencies stay away from 0 and 1
by at least const/L and W/L; sum |c_n|=O(sqrt(N)).

For pseudocovariance, use the exact finite kernel D_d(x)=d^-1 sum_(k<d)e^(i2pi kx).
Terms have frequency log(nm)/L. There is one possible interior alias at
nm=X=e^L, since nm<=N^2<X^2 exp(-2W). Outside nm in [X/2,2X],
|D_d|<=O(L/d), giving O(NL/d)=O(N/T), using |c_n|<=const/sqrt(n).
Inside that interval, group by the integer v=nm and use the elementary
divisor bound d(v)<=C_epsilon v^epsilon. The absolute contribution is

    O_epsilon(X^(-1/2+epsilon)
          [1+(XL/d)log X])=o(1), epsilon<1/2.          (C3)

Indeed |D_d(log v/L)|<=min(1,O(XL/(d|v-X|))); the nearest integer has bound
one and the others form a harmonic sum. Here XL/d is bounded. This handles
an EXACT alias as well, without dividing by zero. Extra derivative/lag weights
are bounded and do not change the estimate. Proper-power square mass is
O(L^-2); its sampled L2 norm tends to zero by the same sieve. Thus (C1)
is proved at order two. This is not the state-dependent D2 covariance
substitution, and it supplies no higher conditional-moment comparison.

## 6. Literature audit for THIS vector (searched 2026-10-07)

The averaging law here is a DISCRETE uniform trace index on [T,2T+o(T)]
with mesh 2pi/L. Normalization is log p/(L sqrt p), derivative multiplier
i log p/L, cutoff N=T^(1-o(1)), shifts 2pi r/L, dimension 4(2R+1).
No theorem below matches all these requirements.

| Primary theorem | Averaging / cutoff / coordinates / shifts / tests and rate | Applicability |
|---|---|---|
| [Bourgade, Proposition 3.1](https://arxiv.org/html/0902.1757#S3.SS2) | Continuous uniform omega in (0,1); arbitrary infinitesimal coefficients of bounded square mass; negligible weighted square tail above m_t with log m_t=o(log t); scalar projections give fixed vectors; weak convergence, no stated quantitative rate; derivative multipliers possible if assumptions hold | Closest general array theorem, FAILED tail hypothesis here |
| [Bourgade, Theorem 1.1](https://arxiv.org/html/0902.1757) | Continuous height; shifted log zeta, fixed finite vector; logarithmic variance normalization; near-axis/mesoscopic shifts; weak convergence; no derivative-coordinate claim | Different weights and normalization; not this prime field |
| [Roberts, Theorem 1, v2](https://arxiv.org/html/2212.01411v2) | Uniform [T,2T]; two log-absolute-zeta coordinates; shift separation (log T)^(-alpha), 0<alpha<1; normalization sqrt(log log T/2); Dudley bounded Lipschitz rate (log log log T)^2/sqrt(log log T); proof cuts primes at T^(1/(K' log log log T)) and smaller Y | Our grid is boundary alpha=1, coefficients/derivatives and discrete sampling differ |
| [Tudor, multidimensional Selberg/Stein estimates](https://arxiv.org/pdf/1601.02515) | Continuous uniform U in [0,1]; fixed vectors of normalized log-zeta/prime 1/sqrt p approximants; large or small shifts; Wasserstein/smooth estimates; logarithmic-normalization rates; no theorem for our derivative-weighted array | Stein machinery adaptable; stated variable and coefficient hypotheses do not establish ours |
| [Wahl, Theorem 1.1](https://arxiv.org/html/1201.5295) | Uniform [T,2T]; scalar sine sum with 1/sqrt p; cutoff exp(log T/M), M/log log T->infinity; locally uniform real characteristic-frequency mod-Gaussian convergence; not derivative vector | Bessel/Fourier proof mechanism adaptable; scale/weights incompatible |
| [Bourgade--Kuan, strong Szego theorem](https://arxiv.org/html/1203.5328) | Continuous uniform omega in (1,2); RH; fixed test-function zero statistics, scale 1<<lambda_T<<log T; Gaussian field under Fourier/regularity hypotheses; no quantitative rate asserted here | Our lambda_T~L~log T is microscopic boundary, not that mesoscopic theorem |

For Bourgade's general array theorem the failure is exact, already on the
single Q coordinate: if log m_T=o(log T), then

    sum_(p<=m_T) (log p)^2/(L^2 p)->0,
    sum_(m_T<p<=N) (log p)^2/(L^2 p)->1/2.

The factor 1+p/T does not repair a nonvanishing tail. This also explains
why the familiar Selberg shortening argument cannot preserve our covariance.
We do not differentiate a log-zeta CLT; convergence in distribution of
functions does not justify convergence of derivatives. No assertion that
the literature contains no other theorem is made; the audited matches fail.

## 7. Prime-level smooth replacement and its exact obstruction

For each ordinary prime p, the complex vector contribution at trace index K is

    V_p(K)=c_p exp(iT log p) exp(i2pi K s_p)
                  (exp(i2pi r s_p), i s_p exp(i2pi r s_p))_(|r|<=R).

Take its explicit real/imaginary components. A prime-base group includes
the analogous sum over powers p^v, with s=powers' logarithmic coordinate.
The entire contribution has deterministic norm <=const_R log p/
[L(sqrt p-1)]. Consequently its accumulated cube mass is O_R(L^-3).
For independent uniform circle phases, replacing these grouped variables
by independent matching Gaussian vectors incurs only
O(||D3 Phi_R|| O_R(L^-3)), using ordinary multivariate Taylor/Lindeberg.
Proper-power L2 deletion is also legitimate for this Lipschitz cylinder.
It is NOT legitimate to randomize the deterministic phases for free.

Choose any ordering and put Y_p(K,g)=the hybrid sum excluding the current
prime, with previously replaced Gaussian contributions. The exact Taylor
telescope, in real coordinates, contains

    A1_T,R=sum_p E [D Phi_R(Y_p) . V_p(K)],
    A2_T,R=1/2 sum_p E [D2 Phi_R(Y_p):
                                  (V_p(K)V_p(K)^T-Sigma_p)],
    E Phi_R(X_T,R)-E Phi_R(G_T,R)
               =A1_T,R+A2_T,R+O_R(L^-3).                (A1)

Here Sigma_p is the independent-circle covariance. Means/second moments
of the unconditional total vector are already controlled in section 5.
Y_p nevertheless depends on THE SAME K as V_p. Neither conditional
contraction in (A1) is shown to vanish. Taking absolute values only gives
first mass O(sqrt N/L) and second mass O(1), not o(1).
Our exact hostile test uses pairwise independent signs X,Y,XY: all means
and off-diagonal covariances vanish but E X Y (XY)=1. This illustrates the
invalid implication being rejected; it is not a counterexample made of primes.
Stein's method likewise needs a conditional regression/Stein-kernel error
estimate. No dependency graph with negligible total error has been supplied.

The precise remaining arithmetic sufficient theorem is, for every FIXED R
and the explicit fixed-U function (P1),

    A1_T,R+A2_T,R ->0,

or directly E Phi_R(X_T,R)-E Phi_R(X_R^G)->0. A full CLT is stronger than
necessary. We do not assert that it fails, or that high-product expansion
is unavoidable; we have exposed its unproved dependence-sensitive terms.

## 8. Resonances, aliases, and bounded-frequency smoothing

For a prime phase multi-index nu of finite support,

    omega_nu=sum_p nu_p log p/L=log(A/B)/L,
    E_K exp(i tau_K log(A/B))
      =exp(iT log(A/B)) D_d(omega_nu),
    D_d(x)=exp(i pi(d-1)x) sin(pi d x)/(d sin(pi x)).      (A2)

At integer x use D_d=1. Exact A=B corresponds to nu=0 after prime-base
valuation cancellation. Near resonances have dist(omega_nu,Z)<=1/d;
periodic aliases have log(A/B)=m L, m!=0, or approach these at that scale.
Nonresonant terms are bounded by min(1,1/(2d||omega_nu||)).
The two-coordinate pseudocovariance aliases were disposed of in (C3).
That divisor argument does NOT handle the response-weighted multi-prime
Fourier coefficients of Phi_R in (A1).

Keeping Gaussian convolution in (P1) yields smooth bounded tests. In the
relevant (alpha,beta) coordinates its finite-block covariance is positive
definite: the beta spectral density is the periodized positive polynomial
2s(1-s)^2, vanishing only at isolated endpoints, so no nonzero finite
trigonometric polynomial has zero energy. For rho<1 a common Gaussian
component of variance u rho C_ref smooths a common baseline; at rho=1 use
variance u C_ref. At delta use delta C_ref. On compact baseline truncations,
Gaussian convolution supports finite characteristic-frequency approximation.
In L2 Fourier language its multiplier is exp(-u rho xi^T C_ref xi/2)
for the common shift. The smallest finite-section eigenvalue may shrink
with R; no dimension-free positive lower eigenvalue is asserted.

Finite characteristic frequencies do not imply finite prime-phase harmonics.
Already exp(i xi . sum_p V_p(K)) has a Bessel product with unbounded phase
multi-indices. Truncating spatial input using the second-mass bound, then
approximating a bounded smooth test to accuracy epsilon, can use a finite
degree depending on epsilon,R. It does not make N^q/T small for that degree.
There is no demonstrated Fourier-coefficient weighted estimate removing the
near-resonance/alias terms of (A2). Smoothing helps the test class; it has
not closed the arithmetic dependence error.

## 9. Pinned public arithmetic machinery, audited only after (P1)

**PUBLIC CANDIDATE SOURCE — NOT ASSUMED CORRECT.**
Pin: JoshuaHKU/zeta-0.7947-reproduction,
d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8.
[paper.tex, product identity and W1--W3](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex).

The public object is an affine additive lock/cycle density with resolved
position coordinates. Our object (A2) is a multiplicative product-ratio
characteristic average on one discrete height grid.

| Mechanism | Classification for (P1)/(A1) |
|---|---|
| Product/autocorrelation identity | ADAPTABLE finite algebra, not a smooth comparison theorem |
| Complete multidimensional Parseval | ADAPTABLE bookkeeping after specifying phase measures and normalizations |
| Affine lock coordinates, CRT coincidence closure | INCOMPATIBLE as a direct theorem for log(A/B) aliases |
| Logarithmic cells, Siegel--Walfisz, Vaughan | ADAPTABLE single-prime factor estimates; conditional response coupling remains |
| Claimed factor-by-factor transport W1/W3 | INCOMPATIBLE as an established bound for the smooth nonlinear test (P1) |

No DIRECT theorem match is identified. The public face_parseval.py checks
a finite FFT identity; face_local_closure.py enumerates finite residue
classes; writeouts_verification.py tests selected cycle/shift families.
They do not evaluate our response-weighted characteristic sum or control
its phase-harmonic tail. Their source was inspected at the pinned commit.
No public headline percentage or connected constant enters our ledger.

## 10. Gaussian evaluation, independent replay, and limit order

The finite Gaussian target is COMPLETELY SPECIFIED: substitute a centered
circular vector with covariance (C1) into (P1), and integrate also the
independent, correlated Mehler noise already present in (P1).
This is a finite Gaussian integral of bounded rational resolvent factors,
with a positive semidefinite explicit covariance. It is not the old synthetic
geometric chaos model. Its value at a favorable FIXED U is unknown here.

One rigorously replayed, but deliberately NON-useful, enclosure is

    E Phi_R(X_R^G) in
      [E_inf (sum_(lambda_j<0) lambda_j -1),
                         E_inf sum_(lambda_j>0) lambda_j]. (G1)

Each column Mehler correlation is a Hilbert-space OU quadratic form, hence
nonnegative and at most E_inf; (G1) follows with exact rational signs.
The certificate gives both endpoints. This is a universal cap enclosure,
NOT a useful Gaussian quadrature certificate and NOT a reference lower
value satisfying the ledger. No Monte Carlo or uncertified decimal is used.
A narrow interval quadrature/Arb evaluation, a winning U, and independent
replay of that useful value remain obligations. No numerical stopping
criterion is met that would justify an unconditional claim or decision B.

There is also a nontrivial FINITE Gaussian diagnostic at R=0. Its initial
energy is exactly the one-dimensional integral of f(1+x) against
N(0,v), v=100001/600000. Outward interval Riemann integration on [-4,4]
with 4096 dyadic bins and the Gaussian Chernoff tail gives

    E f(1+sqrt(v)Z) in
       [58764149/200000000, 60589871/125000000].          (G2)

This coarse numerical theorem is not a favorable reference value. A separate
Fraction-only replay proves a simpler exact lower certificate, independently
of the interval engine: Sturm gives f(x)>=29/50 on [9/10,11/10]; on the
centered interval [-1/10,1/10] the normal density is >=97/103. Indeed
2pi v<(103/100)^2 using pi<22/7, and exp(-x^2/(2v))>=1-3/100.
Hence

    E f(1+sqrt(v)Z)>=2813/25750>21/200.                 (G3)

Since the weak-dual terminal energy is at most E_inf, the R=0 signed
Gaussian value for EVERY U is <=E_inf-2813/25750 and cannot reach the
consumer threshold. This is an independently replayed scalar obstruction,
not a proof of failure at R>0. Cutting all off-diagonal structure is not
an admissible extrapolation of this diagnostic to the full operator.

If the smooth comparison is proved, the only valid order is fixed R,
then T->infinity, then R->infinity using (L2) on both sides. There is no R(T).
No interchange or Gaussian evaluation is hidden in the covariance formulas.

## 11. Full exact consumer ledger

For a finite Gaussian lower enclosure g_(R,U), the sufficient margin is

    margin >= epsilon-[E_inf-w0-g_(R,U)]-53503/66000000
                  -e_loc,prime(R)-e_loc,Gauss(R)-e_compare(R)
                  -e_quad(R)-e_other,

where e_quad is zero if g is already a lower interval endpoint (do not pay
quadrature width twice), e_compare is zero asymptotically ONLY AFTER a proof
of (A1), and e_other includes any genuinely new nonvanishing transfer cost.
Physical edge loss is o_T(1) for fixed R. Existing background, covariance,
prime-power L2 and cube remainders retain their o_T(1) scopes. Endpoint and
zero-side frozen payments are already represented in the inherited cushion;
they are not waived. Weak-dual slack is intrinsic to g, not a second payment.
Adjoint/flux residual and additional physical large-u loss are zero by the
frozen exact telescope and scalar cap. Finite-lag approximation is a new,
separate error, not a second charge of any reprojection/geometry error.

Equivalently, any actual certified lower value l and total new error e must obey

    l-e > 83446820694177651440799215197979/
          18482819123692026401760000000000.

No l, favorable U, arithmetic error bound, or positive actual margin is
certified. Strict >79 remains OPEN. The exact cushion is unchanged.

## 12. Cross-archive methods and verification boundary

The available full-archive inventory and pinned provenance are in
WP84_CROSS_REPOSITORY_SOURCE_MANIFEST.json and the associated transplant
audit. Reused mechanisms: LRSC exact finite inequalities, weak dual and
independent rational replay; NS shell/boundary localization with vector
errors; Riemann rank-six/K2 cancellations and endpoint bookkeeping. Here
translated block boundaries are the new localization device; no NS viscous
estimate or LRSC reference energy is imported as arithmetic evidence.
There is no claim to have newly rerun all historical source archives.

Run:

    python src/wp84_direct_prime_field_state_law.py
    python src/wp84_mehler_weak_dual_certificate.py notes/WP84_DIRECT_PRIME_FIELD_STATE_LAW_CERTIFICATE.json
    python src/wp84_direct_prime_field_scalar_gaussian_replay.py

The first verifier checks exact translated-boundary counts, the squared
cut estimate with rational sequences, harmonic necessity in that estimate,
covariance recurrences and derivative Gram, a hostile conditional-dependence
example, rational derivative envelopes, all-n witnesses and the exact ledger.
The independent verifier replays those same witnesses without importing
our localization implementation. It also rejects corrupted witnesses.
These finite checks supplement the analytic proofs of (L1)--(C3); they are
not a deterministic-prime CLT or useful signed Gaussian integration result.

The producer additionally computes (G2) by directed interval arithmetic.
The separate scalar replay reconstructs the polynomial using Fraction-only
operations and checks its interval Sturm root count, the density bound and
(G3), without importing SymPy, mpmath, the producer or its quadrature.
The broad all-R cap enclosure (G1) and scalar diagnostic (G2)--(G3) do not
certify the unknown useful signed expectation at positive R.

The first obstruction to the proposed prime replacement is precisely the
conditional first/second response in (A1), not a surviving absolute Hilbert
tail. Even closing it would still require a favorable certified Gaussian
value before the strict >79 consumer could be declared closed.
