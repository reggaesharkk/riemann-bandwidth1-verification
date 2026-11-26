# Additive reduction through degree six

The localized tapered moments through degree six admit a common
additive kernel with a first-order correction. This preserves the
signed combination in the square. It also permits subtraction of a
constant reference density on sufficiently fine numerator lattices.
The remaining arithmetic discrepancy still needs a signed bound.

## Total weight in one resonance window

Use the [tapered localization](WP84_TAPERED_RESONANCE_LOCALIZATION.md)
on a section with starting index \(0\le a=O(XL)\).
Put \(B=200L\log L\). For a fixed path and sign pattern write
\(\lambda=\log(u/v)\), with \(u,v\) the products of the positive and
negative slots and an empty product set equal to one.
For a resonance indexed by \(m\ge0\) write
\[
 z=X\bigl(u/(X^m v)-1\bigr),\qquad |z|\le B.
\]
Negative resonances follow by reversing all signs. The larger window
in \(z\) includes the logarithmic window and adds only terms covered
by the localization error. The original coefficient and displacement
phases remain in every term. Each ordered factorization of \(u,v\)
has weight \(O_R(1/\sqrt{uv})\). For ordinary primes the multiplicities
are bounded by factorials of the slot counts. For prime powers
distribute the prime bases over at most six slots, then bound each
slot exponent by \(O(L)\). Thus the combined multiplicity costs
at most \(O(L^6)\), including repeated bases.

Write \(j_+,j_-\) for the slot counts and
\(V=2\min(N^{j_-},N^{j_+}X^{-m})\). The window forces \(v\le V\).
At fixed \(v\) there are \(O(1+B X^{m-1}v)\) integer numerators,
with coefficient \(O_R(X^{-m/2}/v)\). As
\(X^{m/2}V\le 2N^{(j_++j_-)/2}\), the summed absolute coefficient
mass is
\[
 O_R\left(L^6(L+B N^{(j_++j_-)/2}/X)\right).
\]
At degree at most six this is \(O_R(L^6(L+B X^2e^{-3\sqrt L}))\),
using this larger common upper bound for all the degrees.

## Phase and lattice cancellation

For row \(i\) put \(\xi_i=1+(a+i)/(XL)\), which is bounded and
at least one. With \(e(t)=\exp(2\pi it)\) the phase is exactly
\(e(mXL)e(\xi_i X\log(1+z/X))\). Smooth the row distribution by
adding independent centered uniform jitters on \([-1/2,1/2]\)
to its long box and its \(k\) short boxes.
For a fixed logarithmic offset this changes the expectation
by \(O(k(B/(XL))^2)\): the phase increment has mean zero and its
second moment is \(O(k(B/(XL))^2)\).
The resulting frequency variable \(\xi\) has continuous density
supported in \([1/2,C]\), with a fixed \(C\).
Write \(G_0(z)=\mathbb E e(\xi z)\) and
\(G_1(z)=\mathbb E[\xi e(\xi z)]\).
Taylor expansion gives the replacement kernel
\[
 e(mXL)\left(G_0(z)-\frac{\pi i z^2}{X}G_1(z)\right)
\]
with error \(O(B^4/X^2+k(B/(XL))^2)\) per term.
Multiplying by the coefficient mass above proves a total \(o(1)\)
error uniformly in the height. This is why the quadratic term in
the logarithm is retained at the higher degrees.
The number of paths and aliases is bounded at fixed radius and degree.

For a fixed denominator product \(v\), the numerator lattice in \(z\)
has step \(1/D\), where \(D=X^{m-1}v\). If \(D>C\), the periodized
sum on this lattice of each of \(G_0(z)\) and \(z^2G_1(z)\) is zero.
Indeed their Fourier transforms are supported in \([1/2,C]\).
Multiplication by \(z^2\) differentiates the Fourier transform
and preserves its support. The convolution of the long and short
interval densities has the required differentiability for large \(k\).
Poisson summation then samples only frequencies in \(D\mathbb Z\),
which are disjoint from this support.

The same subtraction in the finite window costs \(o(1)\) in the
normalized moment. To see this, outside \(|z|\le B\) the sinc
factors give \(|G_0(z)|\le(B/(100|z|))^k\).
For \(G_1\), expand \(\xi\) as a constant plus its independent
box variables. Each expectation can lose at most one short
factor, and the sum of the absolute sizes of the scaled variables
is bounded. Thus \(|G_1(z)|\ll(B/(100|z|))^{k-1}\).
Summing the decreasing envelopes over the two lattice tails,
including \(z^2/X\), costs
\(O((1+DB)(1+B^2/X)100^{-(k-1)})\) per \(v\).
For any bounded baseline in the coefficients normalized by
\(X^{-m/2}/v\), the summed error is \(o(1)\) by the same
estimate \(X^{m/2}V\le 2N^{(j_++j_-)/2}\).
At coarse lattices keep the original coefficients.

In the first mixed cubic the reduction recovers the linear kernel
with a vanishing error. Here it also covers the denser high-degree
resonances. In the joint square, each degree still has its own
coefficient and arithmetic support. Neither the additive expansion
nor the constant-density subtraction bounds the weighted prime
discrepancy.
