#!/usr/bin/env python3
"""Exact R=400 pair-layer upper certificate with a rational pi enclosure."""

from fractions import Fraction as F

R=400

def harmonics(R):
    h1=[F(0)]*(R+1)
    h2=[F(0)]*(R+1)
    h4=[F(0)]*(R+1)
    for n in range(1,R+1):
        h1[n]=h1[n-1]+F(1,n)
        h2[n]=h2[n-1]+F(1,n*n)
        h4[n]=h4[n-1]+F(1,n**4)
    return h1,h2,h4

def conv_coeff(r,R,h1):
    if 1<=r<=R:
        return F(2,r)*(h1[r-1]+h1[R]-h1[r]-h1[R-r])
    if R<r<=2*R:
        return F(2,r)*(h1[R]-h1[r-R-1])
    raise ValueError(r)

def atan_bounds_inv(q,terms):
    s=F(0)
    for n in range(terms):
        t=F(1,(2*n+1)*q**(2*n+1))
        s += t if n%2==0 else -t
    nxt=F(1,(2*terms+1)*q**(2*terms+1))
    if terms%2==0:
        return s,s+nxt
    return s-nxt,s

def main():
    h1,h2,h4=harmonics(R)
    H2=h2[R]
    H4=h4[R]

    E4=4*H2*H2
    for r in range(1,2*R+1):
        s=conv_coeff(r,R,h1)
        E4 += 2*s*s

    lo5,hi5=atan_bounds_inv(5,20)
    lo239,hi239=atan_bounds_inv(239,6)

    pi_lo=16*lo5-4*hi239
    pi_hi=16*hi5-4*lo239
    assert pi_lo<pi_hi

    x_up=1/(pi_lo*pi_lo)

    C2=E4/F(8)+2*H2*H2-F(3,4)*H4
    assert C2>0

    pair_up=(
        F(1,12)
        +F(2,3)*H2*x_up
        +C2*x_up*x_up
    )

    headline=F(266329,1000000)
    assert pair_up<headline

    print("R =",R)
    print("pi interval width <",float(pi_hi-pi_lo))
    print("rigorous Pair_R upper ~",float(pair_up))
    print("headline =",float(headline))
    print("margin =",float(headline-pair_up))
    print("RESULT: WP84_R400_PAIR_LAYER_PASS")

if __name__=="__main__":
    main()
