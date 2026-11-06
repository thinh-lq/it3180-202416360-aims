import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation")
        ]

    def test_search_by_title(self):
        result = search_by_title(self.dvds, "Lion")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")

    def test_search_by_category(self):
        result = search_by_category(self.dvds, "Animation")

        self.assertEqual(len(result), 2)

        titles = [dvd.title for dvd in result]

        self.assertIn("The Lion King", titles)
        self.assertIn("Aladdin", titles)


if __name__ == "__main__":
    unittest.main()