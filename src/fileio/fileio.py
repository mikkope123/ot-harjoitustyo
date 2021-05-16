import matplotlib.pyplot as plt
from city.city import City

class File_reader:
    def __init__(self, filename):
        self.file = filename
        self.__cities = []

    def read_file(self):
        with open(self.file) as data:
            for line in data:
                raw_split = line.split()
                self.__cities.append(City(float(raw_split[0]), float(raw_split[1])))
        return self.__cities

class Output_handler:
    def __init__(self, final_route, image_file, result_file, output_type):
        self.image_file = image_file
        self.result_file = result_file
        self.route = final_route
        self.format = output_type

    def plot(self):
        """Plots the current route and saves it as an image.

        Returns:
            True if the image is succesfully created."""
        x = []
        y = []
        for city in self.route:
            coordinates = city.get_coordinates()
            x.append(coordinates[0])
            y.append(coordinates[1])
        plt.plot(x,y)
        plt.savefig(self.image_file, format=self.format)
        print("The plot of the route saved to file:", self.image_file)
        return True

    def print_to_file(self):
        """Saves the current route to a file.

        Returns:
            True if writing was succesful"""
        f = open(self.result_file, "w")
        for city in self.route:
            coordinates = city.get_coordinates()
            coordinate_string = str(coordinates[0]) + " " + str(coordinates[1]) + "\n"
            f.write(str(coordinate_string))
        f.close()
        print("The route saved to file:", self.result_file)
        return True
