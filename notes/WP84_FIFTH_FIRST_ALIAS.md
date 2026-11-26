# The small-product region of the fifth first alias

For the sign pattern with three numerator slots and two denominator
slots, let \(u/v\) be their ratio and restrict to the localized first
alias \(|u-Xv|\le vB\), \(B=200L\log L\). This note checks the two
regions in the Neon review dated 27 November 2026 and strengthens its
Poisson range. All statements keep the original path weights and
height carrier. The contribution in the regions proved here is \(o(1)\).

## Small denominator products

The assertion for \(v\le V=o(\sqrt X L^2/\log L)\) holds for both
ordinary primes and von Mangoldt slots. For ordinary primes use
the completely multiplicative weight \(g(p)=(\log p)/L\) for \(p\le N\),
zero otherwise. For prime-power slots use the multiplicative majorant
\(f(p^e)=e^6 g(p)\) for positive integer \(e\). At fixed slot count
\(j\le6\) the sum of products of logarithmic weights over ordered
prime-power factorizations of \(u\) is \(O_j(f(u))\): each distinct
prime must occur, its powers have weight \(g(p)\le1\), and assigning
the bases and splitting their exponents costs at most a constant
times the product of \(e^6\). The same estimate holds for \(v\).
The normalized weights before the kernel are therefore
\(O_R(f(u)f(v)/(v\sqrt X))\).
The prime values of \(f\) are still \(g(p)\), and its other values
are bounded by \(\tau(u)^6\). Shiu's modulus-one estimate thus
applies uniformly with the same \(O(h/L)\) bound at scale \(Xv\)
on intervals of length \(h\ge v\) for \(v>X^{1/4}\).
See [Nair and Tenenbaum, §1](https://tenenb.perso.math.cnrs.fr/PPP/ShortSums.pdf).

The long box gives \(G_0(z),G_1(z)=O(\min(1,1/|z|))\).
For \(G_1\), expanding the expectation of the frequency times the
exponential gives either the long-box sinc factor or the transform
of the long box times a linear weight. The latter has the same
decay by integration by parts. The core and dyadic shells then
give \(O(v(\log L)/L)\) for the linear kernel before the factor
\(f(v)/(v\sqrt X)\). The quadratic term contributes
\(O(vB^2/(XL))\), which is smaller. For \(v\le X^{1/4}\) one can
bound the individual coefficients with a constant for ordinary
primes. For prime-power slots the same small range can instead
be handled by the elementary coefficient bound
\(f(u)\ll_\varepsilon u^\varepsilon\). The summed bound in that
small range is \(O_{R,\varepsilon}(X^{-1/4+2\varepsilon}\log L)\)
by counting the numerator integers and using the corresponding
bound for \(f(v)\). For larger \(v\), the long-interval case of
Shiu gives \(\sum_{v\le V} f(v)\ll V/L\) when \(V>X^{1/4}\).
This proves the claimed \(o(1)\) range. The sharper
\(O_R(X^{-1/4}(\log L)/L)\) small-range bound uses ordinary primes.

## Weighted Poisson reduction

Keep \(p_1,p_2,q_1,q_2\) ordinary prime slots, with the full ordered
sum and repetitions allowed. Expand only the third numerator
slot \(\Lambda(n_3)\) as \(\sum_{ds=n_3}\mu(d)\log s\).
Put \(A=p_1p_2\), \(v=q_1q_2\), \(m=Ad\). Retain
\[
v>Q=\sqrt X e^{-\sqrt L/2},\qquad m\le U,\qquad ds\le N ,
\]
where \(U=o(X/L^3)\). On the source window \(A\ge (X-B)v/N\),
so \(m/v\ge (X-B)/N\gg B\). Each triple of fixed parameters
\(p_1,p_2,d\), together with \(v\), admits at most one integer \(s\).

The logarithmic weights give a bound independent of the divisor
function. For \(m\le X\),
\[
\sum_{p_1p_2\mid m}g(p_1)g(p_2)
\le \left(\sum_{p\mid m}\frac{\log p}{L}\right)^2
\le1 .
\]
The sum is over ordered primes, and \(d\) is determined by \(m\)
and the pair. Also the sum over all ordered denominator pairs of
\(g(q_1)g(q_2)/(q_1q_2)\) is \(O(1)\).
Thus the total coefficient mass of this Type-I window is
\(O_R(U/\sqrt X)\). Expanding the Möbius sum preserves the
validity of the phase reduction on this window: the phase
approximation error times this mass is \(o(1)\).
The quadratic phase correction costs \(O_R(UB^2/X^{3/2})=o(1)\)
directly here, using the boundedness of \(G_1\).
Freezing the smooth factor at \(s_0=Xv/m\) costs
\(O_R(UB/X^{3/2})\), since the relative change is \(O(B/X)\).

In the cutoff strip \(|Xv-AN|\le vB\), any admissible \(ds\)
satisfies \(|ds-N|\le2vB/A=o(1)\), so \(ds=N\).
There are \(O(1+Bv/N)\) possible integers \(A\), with at most
two ordered prime factorizations each, and at most \(\tau(N)\)
choices of \(d\). Since \(v\le UN/(X-B)\) in this strip, its
total cost is \(O_R((1+B)\tau(N)/\sqrt X)=o(1)\), using the
usual divisor bound \(N^{o(1)}\).
Outside the strip the sharp cutoff becomes \(Xv\le AN\).
The s-lattice still has spacing much greater than \(B\).
The kernel tail summed over \(s\) is \(O(100^{-k})\) per tuple,
so extension to all integers costs \(O_R(U100^{-k}/\sqrt X)\).

Poisson summation of the remaining \(G_0(ms/v-X)\) gives
\[
\frac{v}{m}\sum_{j\ge1}\rho(vj/m)e(-Xvj/m).
\]
The factor \(v\) cancels the frozen \(v^{-1}\) as in the cubic
proof. The frozen source factors separate into finitely many
products in \(p_1,p_2,d\) and \(q_1,q_2\), by expanding the
Fourier factors and the linear logarithmic factors at \(s_0\).
On the resulting ranges these factors are bounded apart from the
explicit logarithmic prime weights. Keep the implied restriction
\(A>XQ/N\) before separating the cutoff. The exact rank comparison
for \(Xv\le AN\) has Fourier coefficient mass \(O(L)\), by the
same finite cyclic expansion as in the
[small-divisor proof](WP84_MIXED_ALIAS_SMALL_DIVISORS.md).

On dyadic blocks \(m\asymp M\), \(n=vj\asymp M\), the
\(m\) coefficients are \(O_R(1)\) by the weighted divisor
bound above. The \(n\) coefficients are also \(O_R(1)\):
their absolute values are bounded by a constant times
\((\sum_{q\mid n}(\log q)/L)^2\), and \(n\ll X\).
The reciprocal-phase estimate therefore costs a factor \(\sqrt L\)
for the unsplit denominator norm \(O(M)\).
Geometrically summing over \(M\gg XQ/N\) and charging \(O(L)\)
for the cutoff gives
\[
 O_R\left(L^{3/2}\sqrt{U/X}+L e^{-\sqrt L/4}\right)=o(1).
\]
For example \(U=X/[L^3(\log L)^2]\) is admissible.
This estimate remains within the stated von Mangoldt expansion.
It does not show that replacing the third ordinary-prime slot by
a von Mangoldt slot has a vanishing error over the full complement.

## The height phase

A half-turn of \(e(XL)\) would exclude a uniform positive
contribution from an amplitude proved stable under that shift.
Such stability has not been proved for the surviving prime-product
sum. The carrier alone gives no sign bound and does not restrict
potential savings to the central frequency.
