#!/usr/bin/env python3
"""Exact pointwise sign certificate for the connected b=5 cycle.

Proves on the closed outer-support polytope:

    0 <= C5(v) <= max(0, s(v)-1),

where sum(v)=0 and s(v)=sum(abs(v_j))/2.

Method:
- construct the exact 150-term connected kernel;
- construct the common breakpoint hyperplane arrangement;
- enumerate every 4-fold intersection exactly;
- retain all vertices in the bounded outer-support polytope;
- verify both affine inequalities on every vertex.

Standard library only.
"""

from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd

ZERO=F(0)
ONE=F(1)

def set_partitions(items):
    if not items:
        yield []
        return
    first,rest=items[0],items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i]+[[first]+part[i]]+part[i+1:]
        yield [[first]]+part

def compile_terms(b):
    out=[]
    for P in set_partitions(list(range(b))):
        m=len(P)
        sign=(-1)**(m-1)
        first=next(i for i,blk in enumerate(P) if 0 in blk)
        others=[i for i in range(m) if i!=first]
        for perm in permutations(others):
            order=[first]+list(perm)
            masks=[]
            cur=frozenset()
            for bi in order[:-1]:
                cur=cur|frozenset(P[bi])
                masks.append(tuple(sorted(cur)))
            out.append((sign,tuple(masks)))
    return out

TERMS=compile_terms(5)
assert len(TERMS)==150

def mask_pos(mask):
    # free coordinates v0..v3; v4=-(v0+...+v3)
    a=[0,0,0,0]
    for j in mask:
        if j<4:
            a[j]+=1
        else:
            for k in range(4):
                a[k]-=1
    return tuple(a)

OUTER=[
    (0,0,0,0),
    (1,0,0,0),
    (1,1,0,0),
    (1,1,1,0),
    (1,1,1,1),
]

def dot(a,x):
    return sum(F(ai)*xi for ai,xi in zip(a,x))

def ov(vals):
    spread=max(vals)-min(vals)
    return max(ZERO,ONE-spread)

def outer_overlap(x):
    return ov([dot(a,x) for a in OUTER])

def c5(x):
    v=list(x)+[-sum(x)]
    total=ZERO
    for sign,masks in TERMS:
        pos=[ZERO]
        for mk in masks:
            pos.append(sum(v[j] for j in mk))
        total+=sign*ov(pos)
    return total

def half_l1(x):
    v=list(x)+[-sum(x)]
    return sum(abs(t) for t in v)/2

def canon(a,c):
    vals=[int(t) for t in a]+[int(c)]
    g=0
    for t in vals:
        g=gcd(g,abs(t))
    if g:
        a=tuple(int(t//g) for t in a)
        c=int(c//g)
    for t in list(a)+[c]:
        if t:
            if t<0:
                a=tuple(-u for u in a)
                c=-c
            break
    return a,c

def arrangement():
    H=set()
    families=[OUTER]
    for _,masks in TERMS:
        families.append([(0,0,0,0)]+[mask_pos(m) for m in masks])

    for pos in families:
        for i in range(len(pos)):
            for j in range(i+1,len(pos)):
                a=tuple(pos[i][k]-pos[j][k] for k in range(4))
                if not any(a):
                    continue
                for c in (-1,0,1):
                    H.add(canon(a,c))

    # Fail-closed checks that the same arrangement refines s(v).
    # All five sign walls v_j=0.
    sign_walls=[]
    for j in range(5):
        if j<4:
            a=tuple(1 if k==j else 0 for k in range(4))
        else:
            a=(-1,-1,-1,-1)
        sign_walls.append(canon(a,0))
    assert all(h in H for h in sign_walls)

    # In each sign chamber s=1 is sum sigma_j v_j = 2.
    for sig in product((-1,1),repeat=5):
        a=tuple(sig[j]-sig[4] for j in range(4))
        if any(a):
            assert canon(a,2) in H

    assert len(H)==45
    return sorted(H)

def solve4(rows):
    A=[[F(t) for t in a]+[F(c)] for a,c in rows]
    n=4
    r=0
    for col in range(n):
        piv=next((i for i in range(r,n) if A[i][col]),None)
        if piv is None:
            return None
        A[r],A[piv]=A[piv],A[r]
        p=A[r][col]
        A[r]=[t/p for t in A[r]]
        for i in range(n):
            if i!=r and A[i][col]:
                f=A[i][col]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n+1)]
        r+=1
    return tuple(A[i][n] for i in range(n))

def main():
    H=arrangement()
    verts=set()
    tested=0

    for rows in combinations(H,4):
        tested+=1
        x=solve4(rows)
        if x is None:
            continue
        if outer_overlap(x)>=0:
            # Closed outer support means spread<=1.
            vals=[dot(a,x) for a in OUTER]
            if max(vals)-min(vals)<=1:
                verts.add(x)

    assert tested==148995
    assert len(verts)==151

    mn=None
    mx=None
    for x in verts:
        C=c5(x)
        s=half_l1(x)
        rhs=max(ZERO,s-ONE)
        assert C>=0,(x,C,s)
        assert C<=rhs,(x,C,s,rhs)
        mn=C if mn is None or C<mn else mn
        mx=C if mx is None or C>mx else mx

    assert mn==0
    assert mx==F(1,2)

    print("hyperplanes",len(H))
    print("candidate intersections",tested)
    print("relevant vertices",len(verts))
    print("min C5",mn)
    print("max C5",mx)
    print("RESULT: WP84_C5_POINTWISE_SUPERCRITICAL_SIGN_PASS")

if __name__=="__main__":
    main()
