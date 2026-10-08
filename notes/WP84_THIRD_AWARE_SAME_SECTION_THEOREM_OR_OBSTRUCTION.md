# WP84: same-section third obligation, exact tradeoff, and variance credit

2026-10-08. Same-section third-moment analysis.
This publication copy omits private branch and commit references. Four
artifacts are discussed. No push,
merge, consumer change, historical edit, rank/GUE route, or packet alteration.

**Result:** a same-section prime-matrix first/second-moment theorem is proved
below. Its sharper variance tail earns the exact defect-payment reduction

    156386774119/152831638033593750
       =0.0000010232617809450214... .

It raises the conditional reference margin to 0.00009344430132847649... .
Centered mu3=o(1) is unnecessary as a logical consumer premise, but no
source-legal estimate here proves even the weaker small upper bound.
The least restrictive sufficient arithmetic requirement is one **joint**
third/fifth/sixth signed gate. The third alias/tail sum remains OPEN. Source
identification and zero-side transfer remain separate obligations.

## 1. The frozen consumer with the actual third moment

Keep q(X)=-19101/185500+(961/3710)X+(31/50)X^2-(371/500)X^3,
and the bounded p_dag from the preceding referee report. Exactly,

    q(X)^2=c0+c1 X+c2 X^2+c3 X^3-A X^5+B X^6,
    c0=364848201/34410250000,
    c1=-18356061/344102500,
    c2=-26060119/430128125,
    c3=21981971/46375000>0,
    A=11501/12500, B=137641/250000.

The fourth coefficient is zero; no fourth-moment model is consumed.
For the SAME section and actual centered normalization write mu_j=tau(Y^j).
The exact untruncated polynomial identity retains every coefficient, including
c3*mu3. Under the independently specified source/band/zero interfaces, the
consumer defect is bounded by

    c0+c1*mu1+c2*mu2+c3*mu3-A*mu5+B*mu6
                       +e_band+kappa+o(1).         (1)

Here e_band=128952763/92407500000 is the frozen curvature payment at R=6000.
kappa>=0 denotes any additionally required normalized defect payment from
source/zero/tail transfer; it is a visible obligation, not an established
zero cost. If those interfaces prove only o(1) errors, kappa=0 is legal.
Strict >79 requires a limsup defect at most 21/200-eta for some eta>0.
Equality at the budget ceiling is insufficient. The usual .79+2eta simple-
zero implication is conditional on the block/index/count transfer, not a
consequence of (1) alone.

If mu1=o(1) and mu2>=1/3-delta_var+o(1), then c2<0 gives the sufficient gate

    limsup[c3*mu3-A*mu5+B*mu6]
         <= Jcap-kappa-eta,
    Jcap=21/200-c0-c2/3-e_band-|c2|*delta_var.       (2)

No fifth/sixth model value is inserted in this identity. The original
conservative delta_var=2*(106/333)^2/6000 recovers Jstar exactly. Section 3
proves a smaller actual source payment without altering the consumer.

## 2. Weakest one-sided third bound and the genuine joint budget

Suppose a theorem on the same section supplies
limsup(-A*mu5+B*mu6)<=H. Then the weakest **separate constant sufficient
upper bound** (for chosen eta and kappa) is

    limsup mu3 <= (Jcap-H-kappa-eta)/c3.           (3)

The sign c3>0 is decisive: no lower bound on mu3 is required. A negative
third contribution is favorable and must not be clipped away. Because H is
still unproved, there is no unconditional universal numerical third ceiling
that by itself establishes the consumer: the right side depends on the
actual fifth/sixth estimate and other payments. In particular neither
mu3=o(1) nor mu3<=0 alone closes (2).

For transparent bookkeeping define the SIGNED reference debits

    delta5=1/36-mu5, delta6=mu6-34/135,
    D56=A*delta5+B*delta6.

These are reference differences, not assumptions about zeta moments. With
the chosen variance payment, (2) is equivalently

    limsup[c3*mu3+D56] <= Mref-kappa-eta.          (4)

Positive-part clipping A(delta5)_++B(delta6)_+ is more restrictive. The
joint limsup in (4) is also less restrictive than adding separately proved
limsup ceilings: favorable third and fifth/sixth contributions may occur
together even if their separate suprema occur on different heights.
Both contributions must refer to the same T and same section. There is no
license to combine an existential third section with a different sixth one.

At the frozen reference inequalities mu5>=1/36-o(1), mu6<=34/135+o(1),
D56<=o(1). Only **conditionally on those still-open estimates**, kappa=0
and a strictly positive unused gap, mu3 need merely have upper limit below
Mref/c3. This allows a small positive third moment and is weaker than o(1).
It is not a proved small upper bound.

## 3. First and second moments: direct SAME-section source theorem

Let X=T/(2*pi), L=log X, N=floor(exp(L-sqrt L)), h=2*pi/L,
d=floor(TL/(2*pi)), R=6000. Retain all ordinary primes p<=N, coefficients
c_p=-log(p)/(a_phi L sqrt p), a_phi->1, and any contiguous I=[a,a+n-1]
with n/d->1. Endpoints may depend on T and on the fields. For the actual
prime matrix use the alpha/beta and Loewner entries from the referee note.

**Theorem.** Uniformly over these sections (with n/d->1),

    mu1(Y)=o(1),
    mu2(Y)=1/6+(1/pi^2)*sum_(r=1)^6000 1/r^2+o(1),
    avg_(i in I) alpha_i^2=1/4+o(1).              (5)

Proof of uniformity and nonexact disposal. The exact grid kernel is
exp(i*(T+h*a)*lambda)/n*sum_(j=0)^(rho-1)exp(i*h*j*lambda), with the
original path range rho=n-O_R(1). For a single prime, distance from the
zero or first periodic alias is at least log 2 in logarithmic units for
large T. The geometric bound is O(1/T), uniformly in the initial phase.
The coefficient l1 sum is O(sqrt N), so mu1=o(1).

For the quadratic expansion, nonexact opposite-sign p!=q terms near zero
are O(N log N/T), by |log(p/q)|^-1<=C sqrt(pq)/|p-q| and summing the
integer harmonic majorant; outside the central unit window they are O(N/T).
The natural cutoff excludes a near first alias in this ratio sector.
Same-sign products u=pq have at most two ordered representations. Near the
first alias u~X their coefficients are O(X^-1/2) and the kernel is bounded
by min(1,C X/(T|u-X|)). The nearest integer costs O(X^-1/2), including
an exact alias; the remaining integer sum costs O(L/sqrt X). Away from that
alias use O(N/T). The second alias is quarantined by 2sqrt L. These bounds
are independent of the initial phase, fixed displacements, and original
slot windows. All aliases and far terms are therefore controlled at degree
two; no continuous mean value replaces the grid.

On the exact opposite-sign p=q diagonal, prime-square PNT gives

    avg alpha_i^2 -> (1/2)*integral_0^1 s ds=1/4,
    avg alpha_i alpha_(i+r) -> (1/2)*integral_0^1 s*cos(2*pi*r*s) ds=0,
                           r any fixed nonzero integer,
    avg beta_i^2 -> 2*integral_0^1 s*(1-s)^2 ds=1/6.

The original natural endpoint log N/L=1-1/sqrt L tends to 1, and a_phi->1
is the stated source normalization. Thus each off-diagonal squared entry
at displacement r has average 1/(2*pi^2*r^2)+o(1). There are n-r entries
in each of the two orientations. Summing finitely many r<=6000 yields (5).
All error bounds were uniform in endpoints, so adaptive good-section
selection does not bias this theorem. The same proof gives q_alpha=1/4+o(1)
needed in the functional band theorem.

Complete prime powers are also present in the original matrix. Their linear
field coefficient second mass is O(L^-2); separated-frequency sampling
gives band-matrix normalized Hilbert-Schmidt norm O_R(L^-1). The coefficient
l1 sum is O(1), giving operator norm O_R(1). For first/second moments,
Cauchy-Schwarz with the bounded ordinary-prime second mass proves that
including this power matrix changes (5) by o(1), unconditionally on a
sixth bound. No frequency-masked higher power moment is disposed of here.

**Identification boundary.** Formula (5) is proved for the actual prime
matrix, not automatically for the centered normalized Weil/zero matrix.
If its SAME-section source representation is Z=Y+E with ||E||_(2,n)=o(1),
then |tau Z-tau Y|<=||E||2 and
|tau Z^2-tau Y^2|<=2||Y||2||E||2+||E||2^2=o(1). These suffice to transfer
the lower moments without a sixth assumption. The taper/ramp/background
and zero-side source theorem must supply that identification; the audit
does not invent it or infer it from the model.

## 4. Earned quantitative credit from the variance tail

Parseval for s-1/2 on [0,1] gives sum_(r>=1)1/r^2=pi^2/6. Hence (5)
is equivalently

    mu2=1/3-(1/pi^2)*sum_(r>R)1/r^2+o(1).

Convexity of x^-2 implies r^-2<integral_(r-1/2)^(r+1/2)x^-2 dx.
Summing r>R yields the strict majorant sum_(r>R)r^-2<1/(R+1/2).
Using pi>333/106 and c2<0 is therefore sufficient to pay

    e_var,new=|c2|*(106/333)^2/(6000+1/2)
             =208480952/203775517378125.

The original payment e_var,old=26060119/12734908593750 remains recorded;
their difference is the earned positive credit in the opening paragraph.
It comes from the SOURCE second moment, not a third/fifth/sixth signed gain
and not changing q, R, a_phi, or prime cutoff. Do not pay both variance
amounts: the new amount replaces the old one in the refined ledger only.

The independently replayed 6000-term rational harmonic sum is recorded by
its exact canonical Fraction hash; no enormous-prime numerical experiment
or extrapolation is used.

## 5. Third estimate sought: exact formula and current obstruction

For every original b=3 closed ordered displacement path |ell_j|<=6000,
q_0=0, q_j=sum_(t<=j)ell_t, rho=n-max q+min q, i_min=a-min q, put

    f_0^eps(s)=1-s,
    f_l^+(s)=(1-exp(2*pi*i*l*s))/(2*pi*i*l), f_l^-=conjugate(f_l^+),
    W=product_j c_(m_j) f_(ell_j)^(eps_j)(log(m_j)/L)
          *exp(2*pi*i*sum_j eps_j*q_(j-1)*log(m_j)/L),
    lambda=sum_j eps_j log(m_j),
    K_ell(lambda)=exp(i*(T+h*i_min)*lambda)/n
                         *sum_(r=0)^(rho-1)exp(i*h*r*lambda).

Then the COMPLETE prime-power third moment is exactly sum_(ell,eps,m)W*K.
At lambda=mL+delta the carrier exp(i*T*mL) remains; nothing at an alias is
silently converted to the zero-frequency diagonal. This is the source
object being estimated, with absolute Fourier root indices retained.

Use the previously proved repeated-base estimates, without reopening the
census: ordinary-prime pair+singleton sums and triple-base sums are o(1).
No exact ordinary-prime third closure exists by unique factorization. Let
D3 be the remaining all-distinct ordinary-prime sum. The one-prime-side
central theorem applies at degree three too, so its complete 1:2/2:1
central population obeys

    |D3_central| <= (2433429520896/7)
                           *N*(1+log(3N))/T=o(1).                (6)

This bound counts the six mixed sign placements, two ordered prime-product
representations, and at most 12001^2 closed paths. All-same-sign central
cells are empty. For the actual remaining third sum, mixed signs retain
their +/-first aliases; all-same signs retain +/-first and +/-second aliases;
every far/transition tail stays included. Thus

    mu3(Y)=Re D3_(nonzero aliases + tails)+o(1).    (7)

Proof of a small one-sided upper bound on (7) is the genuine missing theorem.
The degree-three generic sampled-product bounds scale like logarithmic
factors times N^(3/2)/T and do not vanish at the natural cutoff. That is
failure of an upper estimate, not evidence the actual moment grows.
Odd-degree exact-equality absence, conjugate pairing, and vanishing central
cells do not assign a sign to (7). No unsupported nonpositivity is used.

The source entry identity offers another exact check, but not a saving:
writing Y=diag(beta)+O with O diagonal-free,

    tau Y^3=avg beta_i^3+3*tau(diag(beta)*O^2)+tau O^3.

The mixed diagonal/off-diagonal and triangular terms must stay together.
The Loewner entry form alone has no sign theorem: alpha=(0,1,2), beta=0
on three consecutive sites gives off-diagonal entries -1/pi and
tau Y^3=-2/pi^3; negating alpha gives +2/pi^3. Equivalently alpha=pi*(0,1,2)
has cubic traces -2 and +2, checked exactly in the replay. These are counterexamples to a deterministic sign
shortcut, **not source-prime samples** or a falsifier of (7).

Under a bounded third-aware gate, coercivity controls the sixth norm:

    Bx^6-Ax^5+c3*x^3 >= (B/4)|x|^6-C-c3^2/B,
    C=(A/6)*(5A/(3B))^5.

This legitimizes complete power disposal for the joint bounded gate, and
third-moment transfer across o(n) row deletions, without assuming mu3=o(1).
In particular ||V_power||3=O_R(L^-2/3) and bounded ||Y||3 make the complete
power third error o(1). Small row deletion changes tau Y^3 by
O(||Y||6^3*(r/n)^(1/2)). These are conditional norm consequences, not
a canonical third estimate. C_ab->k_ab likewise remains valid under this
coercive joint gate.

There is a rigorous but insufficient conditional one-sided estimate:
Holder gives |mu3|<=mu2^(3/4)*mu6^(1/4). If the still-open actual sixth
ceiling mu6<=34/135+o(1) holds, (5) gives

    limsup mu3 <= (34/3645)^(1/4) <0.32.

The bound lies between 0.31 and 0.32, far above the necessary separate
reference allowance near 0.000197. It cannot repair the missing third input.
No unconditional small one-sided bound or o(1) theorem is obtained here.

## 6. Joint target, reference sensitivities and explicit numerical ledger

| Payment or cap | Original ledger | Refined same-consumer ledger |
|---|---:|---:|
| bounded functional band payment | 0.0013954794037280523... | unchanged |
| variance-deficit payment | 0.0000020463530466790872... | 0.0000010230912657340656... |
| Jcap | 0.11319520622473271... | 0.11319622948651366... |
| conditional reference margin | 0.00009242103954753147... | 0.00009344430132847649... |
| conditional third ceiling, zero D56/kappa/eta | 0.00019497913581165092... | 0.00019713789423651305... |

The exact refined constants are

    Jcap,new=51835308978310574561/457924342652122500000,
    Mref,new=8558084052085891/91584868530424500000,
    U3,new=8558084052085891/43411664130988764996.

U3,new is the equality boundary, not itself a strict >79 theorem. For a
positive eta and extra cost kappa subtract (eta+kappa)/c3 from the ceiling.
With a proved upper D56=d, the following boundaries illustrate (3):

| Signed fifth/sixth debit d | Third upper boundary, kappa=eta=0 |
|---|---:|
| -0.0001 | 0.0004081062373391402... |
| 0 | 0.00019713789423651305... |
| 0.00001 | 0.00017604105992625034... |
| 0.00005 | 0.0000916537226851995... |
| 0.0001 | -0.000013830448866114084... |

These are conditional tradeoffs, not claimed prime values. A positive
third ceiling is unavailable if uncompensated debit/cost reaches Mref,new.

For the preceding arithmetic representation let F_remaining be the reduced
fifth/sixth signed sum and Pair6_6000 its exact filtered three-pair term.
Then the refined source-matched single target is

    limsup Re[c3*D3_(aliases+tails)+F_remaining]
       <= Jcap,new-B*Pair6_6000-kappa-eta.          (8)

This restores the original third coefficient and allows joint compensation.
Using the proved pair LOWER bound, the necessary joint saving magnitude is

    g9,new=15909857470864664470267332031322977
              /7733161315109907280429056000000000000
           =0.002057354918974498...,

plus kappa+eta. It is only a necessary minimum; the exact sufficient cap in
(8) still contains full Pair6_6000. The earned variance credit reduces the
old necessary minimum by exactly its payment saving. It is not a proved
positive third/fifth/sixth cancellation. That joint estimate remains OPEN.

To demonstrate why mu3=0 need not be imposed, take the exact spectral law
with atoms 1,-1/3 and weights 1/4,3/4. Its moments are

    [1,0,1/3,2/9,7/27,20/81,61/243].

It has mu3=2/9, mu5>1/36 and mu6<34/135; the original square expectation
is 14149731073/2090422687500. Including band and refined variance payments
still gives defect below 21/200. Thus compensation can satisfy the consumer
while an independently imposed micro-sized third cap fails. This is an
exact moment-admissible falsifier of **necessity of the separate cap**, not
a prime model, optimization witness, or evidence about zeta zeros. It
supplies no saving to (8).

## 7. What is proved, conditional, and unsupported

- Proved for the normalized source prime matrix: same-section mu1=o(1),
  exact mu2 in (5), q_alpha=1/4+o(1), the variance-payment improvement,
  central third removal (6), and exact consumer tradeoff algebra.
- Valid conditional implications: transfer of first/second moments under
  the stated source Hilbert-Schmidt error, sixth-norm coercivity from a
  bounded joint gate, power/row-deletion/PNT transfer under that bound,
  and the large Holder third ceiling under the actual sixth ceiling.
- Sufficient but OPEN: the small one-sided third estimate (3) for a proved
  fifth/sixth budget, or the weaker joint estimate (8).
- Unsupported: mu3<=0 by symmetry, mu3=o(1) from wordwise central leakage,
  or treating 1/36 and 34/135 as actual source moments.

Zero-side block structure, tail-Weyl comparison, d/N normalization, scalar
background/taper identification, and its same-section error accounting
remain visible inherited obligations. This report does not certify them
through the moment identities. No strict >79 claim follows until these
and (8), or an equivalent set of signed estimates, all close.

## Reproduction

The new producer `src/wp84_third_aware_margin.py` writes only its new JSON.
The independent replay `src/wp84_third_aware_margin_replay.py` imports no
producer; it checks the square by a separate convolution, 6000 displacement
sum in reverse order, convex-tail inequalities, exact old/new payments and
strict boundaries, the rational spectral-law example, frozen inputs and
packet hashes. Eight hostile mutations reject consumer/R changes, incorrect
double credit, prime-to-zeta promotion, and unsupported third or >79 claims.
The note supplies the analytic proofs; rational replays do not prove the
remaining alias/tail estimate.
