#!/usr/bin/env python3
"""WP84 bounded rationalized Christoffel consumer.

Let P be the exact degree-3 Christoffel minimizer and g=P^2.  For delta>0,

    F_delta(x)=(1+delta) g(x)/(g(x)+delta).

For x<=0, g>=1, hence F_delta>=1.
For all real x, 0<=F_delta<=(1+1/delta)g.

At delta=61 this gives a support-free >79% consumer while F_delta is bounded
and has only six simple nonreal poles.

Exact algebra is SymPy rational; pole locations/residue norms are diagnostic
floating-point summaries.
"""
import sympy as sp

x=sp.symbols("x", real=True)
P=(
    1
    -sp.Rational(43428,13891)*x
    +sp.Rational(37704,13891)*x**2
    -sp.Rational(9660,13891)*x**3
)
g=sp.expand(P**2)
w0=sp.Rational(1415,13891)
delta=sp.Integer(61)
F=sp.cancel((delta+1)*g/(g+delta))

def main():
    # Pointwise identities.
    assert sp.simplify(F-1-delta*(g-1)/(g+delta))==0
    rational_bound_gap = (
        sp.Rational(delta + 1, delta) * g
        - F
        - (delta + 1) * g * g / (delta * (g + delta))
    )
    assert sp.simplify(rational_bound_gap) == 0

    # Denominator is strictly positive on R because g=P^2>=0.
    D=sp.Poly(g+delta,x)
    assert sp.gcd(D,D.diff()).degree()==0

    neg_cap=sp.factor(sp.Rational(delta+1,delta)*w0)
    pos_floor=sp.factor(1-neg_cap)
    simple_floor=sp.factor(1-2*neg_cap)

    assert neg_cap==sp.Rational(87730,847351)
    assert simple_floor==sp.Rational(671891,847351)
    assert simple_floor>sp.Rational(79,100)

    # Partial fractions: F=(delta+1)+sum c_j/(x-z_j),
    # c_j=-delta(delta+1)/(2 P(z_j) P'(z_j)).
    roots=[complex(r) for r in sp.nroots(D.as_expr(),n=50,maxsteps=200)]
    Pp=sp.diff(P,x)
    residues=[]
    for z in roots:
        pz=complex(sp.N(P.subs(x,z),50))
        dpz=complex(sp.N(Pp.subs(x,z),50))
        residues.append(-float(delta*(delta+1))/(2*pz*dpz))

    min_im=min(abs(z.imag) for z in roots)
    sum_abs=sum(abs(c) for c in residues)
    margin=float(simple_floor-sp.Rational(79,100))
    # If every normalized resolvent value at the six poles has error <= eps,
    # the F-statistic error is <=sum|c_j| eps.  Positive-index-to-simple
    # conversion costs an additional factor 2.
    eps_uniform=margin/(2*sum_abs)

    print("delta =",delta)
    print("negative-mass cap =",neg_cap,"~",float(neg_cap))
    print("positive-index floor =",pos_floor,"~",float(pos_floor))
    print("simple-zero ledger floor =",simple_floor,"~",float(simple_floor))
    print("margin above 0.79 =",margin)
    print("pole min |Im| ~",min_im)
    print("sum |residues| ~",sum_abs)
    print("diagnostic equal-per-pole error budget ~",eps_uniform)
    print("poles:")
    for z,c in sorted(zip(roots,residues),key=lambda zc:(zc[0].imag,zc[0].real)):
        print(" ",z," residue ",c)
    print("RESULT: WP84_BOUNDED_CHRISTOFFEL_CONSUMER_PASS")

if __name__=="__main__":
    main()
