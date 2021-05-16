from city.city import City
from solver.solver import Route
from UI.UI import UI
from tkinter import Tk, ttk
from fileio.fileio import File_reader


if __name__ == "__main__":
    result_file = "results/route"
    input_file = "data/data.txt"
    reader = File_reader(input_file)
    cities = reader.read_file()

    route = Route(cities)

    window = Tk()
    window.title("TSP solver")

    ui = UI(window, route)
    ui.start()

    window.mainloop()
