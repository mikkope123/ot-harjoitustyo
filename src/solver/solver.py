from city.city import City
import matplotlib.pyplot as plt



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
        print(f"Route length: {self.__route_length:.2f} units")

    def print_to_file(self, filename):
        f = open(filename, "w")
        for city in self.__route:
            coordinates = city.get_coordinates()
            coordinate_string = str(coordinates[0]) + " " + str(coordinates[1]) + "\n"
            f.write(str(coordinate_string))
        f.close

    def solve(self):
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



    def plot(self):
        x = []
        y = []
        for city in self.__route:
            coordinates = city.get_coordinates()
            x.append(coordinates[0])
            y.append(coordinates[1])
        
        plt.plot(x,y)
        plt.savefig("results/route.png")
