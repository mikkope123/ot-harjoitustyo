def read_number_of_cities():
    while True:
        n_cities = input("Give the number of cities: ")
        try:
            if int(n_cities) > 0:
                return int(n_cities)
            else:
                print("The number of cities can't be less than 1.'")
        except:
            print("The number of cities must be an integer.")

def read_city_coordinates(n_cities: int):
    coordinates_read = 0
    cities = []
    while coordinates_read < n_cities:
        coordinates = input(f"Give the coordinates of city {coordinates_read+1} (separated by space): ")
        coord_split = coordinates.split()
        if len(coord_split) != 2:
            print("You must give exactly two coordinates!")
        else:
            try:
                x = float(coord_split[0])
                y = float(coord_split[1])
                if (x, y) in cities:
                    print("Duplicate entry!")
                else:
                    cities.append((x, y))
                    coordinates_read += 1
            except:
                print("The coordinates must be floating point numbers!")
    return cities

def write_to_file(cities: list, output: str):
    try:
        f=  open(output, "w")
        for city in cities:
            city_str = str(city[0]) + " " + str(city[1]) + "\n"
            f.write(city_str)
        print("City coordinates written to file", output)
    except:
        print("Could not write to file.")

OUTPUTFILE = "data/data.txt"

n_cities = read_number_of_cities()
cities = read_city_coordinates(n_cities)
write_to_file(cities, OUTPUTFILE)
