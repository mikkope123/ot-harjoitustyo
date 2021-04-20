from city.city import City
from solver.solver import Route

result_file = "results/route"

cities = []
with open("data/data.txt") as data:
    for line in data:
        raw_split = line.split()
        cities.append(City(float(raw_split[0]), float(raw_split[1])))
route = Route()
for city in cities:
    route.add_city(city)

#new_city=cities[0]

print("Cities to visit:")
route.print_cities()
print()
route.solve()
route.print_route()
route.print_to_file(result_file)
route.plot()
print("Solution printed to the file "+ str(result_file))
