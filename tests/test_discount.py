import unittest

from aims.discount import total_cost_with_discount


class TestDiscount(unittest.TestCase):

    def test_discount_20_percent(self):
        self.assertAlmostEqual(
            total_cost_with_discount(100, 20),
            80
        )

    def test_discount_100_percent(self):
        self.assertAlmostEqual(
            total_cost_with_discount(100, 100),
            0
        )

    def test_invalid_discount_percent(self):
        with self.assertRaises(ValueError):
            total_cost_with_discount(100, 150)


if __name__ == "__main__":
    unittest.main()