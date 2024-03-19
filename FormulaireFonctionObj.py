from pulp import LpProblem, LpVariable, LpStatus, LpMaximize, LpMinimize
import tkinter as tk
import FormulaireContrainte

class FormulaireFonctionObj(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Variable and Coefficient Form")
        self.variable_fields = []  # Pour stocker les champs d'entrée des noms des variables
        self.constante_fields = []  # Pour stocker les champs d'entrée des constantes
        self.variables = []  # Pour stocker les objets LpVariable créés
        self.constantes = []
        self.create_variable_form()

    def create_variable_form(self):
        self.clear_widgets()

        tk.Label(self, text="Enter the number of variables:").pack()
        self.num_var_entry = tk.Entry(self)
        self.num_var_entry.pack()

        tk.Button(self, text="Next", command=self.create_fields).pack()

    def create_fields(self):
        num_variables = int(self.num_var_entry.get())
        self.clear_widgets()
        self.variable_fields.clear()
        self.constante_fields.clear()

        for i in range(num_variables):
            tk.Label(self, text=f"Variable {i+1} name:").pack()
            variable_entry = tk.Entry(self)
            variable_entry.pack()
            self.variable_fields.append(variable_entry)

            tk.Label(self, text=f"Variable {i+1} coefficient:").pack()
            constante_entry = tk.Entry(self)
            constante_entry.pack()
            self.constante_fields.append(constante_entry)

        tk.Button(self, text="Next", command=self.create_variables).pack()
        tk.Button(self, text="Back", command=self.create_variable_form).pack()

    def create_variables(self):
        for i in range(len(self.variable_fields)):
            variable = LpVariable(self.variable_fields[i].get(), cat="Integer")
            self.variables.append(variable)
            self.constantes.append( int(self.constante_fields[i].get()) )

            print(self.variable_fields[i].get()+" : "+self.constante_fields[i].get())

        window = FormulaireContrainte.FormulaireContrainte(self.variables,self.constantes)
        # self.clear_widgets()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

def main():
    window = FormulaireFonctionObj()
    window.mainloop()

if __name__ == "__main__":
    main()
