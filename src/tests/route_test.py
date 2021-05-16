import unittest
from solver.solver import Route
from city.city import City


class TestRoute(unittest.TestCase):
    def setUp(self):
        city1 = City(0, 0)
        city2 = City(1, 0)
        city3 = City(1, 1)
        city4 = City(0, 1)
        cities = [city1, city2, city3, city4]
        self.route = Route(cities)

    def test_add_to_route(self):
        city = City(2,-2)
        self.assertEqual(self.route.add_to_route(city), True)

    def test_solve(self):
        self.assertEqual(self.route.solve(), 4)

    def test_print_route(self):
        self.route.solve()
        self.assertEqual(self.route.print_route(), True)

    def test_get_route(self):
        self.route.solve()
        self.assertEqual(len(self.route.get_route()), 5)
