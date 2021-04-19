import math

class City:
    def __init__(self, x1: float, x2: float):
        self.__x1 = x1
        self.__x2 = x2

    def __str__(self):
        city_tuple = (self.__x1, self.__x2)
        return str(city_tuple)

    def distance(self, other):
        return math.sqrt((self.__x1-other.__x1)**2 + (self.__x2-other.__x2)**2)

    def find_nearest(self, other_cities):
        nearest_city = None
        shortest_distance = 10**9 #find a better way to do this
        for city in other_cities:
            r = self.distance(city)
            if r < shortest_distance:
                shortest_distance = r
                nearest_city = city
        return (nearest_city, shortest_distance)

    def get_coordinates(self):
        return self.__x1, self.__x2
