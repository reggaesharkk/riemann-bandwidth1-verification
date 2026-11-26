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
