from city.city import City
from solver.solver import Route
from UI.UI import UI
from tkinter import Tk, ttk

result_file = "results/route"

cities = []
with open("data/data.txt") as data:
    for line in data:
        raw_split = line.split()
        cities.append(City(float(raw_split[0]), float(raw_split[1])))
route = Route()
for city in cities:
    route.add_city(city)

window = Tk()
window.title("TSP solver")

ui = UI(window, route)
ui.start()

window.mainloop()
