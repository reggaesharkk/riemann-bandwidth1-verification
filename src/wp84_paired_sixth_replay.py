"""Exact small-section Wick polynomial for the paired sixth-moment difference."""
import argparse
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import pi


@lru_cache(None)
def covariance(a, b):
    """Return coefficient and degree in x=pi^-2 for a nonzero covariance."""
    i, j = a
    k, l = b
    if i == j and k == l:
        if i == k:
            return Fraction(1, 6), 0
        return Fraction(-1, 2 * (i-k)**2), 1
    if i == j or k == l:
        return 0, 0
    numerator = int(i == k) - (i == l) - (j == k) + (j == l)
    return Fraction(numerator, 4 * (j-i) * (l-k)), 1


@lru_cache(None)
def wick(edges):
    if not edges:
        return (1, 0, 0, 0)
    coeff = [0] * 4
    for i in range(1, len(edges)):
        scale, shift = covariance(edges[0], edges[i])
        if scale:
            sub = wick(edges[1:i] + edges[i+1:])
            for degree in range(4-shift):
                coeff[degree+shift] += scale * sub[degree]
    return tuple(coeff)


def difference(n, radius):
    coeff = [Fraction(0) for _ in range(4)]
    for vertices in product(range(n), repeat=6):
        edges = tuple(zip(vertices, vertices[1:] + vertices[:1]))
        if any(abs(a-b) > radius for a, b in edges):
            weight = wick(tuple(sorted(tuple(sorted(edge)) for edge in edges)))
            for i, value in enumerate(weight):
                coeff[i] -= value
    return [value/n for value in coeff]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=6)
    parser.add_argument("--radius", type=int, default=2)
    args = parser.parse_args()
    if args.size < 1 or args.radius < 0:
        parser.error("size must be positive and radius nonnegative")
    coefficients = difference(args.size, args.radius)
    print("Coefficients in ascending powers of pi^-2:", *coefficients)
    print("Difference:", sum(float(c)/pi**(2*i) for i, c in enumerate(coefficients)))
