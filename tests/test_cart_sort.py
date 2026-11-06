import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartSort(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        self.cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))

    def test_sort_by_title(self):
        self.cart.sort_by_title()

        titles = [dvd.title for dvd in self.cart.items]

        self.assertEqual(
            titles,
            ["Aladdin", "Star Wars", "The Lion King"]
        )

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()

        costs = [dvd.cost for dvd in self.cart.items]

        self.assertEqual(
            costs,
            [18.99, 19.95, 24.95]
        )


if __name__ == "__main__":
    unittest.main()