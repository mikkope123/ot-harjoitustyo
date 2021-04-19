import unittest
from city.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City(0,0)
        self.city2 = City(1,0)
        self.city3 = City(1,1)

    def test_distance(self):
        self.assertEqual(self.city.distance(self.city2), 1)

    def test_get_coordinates(self):
        self.assertEqual(self.city.get_coordinates(), (0,0))

    def test_find_nearest(self):
        other_cities = [self.city2, self.city3]
        self.assertEqual(self.city.find_nearest(other_cities), (self.city2, 1))
