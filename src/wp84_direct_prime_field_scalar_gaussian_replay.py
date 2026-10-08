"""Independent Fraction-only replay of the R0 Gaussian lower obstruction.

No SymPy, mpmath, quadrature engine or producer import is used.
"""
import json
from fractions import Fraction as F
from pathlib import Path


def check(ok, msg):
    if not ok:
        raise ValueError(msg)


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def remainder(p, q):
    p = list(p)
    while len(p) >= len(q) and any(p):
        k, v = len(p)-len(q), p[-1]/q[-1]
        for j in range(len(q)):
            p[j+k] -= v*q[j]
        trim(p)
    return p


def value(p, x):
    out = F(0)
    for c in reversed(p):
        out = out*x+c
    return out


def variations(seq, x):
    signs = [(1 if v > 0 else -1) for p in seq if (v := value(p, x)) != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def multiply(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def main():
    check(__debug__, 'No -O')
    path = Path(__file__).resolve().parents[1]/'notes/WP84_DIRECT_PRIME_FIELD_STATE_LAW_CERTIFICATE.json'
    cert = json.loads(path.read_text())
    g = cert['scalar_gaussian_diagnostic']
    c, a = F(3142, 2415), F(131, 200)
    p = [F(1), -F(43428, 13891), F(37704, 13891), -F(9660, 13891)]
    den = [c*c+a*a, -2*c, F(1)]
    den = multiply(multiply(den, den), den)
    num = [x*(c*c+a*a)**3 for x in multiply(p, p)]
    poly = [x-F(29, 50)*y for x, y in zip(num, den)]
    check(poly == list(map(F, g['consumer_lower_polynomial_ascending'])), 'producer polynomial')
    seq = [poly, [j*poly[j] for j in range(1, len(poly))]]
    while len(seq[-1]) > 1:
        r = [-v for v in remainder(seq[-2], seq[-1])]
        check(any(r), 'non-squarefree diagnostic polynomial')
        seq.append(r)
    check(variations(seq, F(9, 10))-variations(seq, F(11, 10)) == 0, 'independent root count')
    check(value(poly, F(1)) > 0, 'positive sign between endpoints')
    v = F(100001, 600000)
    check(2*F(22, 7)*v < F(103, 100)**2, 'pi upper normalization')
    check(F(1, 100)/(2*v) < F(3, 100), 'exp lower via 1-x')
    lo = F(29, 50)*F(1, 5)*F(97, 103)
    check(lo == F(g['independent_rational_initial_lower']), 'exact lower mass')
    check(lo > F(21, 200), 'R0 cannot pay target')
    check(F(cert['E_inf'])-lo == F(g['R0_any_U_signed_upper']), 'cap plus weak dual upper')
    check(g['extension_to_positive_R_claimed'] is False, 'no extrapolation')
    print('PASS: independent Fraction Sturm, Gaussian density lower bound, and R0 obstruction.')
    print('Initial Gaussian energy >=', lo, '; no positive-R conclusion.')


if __name__ == '__main__':
    main()
