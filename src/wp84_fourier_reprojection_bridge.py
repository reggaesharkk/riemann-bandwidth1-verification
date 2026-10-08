#!/usr/bin/env python3
"""WP84 reprojection proof diagnostics and independent exact scalar checks.

The asymptotic theorems are proved in the companion notes. Numerical finite
checks here do not assert a prime-law limit or a simple-zero theorem.
"""
from fractions import Fraction as F
import argparse


def joint_budget():
    a = [F(-19101,185500),F(961,3710),F(31,50),F(-371,500)]
    c = [sum((a[j]*a[k-j] for j in range(4) if 0<=k-j<4),F(0))
         for k in range(7)]
    assert sum(a[j]*F(-1)**j for j in range(4))==1
    assert c[4]==0
    assert c[5]==-F(11501,12500) and c[6]==F(137641,250000)
    mu=[F(1),F(0),F(1,3),F(0),F(0),F(1,36),F(34,135)]
    erob=sum((x*y for x,y in zip(c,mu)),F(0))
    assert erob==F(240421959557,2322691875000)
    pi_lower=F(333,106)
    band=3*F(137721,5000)/(pi_lower*pi_lower*6000)
    variance=-c[2]*2/(pi_lower*pi_lower*6000)
    M=F(21,200)-erob-band-variance
    assert M==F(52897896569489,572357731837500000)
    print('CLOSED exact joint budget:',-c[5],c[6],M)
    print('single-error limits:',M/(-c[5]),M/c[6])
    print('single-error decimals:',float(M/(-c[5])),float(M/c[6]))


def half_interval_coefficients(d):
    """Exact leakage = a + b/pi^2, by Parseval for the half interval."""
    h1=sum((F(1,r) for r in range(1,d+1,2)),F(0))
    h2=sum((F(1,r*r) for r in range(1,d+1,2)),F(0))
    return F(d,4),2*(h1-d*h2)


def independent_prior_checks():
    import sympy as sp
    pi=sp.pi
    U=sp.Matrix([[sp.Rational(1,2),-sp.I/pi],[-sp.I/pi,-sp.Rational(1,2)]])
    actual=sp.simplify(sp.trace(U*sp.conjugate(U.T))/2)
    assert actual==sp.Rational(1,4)+1/pi**2
    a,b=half_interval_coefficients(2)
    assert (a,b)==(F(1,2),F(-2))
    assert sp.simplify(sp.Rational(1,2)-actual-(sp.Rational(a.numerator,a.denominator)
                         +sp.Rational(b.numerator,b.denominator)/pi**2)/2)==0
    # Re-evaluate the old C6 witnesses from the existing partition constructor.
    from wp84_c5_pointwise_supercritical_sign import compile_terms
    terms=compile_terms(6)
    assert len(terms)==1082
    for v,expected in [((F(-7,10),F(4,5),F(-7,10),F(3,5),F(-2,5),F(2,5)),F(2,5)),
                       ((F(-1,10),F(3,10),F(-1,5),F(-3,10),F(4,5),F(-1,2)),-F(1,10))]:
        value=F(0)
        assert sum(v)==0
        for sign,masks in terms:
            pos=[F(0)]+[sum((v[j] for j in mask),F(0)) for mask in masks]
            value+=sign*max(F(0),1-max(pos)+min(pos))
        assert value==expected
    print('CLOSED independent prior witness checks: compression and C6 signs')


def numeric_checks():
    import mpmath as mp
    mp.mp.dps=60
    tolerance=mp.mpf('1e-50')
    def M(q):
        if isinstance(q,F):
            return mp.mpf(q.numerator)/q.denominator
        return mp.mpf(q)
    def coefficient(r,left,length):
        if r==0:
            return length
        return (mp.exp(2j*mp.pi*r*(left+length))-mp.exp(2j*mp.pi*r*left))/(2j*mp.pi*r)
    def entry(m,n,left,length,y,carrier=0):
        return mp.exp(1j*carrier*y+2j*mp.pi*n*y)*coefficient(n-m,left,length)
    def U(y,d,carrier=0):
        left=max(mp.mpf(0),-y)
        length=max(mp.mpf(0),min(mp.mpf(1),1-y)-left)
        return mp.matrix([[entry(m,n,left,length,y,carrier) for n in range(d)]
                          for m in range(d)])
    def tr(A):
        return sum((A[i,i] for i in range(A.rows)),mp.mpc(0))
    def harmonic(d):
        return sum((mp.mpf(1)/r for r in range(1,d+1)),mp.mpf(0))
    # Direct numerical integration checks the Fourier-entry derivation independently.
    for m,n,left,length,y in [(0,0,M(F(1,7)),M(F(2,5)),M(F(1,9))),
                              (-3,4,M(F(1,8)),M(F(3,7)),M(F(-1,11))),
                              (5,-2,M(F(1,6)),M(F(1,3)),M(F(1,5)))]:
        direct=mp.exp(2j*mp.pi*n*y)*mp.quad(
            lambda x:mp.exp(2j*mp.pi*(n-m)*x),[left,left+length])
        assert abs(direct-entry(m,n,left,length,y))<tolerance
    print('CLOSED finite diagnostic: direct Fourier coefficient integrals PASS')
    # Half-interval exact closed form vs a finite leakage sum plus analytic tail enclosure.
    for d in (1,2,7,31,128):
        a,b=half_interval_coefficients(d)
        exact=M(a)+M(b)/mp.pi**2
        cutoff=10000
        partial=2/mp.pi**2*sum((mp.mpf(min(d,r))/(r*r)
                                for r in range(1,cutoff+1,2)),mp.mpf(0))
        tail_upper=2*d/(mp.pi**2*cutoff)
        assert partial<=exact+tolerance and exact<=partial+tail_upper+tolerance
        assert exact<=2*(harmonic(d)+1)/mp.pi**2+tolerance
    print('CLOSED half-interval series formula; finite tail-enclosure checks PASS')
    max_ratio=mp.mpf(0)
    for d in (3,9,17):
        for shifts in [(F(1,2),F(-1,2)),
                       (F(1,5),F(-1,7),F(1,4),F(-1,3),F(11,420)),
                       (F(1,3),F(-1,5),F(1,7),F(-1,4),F(1,6),F(-1,11))]:
            ys=list(map(M,shifts)); b=len(ys)
            carrier=M(F(17,3))
            A=mp.eye(d)
            for y in ys:
                A=A*U(y,d,carrier)
            positions=[mp.mpf(0)]
            for y in ys:
                positions.append(positions[-1]+y)
            overlap=max(mp.mpf(0),1-max(positions)+min(positions))
            Y=positions[-1]
            model=overlap*mp.exp(1j*carrier*Y)*sum(
                (mp.exp(2j*mp.pi*k*Y) for k in range(d)),mp.mpc(0))/d
            error=abs(tr(A)/d-model)
            bound=2*(b-1)*(harmonic(d)+1)/(mp.pi**2*d)
            assert error<=bound+tolerance
            max_ratio=max(max_ratio,error/bound)
    print('CLOSED finite diagnostic: sharp words b=2,5,6 PASS; max error/bound',mp.nstr(max_ratio,8))
    # The missing fixed-R filter gap has an explicit closed-pair formula.
    for R in (0,1,2,7,6000):
        gap=mp.mpf(1)/4-2/mp.pi**2*sum(
            (mp.mpf(1)/(r*r) for r in range(1,R+1,2)),mp.mpf(0))
        assert gap>0
        if R==6000:
            lo=1/(mp.pi**2*6001)
            hi=lo+2/(mp.pi**2*6001**2)
            assert lo<=gap<=hi
            print('CLOSED fixed-R sharp replacement FALSIFIED; g6000=',mp.nstr(gap,18))
    # Independently check the fixed-band filtered-word zero-frequency coefficient.
    def filtered_overlap(ys,R):
        coefficients={0:mp.mpc(1)}
        prefix=mp.mpf(0)
        for y in ys:
            left=max(mp.mpf(0),-y)
            length=max(mp.mpf(0),min(mp.mpf(1),1-y)-left)
            factor={r:coefficient(-r,left,length)*mp.exp(2j*mp.pi*r*prefix)
                    for r in range(-R,R+1)}
            merged={}
            for p,a in coefficients.items():
                for r,c in factor.items():
                    merged[p+r]=merged.get(p+r,mp.mpc(0))+a*c
            coefficients=merged
            prefix+=y
        return coefficients.get(0,mp.mpc(0))
    for R in (0,1,3):
        pair=filtered_overlap([M(F(1,2)),M(F(-1,2))],R)
        same=filtered_overlap([M(F(1,2)),M(F(1,2))],R)
        expected=mp.mpf(1)/4+2/mp.pi**2*sum(
            (mp.mpf(1)/(r*r) for r in range(1,R+1,2)),mp.mpf(0))
        assert abs(pair-expected)<tolerance
        assert abs(same-(mp.mpf(1)/2-expected))<tolerance
    print('CLOSED finite diagnostic: filtered overlap and wrap-alias witnesses PASS')
    # Group actual prime fields first, retaining proper powers as explicit coefficients.
    T=mp.mpf(23); L=mp.log(T); d=int(mp.floor(T*L/(2*mp.pi))); R=1
    ns=(2,3,4,5,7,8,9)
    lam={2:mp.log(2),3:mp.log(3),4:mp.log(2),5:mp.log(5),7:mp.log(7),
         8:mp.log(2),9:mp.log(3)}
    c={n:-lam[n]/(L*mp.sqrt(n)) for n in ns}
    def fields(i):
        t=T+2*mp.pi*i/L
        Q=sum((c[n]*mp.exp(1j*t*mp.log(n)) for n in ns),mp.mpc(0))
        Q1=sum((c[n]*(1-mp.log(n)/L)*mp.exp(1j*t*mp.log(n))
                 for n in ns),mp.mpc(0))
        return Q.imag,2*Q1.real
    for b in (5,6):
        indices=list(range(-b*R,d+b*R))
        f={i:fields(i) for i in indices}
        def block_entry(i,j):
            if abs(j-i)>R:
                return mp.mpf(0)
            if i==j:
                return f[i][1]
            return (f[i][0]-f[j][0])/(mp.pi*(j-i))
        ambient=mp.matrix([[block_entry(i,j) for j in indices] for i in indices])
        X=mp.matrix([[block_entry(i,j) for j in range(d)] for i in range(d)])
        power=ambient**b
        actual=tr(X**b)/d
        single=sum((power[indices.index(i),indices.index(i)] for i in range(d)),mp.mpf(0))/d
        root_diff=[(X**b)[i,i]-power[indices.index(i),indices.index(i)] for i in range(d)]
        for i in range(b*R,d-b*R):
            assert abs(root_diff[i])<tolerance
        local_sites=[i for i in indices if abs(i)<=2*b*R or abs(i-(d-1))<=2*b*R]
        Fscore=sum((f[i][0]**2+f[i][1]**2 for i in local_sites),mp.mpf(0))
        K=mp.sqrt(Fscore)*(1+4*harmonic(R)/mp.pi)
        bound=4*b*R*K**b/d
        assert abs(actual-single)<=bound+tolerance
        print('CLOSED finite diagnostic: grouped prime/power boundary bridge degree',b,
              'error',mp.nstr(abs(actual-single),8),'bound',mp.nstr(bound,8))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--exact-only',action='store_true')
    args=parser.parse_args()
    joint_budget()
    independent_prior_checks()
    if not args.exact_only:
        numeric_checks()
    print('RESULT: WP84_FOURIER_REPROJECTION_BRIDGE_PASS')


if __name__=='__main__':
    main()
