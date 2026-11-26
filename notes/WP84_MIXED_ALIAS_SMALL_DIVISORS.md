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
