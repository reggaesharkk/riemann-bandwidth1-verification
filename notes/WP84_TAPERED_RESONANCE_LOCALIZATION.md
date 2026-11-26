# Localizing the tapered WP84 moment sum

For fixed radius $R=9000$, a positive row average localizes every
moment through degree six to logarithmic frequencies within
$100L\log L/X$ of $L\mathbb Z$, where $L=\log X$. It leaves the
numerical threshold of the [bounded consumer](WP84_TAPERED_CUBIC.md)
valid as a sufficient condition. The remaining resonant terms still
require a signed estimate.

## Row weights and transfer

Use the same source, $n\sim XL$ consecutive rows, and band matrix
$H_R=I+Y_R$ as in the [two-interval argument](WP84_TAPERED_CUBIC.md).
For large $L$, set
$$
k=\lceil L\rceil,\qquad m=\left\lfloor\frac{n}{k\log L}\right\rfloor,
\qquad r=6R,\qquad b=n-2r-k(m-1).
$$
Give row $i$ weight $w_i$ equal to the probability that
$r+J+K_1+\cdots+K_k=i$, where $J$ is uniform on $[0,b-1]\cap\mathbb Z$
and the independent $K_j$ are uniform on $[0,m-1]\cap\mathbb Z$.
Then $b/n\to1$, $m\sim X/\log L$, the support is inside
$[r,n-1-r]$, and $w_i\le 1/b$ by conditioning on all short shifts.
Writing $E_w(A)=\sum_i w_i A_{ii}$, the same total-variation argument
as for the two-interval average gives
$$
\tau F_{80}(H_R)
\le h_{80}\big(E_w(P(H_R)^2)\big)+81(1-b/n).
$$
The transfer error is $O(1/\log L+R/n)=o(1)$. With the same unweighted
full-to-band estimate, the square threshold remains
$41218511120/403675173611$ in this weighted state.

## Logarithmic frequency windows

For any path of length $j\le 6$ the row support ensures every vertex
stays inside the section. The exact row sum at frequency $\lambda$
has a unit-modulus phase times
$$
D_b(z)D_m(z)^k,\qquad
 D_s(z)=s^{-1}\sum_{v=0}^{s-1}e^{ivz},\quad z=2\pi\lambda/L.
$$
All original displacement phases and the height carrier stay in the
moment expansion. If $t=\operatorname{dist}(\lambda,L\mathbb Z)$
is positive, the geometric-sum formula gives
$$
|D_m(z)|\le\min(1,L/(2mt))
$$
using $\sin(\pi t/L)\ge 2t/L$ for $t\le L/2$.
For large $X$ one has $m\ge X/(2\log L)$.
Thus $t\ge 100L\log L/X$ gives a kernel at most
$100^{-k}\le X^{-\log 100}$.

This decay can be summed even against the complete coefficient mass.
There are $O_R(1)$ paths and sign patterns for each $j\le6$.
The [entry expansion](WP84_STRICT79_HOSTILE_AUDIT_AND_BALANCED_PAIR_REDUCTION.md)
bounds the weight per slot by $C_R/\sqrt u$. This holds for all
$u=p^a\le N$, since $\Lambda(u)\le\log u\le L$, the normalization
tends to one, and the fixed-radius Fourier factors are bounded. The
total absolute weight before the row kernel is at most
$C_R N^{j/2}\le C_R X^3$, even if repeated bases and complete prime
powers are retained. Consequently the terms outside the indicated
windows cost $O_R(X^{3-\log 100})=o(1)$ in each of the six moments
and in the polynomial square. No moment size estimate is used here.

For mixed cubic words written $\lambda=\log(p_1p_2/q)$, the natural
cutoff gives $4/N\le p_1p_2/q\le N^2/2$. Only the central window and
the first positive alias can intersect this range for large $X$.
In the first alias the localized estimate uses
$$
|p_1p_2-Xq|\le 200q L\log L,
$$
by exponentiating the logarithmic window. The reversed sign pattern has
the reflected windows. Exact resonances are retained at all degrees.
The core obstruction in the two-interval note applies to these positive
row weights as well. Closing the weighted square needs a joint bound
on the surviving frequencies and the subsequent transfers to the zero count.
