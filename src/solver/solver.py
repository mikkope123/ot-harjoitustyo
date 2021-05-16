from city.city import City

class Route:
    """Class that represents the route that the salesman follows.

    Attribues:
        cities: Cities to visit
        route: visited cities in order of visits
        route_length: the distance traveled"""

    def __init__(self, cities):
        """Class constructor that creates an empty route."""
        self.__route = []
        self.__route_length = 0
        self.__cities = cities

    def add_to_route(self, city: City):
        """Adds city to the route of the salesman.

        Args:
            city: A city class object.

        Returns:
            True if city was added to the route."""
        self.__route.append(city)
        return True

    def print_route(self):
        """Prints the current route on the terminal.

        Returns:
            True if successful"""
        print("Solved route:")
        for city in self.__route:
            print(city)
        print(f"Route length: {self.__route_length:.2f} units")
        return True

    def solve(self):
        """Calculates the approximation of the shortest route through all the given cities to visit.

        Returns:
            The length of the approximated route."""
        #choose a starting city
        current = self.__cities[0]
        first = current
        self.add_to_route(current)
        self.__cities.remove(current)
        while len(self.__cities) != 0:
            next_city, dist = current.find_nearest(self.__cities)
            self.add_to_route(next_city)
            self.__route_length += dist
            self.__cities.remove(next_city)
            current = next_city
        self.add_to_route(first)
        self.__route_length += current.distance(first)
        return self.__route_length

    def get_route(self):
        """Returns the current route."""
        return self.__route
