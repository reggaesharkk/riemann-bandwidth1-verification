from __future__ import annotations

import contextlib
import io
import sys
import unittest
import sympy as sp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wp84_bounded_christoffel_consumer import delta, F, g, main  # noqa: E402


class BoundedChristoffelConsumerRegression(unittest.TestCase):
    def test_equivalent_rational_bound_is_checked_by_exact_difference(self) -> None:
        lhs = sp.Rational(delta + 1, delta) * g - F
        rhs = (delta + 1) * g * g / (delta * (g + delta))
        self.assertEqual(sp.simplify(lhs - rhs), 0)

    def test_exact_candidate_checker_completes_and_reports_model_bound(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main()
        text = output.getvalue()
        self.assertIn("negative-mass cap = 87730/847351", text)
        self.assertIn("simple-zero ledger floor = 671891/847351", text)
        self.assertIn("RESULT: WP84_BOUNDED_CHRISTOFFEL_CONSUMER_PASS", text)


if __name__ == "__main__":
    unittest.main()
