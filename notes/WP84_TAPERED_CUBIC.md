# A row average for the bounded WP84 consumer

At fixed radius R=9000, a positive row taper gives an alternative sufficient
square inequality for the bounded delta-80 consumer. In this alternative,
the entire ordinary-prime same-sign cubic population is o(1) in absolute
value after row averaging. This includes products near all allowed aliases.
The sharp-section third moment and the signed higher-moment gate remain open.

## Finite transfer

Use the n-row matrix and normalization of [the band theorem, §9](WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md).
Number the rows from 0 to n−1. Put L=log X, m=floor(n/L),
r=6R and b=n−2r−m+1. Consider sufficiently large X so both lengths
are positive. Independently choose J and K uniformly from 0,…,b−1
and 0,…,m−1. Give row i the probability w_i=Pr(r+J+K=i).
The support is [r,n−1−r], and w_i≤1/b. Define
E_w(A)=sum_i w_i A_ii. For every Hermitian A and 0≤F≤M,

    |E_w(F(A)) − tau F(A)| ≤ M(1−b/n).

Indeed the total variation distance from uniform is at most 1−b/n:
min(w_i,1/n)≥(b/n)w_i. The spectral measure obtained by mixing row
spectral measures with weights w_i is a probability measure. With
h(t)=81t/(80+t), Jensen therefore gives

    tau F80(H_R) ≤ h(E_w(P(H_R)^2)) + 81(1−b/n).

The error tends to zero. Apply the original full-to-band estimate with its
original unweighted trace. The sufficient bound for the full bounded
statistic is consequently the same numerical threshold in a new state:

    limsup E_w(P(H_R)^2) < 41218511120/403675173611
       implies limsup tau F80(H) < 21/200.

This argument transfers bounded functions. It does not infer that the
unweighted polynomial square has the same mean. Every term used to
estimate the weighted square must be evaluated or justified in this state.
The independent prime-to-Weil and zero-count transfers still apply as
obligations under their own hypotheses.

## Extra decay of the row kernel

The margin r ensures that no path of at most six band steps started at a
weighted row exits the section. For each path the entire row sum is thus
a product of two normalized geometric sums, times a phase of modulus one.
With the original step 2π/L, t=dist(λ,Lℤ), n asymptotic to TL/(2π),
b asymptotic to n and m asymptotic to n/L, this gives

    |K_w(λ)| ≪ min(1,1/(Tt)) min(1,L/(Tt)).

Use the trivial bound at t=0. Displacement phases, the original height
and the original prime cutoff N=floor(exp(L−√L)) are retained.

## The ordinary-prime same-sign cubic

Write u=pqr. The positive signs have λ=log u; reflection gives the same
absolute bound for negative signs. At fixed R there are O_R(1) paths,
at most six prime orderings per u, and coefficient weight
O_R(g(u)/√u) with g the completely multiplicative prime weight of
[the cubic sieve note](WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md#retaining-the-prime-weights-in-the-cubic-sieve).
Use its modulus-one Shiu estimate: at scale X² and interval length
h≥X up to a constant multiple of X², the weighted count is O(h/L),
using a bounded number of intervals where necessary.

- For X/2≤u≤2X, retain the first kernel factor. The nearest integers
  cost O_R(1/√X). Summing the inverse distances to X costs
  O_R((1+L)/√X), using g≤1.
- For X²/2≤u≤2X², write H=|u−X²|. The core H≤X costs O_R(1/L).
  Each shell h<H≤2h with h≥X has weight including the kernel at most
  O_R((1/L) min(1,LX/h)) after summing over products: the two factors
  save O(X/h) and O(min(1,LX/h)), respectively. There are O(1+log L)
  dyadic shells through LX, and the rest form a geometric tail. End
  shells use the comparable-scale interval enlargements of the sieve note.
- Elsewhere 2≤u≤N³ and t≥log 2 for large X: the first two comparable
  ranges were removed and 3L−log u≥3√L. Both kernel factors together
  cost O(L/T²). Summing u^(-1/2) through N³ costs O(N^(3/2)).

Hence the whole absolute sum is
O_R((1+L)/√X + (1+log L)/L + LN^(3/2)/T²) = o(1).
Absolute values here apply to each path/product **after** its row sum.
No signed gain is assigned to this vanishing population. In particular,
mixed-sign ratios near X with large denominator, and weighted fourth
through sixth moments, are outside the conclusion.
