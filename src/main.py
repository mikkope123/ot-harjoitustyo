from tkinter import Tk
from fileio.fileio import File_reader
from solver.solver import Route
from UI.UI import UI


if __name__ == "__main__":
    INPUT_FILE = "data/data.txt"
    reader = File_reader(INPUT_FILE)
    cities = reader.read_file()

    route = Route(cities)

    window = Tk()
    window.title("TSP solver")

    ui = UI(window, route)
    ui.start()

    window.mainloop()
