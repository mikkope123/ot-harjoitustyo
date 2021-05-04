import matplotlib.pyplot as plt
from city.city import City

class Route:
    """Class that represents the route that the salesman follows.

    Attribues:
        cities: Cities to visit
        route: visited cities in order of visits
        route_length: the distance traveled"""

    def __init__(self):
        """Class constructor that creates an empty route."""
        self.__cities = [] #should be a set?
        self.__route = []
        self.__route_length = 0

    def add_city(self, city: City):
        """Adds a city to the list of cities to visit (self.__cities).

        Args:
            city: A city class object.

        Returns:
            True if the city was added to the list of cities to visit."""
        self.__cities.append(city)
        return True

    def add_to_route(self, city: City):
        """Adds city to the route of the salesman.

        Args:
            city: A city class object.

        Returns:
            True if city was added to the route."""
        self.__route.append(city)
        return True

    def print_cities(self):
        """Prints the list of cities to visit on the terminal."""
        for city in self.__cities:
            print(city)

    def print_route(self): #reduntant code!!!!!
        """Prints the current route on the terminal."""
        print("Solved route:")
        for city in self.__route:
            print(city)
        print(f"Route length: {self.__route_length:.2f} units")

    def print_to_file(self, filename):
        """Saves the current route to a file.

        Args:
            filename: The file in which the route will be saved.

        Returns:
            True if writing was succesful"""
        f = open(filename, "w")
        for city in self.__route:
            coordinates = city.get_coordinates()
            coordinate_string = str(coordinates[0]) + " " + str(coordinates[1]) + "\n"
            f.write(str(coordinate_string))
        f.close()
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
            next, dist = current.find_nearest(self.__cities)
            self.add_to_route(next)
            self.__route_length += dist #add this to add_to_route
            self.__cities.remove(next) #ditto
            current = next
        self.add_to_route(first)
        self.__route_length += current.distance(first) #what if only one city
        return self.__route_length



    def plot(self):
        """Plots the current route and saves it as an image.

        Returns:
            True if the image is succesfully created."""
        x = []
        y = []
        for city in self.__route:
            coordinates = city.get_coordinates()
            x.append(coordinates[0])
            y.append(coordinates[1])
        plt.plot(x,y)
        plt.savefig("results/route.png")
        return True
