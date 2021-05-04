from tkinter import Tk, ttk
import sys
from solver.solver import Route

class UI:
    def __init__(self, root, route):
        self._root = root
        self.route = route
        self.result_file = "results/route"

    def start(self):
        solve = ttk.Button(master=self._root, text="Solve", command=self._start_solve)
        solve.pack()

    def _start_solve(self):
        self.route.solve()
        self.route.print_route()
        self.route.print_to_file(self.result_file)
        self.route.plot()
        sys.exit()


