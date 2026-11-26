# The zero-count transfer needed by WP84

The finite inertia implication can be proved directly. Its application
requires a comparison between the actual WP84 prime-side matrix and a
zero-side compression on a matched interval. That comparison remains open.

## Finite transfer criterion

Let \(Z\) count zeros with multiplicity in a finite interval whose set of
zeros is closed under \(\rho\mapsto1-\overline\rho\).
Let \(S\) count the simple critical-line zeros in that interval.
Suppose a Hermitian \(d\times d\) matrix has a representation
\[
 H=A^* D A+K+E
\]
with Hermitian \(K,E\). Here \(D\) is a block form for those zeros,
with at most one positive direction for each distinct on-line zero
and each off-line reflection pair.

Write \(b=n_+(D)\). Every block beyond the \(S\) simple on-line zeros
uses at least two units of multiplicity, so \(b\le (Z+S)/2\).
Pullback cannot increase positive inertia. For \(\epsilon>0\), take
the intersection of \(\ker K\), a nonpositive subspace of \(A^*DA\),
and the spectral subspace \(E\le\epsilon\). The codimension of this
intersection is at most \(b+\operatorname{rank}K+n_{>\epsilon}(E)\).
On it \(H\le\epsilon\) in quadratic-form sense. The min–max principle
and the bound \(n_{>\epsilon}(E)\le\|E\|_1/\epsilon\), where the
norm is the sum of the singular values, give
\[
 S\ge 2 n_{>\epsilon}(H)-Z-2\operatorname{rank}K
           -2\|E\|_1/\epsilon.
\]

Now suppose \(d/Z\to1\), \(\operatorname{rank}K=o(d)\), and
\(\|E\|_1=o(d)\). Take \(\epsilon\to0\) slowly enough that
\(\|E\|_1/\epsilon=o(d)\). For the nonnegative bounded WP84
consumer \(F_{80}\), the scalar majorant on \(x\le0\) and continuity
at zero give \(\inf_{x\le\epsilon}F_{80}(x)\ge1-o(1)\).
Therefore \(n_{>\epsilon}(H)/d\ge1-\tau F_{80}(H)-o(1)\), and
\[
\liminf S/Z\ \ge\ 1-2\limsup\tau F_{80}(H).
\]
Under these matched hypotheses a trace limsup strictly below
\(21/200\) gives a simple-zero fraction strictly above \(79\%\)
on the corresponding intervals. An overall counting theorem
also needs interval coverage and error control in its stated range.

## What the external theorem supplies

Alpöge and Furman prove an on-line rank-one and off-line paired
block structure for their own finite Weil compression. In their
Proposition 4.1 the reflected off-line pair contributes a difference
of two real rank-one matrices and hence at most one positive direction.
The same block count above applies whenever that representation is
proved for the chosen compression. Their 67.25% result uses their
window and rank–trace estimates. [Alpöge–Furman, §§3–6](https://arxiv.org/html/2608.13637v2#S4)

The target for WP84 is the actual source comparison in its own
normalization: construct the block form on the matched zero interval,
identify the scalar background and taper, and bound the remaining
error by \(K\) and \(E\) as above or by an estimate that gives equivalent
inertia control. Establish \(d/Z\to1\) for the same interval.
A positive density of unaccounted scalar background can affect
positive inertia, so that term needs explicit identification.
The full-to-band inequality compares two prime-side matrices and
supplies no such source comparison.

The November RH proof concerns zero locations. On the zero side,
RH removes the off-line blocks once the correct form is identified,
and multiplicities still enter the block count. The finite argument
above already accommodates off-line pairs, so it requires no RH
assumption. The WP84 arithmetic inequality remains a separate
open input.
