# WP84 — bounded rational consumer candidate

Date: 2026-10-05

## Evidence class and limits

The exact algebra below gives a bounded rational moment-consumer bound for probability laws with the stated pinned model moments. It does not identify those moments with the actual zeta-prime data, prove the required six-pole comparison for arithmetic matrices, or close the prime-to-Weil and zero-side transfers. The resulting >79% coefficient is a model/conditional candidate; the strict >79% theorem remains OPEN.

Status: **MODEL-MOMENT BOUND CHECKED; SIX-POLE ARITHMETIC COMPARISON OPEN**

The exact degree-6 polynomial certificate is powerful but unbounded.  The
fixed-pole beta consumers are bounded but their strongest displayed values
were surrogate-law evaluations rather than moment-forced bounds.

There is a direct interpolation between the two.

## 1. Start from the exact Christoffel square

Let

    P(x)
      = 1
        - (43428/13891)x
        + (37704/13891)x^2
        - (9660/13891)x^3,

and put

    g(x)=P(x)^2.

For every positive Borel probability measure with the pinned moments through
degree six,

    integral g dnu = w0
                   = 1415/13891.

The coefficient-sign certificate gives

    g(x)>=1 for x<=0.

## 2. Rationalize without losing the half-line majorant

For any fixed delta>0 define

    F_delta(x)
      = (1+delta) g(x)/(g(x)+delta).

Then exactly

    F_delta(x)-1
      = delta (g(x)-1)/(g(x)+delta).

Since g+delta>0 on R,

    boxed:
    F_delta(x)>=1 for every x<=0.

Also

    0 <= F_delta(x)
      <= ((1+delta)/delta) g(x),

because g+delta>=delta.

Therefore every measure with the pinned moments satisfies

    nu((-infinity,0])
      <= integral F_delta dnu
      <= (1+1/delta) * 1415/13891.

This is a **moment-forced bound**, not an evaluation on one extremal
quadrature.

## 3. Choose delta=61

At delta=61,

    F_61(x)=62 g(x)/(g(x)+61).

The universal negative-mass cap is

    62/61 * 1415/13891
      = 87730/847351
      = 0.1035344267....

Hence

    positive-index mass
      >= 759621/847351
      = 0.8964655733....

and the frozen zero-side ledger would yield the candidate coefficient

    671891/847351 = 0.7929311466... > 0.79.

This remains a model/conditional frontier candidate, not a proved zeta-zero proportion. The arithmetic-matrix bound and the prime-to-Weil and zero-side transfers are OPEN.

It deliberately sacrifices part of the 79.627% polynomial optimum in exchange
for bounded functional calculus.

### 3.1. Jensen refinement at the same six poles

The [delta=80 band note](WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md) already
uses Jensen's inequality. Its specialization here preserves the six poles of
section 4. Write $h(t)=62t/(61+t)$ and $w=1415/13891$. For every $t\ge0$,

$$
h(w)+h'(w)(t-w)-h(t)
=\frac{62\cdot61(t-w)^2}{(61+w)^2(61+t)}.
$$

Integrating at $t=P(x)^2$ cancels the linear term under the pinned moments.
Thus the negative-half-line mass is at most the expectation of $F_{61}$,
which is at most $h(w)=43865/424383$. The model ledger gives
$1-2h(w)=336653/424383$ (about 79.32764%). This bounds the rational
consumer in the pinned model. The polynomial bound in section 1 remains
stronger for the model mass itself.

For any fixed comparison law with those moments, a sufficient one-sided
error budget for the **original section 8 target** is
$87730/847351-43865/424383$: if the limsup of the arithmetic trace minus
the comparison-law expectation is at most this difference, section 8 follows.
No such comparison estimate is established here.

## 4. Resolvent representation

The denominator

    g(z)+61 = P(z)^2+61

has degree six and no real zeros, because g(x)>=0 on R.

Its roots are six simple nonreal algebraic poles.  Numerically the smallest
absolute imaginary part is about

    1.0760.

Thus every consumed resolvent is safely separated from the real axis.

Writing the poles as z_j,

    F_61(x)
      = 62 + sum_{j=1}^6 c_j/(x-z_j),

with

    c_j
      = -61*62 / (2 P(z_j) P'(z_j)).

Therefore

    tau(F_61(H))
      = 62 + sum_j c_j m_H(z_j).

The theorem no longer needs:

- a high-order pole at i;
- a Cauchy circle;
- resolvent derivatives;
- a surrogate target law.

It needs only six simple fixed nonreal resolvent values.

## 5. Rank robustness

Because the consumer is a fixed bounded rational function and all six poles
stay a fixed distance from R, an o(d)-rank perturbation changes the statistic
by o(1).  This follows directly from the rank-Stieltjes bound applied to the
six partial fractions.

Thus the deep-zero deletion architecture remains intact.

## 6. Moving positive threshold

The zero-side count uses theta_T->0 rather than the strict half-line.

Since F_61 is continuous and F_61(0)=1, define

    q(theta)
      = inf_{x<=theta} F_61(x).

For sufficiently small positive theta, q(theta)>0 and q(theta)->1.

Then

    1_{x<=theta}
      <= F_61(x)/q(theta),

so the same asymptotic cap holds with a factor 1+o(1).

## 7. Quantitative diagnostic

The six residues have

    sum_j |c_j| ~= 138.885.

The certified simple-zero margin above 79% is

    0.0029311466....

Under the crude assumption that all six normalized resolvents are controlled
with the same absolute error epsilon, it is sufficient that

    epsilon
      < margin / (2 sum |c_j|)
      ~= 1.06e-5.

This number is only a diagnostic error allocation.  The asymptotic theorem
needs o(1) at the fixed poles.

## 8. Why this changes the kill gate

The previous shortest route aimed to identify an entire limiting spectral law
and then recover its moments.

For a >79 theorem that is stronger than necessary.

A sufficient bounded theorem is now:

    boxed:
    limsup_T tau(F_61(H_T))
      <= 87730/847351.

After the vanishing-threshold correction and o(d)-rank deletion, this alone
yields the 79.2931% simple-zero coefficient above.

Because F_61 is a six-pole resolvent combination, the theorem-side problem
reduces to one scalar linear combination of six fixed resolvent laws.

## 9. New active target

Attack directly

    L_61(T)
      := 62 + sum_j c_j m_{H_T}(z_j)

through the exact permutation-Lindeberg first/second-order expansion.

The required asymptotic inequality is

    limsup L_61(T)
      <= 87730/847351.

This is strictly narrower than identifying the full spectral law and avoids
finite-T raw higher moments by construction.

Companion checker:

    src/wp84_bounded_christoffel_consumer.py

No unconditional >79% theorem is claimed until this six-pole inequality is
proved.


## Source and implementation record

Curated from the publicly accessible frontier-audit candidate. The source note blob was `35bf92297730f9817d965480ab33e2bbf31dcaf3`; the accompanying checker blob was `77a359c0488e5143992b5290412979e9109cbc33`. In the checker, an algebraically equivalent expression was incorrectly tested by comparing two separately simplified SymPy trees. A Windows run showed that this structural comparison can fail even when their exact difference simplifies to zero. The curated checker now asserts the exact difference is zero. This is a checker reliability fix; it does not change the mathematical model result or close the analytic gate.
