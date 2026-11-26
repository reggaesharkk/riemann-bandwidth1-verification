# Lower moments and the central window in the tapered square

This note verifies two reductions from the Antigravity work bundle dated
26 November 2026. The joint arithmetic upper bound remains open.

## The first two moments transfer on the same section

Use the row weights in [the localization note](WP84_TAPERED_RESONANCE_LOCALIZATION.md),
the \(R=9000\) band, and \(Y=H_R-I\). Write \(E_w(A)=\sum_iw_iA_{ii}\).
The unweighted first- and second-moment estimates of
[the same-section proof](WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md)
apply at each fixed radius. The lower moment estimates on near-full
contiguous sections are uniform in the location of the section.

Since \(w_i\le1/b\), we have \(n\sum_i w_i^2-1\le n/b-1=o(1)\).
Cauchy–Schwarz and \(n^{-1}\sum_i |Y_{ii}|^2\le\tau(Y^2)=O(1)\)
give \(E_w(Y)-\tau(Y)=o(1)\).
The plateau of rows reached from every short-box shift has length
\(b-k(m-1)\sim n\) and constant weight \(1/b\).
Call it \(J\). As \(Y\) is Hermitian, for \(i\in J\) the row square
\((Y^2)_{ii}\) is at least that of the principal compression \(Y_J\).
Hence
\[
\frac{|J|}{b}\tau_J(Y_J^2)\le E_w(Y^2)\le\frac{n}{b}\tau(Y^2).
\]
Both bounds tend to \(1/3-v_R\), where
\(v_R=\pi^{-2}\sum_{l>R}l^{-2}\). This does not require a sixth-moment
bound or cyclicity in the weighted state.

Consequently the exact polynomial identity from
[§§10–11 of the band note](WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md)
takes the same form in the tapered state. Its variance debit is
\(17049864\,v_{9000}/192959881\), about \(9.95\cdot10^{-7}\) in square
units. The strict upper bound on the signed higher-moment combination
is still required.

## Removing small non-exact ratios at the central frequency

In the localized central window put \(\lambda=\log(u/v)\), where
\(u,v\) are the products of the positively and negatively signed
ordinary primes. By conjugation take \(u>v\).
The small-frequency window implies \(1\le u-v\ll vL\log L/X\).
Thus a non-exact term requires \(v\gg X/(L\log L)\).
In particular the central window has no non-exact terms if one
side is a single prime within the natural cutoff.

For fixed \(v\), put \(h=u-v\). The long box alone bounds the kernel
by \(O(\min(1,v/(Xh)))\) since \(|\log(u/v)|\asymp h/v\).
The short boxes keep the sum over \(h\) to \(h\ll vL\log L/X\).
On any dyadic block \(v\asymp V_0\) the sum of these kernel bounds
over \(h\ge1\) is \(O((V_0/X)\log L)\) when
\(V_0\le XL/\log L\). This follows by separately summing
\(h\le V_0/X\) and the harmonic tail. The coefficient weight is
at most \(O_R(g(v)/V_0)\), with \(g\) the logarithmic prime
weight from the [weighted sieve](WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md#retaining-the-prime-weights-in-the-cubic-sieve).
There are only boundedly many ordered factorizations of each
\(u,v\) at these degrees. At the scales that can contribute,
\(\log V_0\asymp L\). The long-interval case of the weighted sieve
gives \(\sum_{v\asymp V_0}g(v)=O(V_0/L)\).
Geometric summation gives the bound
\[
 O_R\left(\frac{V\log L}{XL}\right)
\]
for all the central non-exact terms with
\(\min(u,v)\le V=o(XL/\log L)\), for degrees through six.
The complement retains central near-equalities at larger products
and the surviving nonzero aliases.

## The paired contribution and the cost of omitting the signed remainder

The Antigravity bundle separately evaluated the contribution of
fully balanced pairs. In this sector the row factor is one.
At fixed radius the same covariance and Wick expansion as in
[the R=6000 audit, §4](WP84_INDEPENDENT_REFEREE_RESPONSE_FOUNDATIONS_AND_GUE.md)
apply with \(R=9000\). Thus the pair moments are the Gaussian
Loewner moments with independent fields \(\alpha,\beta\), with
\(\operatorname{Cov}(\alpha_i,\alpha_j)=\mathbf1_{i=j}/4\),
\(\operatorname{Var}\beta_i=1/6\), and
\(\operatorname{Cov}(\beta_i,\beta_j)=-1/[2\pi^2(i-j)^2]\) for \(i\ne j\).
Pair identifications that repeat a prime beyond its designated pair
have vanishing coefficient mass. Odd paired moments are zero.

The fourth-moment Wick calculation gives, with \(x=\pi^{-2}\) and
\(H_{\nu,R}=\sum_{r=1}^R r^{-\nu}\),
\[
m_4=\frac1{12}+\frac23 H_{2,R}x+
\left(\frac52 H_{2,R}^2-\frac34 H_{4,R}+
      \sum_{r=1}^{2R}D_r^2/r^2\right)x^2,
\]
where \(D_r=H_{1,R}-H_{1,R-r}-1/r\) for \(r\le R\) and
\(D_r=H_{1,R}-H_{1,r-R-1}\) otherwise.
For the sixth moment, pinch to adjacent blocks of size 23 as in
the same audit. Since \(22\le R\), the sixth trace moment of that
block bounds the paired moment from below. The replay coefficients
of the block polynomial in ascending powers of \(x\) are:

    5/72
    2229670667130583/2654320456719360
    2414867557599547079884685634744439/355977407950089464288722452480000
    1260922746777464675015592375843639436751585406530413/42440775379329171729001405552907021867129241600000

These are obtained by summing the products of three Gaussian
covariances over the fifteen matchings of every six-edge closed
walk in the block, then dividing by 23. The supplied two CRT
implementations agreed exactly on replay. At \(R=9000\) the
enclosed fourth moment is about 0.266651653337216 and the block
sixth-moment lower bound is about 0.255101223613.
Together with the second moment and the coefficients in §10 of
the band note, these give a paired contribution of at least
0.13054588 to the frozen square, so the other sectors must
supply a signed saving exceeding 0.02843776 in square units.
Inserting the reference fifth moment \(1/36\) alone would supply
only \(168547680/(36\cdot192959881)\), about 0.02426349.

A separate exact check shows that even refitting the cubic cannot
meet the same numerical threshold on the paired law.
Let \(M\) be its moment matrix indexed by degrees 0 through 3,
and \(v=(1,-1,1,-1)^\mathsf{T}\). Form \(M_0\) from moments
\((1,0,0.333325,0,0.266655,0,0.2551)\), interpreted as rationals.
The exact enclosures \(m_2\in[0.33332,0.33333]\),
\(m_4\in[0.26665,0.26666]\), and \(m_6\ge0.2551\)
give \(M\succeq M_0-10^{-5}I\) by the maximum row-sum bound,
after counting the excess at entry \((3,3)\) separately.
The four leading minors of
\(M_0-10^{-5}I-(1279/10000)vv^\mathsf{T}\) are respectively
\[
 \frac{87209}{100000},\quad
 \frac{3255639147}{20000000000},\quad
 \frac{50973068818331}{8000000000000000},\quad
 \frac{1438023273975321}{1600000000000000000000}.
\]
They are positive. A cubic with coefficient vector \(c\) normalized
by \(c^\mathsf{T}v=1\) therefore has paired squared mean at least
\(1279/10000\). This compares against the fixed numerical threshold.
Changing the rational consumer would also require a new band-error
calculation. The bound concerns the fully paired contribution,
and the arithmetic remainder can have either sign.
