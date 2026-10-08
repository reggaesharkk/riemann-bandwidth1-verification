# WP84 — weighted fixed-band reprojection on selected principal sections

Date: 2026-10-06. Fixed-band reprojection theorem.

Status: **CLOSED weighted b=5 and b=6 reprojection to filtered words on a
selected principal section; OPEN original-endpoint and sharp-model transport.**

This note closes a narrower bridge than an equality to the public sharp
overlap kernels. It preserves the true displacement band R before taking
T to infinity. It never sums prime-word absolute errors with coefficient
l1 mass. No fifth/sixth moment theorem or zero-proportion theorem is claimed.

## 1. Exact weighted object and assumptions

Let L~log T, d=floor(TL/(2pi)), h=2pi/L, and

    c_n=-Lambda(n)/(a_phi L sqrt(n)),  2<=n<=N<=exp(L),
    Q(t)=sum_(n<=N) c_n exp(i t log n),
    alpha_i=Im Q(T+h i),
    beta_i=2 Re sum_(n<=N) c_n(1-log(n)/L) exp(i(T+h i)log n).

The coefficients include ordinary primes AND proper prime powers, with
Lambda(p^k)=log p. Assume a_phi stays bounded away from zero and tends to 1.
The PNT prime-square measure and absolute convergence of the proper-power
square sum give

    M=sum_(n<=N)|c_n|^2=O(1).

For primes this follows from sum_(p<=N)(log p)^2/p=O(log^2 N); proper powers
contribute O(L^-2), since sum_(p,k>=2)(log p)^2/p^k converges. This is only
second-mass control; no high-moment power deletion is inferred from it.

Choose epsilon_L=L^(-1/2), q=floor(epsilon_L d), and require

    N/(q h) -> 0.

The previously available adaptive endpoint quarantine N<=T exp(-sqrt(L)+o(1))
implies this condition. The theorem concerns the retained SHARP prime state;
quarantine transfer to it occurs first at a bounded consumer, as in the source
notes. Any additional coefficient weights require the corresponding second
mass bound and log-frequency support; they are not silently discarded.

Fix R and b0=6. Extend the hard-band prime matrix to Fourier indices i,j in Z:

    (A_R)_(ii)=beta_i,
    (A_R)_(ij)=(alpha_i-alpha_j)/(pi(j-i)), 0<|j-i|<=R,
    (A_R)_(ij)=0 otherwise.

This equals the sum of the band-filtered signed partial translations
V_(epsilon log n,R) from WP84_FOURIER_REPROJECTION_BRIDGE_AUDIT. Its finite
compression on any index interval I is the actual hard-band matrix X_(R,I).

## 2. CLOSED: exact weighted b=5 / b=6 error expression

For I=[k_-,k_+] of length d', P=P_I and Q_I=I-P_I, define

    E_(b,R)(I)=d'^(-1) tr((P A_R P)^b-P A_R^b P), b=5,6.

Exactly,

    E_(b,R)(I)
      = -d'^(-1) sum_(j=1)^(b-1)
                    tr(P A_R P ... P A_R Q_I A_R^(b-j) P).

There are j prefix copies of A_R. Equivalently,

    E_(b,R)(I)
      = sum_(n_1,...,n_b<=N) sum_(epsilon in {+,-}^b)
          [product_j c_(n_j)] exp(i T Y)
          d'^(-1) tr(
             P V_1 P ... P V_b P - P V_1 ... V_b P),

    V_j=V_(epsilon_j log n_j,R), Y=sum_j epsilon_j log n_j.

These are finite weighted prime / prime-power expansions with the actual
band and carrier. They are the requested fifth/sixth reprojection errors to
the correctly FILTERED single-compression words. Replacing V_j by U_j on the
right is an additional fixed-R error, which this theorem does not close.

## 3. CLOSED: generic mean square controls only linear fields at the edges

The classical Montgomery--Vaughan inequality for distinct real frequencies
with minimum separation delta gives, on any interval of length U,

    int |sum_n a_n exp(i t log n)|^2 dt
      <= (U+2pi(N+1)) sum_n |a_n|^2.

Indeed delta>=log(1+1/N)>=1/(N+1), and Theorem 2 / Corollary 2 of
Montgomery--Vaughan, "Hilbert's Inequality", JLMS (1974), bounds the endpoint
cross terms by 2pi/delta. Arbitrary interval locations are handled by absorbing
their starting phase into a_n. Source:
[author-hosted original paper, pp. 74–75](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf).

For q grid samples with spacing h, the elementary cell inequality

    |S(t_k)|^2 <= (2/h) int_(cell k)|S(t)|^2 dt
                           +2h int_(cell k)|S'(t)|^2 dt

follows from the fundamental theorem of calculus and Cauchy--Schwarz, using
disjoint centered h-cells. The union has length qh. Since log n<=L,
the derivative coefficient second mass is at most L^2 times the original
mass. Thus the grid average is at most

    C_grid M,
    C_grid=2(1+4pi^2)[1+2pi(N+1)/(q h)].

For alpha^2+beta^2 use |Q|^2+4|Q_1|^2, where Q_1 has coefficients
c_n(1-log n/L). Its squared coefficient mass is <=M. Hence

    average_(q consecutive k) (|alpha_k|^2+|beta_k|^2)
      <= 5 C_grid M.

This bound applies to every fixed translate of a candidate endpoint window,
with the same constant. It uses the linear polynomial of length N, not a
product polynomial of length N^3. This is the difference from the unsuccessful
sharp connected-feature endpoint argument at fifth/sixth degree.

## 4. CLOSED: simultaneously good finite neighborhoods

Put m=2 b0 R=12R and define the endpoint score

    S(k)=sum_(t=-m)^m (|alpha_(k+t)|^2+|beta_(k+t)|^2),
    F=(2m+1)*5 C_grid M.

Average S over k in {0,...,q-1}, and separately over k in {d-q,...,d-1}.
Each average is <=F. Therefore endpoints k_- and k_+ exist in the respective
windows with S(k_-)<=F and S(k_+)<=F. They select a single common contiguous
principal section I, with d'>=d-2q and d'/d->1.

Since R,b0 are fixed, N/(qh)->0 and M=O(1), F=O_R(1). Both fifth and sixth
degrees use the SAME endpoints. Additional finitely many existing endpoint
scores may be accommodated by averaging their normalized sum, multiplying
F by a fixed constant; no incompatibility with the earlier selection is
being assumed away.

On these neighborhoods |alpha|,|beta|<=sqrt(F). Any relevant local principal
block of A_R has operator norm bounded by its maximum absolute row sum:

    K=sqrt(F)[1+4 H_R/pi], H_R=sum_(r=1)^R 1/r.

Both sites of every relevant entry lie inside a selected neighborhood.
No global operator norm bound on the prime matrix is asserted.

## 5. CLOSED: weighted trace error is a finite boundary-path sum

For b<=b0, a length-b path of bandwidth R starting more than bR away from
both ends of I never leaves I. Therefore its diagonal contribution to
(P A_R P)^b and P A_R^b P is identical. Only <=2bR root indices can differ.

For an exceptional root, every path lies within 2bR of one endpoint, so it
can be calculated inside that bounded local block. Each of the two diagonal
matrix-power contributions has magnitude <=K^b by functional calculus / the
operator norm. Consequently

    |E_(b,R)(I)| <= rho_b,
    rho_b = 4 b R K^b/d', b=5,6.

This is O_R(1/d')=o(1), and is a bound on the ENTIRE weighted prime sum.
The proof first groups all primes into the linear fields; it does not use
coefficient l1 mass or bound high prime products separately. Proper powers
are included without needing a sixth-moment deletion theorem.

**Scope:** weighted b=5 and b=6 reprojection to filtered words is CLOSED on
this selected section. It is OPEN at the original, unselected endpoints.
This note does not assert tau(X_(R,I)^b)=tau(X_(R,[0,d-1])^b)+o(1).
Such raw moment stability would require separate tail control.

Deleting <=2q rows is allowed at the bounded-consumer stage: embedding the
principal section with zero rows changes the full finite matrix by rank at
most twice the number removed. A bounded-variation consumer changes by
O(q/d)=o(1), including trace-normalization correction. Thus selected-section
moment bounds would still suffice for the zero-count consumer, even though
original-section raw moment stability has not been proved.

## 6. CONDITIONAL: insertion into the exact joint budget

Define the filtered single-compression moments

    nu_(b,R)(I)=d'^(-1) tr(P_I A_R^b P_I).

The CLOSED bridge says |mu_(b,R)(I)-nu_(b,R)(I)|<=rho_b. If future arithmetic
work proves

    nu_(5,R)(I)>=1/36-eta5-o(1),
    nu_(6,R)(I)<=34/135+eta6+o(1),

then eps5=eta5+rho5 and eps6=eta6+rho6 may be inserted into

    (11501/12500) eps5+(137641/250000) eps6
      < 52897896569489/572357731837500000.

The reprojection charge itself tends to zero at fixed R=6000, so it consumes
no limiting cushion. The arithmetic eta5/eta6, filtered-to-sharp error,
connected-sector matching, and selected-section lower-moment controls remain
OPEN. No values of eta5/eta6 inside the budget have been proved here.

## 7. OPEN: why this does not yet reconnect C5/C6 or promote R400

The exact single-compression object is built from phi_(y,R)=F_R 1_(J_y),
not from the sharp indicators. Consequently it has the filtered overlap
Omega_(b,R) of the deterministic bridge note. Its bulk differs from the
sharp overlap even as T->infinity at fixed R. That note preserves an explicit
closed-pair counterexample, including a positive gap at R=6000.

The public 150-term C5 sign theorem and 1082-term C6 kernel therefore cannot
be applied to nu_(b,R) without another identification / quantitative filter
transport theorem. The same issue occurs at R=400 before applying the sharp
Brownian connected-kernel and detuning formulas. The weighted finite-boundary
reprojection is repaired, but the connected-sign application is still OPEN.

## 8. Verification

The accompanying script checks the exact budget independently, verifies the
finite Fourier entries by direct integration, checks deterministic words
against the leakage bound, and checks the grouped finite prime-band error
against the boundary estimate. Numerical checks are diagnostics; the proofs
in Sections 3–5 establish the stated asymptotic selected-section result.

Only the new bridge statements are promoted to CLOSED. The >79 and R400
zero-proportion consequences remain CONDITIONAL / OPEN.
