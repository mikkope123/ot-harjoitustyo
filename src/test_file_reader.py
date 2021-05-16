from fileio.fileio import File_reader
from city.city import City

filename = "data/data.txt"
reader = File_reader(filename)
cities = reader.read_file()
for city in cities:
    print(city)
