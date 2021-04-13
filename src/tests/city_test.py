import unittest
from main import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City(0,0)
        self.city2 = City(1,0)

    def test_distance(self):
        self.assertEqual(self.city.distance(self.city2), 1)
