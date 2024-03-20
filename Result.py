from pulp import LpProblem,LpVariable,LpStatus,LpMaximize,LpMinimize
from pulp import LpProblem, LpVariable, LpStatus, LpMaximize, LpMinimize
import tkinter as tk
import function
class Result(tk.Tk):
    def __init__(self, prob, variables):
        super().__init__()
        self.prob = prob
        self.variables = variables
        self.display_results()

    def display_results(self):
        status_label = tk.Label(self, text="Status de la résolution après : " + LpStatus[self.prob.status])
        status_label.pack()

        value_label = tk.Label(self, text="Valeur optimale de la fonction objective : " + str(self.prob.objective.value()))
        value_label.pack()

        for var in self.variables:
            var_value = str(self.prob.variables_dict[var].value())
            var_label = tk.Label(self, text=f"{var} : {var_value}")
            var_label.pack()

