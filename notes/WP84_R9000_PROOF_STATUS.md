# WP84 at radius 9000

**Status: conditional route to strictly more than 79% simple critical-line zeros.**
The matched matrix comparison is proved for the specified source family
with \(a_\phi\to1\). The signed arithmetic upper bound remains open.

| Step | Result |
| --- | --- |
| Prime-to-zero comparison | The full sharp matrix matches the smoothed Weil compression up to \(o(d)\) in trace norm after diagonal conjugation. The zero-side block count and negligible endpoint errors give the simple-zero lower bound from the bounded trace. [Comparison](WP84_MATCHED_WEIL_COMPRESSION.md) · [Counting criterion](WP84_ZERO_COUNT_TRANSFER.md) |
| Sufficient arithmetic input | At \(R=9000\), \(\limsup E_w[P(H_R)^2]<41218511120/403675173611\) implies \(\limsup\tau F_{80}(H)<21/200\). The bounded trace transfers from the tapered state with vanishing loss. [Band estimate](WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md) · [Taper](WP84_TAPERED_RESONANCE_LOCALIZATION.md) |
| Required signed saving | For the frozen polynomial, the paired contribution is at least 0.13054588. The remaining arithmetic terms must lower it by more than 0.02843776. The 0.1279 refit bound concerns the paired law at the same numerical threshold. [Paired calculation](WP84_TAPERED_MOMENT_REDUCTIONS.md) |
| Resonance reductions | The additive kernel and its quadratic phase correction apply through degree six. The documented Type-I estimates remove specified portions of the first alias. [Additive reduction](WP84_JOINT_ADDITIVE_REDUCTION.md) · [Cubic Type I](WP84_MIXED_ALIAS_SMALL_DIVISORS.md) · [Fifth first alias](WP84_FIFTH_FIRST_ALIAS.md) |

## Small denominator products at any positive alias

Write \(L=\log X\), \(B=200L\log L\) and \(z=X(u/(X^m v)-1)\) for
a fixed positive alias \(m\ge1\) through degree six. Retain
\(|z|\le B\). Let \(D=X^{m-1}v\) be the reciprocal lattice spacing
in \(z\). The coefficient mass at \(u,v\) is
\(O_R(f(u)f(v)/(X^{m/2}v))\), with the multiplicative prime-power
majorant \(f\) of [the fifth-alias note](WP84_FIFTH_FIRST_ALIAS.md).

For \(D>X^{1/4}\), the core and each shell of width \(h\ge D\)
around \(X^m v\) admit the modulus-one Shiu bound \(O(h/L)\) for
the sum of \(f(u)\). Indeed \(X^m v\ll X^6\) in the source window,
so \(D>(2X^m v)^{1/25}\) for large \(X\). Intervals enlarged for
the count have lengths at most \(O(DB)=o(X^m v)\).
The long-box bound \(O(\min(1,1/|z|))\) for both kernel factors
gives \(O(D\log L/L)\) after summing over numerator shells.
The quadratic correction has smaller total bound
\(O(DB^2/(XL))\).

At the denominator scale \(V\), retain the actual logarithmic weight
in every one of the \(j_-\) denominator slots. For \(V\ge2\) define
\(g_V(p)=\log p/\log(2V)\) up to \(\min(V,N)\), zero thereafter, and
use the majorant \(f_V(p^e)=e^6g_V(p)\). The sum of the original
denominator weights for \(v\le V\), counting ordered factorizations,
is at most
\[
 O\left((\log(2V)/L)^{j_-}\sum_{v\le V} f_V(v)\right)
 =O\left(\frac{V(\log(2V))^{j_--1}}{L^{j_-}}\right).
\]
The normalization factor appears once for each slot. The last bound
uses modulus-one Shiu on dyadic intervals and
\(\sum_{p\le V}g_V(p)/p=O(1)\). Combining with the numerator estimate
gives, for \(j_-\ge1\),
\[
 O_R\left(X^{m/2-1}\frac{V(\log(2V))^{j_--1}\log L}{L^{j_-+1}}\right).
\]
For \(m=1\), the portion \(D\le X^{1/4}\) is additionally \(o(1)\)
by the elementary small-range argument in the fifth-alias note.
This proves vanishing for \(V=o(\sqrt X L^2/\log L)\).
For \(m=2\) and any fixed \(j_-\ge1\), it proves vanishing for
\(V=o(L^{j_-+1}/(\log L)^{j_-})\), including the proposed
\(o(L^2/\log L)\) cutoff. Just applying the denominator estimate at
the scale \(X\) would miss the needed saving when \(V\) is small.
When there are no denominator slots, \(v=1\) exactly. The first
alias is \(o(1)\) by counting nearby integers using the bounded
ordinary-prime coefficients or the \(u^\varepsilon\) prime-power
majorant. At the second alias the numerator estimate alone gives
\(O_R(\log L/L)\).

## Boundary of the current reciprocal-phase estimate

If a numerator slot is expanded as \(ds\le N\), write \(A\) for the
product of the other numerator slots. On the source window,
\[
 Ad\ge A\ge (1-B/X)X^m v/N .
\]
For \(m\ge2\) this exceeds \(X\) even at \(v=1\), so the present
reciprocal-phase estimate for \(M\le X\) does not apply. For \(m=1\)
the exact exclusion condition is \(v>N/(1-B/X)\). Exceeding a
proved polylogarithmic cutoff below \(X\) does not in itself put
a block beyond \(M\le X\). These are boundaries of the stated
estimate and reduction. An upper bound on the remaining signed
contribution is still needed.

## Finite-radius model audit

I use the following numbers to test the circular unitary ensemble (CUE) model. Substitution of the proposed infinite-radius centered moments
`(1, 0, 1/3, 0, 1/4, 1/36, 61/252)` in the [square polynomial](WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md) gives exactly
`18989225/192959881`. The difference from the square threshold is about 0.003697891756. Each entry below is in square units. These are rounded working charges conditional on the model and its cumulant reductions.

| Term | Charge |
| --- | ---: |
| Variance | 0.000000994689 |
| Cubic | 0 |
| Fourth | 0.000009972241 |
| Fifth | 0.000278076622 |
| Sixth, fully paired | 0.002254428187 |
| Sixth, fourth cumulant times a pair | 0.001127214093 |
| Remaining before the connected sixth cumulant | 0.000027205923 |

For the fourth cumulant times a pair, the normalized marginal is
$6s^2-4s^3$. Its sum with its reflection about $1/2$ equals two.
The same identity holds for the pair marginal $2s$. Thus each slot has
mean squared Fourier tail $v_R$ by Parseval. The absolute mass is
$15\cdot6/12=7.5$. With $G=1.18$, the averaged telescoping factor is
$6\sqrt2+\sum_{b=1}^5(6-b)G^{b-1}$. Multiplying by $7.5v_R$ and
$93315600/192959881$ gives the semi-connected charge above.

A proposed rational triangulation gives total connected absolute mass
$30(37/2880)+20(757/5832)=69551/23328<3$. The rational addition checks.
Independent verification of the continuous kernels and simplex integration remains open. Two domain checks for replay are the four-positive coordinate volume $11/24$ before ordering, obtained by integrating
$(s^3-4(s-1)^3)/6$ from 1 to 2, and the volume $11/60$ after weighting by $2-s$ for the two negative slots. For three positive and three negative slots the balanced domain above total frequency one has volume $1/2$ in five free coordinates. Conditional on mass at most three and the other ledger inputs, a paired upper debit of 0.001460 suffices. The actual prime matrix still requires the signed arithmetic estimate above.

### Exact small-section test for the paired sector

I sum the 15 Gaussian Wick matchings on each removed closed six-step walk with open boundaries. The [replay script](../src/wp84_paired_sixth_replay.py) keeps rational coefficients in $x=\pi^{-2}$. Run from the repository root:

```sh
python src/wp84_paired_sixth_replay.py --size 6 --radius 2
```

For six sites at radius two, the normalized banded minus full paired sixth moment is exactly
$-2093x/43200-8267831x^2/17280000-111195861539x^3/62208000000$.
It evaluates to about $-0.01168007741$. At radius five the same six-site difference vanishes identically.

For the walk $(0,\ell,0,d,0,d,0)$ with $0<|d|\le R<|\ell|$, the three matchings pairing the two long edges contribute $3/(8\pi^6 d^4\ell^2)$. The twelve remaining matchings contribute the same amount because the edges share the variable at site zero. Even at fixed $d=1$, summing over positive $\ell>R$ gives a cross-pair contribution of order $1/R$. A uniform signed estimate must account for these terms. The small-section replay supplies a check for that calculation. The paired upper bound at radius 9000 and the full finite-radius certificate remain open.
