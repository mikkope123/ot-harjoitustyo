from tkinter import Tk, ttk, Radiobutton, StringVar, Label
import sys
from solver.solver import Route
from fileio.fileio import Output_handler

class UI:
    """Class for user interface for TSP solver"""
    def __init__(self, root, route):
        self._root = root
        self.route = route
        self.result_file = "results/route"
        self.output_type = StringVar()

    def start(self):
        """Creates the UI"""
        label = Label(self._root)
        label.config(text= "Select the format fo the result image (default: png)")
        label.pack()
        r1 = Radiobutton(self._root, text="png", variable = self.output_type, value="png")
        r2 = Radiobutton(self._root, text="pdf", variable = self.output_type, value="pdf")
        r3 = Radiobutton(self._root, text="svg", variable = self.output_type, value="svg")
        r1.pack()
        r2.pack()
        r3.pack()
        solve = ttk.Button(master=self._root, text="Solve", command=self._start_solve)
        solve.pack()

    def _start_solve(self):
        """Calls for solver and output algorithms."""
        output_format = str(self.output_type.get())
        if output_format == "":
            output_format = "png"
        image_file = "results/route."+output_format
        result_file = "results/route"
        self.route.solve()
        self.route.print_route()
        route = self.route.get_route()
        outputs = Output_handler(route, image_file, result_file, output_format)
        outputs.print_to_file()
        outputs.plot()
        sys.exit()


