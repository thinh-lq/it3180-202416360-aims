import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


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

    def test_search_by_title_case_insensitive(self):
        result = search_by_title(self.dvds, "lion")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")

    def test_search_by_title_uppercase(self):
        result = search_by_title(self.dvds, "LION")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()