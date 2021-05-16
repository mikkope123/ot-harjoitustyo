from tkinter import Tk, ttk
import sys
from solver.solver import Route
from fileio.fileio import Output_handler

class UI:
    """Class for user interface for TSP solver"""
    def __init__(self, root, route):
        self._root = root
        self.route = route
        self.result_file = "results/route"

    def start(self):
        solve = ttk.Button(master=self._root, text="Solve", command=self._start_solve)
        solve.pack()

    def _start_solve(self):
        image_file = "results/route.png"
        result_file = "results/route"
        self.route.solve()
        self.route.print_route()
        route = self.route.get_route()
        outputs = Output_handler(route, image_file, result_file)
        outputs.plot()
        outputs.print_to_file()
        sys.exit()


