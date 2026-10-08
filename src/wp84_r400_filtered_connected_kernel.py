#!/usr/bin/env python3
"""Actual row-cumulant kernel: numerical reconnaissance and interval witness.

No continuum arithmetic limit or coefficient-weighted Delta400 is certified.
The 26 terms are products of actual row Dirichlet moments, not overlap paths.
--certificate uses outward-rounded mpmath interval arithmetic and an exact
trapezoidal identity for finite trigonometric polynomials. --search is floating
reconnaissance only. Dependencies: numpy, mpmath.
"""
from fractions import Fraction as F
from itertools import combinations, product
import argparse, math, json
from wp84_r400_filtered_sharp_repair import terms

WITNESS=(F(1,5),-F(2,5),F(3,5),-F(2,5))
RS=(10,20,50,100,200,400)

def rational_cumulant(v,d):
    """Exact d-row mean for rational frequencies with denominators dividing d."""
    assert all(d%x.denominator==0 for x in v)
    total=0
    for sign,blocks in terms():
        total+=sign*math.prod(int(sum((v[j] for j in b),F(0)).denominator==1)
                             for b in blocks)
    return total

def exact_structure():
    assert rational_cumulant(WITNESS,1000000)==1
    p=(F(1,5),F(3,5)); q=(F(2,5),F(2,5))
    assert rational_cumulant(p+tuple(-x for x in p),1000000)==0
    assert rational_cumulant(q+tuple(-x for x in q),1000000)==-1
    p_super=(F(2,5),F(4,5)); q_super=(F(3,5),F(3,5))
    assert rational_cumulant(p_super+tuple(-x for x in p_super),1000000)==0
    assert rational_cumulant(q_super+tuple(-x for x in q_super),1000000)==-1
    assert rational_cumulant((F(2,5),-F(3,5),F(4,5),-F(3,5)),1000000)==1
    # Exhaust all positive pair multisets on denominator grids q<=5. The
    # smallest denominator with a non-pair positive row-cumulant is exactly 5.
    minimal=None
    for den in range(2,6):
        pairs=[(F(a,den),F(b,den)) for a in range(1,den)
               for b in range(a,den)]
        for p in pairs:
            for q in pairs:
                if p==q or sum(p)!=sum(q): continue
                v=p+tuple(-x for x in q)
                if rational_cumulant(v,den)>0:
                    minimal=den if minimal is None else min(minimal,den)
    assert minimal==5
    # A single-tail monomial obeys Fourier closure and survives the actual
    # combined cumulant. No factor is zero at the denominator-5 witness.
    lag=(401,-399,-2,0)
    assert sum(lag)==0 and sum(abs(r)>400 for r in lag)==1
    for r,v in zip(lag,WITNESS):
        if r: assert (r*(1-abs(v))).denominator!=1
    print('EXACT: 26 anchored terms; witness cumulant=1; fixed-scale diagonal cumulants=0,-1')
    print('EXACT: smallest BALANCED non-pair positive ROW-CUMULANT grid denominator is 5')
    minimal_all=None
    for den in range(2,5):
        choices=[F(j,den) for j in range(-den+1,den) if j]
        for head in product(choices,repeat=3):
            v=head+(-sum(head,F(0)),)
            if v[-1] not in choices: continue
            if rational_cumulant(v,den)>0:
                minimal_all=den if minimal_all is None else min(minimal_all,den)
    assert minimal_all==4
    assert rational_cumulant((F(1,4),F(1,4),F(1,4),-F(3,4)),1000000)==1
    print('EXACT: smallest positive ROW-CUMULANT grid denominator in ALL sign populations is 4')
    print('EXACT: one-tail monomial (401,-399,-2,0) survives the combined actual cumulant')

def phase_free_cumulant(v,d):
    def dr(x):
        near=round(x)
        if abs(x-near)<1e-12: return (-1.0)**((d-1)*near)
        return math.sin(math.pi*d*x)/(d*math.sin(math.pi*x))
    return sum(sign*math.prod(dr(sum(v[j] for j in b)) for b in blocks)
               for sign,blocks in terms())

def omega_float(v,R):
    import numpy as np
    M=1
    while M<=4*R: M*=2
    r=np.arange(-R,R+1)
    vals=np.ones(M,dtype=complex); prefix=0.0
    for shift in v:
        shift=float(shift)
        if abs(shift)>=1: return 0.0
        a=max(0.0,-shift); b=min(1.0,1.0-shift)
        coeff=np.empty(2*R+1,dtype=complex)
        nonzero=r!=0
        coeff[nonzero]=(np.exp(-2j*np.pi*r[nonzero]*a)-np.exp(-2j*np.pi*r[nonzero]*b))/(2j*np.pi*r[nonzero])
        coeff[R]=b-a
        coeff*=np.exp(2j*np.pi*r*prefix)
        spectrum=np.zeros(M,dtype=complex); spectrum[r%M]=coeff
        vals*=np.fft.ifft(spectrum)*M
        prefix+=shift
    result=np.mean(vals)
    assert abs(result.imag)<1e-9
    return float(result.real)

def six_vectors(p,q):
    for positive in combinations(range(4),2):
        ip=iter(p); iq=iter(q)
        yield tuple(next(ip) if j in positive else -next(iq) for j in range(4))

def symmetric_gram_entry(p,q,R,iv,cache):
    # Internal pair orderings are actually summed in the arithmetic measure.
    # Their average gives a Hermitian kernel without multiplying the ledger
    # by four. Filtered same-sign translations need not commute.
    total=iv.mpf(0)
    for pp in (p,p[::-1]):
        for qq in (q,q[::-1]):
            total+=sum((omega_interval(v,R,iv,cache) for v in six_vectors(pp,qq)),iv.mpf(0))
    return total/4

def finite_identity_check():
    """Independent finite row-cumulant expansion check; numerical diagnostic."""
    import numpy as np
    v=(F(1,5),-F(1,5),F(2,5),-F(2,5))
    c=(-0.2,-0.2,-0.1,-0.1); d=5; R=1
    def coeff(r,z):
        if not r: return 1-abs(float(z))
        a=max(0,-float(z)); b=min(1,1-float(z))
        # Matrix lag j-i uses the positive-exponent interval coefficient.
        return (np.exp(2j*np.pi*r*b)-np.exp(2j*np.pi*r*a))/(2j*np.pi*r)
    row_total=0j
    for lag in product(range(-R,R+1),repeat=4):
        if sum(lag): continue
        q=0; fields=[]
        for r in lag:
            q+=r
            fields.append(np.array([sum(cn*coeff(r,z)*np.exp(2j*np.pi*(k+q)*float(z))
                                        for cn,z in zip(c,v)) for k in range(d)]))
        row_total+=sum(sign*np.prod([np.mean(np.prod([fields[j] for j in b],axis=0))
                                     for b in blocks]) for sign,blocks in terms())
    tuple_total=0.0
    for labels in product(range(len(v)),repeat=4):
        shifts=tuple(v[j] for j in labels)
        tuple_total+=math.prod(c[j] for j in labels)*rational_cumulant(shifts,d)*omega_float(shifts,R)
    assert abs(row_total-tuple_total)<5e-11
    print('FINITE numerical check: direct band-entry row cumulants equal exact 26-term tuple kernel;'
          ' discrepancy =',abs(row_total-tuple_total))

def iv_fraction(x,iv): return iv.mpf(x.numerator)/x.denominator

def fft_interval(values,iv):
    """Unnormalized inverse DFT; every elementary operation interval rounded."""
    n=len(values); a=list(values); j=0
    for k in range(1,n):
        bit=n>>1
        while j&bit: j^=bit; bit>>=1
        j^=bit
        if k<j: a[k],a[j]=a[j],a[k]
    width=2
    while width<=n:
        angle=2*iv.pi/width
        roots=[iv.mpc(iv.cos(angle*k),iv.sin(angle*k)) for k in range(width//2)]
        for start in range(0,n,width):
            for k,w in enumerate(roots):
                u=a[start+k]; t=w*a[start+k+width//2]
                a[start+k]=u+t; a[start+k+width//2]=u-t
        width*=2
    return a

def omega_interval(v,R,iv,cache):
    M=1
    while M<=4*R: M*=2
    factors=[]; prefix=F(0)
    for shift in v:
        if abs(shift)>=1: return iv.mpf(0)
        key=(shift,prefix%1,R)
        if key not in cache:
            a=max(F(0),-shift); b=min(F(1),1-shift)
            coeff=[iv.mpc(0) for _ in range(M)]
            coeff[0]=iv.mpc(iv_fraction(b-a,iv))
            for r in range(1,R+1):
                aa=2*iv.pi*iv_fraction((prefix-a)*r,iv)
                bb=2*iv.pi*iv_fraction((prefix-b)*r,iv)
                # a_r exp(2pi i r prefix) = (e^iaa-e^ibb)/(2pi i r)
                den=2*iv.pi*r
                z=iv.mpc((iv.sin(aa)-iv.sin(bb))/den,
                         -(iv.cos(aa)-iv.cos(bb))/den)
                coeff[r]=z; coeff[-r]=iv.mpc(z.real,-z.imag)
            cache[key]=fft_interval(coeff,iv)
        factors.append(cache[key]); prefix+=shift
    total=iv.mpc(0)
    for k in range(M):
        z=iv.mpc(1)
        for f in factors: z*=f[k]
        total+=z
    answer=total/M
    assert 0 in answer.imag
    return answer.real

def certificate():
    from mpmath import iv
    iv.dps=35
    for R in RS:
        cache={}
        value=omega_interval(WITNESS,R,iv,cache)
        assert value>iv.mpf('0.35')
        print('CERTIFIED R',R,'Phi_actual closed witness =',value,flush=True)
        if R==400:
            p=(F(1,5),F(3,5)); q=(F(2,5),F(2,5))
            off=symmetric_gram_entry(p,q,R,iv,cache)
            assert off>iv.mpf('0.5')
            determinant=-off**2
            assert determinant<0
            print('CERTIFIED R400 internally symmetrized six-word Gram cross entry =',off,flush=True)
            print('CERTIFIED actual 2x2 connected Gram determinant =',determinant,flush=True)
            p=(F(2,5),F(4,5)); q=(F(3,5),F(3,5))
            off_super=symmetric_gram_entry(p,q,R,iv,cache)
            assert off_super>iv.mpf('0.35')
            print('CERTIFIED R400 SUPERCRITICAL symmetrized six-word cross entry =',off_super,flush=True)
            print('CERTIFIED SUPERCRITICAL 2x2 Gram determinant =',-off_super**2,flush=True)
            unbalanced=omega_interval((F(1,4),F(1,4),F(1,4),-F(3,4)),R,iv,cache)
            assert unbalanced>iv.mpf('0.2')
            print('CERTIFIED R400 denominator-4 unbalanced witness =',unbalanced,flush=True)
    print('RESULT: ACTUAL_ROW_CUMULANT_SIGN_COUNTEREXAMPLE_CERTIFIED; WEIGHTED_DELTA400_OPEN')

def search(count,seed):
    import numpy as np
    rng=np.random.default_rng(seed)
    d=1000000
    closed=[tuple(float(x) for x in WITNESS)]
    # Random points cover the entire closed cube: v0,v1,v2 free and v3 chosen
    # by closure; reject outside [-1,1]. Include all sign populations.
    while len(closed)<count+1:
        z=rng.uniform(-1,1,3); v=tuple(z)+(-float(sum(z)),)
        if abs(v[-1])<1: closed.append(v)
    # Structured subcritical and supercritical equal-product-scale chambers.
    for s in [0.01,0.1,0.5,0.8,1.0,1.2,1.5,1.9,1.99]:
        lo=max(0,s-1); hi=min(1,s)
        for a in [0.001,0.1,0.49,0.5,0.9,0.999]:
            for b in [0.001,0.2,0.5,0.8,0.999]:
                x=lo+(hi-lo)*a; y=lo+(hi-lo)*b
                closed.append((x,-y,s-x,-(s-y)))
    cross=[tuple(v) for v in rng.uniform(-1,1,(count,4))]
    # Explicitly search the narrow physical detuning and alias windows that
    # a uniform random cube search would almost never hit.
    for v in closed[::20]:
        head=sum(v[:3])
        for alias in range(-3,4):
            for delta in [-2,-1.5,-0.5,-0.1,0,0.1,0.5,1.5,2]:
                tail=alias-head+delta/d
                if abs(tail)<1: cross.append(tuple(v[:3])+(tail,))
    for R in RS:
        best=(-float('inf'),None); bestcross=(-float('inf'),None)
        for v in closed:
            z=omega_float(v,R)*phase_free_cumulant(v,d)
            if z>best[0]: best=(z,v)
        for v in cross:
            z=omega_float(v,R)*phase_free_cumulant(v,d)
            if z>bestcross[0]: bestcross=(z,tuple(float(t) for t in v))
        print(json.dumps({'R':R,'d':d,'seed':seed,'closed_samples':len(closed),
                          'cross_samples':len(cross),'closed_positive_max_found':best,
                          'phase_free_cross_positive_max_found':bestcross,
                          'status':'FLOATING RECONNAISSANCE; not a supremum certificate'}),flush=True)

def main():
    if not __debug__:
        raise RuntimeError('Fail-closed certificate requires assertion checks; run without -O.')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate',action='store_true')
    parser.add_argument('--search',action='store_true')
    parser.add_argument('--samples',type=int,default=500)
    parser.add_argument('--seed',type=int,default=7962400)
    args=parser.parse_args()
    exact_structure()
    finite_identity_check()
    if args.search: search(args.samples,args.seed)
    if args.certificate: certificate()

if __name__=='__main__': main()
