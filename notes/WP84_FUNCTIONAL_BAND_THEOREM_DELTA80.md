# WP84 — functional-calculus O(1/R) band theorem for bounded consumers

Date: 2026-10-06

Status: **THEOREM-SIDE BAND COMPARISON CLOSED FOR EVERY C^2 BOUNDED CONSUMER WITH EXPLICIT CONSTANT; DELTA=80 GIVES A CERTIFIED >79 FIXED-BAND TARGET AT R=12000**

No unconditional zero-proportion theorem is claimed here.

The earlier six-pole Christoffel-square fallback bounded the full-to-band error
by summing absolute values of six partial fractions.  That is valid but loses
all cancellation between the poles.

A direct trace-functional argument gives a substantially smaller bound that
depends only on the real-line curvature of the bounded consumer.

## 1. Setup

Let

    H = H_R + Delta_R

be the sharp Loewner matrix and its hard displacement truncation at width R.
Write

    q_alpha = ||alpha||_2^2/d.

The already-established sharp tail estimates are

    tau(Delta_R^2)
      <= 8 q_alpha/(pi^2 R),

and

    ||[D,H_R]||_F^2/d
      <= 8 R q_alpha/pi^2.

For the retained sharp prime field,

    q_alpha = 1/4 + o(1).

Let f:R->R be C^2 with

    M_2 = ||f''||_infinity < infinity.

The Christoffel consumers F_delta satisfy this for every fixed delta>0.

## 2. Trace Taylor remainder

For Hermitian A,E, the trace functional obeys

    tau f(A+E)
      =
      tau f(A)
      + tau(f'(A)E)
      + Rem_2,

with

    boxed:

    |Rem_2|
      <= (M_2/2) tau(E^2).

One proof diagonalizes A+tE inside the exact second Fréchet derivative.
The Hessian kernel is the divided difference

    [f'(x)-f'(y)]/(x-y),

with diagonal f''(x), and its absolute value is bounded by M_2.

Apply this with A=H_R and E=Delta_R:

    |Rem_2|
      <=
      4 q_alpha M_2/(pi^2 R).

## 3. The linear trace gains a second displacement denominator

Since Delta_R has zero diagonal and, for |i-j|>R,

    (Delta_R)_ij
      =
      (alpha_i-alpha_j)/(pi(j-i)),

we have

    tau(Delta_R f'(H_R))
      =
      (1/d)
      sum_{|i-j|>R}
        (alpha_i-alpha_j)
        [D,f'(H_R)]_ji
        /
        [pi(j-i)^2].

Cauchy--Schwarz gives

    |tau(Delta_R f'(H_R))|

      <=
      (1/(d R))
      ||Delta_R||_F
      ||[D,f'(H_R)]||_F.

For Hermitian H_R, spectral divided differences imply the exact
Hilbert--Schmidt commutator Lipschitz estimate

    boxed:

    ||[D,f'(H_R)]||_F
      <=
      M_2 ||[D,H_R]||_F.

Therefore

    boxed:

    |tau(Delta_R f'(H_R))|
      <=
      8 q_alpha M_2/(pi^2 R).

## 4. Universal functional band theorem

Combining the linear and quadratic pieces gives

    boxed:

    |tau f(H)-tau f(H_R)|
      <=
      12 q_alpha M_2/(pi^2 R).

With q_alpha=1/4+o(1),

    boxed:

    |tau f(H)-tau f(H_R)|
      <=
      3 ||f''||_infinity/(pi^2 R)
      +o(R^-1).

This is theorem-side and does not use a partial-fraction decomposition,
pole-by-pole triangle inequality, or a raw moment of the full matrix.

It is especially useful when the residue sum is badly conditioned.

## 5. Exact delta=80 curvature certificate

Take

    F_80(x)
      =
      81 P(x)^2/(P(x)^2+80).

Exact symbolic differentiation gives a rational F_80''=N/D with D>0 on the
real line.

The companion exact gate clears denominators and uses Sturm root counts to
verify

    72 D(x)+N(x) > 0,
    72 D(x)-N(x) > 0

for every real x.

Hence

    boxed:

    ||F_80''||_infinity < 72.

No floating optimization is used in this certificate.

Therefore

    boxed:

    |tau F_80(H)-tau F_80(H_R)|
      <
      216/(pi^2 R)
      +o(R^-1).

Using the elementary exact lower bound

    pi > 333/106,

we may replace this by the fully rational upper bound

    boxed:

    |tau F_80(H)-tau F_80(H_R)|
      <
      C80/R
      +o(R^-1),

where

    C80
      =
      216 (106/333)^2
      =
      2426976/110889
      ~=21.8865351838.

This improves the earlier residue-sum reconnaissance constant at delta=80,
which was about 55.82, by more than a factor 2.5.

## 6. Certified first >79 fixed-band gate at R=12000

The exact Jensen model cap is

    h_80(w0)
      =
      22923/222539
      ~=0.1030066640004673,

where

    w0=1415/13891.

At R=12000 the rational band charge satisfies

    C80/R
      =
      202248/1108890000
      ~=0.00182387793198604.

Therefore

    h_80(w0)+C80/12000
      <
      0.105,

with exact residual margin

    boxed:

    464637587/2741903019000
      ~=0.000169458067546626.

Consequently, if the banded Christoffel square satisfies

    boxed:

    limsup_T tau P(H_12000)^2
      <
      101698640/996729767

      ~=0.102032309425349,

then the bounded consumer gives

    limsup_T tau F_80(H_T)<0.105,

If the matched hypotheses in the [zero-count transfer criterion](WP84_ZERO_COUNT_TRANSFER.md)
are established, this yields a strict simple-zero proportion above 79 percent.

The square threshold lies above the frozen model value by

    boxed:

    2323187935/13845573193397
      ~=0.000167792831871196.

This is a narrow but completely explicit arithmetic allowance.

## 7. Relation to the centered degree-six ledger

The centered Christoffel-square audit showed that replacing the model
centered fourth moment 1/4 by the pair-only ceiling 4/15 costs about

    0.00156752584233,

which is much larger than the R=12000 allowance above.

Therefore the fixed-band route still needs genuine degree-six information:
either quantitative recovery of the negative connected fourth-order sector,
or compensation through the combined fifth/sixth-order square.

The present theorem does not close that arithmetic problem.  It removes a
large avoidable full-to-band constant and freezes a much smaller exact band
radius for further attack.

## 8. Evidence boundary

Closed:

- universal C^2 functional O(1/R) full-to-band theorem;
- exact Sturm certificate ||F_80''||_infinity<72;
- fully rational band constant using pi>333/106;
- exact R=12000 >79 fixed-band threshold.

Open:

- prove the fixed-band arithmetic inequality
      limsup tau P(H_12000)^2 < 101698640/996729767;
- then insert the existing zero-side transfer.

The selected primary route remains the minimal-radius one-point grouped
heat-curvature attack.  This is the strongest current fixed-band fallback.

See:

    notes/WP84_FIXED_BAND_CHRISTOFFEL_SQUARE_FALLBACK.md
    notes/WP84_FIXED_BAND_CHRISTOFFEL_CENTERED_LEDGER.md
    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md

## 9. Weighted displacement estimate and a radius-9000 arithmetic target

Keep the setup and normalization of sections 1–4, with integer radius
$R\ge1$, $D_{ii}=i$, and normalized trace $\tau$. Define $B_{ij}=
(\Delta_R)_{ij}/(j-i)$ for $|i-j|>R$, and zero elsewhere. In the linear
trace term the factor $j-i$ is supplied by $[D,f'(H_R)]_{ji}$.
For each positive displacement $k$, the finite sum of
$|\alpha_i-\alpha_{i+k}|^2$ over admissible indices is at most
$4\Vert\alpha\Vert_2^2$. Counting both orientations gives

$$
\frac{\Vert B\Vert_F^2}{d}
\le \frac{8q_\alpha}{\pi^2}
\sum_{k>R}k^{-4}
\le \frac{8q_\alpha}{3\pi^2R^3}.
$$

The last inequality integrates the decreasing function $x^{-4}$ from $R$
to infinity. Apply Hilbert–Schmidt Cauchy–Schwarz to $B$ and
$[D,f'(H_R)]$, then apply section 3's commutator bound and section 1's
estimate for $[D,H_R]$. The linear term costs at most
$8 q_\alpha M_2/(\sqrt{3}\pi^2R)$.
Adding section 2's Taylor remainder gives the finite-dimensional estimate

$$
|\tau f(H)-\tau f(H_R)|
\le \frac{4q_\alpha M_2}{\pi^2 R}(1+2/\sqrt{3}).
$$

For the retained field, take $T$ to infinity at fixed $R$ so that
$q_\alpha=1/4+o(1)$. Use section 5's Sturm bound $M_2<72$,
$1/\sqrt3<26/45$ and $\pi>333/106$. The resulting limsup charge is at most
$C/R$, where $C=8719136/554445$. At $R=9000$ this charge is smaller
than the original $C_{80}/12000$.

Let $y=21/200-C/9000$. By monotonicity and concavity of
$h_{80}(t)=81t/(80+t)$ on the nonnegative half-line, a sufficient
**open arithmetic inequality** is now

$$
\limsup_{T\to\infty}\tau P(H_{9000})^2
< h_{80}^{-1}(y)
=\frac{41218511120}{403675173611}.
$$

The right side exceeds the pinned mean by
$1365967308355/5607451836630401$, approximately 0.000243599.
The old radius-12000 allowance was approximately 0.000167793.
These thresholds concern different band matrices. The estimate reduces
the analytic truncation cost. A proof for the prime matrix at the chosen
radius and the required zero-side transfers are still needed.

## 10. Radius 9000: the signed arithmetic moment budget

Put Y = H_9000 - I, m_j = tau(Y^j), and use the same prime normalization
and section as in the [second-moment calculation](WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md).
Let K = 41218511120/403675173611 from section 9 and w = 1415/13891.
Expand P(1+y)^2 with common denominator D = 192959881. In ascending order
the seven integer numerators are

    2229049, -8958000, -17049864, 81188760, 18148176, -168547680, 93315600.

The sharp reference vector through degree six is
(1, 0, 1/3, 0, 1/4, 1/36, 157/630). Substitution gives w exactly.
At fixed R the first moment is o(1) and the variance is
1/3 - v_R + o(1), where v_R = sum_{k>R} k^(-2)/pi^2.
Consequently the open square inequality in section 9 is equivalent, under
these two same-section inputs, to the following one-sided joint bound:

    limsup [81188760 m3 + 18148176 (m4-1/4)
            - 168547680 (m5-1/36) + 93315600 (m6-157/630)]
      < D (K-w) - 17049864 v_9000.

The variance debit in square units is positive and less than 0.000001,
using v_R < (106/333)^2/R. The remaining four moments must refer to
the same section. Their individual limits need not exist.

### Can the relaxed sixth moment close this particular square gate?

First grant the reference values of moments three through five and even
remove the variance debit. The required sixth moment is then strictly below
209030582803919701/837093134013658480 (about 0.24971007).
The relaxed reference ceiling 34/135 is about 0.25185185.
At that endpoint the original square has mean 59707895/578879643, above K.
The actual finite-band variance debit further tightens the threshold.

There is also a coefficient-independent diagnostic at this relaxed moment
vector. Form the 4 by 4 Hankel matrix M with entries m_(i+j) for indices
0 through 3, using the sharp reference through degree five and 34/135 at
degree six. Its leading minors are 1, 1/3, 5/108, 127/46656.
For v = (1,-1,1,-1), the minimum of c^t M c subject to c^t v = 1 is
1/(v^t M^(-1)v) = 635/6159, strictly above K. This follows by
Cauchy–Schwarz in the M inner product, with equality for c proportional
to M^(-1)v. Even freely refitting a cubic normalized at y=-1 misses the
**same numerical threshold** for this model vector. Changing the bounded
consumer would require a fresh curvature and band calculation.

This isolates the missing arithmetic information. A sufficiently small
sixth moment, or a compensating signed gain from moments three through
five, would advance this route. The model calculation supplies neither
an actual prime-matrix counterexample nor a bound on zeta-zero multiplicity.

## 11. Same-section square completion and the remaining prime-sum estimate

Let S be the centered combination inside the limsup in section 10. Use the
same normalized trace and matrix Y throughout. Put

    B = 93315600,  G = 57960000,  a = 727/805,  b = 676573/966000,
    Q = tau[(Y^3-a Y^2)^2],
    V = tau[(Y^2-b Y-(m2-b m1)I)^2].

Expanding the first square gives the fifth-degree coefficient -2Ba and
the fourth-degree coefficient Ba^2. The remaining fourth-degree
coefficient is -G. Completing its square together with 2Gb Y^3 and
centering Y^2-bY gives the finite identity

    S = B Q - G V + G [b^2 m2 - (m2-b m1)^2] - 23110004.

Here 23110004 is the reference offset from section 10, and G/B = 100/161.
Put s = 1/3 - v_9000. Using the established first two moments, the exact
threshold for the signed difference is

    theta = [D(K-w) - 17049864 v_9000 + 23110004 - G(b^2 s-s^2)] / B.
    limsup [Q - (100/161)V] < theta.                 (open)

Numerically theta is about 0.21560655. Discarding the nonpositive term
would require Q alone to satisfy this threshold. Even the sharp reference
vector gives Q about 0.403. The difference retains information that the
separate upper bound loses.

For ordinary-prime words, each frequency is the logarithm of a rational
number. The sum of its signed prime exponents has the same parity as the
word length, including after opposite-sign pairs cancel. Unique
factorization therefore separates the exact frequencies at degrees five
and six. This observation allows cancellation between their aggregate
weighted sums but supplies no equality between individual frequencies.
Near aliases can contribute through the finite averaging kernel.

The [same-section cubic analysis, section 5](WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md)
identifies the surviving three-distinct-prime nonzero aliases and tails.
At a new fixed radius the closed-path count depends on that radius.
The first two moments and the square identity supply no upper estimate
for this cubic contribution or for the combined signed residual.
The arithmetic bound and its transfer to the simple-zero count remain open.
