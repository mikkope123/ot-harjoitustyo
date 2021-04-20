import unittest
from solver.solver import Route
from city.city import City


class TestRoute(unittest.TestCase):
    def setUp(self):
        self.route = Route()

    def test_add_city(self):
        city = City(1,-1)
        self.assertEqual(self.route.add_city(city), True)

    def test_add_to_route(self):
        city = City(2,-2)
        self.assertEqual(self.route.add_to_route(city), True)

    def test_solve(self):
        city1 = City(0, 0)
        city2 = City(1, 0)
        city3 = City(1, 1)
        city4 = City(0, 1)
        self.route.add_city(city1)
        self.route.add_city(city2)
        self.route.add_city(city3)
        self.route.add_city(city4)
        self.assertEqual(self.route.solve(), 4)
