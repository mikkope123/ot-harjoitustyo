import math

class City:
    def __init__(self, x1: float, x2: float):
        self.__x1 = x1
        self.__x2 = x2

    def __str__(self):
        city_tuple = ( (self.__x1, self.__x2) )
        return str(city_tuple)

    def distance(self, other):
        return math.sqrt( (self.__x1-other.__x1)**2 + (self.__x2-other.__x2)**2 )

    def find_nearest(self, other_cities):
        nearest_city = None
        shortest_distance = 10**9 #find a better way to do this
        for city in other_cities:
            r = self.distance(city)
            if r < shortest_distance:
                shortest_distance = r
                nearest_city = city
        return (nearest_city, shortest_distance)
        

class Route:
    def __init__(self):
        self.__cities = [] #should be a set?
        self.__route = []
        self.__route_length = 0

    def add_city(self, city: City):
        self.__cities.append(city)

    def add_to_route(self, city: City):
        self.__route.append(city)

    def print_cities(self):
        for city in self.__cities:
            print(city)

    def print_route(self): #reduntant code!!!!!
        print("Solved route:")
        for city in self.__route:
            print(city)
        print("Route length:", self.__route_length)

    def solve_route(self):
        #choose a starting city
        current = self.__cities[0]
        self.add_to_route(current)
        self.__cities.remove(current)
        while len(self.__cities) != 0:
            next, dist = current.find_nearest(self.__cities)
            self.add_to_route(next)
            self.__route_length += dist #add this to add_to_route
            self.__cities.remove(next) #ditto
            current = next
            
""""
class Solver:
    def __init__(self):
        pass
"""

cities = []
with open("src/data.txt") as data:
    for line in data:
        raw_split = line.split()
        cities.append( City(float(raw_split[0]), float(raw_split[1]) ) )
route = Route()
for city in cities:
    route.add_city(city)

#new_city=cities[0]

print("print cities")
route.print_cities()
print()
route.solve_route()
route.print_route()
