# Additive phases at the first mixed cubic alias

For the ordinary-prime mixed cubic at fixed radius, the first alias of the
[localized row average](WP84_TAPERED_RESONANCE_LOCALIZATION.md) can be
written as a signed short sum over integer numerators with an additive
kernel. The total replacement error is \(o(1)\). A constant density on
that integer lattice contributes \(o(1)\) after the window is imposed.
The remaining input is a bound for the weighted semiprime discrepancy.

## Additive reduction

Keep \(T=2\pi X\), \(L=\log X\), the natural cutoff \(N\), and the row
weights of the localization note. Use a section starting at index
\(0\le a=O(XL)\) in the original finite row block. This bound on the starting
index is needed to control the phase replacement. Fix a path and a mixed
sign pattern oriented as \(\lambda=\log(p_1p_2/q)\). Write
\[
u=p_1p_2,\qquad v=u/q-X,\qquad B=200 L\log L.
\]
After localization the entire first alias can be represented by the
window \(|v|\le B\). Enlarging to this window adds only frequencies
outside the smaller localization window, whose total weight after
averaging is \(o(1)\).

Write \(e(x)=\exp(2\pi i x)\) and let \(i\) be the zero-based row within
the section. The carrier is common to the window:
\[
\exp\big(i(T+2\pi(a+i)/L)\lambda\big)
=e(XL)e\big((X+(a+i)/L)\log(1+v/X)\big).
\]
For \(|v|\le B\), the second factor differs from
\(e((1+(a+i)/(XL))v)\) by \(O(B^2/X)\), uniformly in the section.
This follows from the quadratic remainder for \(\log(1+x)\) and the
bound \(a+i=O(XL)\).

In the original row representation \(i=r+J+K_1+\cdots+K_k\), add an
independent uniform variable on \([0,1]\) to each integer uniform
variable. The resulting \(I\) is a shift by \(r\) of a sum of independent
continuous uniforms on intervals of lengths \(b,m,\ldots,m\).
The change in the linearized exponential is \(O(B(k+1)/(XL))\).
Define the continuous additive kernel
\[
G(v)=\mathbb E\, e\big((1+(a+I)/(XL))v\big).
\]
The density of the frequency \(1+(a+I)/(XL)\) is continuous and supported
in a fixed compact interval \([1,C]\). The constant \(C\) depends only on
the section's starting-index bound. Each short uniform factor gives
\(\min(1,XL/(\pi m |v|))\), using the exact sinc formula. Since
\(m\ge X/(2\log L)\), for \(|v|\ge B\),
\[
|G(v)|\le \left(\frac{B}{100|v|}\right)^k.
\]

For each denominator prime \(q\), define \(A_q(u)\) to be \(q\sqrt X\)
times the sum of the original coefficients \(W\) over ordered numerator
prime factorizations in that path and sign pattern. Include only the
original cutoff and any distinctness conditions of the population being
studied. The coefficients include the displacement phase. In the
window they have magnitude \(O_R(1)\) after scaling, since at most two
ordered factorizations give \(u\) and \(q\sqrt X/\sqrt{uq}=O(1)\).
There are \(O(qB)\) possible integer numerators for each \(q\).
The combined absolute error in replacing the two phases is therefore
\[
O_R\!\left(\frac{NB}{\sqrt X}
 \left(\frac{B^2}{X}+\frac{B(k+1)}{XL}\right)\right)=o(1),
\]
using \(N\le X\), \(k=O(L)\) and \(B=200L\log L\).
The first-alias contribution for this path and sign pattern equals
\[
\frac{e(XL)}{\sqrt X}
\sum_{q\le N,\ q\ {\rm prime}}\frac1q
      \sum_{|u-Xq|\le qB} A_q(u) G(u/q-X)+o(1).
\]
All weights on the surviving terms come from the same section. The
opposite signs give the complex conjugate for the corresponding path.

## Constant-density cancellation

Fix a prime \(q>C\). Periodize \(G\) at the lattice spacing \(1/q\).
The sum converges absolutely by the sinc bound. In the convention
\(G(v)=\int \rho(\xi)e(\xi v)\,d\xi\), the resulting Fourier series has
coefficients \(q\rho(qj)\), \(j\in\mathbb Z\). This follows by integration
over a period and Fourier inversion. Every coefficient vanishes because
\(\operatorname{supp}\rho\subset[1,C]\) and \(q>C\). Thus
\[
\sum_{u\in\mathbb Z}G(u/q-X)=0.
\]
Truncating to the window incurs \(O(qB\,100^{-k})\), by summing the
decreasing envelope \((B/(100|v|))^k\) outside the endpoints with mesh
\(1/q\). Consequently one may replace \(A_q(u)\) inside the window by
\(A_q(u)-d_q\) for any uniformly bounded complex constants \(d_q\),
with a total error \(O(\sqrt X B\,100^{-k})=o(1)\).
The finitely many \(q\le C\) contribute \(O_R(B/\sqrt X)=o(1)\) directly. The same subtraction may use \(d_q\,1_{q\nmid u}\).
The multiples of \(q\) provide only \(O(B)\) numerators in the window, so
changing the baseline there costs at most
\(O((B/\sqrt X)\sum_{q\le N}1/q)=o(1)\).

This formulation retains the oscillation ruled out by an absolute-value
estimate of individual prime products. The cancellation shown here is
for a constant reference density. Controlling the actual signed
discrepancy and the coupled higher moments remains open.


## Additional denominator range for the original prime sum

Following Antigravity's review, retain the long uniform factor of
\(G\). Its length divided by \(XL\) tends to one, so
\(|G(v)|\ll\min(1,|v|^{-1})\).
The portion with prime denominators \(q\le Q\) is bounded by
\[
 \ll_R \frac{\log L}{X^{1/4}L}
 +\frac{Q\log L}{\sqrt X L^2}.
\]
Here and below the displayed estimate is for the additive expression.
The replacement of the original row sum also incurs the \(o(1)\) error
proved above.

Indeed, retain the source weights \(g(p)=(\log p)/L\) for \(p\le N\)
and extend them completely multiplicatively with zero at larger primes.
The coefficient of \(G\), including \(1/(q\sqrt X)\), is bounded by
\(C_R g(q)g(u)/(q\sqrt X)\) on this window. For \(q\le X^{1/4}\),
sum the kernel over all integers at mesh \(1/q\). The core and the
\(O(\log B)\) dyadic shells give \(O(q\log L)\). Then
\(\sum_{q\le X^{1/4},\,q\ {\rm prime}}g(q)\ll X^{1/4}/L\).

For \(q>X^{1/4}\), the core and every shell around \(Xq\) have component
intervals of length \(h\ge q\) at scale \(Xq\), with \(h\le 2qB\);
end shells can be enlarged. Since \(q>(2Xq)^{1/8}\) for large \(X\),
the [weighted Shiu estimate](WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md#retaining-the-prime-weights-in-the-cubic-sieve)
bounds their weighted counts by \(O(h/L)\). Multiplying by
\(O(\min(1,q/h))\) costs \(O(q/L)\) per shell before the denominator
weight. Summing over the shells and using
\(\sum_{q\le Q,\,q\ {\rm prime}}g(q)\ll Q/L\) proves the bound.
It tends to zero for every \(Q=o(\sqrt X L^2/\log L)\).
Also \(q\le N^2/(X-B)\) throughout the source window, since
\(u\ge q(X-B)\) and \(u\le N^2\).

## Reciprocal phases in an auxiliary bilinear form

The following bound applies to the dual bilinear form proposed in the
review. It concerns the dual form itself. Passing to it from a term
with sharp cutoffs and two prime-supported variables requires a separate
decomposition with controlled errors.

Let \(\sqrt X\le M\le X\), let \(m\in[M,2M]\), \(n\asymp M\) with fixed
comparison constants, and let \(\rho\) be the frequency density above.
Its longest box has normalized length \(b/(XL)\to1\). Convolution
with a probability measure gives \(\|\rho\|_\infty+\operatorname{Var}(\rho)
=O(1)\), with variation on the full line. If \(|\alpha_m|\le A\) and
\(\sum_n|\beta_n|^2\ll M/L\), then
\[
\left|\frac1{\sqrt X M}\sum_m\alpha_m\sum_n
       \beta_n\,\rho(n/m)e(-Xn/m)\right|
\ll A\left(\sqrt{\frac MX}+\frac{X^{1/4}}{\sqrt{ML}}\right).
\]
The implied constants are independent of \(M\) and \(X\).

Cauchy–Schwarz in \(n\) and summation by parts reduce the square to
\(O(A^2/(XML))\) times
\[
 \sum_{m,m'\in[M,2M]}
   \min\big(M,\|X(1/m-1/m')\|^{-1}\big).
\]
The minimum at an integer is interpreted as \(M\). The product of the
two density factors has bounded variation, so the geometric-sum
estimate applies uniformly.

Assign each pair to a nearest integer \(h\) to \(X(1/m-1/m')\).
For \(h=0\), the diagonal costs \(O(M^2)\); the other pairs cost
\(O(M^3\log M/X)\) from the harmonic sum in \(|m-m'|\).
For nonzero \(|h|\ll X/M\), put \(f_h(x)=x/(1-hx/X)\).
If \(h>0\) and \(1-hm/X<1/4\), then
\(X(1/m-1/m')-h=(X/m)(1-hm/X-m/m')\) has magnitude at least \(1/4\).
Such pairs cost \(O(1)\) each. Otherwise the denominator lies in
\([1/4,4]\) (the upper bound follows from \(|h|\le X/(2M)+1/2\)).
There \(f_h(m)\asymp M\) and
\[
 |X(1/m-1/m')-h|\asymp (X/M^2)|m'-f_h(m)|.
\]
The integers other than a closest one to \(f_h(m)\) cost
\(O(M^2\log M/X)\) per \(m,h\), summing to \(O(M^2\log X)\).
It remains to count \(m\) with \(f_h(m)\) near an integer.

On the interval with denominator in \([1/4,4]\),
\(|f_h''|\asymp |h|/X\). Erdős–Turán with frequency cutoff comparable
to \(1/s\), and the van der Corput second derivative bound
\(O(M\sqrt{j|h|/X}+\sqrt{X/(j|h|)})\) for the \(j\)-th frequency, give
\[
 \#\{m:\|f_h(m)\|\le s\}
 \ll Ms+M\sqrt{|h|/(Xs)}+\sqrt{X/|h|},
 \qquad 0<s\le 1/2.
\]
Use the core \(s\le M/X\) and dyadic shells up to \(1/2\), with the
weight capped by \(M\) in the core. When \(M/X\ge1/2\), use just the
core and the same count with \(s=1/2\).
The three terms above contribute, respectively,
\(O(M^2\log X/X)\), \(O(M^{3/2}\sqrt{|h|})\), and
\(O(M\sqrt{X/|h|})\) for each \(h\).
Summing up to \(O(X/M)\) gives
\(O(M^2\log X+X^{3/2})\), using \(M\le X\).
Substitution proves the displayed bilinear estimate.

The bound provides decay for bounded \(A\) in the interior where
\(M/X=o(1)\) and \(\sqrt X/(ML)=o(1)\).
The remaining prime-supported terms in a Type-II decomposition and the
joint fourth- through sixth-moment estimate remain open for the
original matrix.
