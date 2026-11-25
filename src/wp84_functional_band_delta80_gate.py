#!/usr/bin/env python3
"""Exact gate for the delta=80 functional band theorem.

Checks:
  * exact rational expression for F_80'';
  * global |F_80''|<72 by exact Sturm root counts;
  * rational pi lower bound;
  * R=12000 consumer margin and induced square threshold.
"""

from fractions import Fraction as F
import sympy as sp

x=sp.symbols("x")
A=sp.Rational(43428,13891)
B=sp.Rational(37704,13891)
C=sp.Rational(9660,13891)
P=1-A*x+B*x**2-C*x**3
delta=sp.Rational(80)
g=sp.expand(P**2)
f=sp.factor((delta+1)*g/(g+delta))
fpp=sp.factor(sp.diff(f,x,2))
num,den=map(sp.expand,sp.fraction(fpp))

def integer_poly(expr):
    poly=sp.Poly(expr,x,domain=sp.QQ)
    den_lcm=sp.ilcm(*[c.q for c in poly.all_coeffs()])
    return sp.Poly(sp.expand(expr*den_lcm),x,domain=sp.ZZ)

def no_real_roots(poly):
    # exact real-root count by Sturm
    return sp.count_roots(poly,-sp.oo,sp.oo)==0

def main():
    assert sp.degree(den,x)==18
    # denominator is a positive constant times (P^2+80)^3
    assert sp.simplify(den/(g+80)**3)>0

    qplus=integer_poly(72*den+num)
    qminus=integer_poly(72*den-num)

    assert no_real_roots(qplus)
    assert no_real_roots(qminus)
    assert qplus.eval(0)>0
    assert qminus.eval(0)>0

    # Hence -72 < f'' < 72 globally.
    w0=F(1415,13891)
    h80=F(81)*w0/(F(80)+w0)
    assert h80==F(22923,222539)

    pi_lo=F(333,106)
    C80=F(216)/(pi_lo*pi_lo)
    assert C80==F(2426976,110889)

    R=12000
    charge=C80/R
    ceiling=F(21,200)
    residual=ceiling-h80-charge
    assert residual==F(464637587,2741903019000)
    assert residual>0

    y=ceiling-charge
    square_ceiling=F(80)*y/(F(81)-y)
    assert square_ceiling==F(101698640,996729767)

    allowance=square_ceiling-w0
    assert allowance==F(2323187935,13845573193397)
    assert allowance>0

    # Retaining the displacement weight in the linear term saves sqrt(3).
    inv_sqrt3_upper = F(26, 45)
    assert 3 * inv_sqrt3_upper**2 > 1
    weighted_constant = 72 * (1 + 2 * inv_sqrt3_upper) / pi_lo**2
    assert weighted_constant == F(8719136, 554445)
    weighted_charge = weighted_constant / 9000
    assert weighted_charge < charge
    weighted_y = ceiling - weighted_charge
    weighted_threshold = 80 * weighted_y / (81 - weighted_y)
    assert weighted_threshold == F(41218511120, 403675173611)
    assert weighted_threshold - w0 == F(1365967308355, 5607451836630401)
    assert weighted_threshold > square_ceiling
    print("weighted R=9000 arithmetic target (open): square <", weighted_threshold)

    # Center H at 1 and isolate the exact joint arithmetic moment budget.
    coefficients = list(reversed(sp.Poly(P.subs(x, 1 + x)**2, x).all_coeffs()))
    denominator = 192959881
    assert [v * denominator for v in coefficients] == [
        2229049, -8958000, -17049864, 81188760, 18148176, -168547680, 93315600
    ]
    moments = [1, 0, F(1, 3), 0, F(1, 4), F(1, 36), F(157, 630)]
    assert sum(a*b for a, b in zip(coefficients, moments)) == w0
    assert 0 < -coefficients[2] / (pi_lo**2 * 9000) < F(1, 10**6)
    sixth_ceiling = moments[6] + (weighted_threshold - w0) / coefficients[6]
    assert sixth_ceiling == F(209030582803919701, 837093134013658480)
    moments[6] = F(34, 135)
    assert sum(a*b for a, b in zip(coefficients, moments)) == F(59707895, 578879643)
    hankel = sp.Matrix(4, 4, lambda i, j: moments[i+j])
    assert [hankel[:k, :k].det() for k in range(1, 5)] == [
        1, F(1, 3), F(5, 108), F(127, 46656)
    ]
    at_minus_one = sp.Matrix([1, -1, 1, -1])
    best_square = 1 / at_minus_one.dot(hankel.inv() * at_minus_one)
    assert best_square == F(635, 6159) > weighted_threshold
    print("relaxed model: minimum normalized cubic square =", best_square)

    print("STURM_PLUS_REAL_ROOTS = 0")
    print("STURM_MINUS_REAL_ROOTS = 0")
    print("GLOBAL_CURVATURE_BOUND: |F80''| < 72")
    print("C80 rational upper =",C80,"~",float(C80))
    print("R =",R)
    print("band charge <=",charge,"~",float(charge))
    print("Jensen model cap =",h80,"~",float(h80))
    print("residual below 0.105 =",residual,"~",float(residual))
    print("required square <",square_ceiling,"~",float(square_ceiling))
    print("allowance above w0 =",allowance,"~",float(allowance))
    print("RESULT: WP84_FUNCTIONAL_BAND_DELTA80_R12000_PASS")

if __name__=="__main__":
    main()
