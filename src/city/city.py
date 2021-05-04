import math

class City:
    """Class: 

    Attributes:
        x1, x2: cartesian coordinates representing the location of the city on the map

    """
    def __init__(self, x1: float, x2: float):
        """Class constructor that creates a new city

        Args:
            self.__x1, self.__x2: cartesian coordinates representing the location of the city on the map"""
        self.__x1 = x1
        self.__x2 = x2

    def __str__(self):
        """Returns the string attribute of the class.

        Returns:
            A string consisting of a tuple of city coordinates."""
        city_tuple = (self.__x1, self.__x2)
        return str(city_tuple)

    def distance(self, other):
        """Calculates the distance from the city to another

        Args:
            City class object

        Returns:
            euclidian distance between the cities"""
        return math.sqrt((self.__x1-other.__x1)**2 + (self.__x2-other.__x2)**2)

    def find_nearest(self, other_cities):
        """Finds the city nearest to this one.

        Args:
            A list of cities.

        Returns:
            A tuple consisting of the nearest city and the distance from self to there."""
        nearest_city = None
        shortest_distance = 10**9 #find a better way to do this
        for city in other_cities:
            r = self.distance(city)
            if r < shortest_distance:
                shortest_distance = r
                nearest_city = city
        return (nearest_city, shortest_distance)

    def get_coordinates(self):
        """
        A method to get the cartesian coordinates of the city.

        Returns:
            Cartesian coordinates of the city."""
        return self.__x1, self.__x2
