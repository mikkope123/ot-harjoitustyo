class File_builder:
    """Class for creating input file for TSP solver."""

    def __init__(self, outputfile: str):
        """Class constructor for File_builder class.

        Args:
            outputfile: The name of the input file to be created."""
        self.output = outputfile
        self.cities = []

    def build(self):
        """Builds the input file."""
        n_cities = self.read_number_of_cities()
        self.read_city_coordinates(n_cities)
        self.write_to_file(self.output)

    def read_number_of_cities(self):
        """Reads the number of cities to be included in the input file."""
        while True:
            n_cities = input("Give the number of cities: ")
            try:
                if int(n_cities) > 0:
                    return int(n_cities)
                print("The number of cities can't be less than 1.'")
            except:
                print("The number of cities must be an integer.")

    def read_city_coordinates(self, n_cities: int):
        coordinates_read = 0
        #cities = []
        while coordinates_read < n_cities:
            coordinates = input(f"Give the coordinates of city {coordinates_read+1} (separated by space): ")
            coord_split = coordinates.split()
            if not self.two_coordinates(coord_split):
                print("You must give exactly two coordinates!")
            else:
                if self.proper_coordinates(coord_split):
                    coordinates_read += 1
                else:
                    pass

        return self.cities

    def two_coordinates(self, coordinates: list):
        return len(coordinates) == 2

    def proper_coordinates(self, coordinates: list):
        try:
            x = float(coordinates[0])
            y = float(coordinates[1])
            if (x,y) in self.cities:
                print("Duplicate entry!")
                return False
            self.cities.append((x, y))
            return True
        except:
            print("The coordinates must be floating point numbers!")
            return False

    def write_to_file(self, output: str):
        try:
            f=  open(output, "w")
            for city in self.cities:
                city_str = str(city[0]) + " " + str(city[1]) + "\n"
                f.write(city_str)
            print("City coordinates written to file", output)
        except:
            print("Could not write to file.")

if __name__ == "__main__":
    build = File_builder("data/data.txt")
    build.build()
