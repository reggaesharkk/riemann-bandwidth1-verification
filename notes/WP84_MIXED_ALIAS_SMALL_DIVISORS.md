# Sharp cutoff and the small Möbius divisors

This note uses the [additive kernel and reciprocal-phase bound](WP84_MIXED_ALIAS_ADDITIVE.md)
for the original first mixed cubic window. The second numerator prime
can be replaced by a von Mangoldt weight with error \(o(1)\).
In the resulting divisor expansion, the full contribution from
\(d\le e^{\sqrt L}/L^4\) tends to zero, with the sharp cutoff kept.
The proof uses the sharp-cutoff reduction checked in the Gemini Neon review.

## The exact divisor residual

Fix one closed displacement path and the signs oriented as \(pv/q\).
Keep \(p,q\) prime, the cutoff \(N=\lfloor Xe^{-\sqrt L}\rfloor\),
\(L=\log X\), and the window \(|pv-Xq|\le qB\), \(B=200L\log L\).
Write the factor in the \(v\) slot as
\(-(\log v)/(a_\phi L\sqrt v)\) times its bounded Fourier and displacement
factors. Replace \(\log v\) on primes by \(\Lambda(v)\) on integers.

For a proper prime power \(v\le N\) and fixed \(q\), the window can
contain at most one integer \(p\): if it intersects \(p\le N\), then
\(v\ge q(X-B)/N\), and its length in \(p\) is
\(2qB/v\le2BN/(X-B)=o(1)\).
The coefficient is \(O_R(1/(q\sqrt X))\).
There are \(O(\sqrt N\log N)\) proper powers, and
\(\sum_{q\le N}1/q\ll L\), even over integers. Thus the introduced
terms cost \(O_R(L^2\sqrt{N/X})=o(1)\).
The window gives \(p,v>q\) for admissible genuine primes. If the
distinctness mask is needed, \(p=v\) can be restored at cost \(o(1)\):
for each \(q\) the interval in \(p\) then has length
\(O(B\sqrt{q/X})=o(1)\), since \(q\le N^2/(X-B)\).
Allowing equality therefore costs \(O_R(L/\sqrt X)\) before expansion.

Use \(\Lambda(v)=\sum_{d\mid v}\mu(d)\log(v/d)\) and \(v=ds\).
The sum is now over \(ds\le N\) with weight \(\mu(d)\log s/L\)
in the \(v\) slot, together with its original Fourier, displacement,
and normalization factors. Write \(D=e^{\sqrt L}/L^4\).
The result below leaves precisely \(d>D\) in this identity, up to
\(o(1)\). No asymptotic formula for the prime-supported remainder
is assumed.

## Small divisors under the sharp cutoff

Take \(Q=\sqrt X e^{-\sqrt L/2}\). For \(q\le Q\) and fixed \(d\)
the sum of the absolute kernel over multiples \(u=pds\) of \(d\)
in the window is \(O((q/d)\log L+1)\) before multiplicities.
This follows by summing \(O(\min(1,q/|u-Xq|))\) on dyadic shells:
the errors of at most one lattice point per side sum geometrically.
At most \(O(L)\) prime divisors of \(u/d\) can occur as \(p\).
Using the prefactor \(O_R(1/(q\sqrt X))\), Chebyshev's bound for the
number of denominator primes, and \(\sum_{d\le D}1/d=O(1+\log D)\),
the contribution is bounded by
\[
O_R\!\left(
\frac{Q(1+\log D)\log L}{\sqrt X}+
\frac{DL^2}{\sqrt X}\right)=o(1).
\]

For \(q>Q\), freeze the smooth part, including the relative square-root
factor, at \(s_0=Xq/(pd)\). The fractional change in \(s\) is \(O(B/X)\)
and the logarithmic derivative of each weight factor is bounded
uniformly at fixed \(R\). The frozen normalization is \(1/(q\sqrt X)\).
For an absolute error bound, count at most \(O(qB/d+1)\) possible
multiples \(u\) of \(d\) and \(O(L)\) representations per multiple.
Summing over \(q\le N\), using \(N\le X\), bounds the freeze error by
\(O_R(B^2 L(1+\log D)/\sqrt X+BDL^2/X^{3/2})=o(1)\).

In the cutoff strip \(|Xq-pN|\le qB\), any admissible \(ds\) satisfies
\(|ds-N|\le2qB/p=o(1)\), hence \(ds=N\). For each \(q\) there are
\(O(B)\) candidate integers \(p\), since \(q\le N^2/(X-B)\le N\)
for large \(X\). There are at most \(D\) candidate \(d\). Thus discarding
the strip costs \(O_R(BDL/\sqrt X)=o(1)\). Away from the strip the
condition \(ds\le N\) reduces exactly to \(Xq\le pN\) within the window.
On this remaining domain the spacing \(pd/q\ge X/N\gg B\).
The tail of the kernel beyond \(|pds/q-X|\le B\) is
\(O(100^{-k})\) per triple \(p,q,d\), by summing
\((B/(100|pds/q-X|))^k\) on the lattice. Extending to all integral
\(s\) thus costs \(O_R(NDL\,100^{-k}/\sqrt X)=o(1)\).

Poisson summation for \(G((pd/q)s-X)\) now gives
\[
\frac{q}{pd}\sum_{j\ge1}\rho(qj/(pd))e(-Xqj/(pd)).
\]
The sinc decay ensures absolute summability and the density is
continuous with compact support in \([1,C]\). The transform follows
by the change of variables \(v=(pd/q)s-X\). The factor \(q\) cancels
the frozen \(q^{-1}\). The frozen slot weights separate in \(p,d,q\):
the Fourier and displacement factors are finite sums of exponentials
in \(\log(ds_0)/L\), with linear factors for a zero displacement,
and \(\log s_0=L+\log q-\log(pd)\).
Expanding these expressions gives finitely many products of bounded
factors on the ranges in use.

Before separating \(Xq\le pN\), keep the exact implied restriction
\(p>XQ/N\). Every \(m=pd\) then has a unique such representation,
since \(p>D\) and every prime factor of \(d\) is at most \(D\).
Rank the primes \(q\) in the remaining list of length \(J\).
Let \(a(p)\) be the number up to \(pN/X\). The cutoff compares
\(a(p)\) with the rank of \(q\). The indicator of \([0,J]\) on the
cyclic group of order \(2J+1\) evaluates this comparison on the
difference of the ranks. Its normalized Fourier coefficients have
total absolute mass \(O(1+\log(J+1))=O(L)\), from the geometric-sum
bound and the harmonic series. Each mode has modulus-one factors
in the separated variables.

On dyadic blocks \(m\asymp M\), use \(n=qj\asymp M\). The resulting
bilinear form has normalization \(1/(\sqrt X M)\), and the \(m\)
coefficients are uniformly bounded. Each \(n\ll X\) has \(O(1)\)
distinct prime divisors above \(Q\), since \(Q=X^{1/2-o(1)}\).
Hence by Cauchy–Schwarz over those divisors,
\(\sum_{n\asymp M}|\beta_n|^2\ll M\sum_{Q<q\ll M}1/q\ll M\)
using the prime reciprocal estimate. Apply the reciprocal-phase
bound with the resulting factor \(\sqrt L\) relative to its
\(M/L\) normalization. Summing dyadic \(M\) geometrically and
charging the rank expansion gives
\[
O_R\!\left(L^{3/2}
\left(\sqrt{ND/X}+\frac{X^{1/4}}{\sqrt{(XQ/N)L}}\right)\right)
=O_R(L^{-1/2}+L e^{-\sqrt L/4})=o(1).
\]
The support lies inside the reciprocal estimate's range because
\(XQ/N\gg\sqrt X\) and \(ND\le X/L^4\).

This leaves the signed Möbius divisor sum with \(d>D\) on the original
window. Its bound, the coupled higher moments, and the zero-count
transfer remain open.

## Cutting on the product of the prime and divisor

The reciprocal-phase estimate is governed by \(m=pd\). The cutoff on
\(d\) above is a sufficient way to bound every such product, and has
room at its upper endpoint.

In the proof above, retain \(d\le D_*\) and impose an additional mask
\(pd\le U\), where
\[
 D_*=o(\sqrt X/(BL)),\qquad U=o(X/L^3).
\]
The original sum on this region is \(o(1)\). Indeed the small-\(q\)
bound, freeze error, strip error and tail error remain valid with
\(D_*\) in place of \(D\), since a product mask can only reduce each
absolute count. In the small-\(q\) bound,
\(\log(2+D_*)=O(L)\) and \(D_*L^2/\sqrt X=o(1)\).
These follow from \(B=200L\log L\). The cutoff strip cost is
\(O_R(BD_*L/\sqrt X)=o(1)\), and the freeze and tail bounds also tend
to zero.

The product mask does not depend on the integer variable being
summed by Poisson. On \(q>Q\) the lower bound \(p>XQ/N>D_*\)
still makes \(m=pd\) unique. The mask \(m\le U\) therefore belongs
entirely to the \(m\) coefficient and does not add any Fourier cost.
Dyadic summation of the same reciprocal-phase bound now gives
\[
 O_R\left(L^{3/2}\sqrt{U/X}+L e^{-\sqrt L/4}\right)=o(1).
\]
If \(U<XQ/N\) the large-\(q\) portion is empty.

For example, take \(D_*=\sqrt X/L^5\) and
\(U=X/[L^3(\log L)^2]\). These choices cover every
\(d\le e^{\sqrt L}/[L^3(\log L)^2]\), since \(p\le N\).
They also cover larger divisors up to
\(\min(D_*,U/p)\) when \(p\) is smaller. This leaves the signed sum
over the complementary region. The conclusion applies to the same
sharp cutoff and the bounded Möbius coefficients of the original
divisor expansion.

## Product cutoff for a restricted set of denominator bands

Let \(Q=\sqrt X e^{-\sqrt L/2}\) as above. Restrict the original divisor
sum to \(q>Q\) in a union of \(J\ge1\) dyadic intervals, or to a subset
of the primes in such a union. Impose \(pd\le U\), with
\[
U=o\bigl(X/(L^2 J)\bigr).
\]
This entire restriction contributes \(o(1)\) with no separate cutoff
on \(d\). The interval selection and product cutoff may depend on \(X\).

Indeed, for any term in the original window with \(ds\le N\),
\(p\ge (X-B)q/N\). The same lower bound, up to the use of \(X\) in
place of \(X-B\), applies on the frozen cutoff domain \(Xq\le pN\).
Both domains and the cutoff boundary strip therefore have
\[
 d\le \frac{2UN}{(X-B)Q}=:D'.
\]
Since \(U\le X\) for large \(X\), this is
\(O(\sqrt X e^{-\sqrt L/2})=o(\sqrt X/(BL))\).
The absolute freezing, cutoff strip and kernel tail estimates already
proved apply with this \(D'\). The mask \(pd\le U\) stays in the
\(m\) coefficient after Poisson. On the frozen cutoff domain one still
imposes \(p>XQ/N\) before expanding the rank indicator, so \(m=pd\)
is uniquely represented and the coefficients are bounded.
The rank expansion over the selected list of denominator primes
continues to cost \(O(L)\).

Each \(n\asymp M\) has \(O(1)\) prime divisors \(q>Q\).
The sum of \(1/q\) over the selected primes in a single denominator
interval is \(O(1/L)\), by the prime counting upper bound and
\(\log Q\asymp L\). Consequently
\(\sum_{n\asymp M}|\beta_n|^2\ll MJ/L\), including the phases from
the rank expansion. Keeping this union in one bilinear form, the
reciprocal-phase estimate and geometric summation in \(M\) give
\[
 O_R\!\left(
 L\sqrt J\sqrt{U/X}+\sqrt{LJ}\,e^{-\sqrt L/4}\right).
\]
Here the second term uses \(M\gg XQ/N\) and \(J=O(L)\) for the
disjoint dyadic bands that meet the source range. One may always
take the bands disjoint by using the standard dyadic partition.
Both terms vanish under the stated hypothesis.

For example, the uppermost range
\[
 \frac{N^2}{(X-B)L^{10}}\le q\le\frac{N^2}{X-B}
\]
meets \(O(\log L)\) dyadic bands. It admits the explicit cutoff
\(U=X/[L^2(\log L)^3]\) at cost \(O_R(1/\log L)+o(1)\).
This exceeds the global product cutoff by \(L/\log L\).
The remaining high-product terms in these bands still need a signed
estimate.

## Close prime ratios and the zero Poisson mode

The number of close ratios in the top denominator range can be
bounded below without a conjecture about prime quadruples. Fix dyadic
blocks \(p\in[P,2P]\), \(q\in[Q_0,2Q_0]\), with
\(P\asymp N\), \(Q_0\asymp N^2/X\), and with the two prime blocks
disjoint for large \(X\). Write \(L=\log X\).
The prime number theorem on fixed-ratio intervals gives
\(K\gg P Q_0/L^2\) pairs. Their ratios \(p/q\) are distinct by
unique factorization. For any fixed \(\eta>0\), partition their
range into \(O_\eta(X)\) intervals of length
\(\eta P/(Q_0 X)\). If the occupancies are \(k_i\), the number of
ordered distinct pairs in the same interval is
\(\sum_i k_i(k_i-1)\gg_\eta K^2/X\), by Cauchy–Schwarz and
\(K/X\to\infty\). Each such pair satisfies
\[
0< |pq'-p'q|\le 4\eta P Q_0/X .
\]
This bound counts the pairs without invoking a short-interval
equidistribution statement.

For their kernels put \(a=sp/q\), \(b=sp'/q'\), and use
\(G(v)=\int \rho(\xi)e(\xi v)\,d\xi\) from the additive reduction.
For any positive \(a,b\), Plancherel gives the exact identity
\[
 \int_{\mathbb R}G(at-X)\overline{G(bt-X)}\,dt
 =\frac{1}{b}\int \rho(\xi)\rho(a\xi/b)e\bigl(X(a/b-1)\xi\bigr)\,d\xi .
\]
This follows from matching the Fourier frequencies \(a\xi=b\xi'\).
For the close ratios just counted, \(|X(a/b-1)|\ll\eta\).
Choosing \(\eta\) small in terms of \(C\) makes the real part of
the exponential at least \(1/2\) on the support. The integral of
\(\rho(\xi)\rho(a\xi/b)\) is bounded below by a positive constant:
\(\int\rho^2\ge1/C\), and the dilation changes \(\rho\) in \(L^1\)
by \(O(|a/b-1|)\), using its uniformly bounded variation and compact
support. Thus each of these unweighted cross integrals has real part
\(\gg 1/b\). The same conclusion holds with a fixed smooth cutoff
\(W(t/D_0)\) that equals one near both centers \(X/a\) and \(X/b\),
with a margin comparable to \(D_0\asymp X/a\). The part modified by
this cutoff has both kernel arguments of size \(\gg X\) and is
\(o(1/b)\) by sinc decay.

For a smooth compactly supported \(W\) the full Poisson identity
for one pair has terms
\[
 D_0\iint \rho(\xi)\rho(\xi')e\bigl(X(\xi'-\xi)\bigr)
 \widehat W\bigl(D_0(h-a\xi+b\xi')\bigr)\,d\xi\,d\xi',
 \qquad h\in\mathbb Z,
\]
where \(\widehat W(y)=\int W(t)e(-yt)\,dt\). In particular, the
zero mode for the full quadratic energy is the continuous weighted
energy itself. A positive subfamily of its cross integrals alone
gives no lower bound for that full mode or for the discrete energy.
Other cross integrals and path coefficients may carry different
signs. The nonzero modes can have support near
\(h\in[a-Cb,Ca-b]\), an interval of length growing with \(a+b\)
in the top blocks. Bounding those modes together with the remaining
zero-mode terms is still required for a Cauchy–Schwarz argument.
