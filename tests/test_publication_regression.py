from __future__ import annotations

import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wp84_c5_pointwise_supercritical_sign import c5, half_l1  # noqa: E402


class ExactC5Regression(unittest.TestCase):
    def test_documented_rational_points_obey_pointwise_inequality(self) -> None:
        points = [
            (Fraction(0),) * 4,
            (Fraction(1, 4), Fraction(0), Fraction(0), Fraction(0)),
            (Fraction(1, 5), Fraction(-2, 5), Fraction(3, 5), Fraction(-2, 5)),
            (Fraction(1, 3), Fraction(1, 3), Fraction(-1, 3), Fraction(0)),
        ]
        for x in points:
            value = c5(x)
            s = half_l1(x)
            self.assertGreaterEqual(value, 0, (x, value))
            self.assertLessEqual(value, max(Fraction(0), s - 1), (x, value, s))

    def test_c5_is_exact_rational_on_rational_inputs(self) -> None:
        value = c5((Fraction(1, 5), Fraction(-2, 5), Fraction(3, 5), Fraction(-2, 5)))
        self.assertIsInstance(value, Fraction)
        self.assertEqual(value, Fraction(0, 1))


if __name__ == "__main__":
    unittest.main()
