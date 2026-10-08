#!/usr/bin/env python3
"""Exact R400 audit certificates, not an arithmetic fourth-moment theorem.

All acceptance decisions use Fraction intervals. Decimal output is display only.
The filtered merged-block cumulant is explicitly a diagnostic model, not the
unproved connected prime trace. Run --terms to print the entire 26-term ledger.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from collections import Counter
from itertools import combinations, permutations, product
from math import comb
import argparse
from wp84_r400_pair_layer_exact import atan_bounds_inv, harmonics, conv_coeff

R=400

def display(x,rounding=None):
    with localcontext() as ctx:
        ctx.prec=45
        if rounding: ctx.rounding=rounding
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def interval_add(a,b): return (a[0]+b[0],a[1]+b[1])
def interval_scale(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def interval_mul(a,b):
    values=[x*y for x in a for y in b]
    return min(values),max(values)
def show(name,value):
    if isinstance(value,tuple):
        print(name+' = ['+display(value[0],ROUND_FLOOR)+', '+display(value[1],ROUND_CEILING)+']')
    else: print(name+' = '+str(value)+' (~ '+display(value)+')')

def pi_bounds():
    a,b=atan_bounds_inv(5,28); c,d=atan_bounds_inv(239,9)
    return 16*a-4*d,16*b-4*c

def partitions(items):
    if not items:
        yield []
        return
    first,*rest=items
    for p in partitions(rest):
        for k in range(len(p)):
            yield p[:k]+[[first]+p[k]]+p[k+1:]
        yield [[first]]+p

def terms():
    out=[]
    for p in partitions(list(range(4))):
        anchor=next(k for k,b in enumerate(p) if 0 in b)
        for order in permutations([k for k in range(len(p)) if k!=anchor]):
            blocks=tuple(tuple(sorted(p[k])) for k in (anchor,)+order)
            out.append(((-1)**(len(p)-1),blocks))
    assert len(out)==26
    assert Counter(len(b) for _,b in out)=={1:1,2:7,3:12,4:6}
    assert Counter(s for s,_ in out)=={-1:13,1:13}
    return out

def half_word_moments(x):
    # f=1/2+u, u_hat(r)=1/(pi*i*r) on nonzero odd |r|<=R.
    last=R if R%2 else R-1
    odd=[j for j in range(1,last+1,2)]
    h2=sum((F(1,j*j) for j in odd),F(0))
    a=interval_scale(2*h2,x)
    # u^2 coefficient at r>0 even is -s_r/pi^2. Partial fractions
    # 1/(j(r-j))=(1/j+1/(r-j))/r collapse the convolution exactly.
    prefix={-1:F(0)}; acc=F(0)
    for j in odd:
        acc+=F(1,j); prefix[j]=acc
    def odd_sum(lo,hi):
        assert lo%2 and hi%2
        return prefix[hi]-prefix.get(lo-2,F(0))
    def signed_sum(lo,hi):
        if lo>0: return odd_sum(lo,hi)
        return prefix[hi]-prefix[-lo]
    s0=-2*h2
    e=s0*s0
    for r in range(2,2*last+1,2):
        lo=max(-last,r-last); hi=min(last,r+last)
        sr=F(2,r)*signed_sum(lo,hi)
        e+=2*sr*sr
    # Independently check the convolution identity at selected even lags.
    for r in [2,198,398,400,598,798]:
        direct=sum((F(1,j*(r-j)) for j in range(-last,last+1,2)
                    if -last<=r-j<=last and r-j!=0),F(0))
        fast=F(2,r)*signed_sum(max(-last,r-last),min(last,r+last))
        assert direct==fast
    b=interval_scale(e,interval_mul(x,x))
    alt=interval_add((F(1,16),)*2,interval_add(interval_scale(F(3,2),a),b))
    mixed=interval_add((F(1,16),)*2,interval_add(interval_scale(-F(1,2),a),b))
    gap=interval_add((F(1,4),)*2,interval_scale(-1,a))
    outer=interval_add(interval_scale(2,alt),interval_scale(4,mixed))
    bracket=interval_add((-F(3,8),)*2,
                         interval_add(interval_scale(3,a),interval_scale(-6,b)))
    connected=interval_mul(outer,bracket)
    assert gap[0]>0 and alt[1]<F(1,2) and mixed[0]>0
    alternating_loss=(F(1,2)-alt[1],F(1,2)-alt[0])
    assert alternating_loss[0]>gap[1]
    # Kouter-1 differs from -g by the nonzero fourth-order cancellation residue.
    difference_from_minus_g=interval_add(interval_add(outer,(-F(1),)*2),gap)
    assert difference_from_minus_g[1]<0
    assert bracket[1]<0 and connected[1]<0
    # Classify all 26 merged-block paths at (+1/2,+1/2,-1/2,-1/2).
    v=[F(1,2),F(1,2),-F(1,2),-F(1,2)]
    counts=Counter()
    for sign,blocks in terms():
        steps=[sum((v[j] for j in block),F(0)) for block in blocks]
        if any(abs(s)>=1 for s in steps): key='zero'
        else:
            half=[s for s in steps if s]
            if not half: key='one'
            elif len(half)==2: key='pair'
            else: key='alternating4' if all(half[k]!=half[(k+1)%4] for k in range(4)) else 'mixed4'
        counts[key]+=sign
    assert counts['one']==-1 and counts['pair']==4
    assert counts['alternating4']==-2 and counts['mixed4']==-4
    show('g400 (closed-pair gap AND same-sign pair alias overlap)',gap)
    show('Omega4_R alternating half-steps',alt)
    show('Omega4_R nonalternating half-steps',mixed)
    show('six-word OUTER overlap minus sharp six-word value',interval_add(outer,(-F(1),)*2))
    show('DIAGNOSTIC merged-filter B4 bracket',bracket)
    show('DIAGNOSTIC merged-filter six-word connected kernel',connected)
    return gap,alt,mixed,connected

def ledger(x):
    c4=F(593,2000); c2=F(213,1000)
    # Retain the displayed source numbers as exact conservative ledger inputs.
    paircap=F('0.266329'); bandconstant=F('2.1728342265')
    ceiling=F('0.163249981456072')
    old=F(1,2000)+c2/3+c4*paircap+bandconstant/R
    margin=ceiling-old; tolerance=margin/c4
    assert old==F('0.15589863406625')
    assert margin==F('0.007351347389822')
    show('old conditional defect',old)
    show('conditional record margin',margin)
    show('STRICT allowable Delta400 with all other debts o(1)',tolerance)
    show('old conditional simple-zero coefficient',1-2*old)
    h1,h2,h4=harmonics(R)
    e4=4*h2[R]**2+2*sum((conv_coeff(r,R,h1)**2 for r in range(1,2*R+1)),F(0))
    k=e4/8+2*h2[R]**2-F(3,4)*h4[R]
    assert k>0
    pair=interval_add((F(1,12),)*2,
                      interval_add(interval_scale(F(2,3)*h2[R],x),
                                   interval_scale(k,interval_mul(x,x))))
    assert pair[1]<paircap
    show('Pair400 retained finite-lag covariance interval',pair)
    # Exact centered polynomial, including terms omitted by the old moment gate.
    raw=[F(1011,1000),-F(3133,1000),F(1761,500),-F(212,125),F(593,2000)]
    centered=[sum((raw[j]*comb(j,k) for j in range(k,5)),F(0)) for k in range(5)]
    assert centered==[F(1,2000),F(9,1000),c2,-F(51,100),c4]
    print('EXACT centered coefficients (degree 0..4):',','.join(map(str,centered)))
    paths=comb(4*R+3,3)-4*comb(2*R+2,3)
    # Inclusion-exclusion coefficient of (1+...+z^(2R))^4 at z^(4R).
    print('EXACT closed Fourier-displacement paths at R400:',paths)
    print('CORRECTION: defect <= old + (593/2000)*Delta4 + (213/1000)*Delta2'
          ' + (9/1000)*eta1 + (51/100)*eta3 + etaBand + etaRank')
    print('CORRECTION: simple >= 0.6882027318675 - (593/1000)*Delta4'
          ' - (213/500)*Delta2 - (9/500)*eta1 - (51/50)*eta3 - 2*etaBand - 2*etaRank')
    return tolerance

def norm_obstruction():
    # K=11* is an admissible same-phase Dirichlet Gram matrix. An arbitrarily
    # small entrywise error epsilon*11* has unbounded weighted amplification.
    eps=F(1,4000); m=400
    coefficient_second_mass=F(1)
    weighted_error=eps*m
    assert coefficient_second_mass==1 and weighted_error==F(1,10)
    show('abstract Gram amplification witness (not a prime counterexample)',weighted_error)
    print('OPEN: actual filtered non-pair arithmetic residual and its weighted operator bound.')
    print('NO CERTIFIED Delta400 for actual w400; margin is NOT proved exhausted.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--terms',action='store_true')
    args=parser.parse_args()
    plo,phi=pi_bounds(); x=(1/phi**2,1/plo**2)
    show('pi interval',(plo,phi))
    ledger(x); half_word_moments(x); norm_obstruction()
    if args.terms:
        for n,(sign,blocks) in enumerate(terms(),1):
            print('TERM',n,'coefficient',sign,'blocks',blocks)
    print('RESULT: EXACT_SCALAR_AND_DEGREE_FOUR_DIAGNOSTICS_PASS; ACTUAL_R400_REPAIR_OPEN')

if __name__=='__main__': main()
