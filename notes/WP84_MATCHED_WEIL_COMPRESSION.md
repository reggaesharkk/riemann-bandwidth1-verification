# Matching the WP84 sharp matrix to a Weil compression

For the radius-9000 route, let \(H\) be the full sharp WP84 prime
matrix with diagonal background \(1\), before hard band truncation.
Use \(X=T/(2\pi)\), \(L=\log X\), \(N=\lfloor Xe^{-\sqrt L}\rfloor\),
\(d=\lfloor XL\rfloor\) and \(t_j=T+2\pi j/L\), \(0\le j<d\).
The prime coefficients are \(-\Lambda(n)/(a_\phi L\sqrt n)\) with
\(a_\phi\to1\). The comparison below also applies if the WP84
matrix keeps ordinary primes only.

Take the rectangular choice \(\psi_0\) in
[Alpöge–Furman, §§2.1–2.3](https://arxiv.org/html/2608.13637v2#S2),
with their smooth unit-width endpoint taper \(\phi\) and
\(a=\|\phi\|_2^2/L=1+O(L^{-1})\).
Their full zero sum is \(\widetilde G+\widetilde E\).
With the diagonal unitary \(U_{jj}=(-1)^j\), we have
\[
 \|H-U(\widetilde G+\widetilde E)U^*\|_1=o(d).
\]
The estimate transfers to any principal section of size \(d-o(d)\).

## Background and pole

The explicit formula writes the full zero matrix as an integral
of the real rank-one outer product of
\((\widehat\phi(\tau-t_j))_j\) against
\((\mu(\tau)+\Pi_X(\tau)+P_X(\tau))/(aL^2)\).
On \([T/2,3T]\) the differences \(\mu-L/(2\pi)\) and
\(\Pi_X\) are uniformly \(O(1)\), by (2.3)–(2.4) of that paper.
Parseval gives \(\int |\widehat\phi(\tau-t_j)|^2\,d\tau=2\pi aL\).
Outside this interval, the bound \(O(|\tau-t_j|^{-2})\) for
\(\widehat\phi\) and the logarithmic growth bound for \(\mu\) make
the integral of
\((|\mu-L/(2\pi)|+|\Pi_X|)|\widehat\phi(\tau-t_j)|^2\)
\(O(LT^{-3})\), uniformly in \(j\).
The rank-one trace-norm bound and the factor \(1/(aL^2)\) therefore
give \(O(d/L)\) for replacing the background and pole by \(L/(2\pi)\).

By Fourier inversion, this constant background has entries
\[
 a^{-1}\int_{-1/2}^{1/2} w(x)^2 e^{-2\pi i (j-i)x}\,dx,
 \qquad w(x)=\phi(Lx).
\]
It differs from the identity by \(O(d/L)\) in trace norm. Indeed,
\(w^2-1\) is supported on two strips of total length \(O(L^{-1})\)
in this interval, \(a^{-1}=1+O(L^{-1})\), and a Fourier compression
of multiplication by \(g\) has trace norm at most \(d\int|g|\).
The last bound follows by integrating outer products of the vector
of \(d\) Fourier exponentials, of squared norm \(d\).

## Prime entries and the taper error

Put \(l=j-i\), \(s_n=\log n/L\). The positive-frequency prime term at
\(n\le X\) is the coefficient \(-\Lambda(n)/(aL\sqrt n)\) times
\[
 e^{it_i\log n}\int_{-1/2}^{1/2}w(x)w(x+s_n)e^{-2\pi ilx}\,dx ,
\]
with \(w\) extended by zero. The negative-frequency term uses
\(-s_n\) and \(e^{-it_i\log n}\). These formulas follow by Fourier
inversion in the explicit-formula integral for the corresponding
exponential in the cosine sum \(P_X\). In particular, the factor
\(2\pi\) from inversion cancels \(1/(2\pi)\) from that exponential's
coefficient in \(P_X\).

For the rectangle \(w_0=1_{[-1/2,1/2]}\), the positive shift integral
is \(1-s_n\) when \(l=0\), and otherwise it is
\[
 (-1)^l\frac{1-e^{2\pi i l s_n}}{2\pi i l}.
\]
The negative shift integral gives the conjugate. Conjugation by \(U\)
removes the parity factor, which gives exactly the diagonal and
off-diagonal kernels in the [WP84 entry formula](WP84_STRICT79_HOSTILE_AUDIT_AND_BALANCED_PAIR_REDUCTION.md).
This identifies the coefficient sign, the grid, and the matrix
background in the same normalization.

For one sign at a time, Parseval over the unrestricted column index
bounds the squared row error by an integral of
\[
 \left|\sum_{2\le n\le X} c_n e^{\pm it_i\log n} b_n(x)\right|^2,
 \qquad c_n=-\Lambda(n)/(aL\sqrt n).
\]
Here \(b_n\) is the difference between the tapered overlap and the
retained rectangular overlap at \(n\le N\). For \(n\le N\) it is bounded
and supported on endpoint strips of total length \(O(L^{-1})\),
uniformly in \(n\). For \(N<n\le X\), \(|b_n|\le1\).
The frequencies \(\log n/L\) for \(2\le n\le X\) are separated
modulo one by \(\gg1/(XL)\): consecutive gaps have that size or
larger, and the wraparound gap is at least \(\log 2/L\).
The same separation holds for the negative sign. The
[dual discrete large sieve](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf)
over \(d\asymp XL\) consecutive rows bounds the integrated average
by \(O(\sum_n |c_n|^2\int|b_n|^2)\).
There is no need to combine the two sign sets in this estimate.
By (5.6) of Alpöge–Furman,
\(\sum_{n\le X}|c_n|^2=O(1)\) and
\(\sum_{N<n\le X}|c_n|^2=O(L^{-1/2})\).
Thus the squared Hilbert–Schmidt error divided by \(d\) is
\(O(L^{-1/2})\), which gives trace norm \(O(dL^{-1/4})\).
The same argument bounds the normalized Hilbert–Schmidt size of
the retained prime matrix by \(O(1)\), so replacing \(a\) by \(a_\phi\)
costs \(o(d)\) in trace norm.
If only ordinary primes are retained, the sum of squared coefficients
of proper powers is \(O(L^{-2})\), since
\(\sum_p(\log p)^2\sum_{j\ge2}p^{-j}<\infty\).
This costs another \(O(d/L)\) in trace norm.

## Application to the finite count

Use the smoothed zero form \(\widetilde G\) on \(I'=[T-\sqrt T,2T+\sqrt T)\).
Alpöge–Furman Proposition 4.3 gives
\(\|\widetilde E\|_1=o(1)\) for that taper, and their zero counts give
\(Z(I')/d\to1\) and \(Z(I'\setminus[T,2T))=o(d)\).
Their Proposition 4.1 supplies the block inertia hypotheses of the
[finite WP84 criterion](WP84_ZERO_COUNT_TRANSFER.md).
Conjugation and principal compression preserve the representation
as a pullback. Trace norm does not increase under principal
compression, so the comparison applies on every such section
of dimension \(d-o(d)\), with no rank error needed.
This gives the zero-side comparison for the specified sharp-matrix
route, and the exceptional endpoint count can be removed at \(o(d)\)
cost. The arithmetic upper bound on the bounded consumer remains open.
