import tkinter as tk
from tkinter import ttk
import Contrainte
import function
import Result

class FormulaireContrainte(tk.Tk):
    def __init__(self, variables, constantes):
        super().__init__()
        self.variables = variables
        self.constantesFonctionObj = constantes
        self.contrainte_entries = []
        self.inegalite_comboboxes = []
        self.disponible_entries = []
        self.create_contrainte_form()

    def create_contrainte_form(self):
        self.clear_widgets()

        tk.Label(self, text="Nombre de contraintes:").pack()
        self.nb_contraintes_entry = tk.Entry(self)
        self.nb_contraintes_entry.pack()

        tk.Button(self, text="Suivant", command=self.create_contrainte_fields).pack()

    def create_contrainte_fields(self):
        nb_contraintes = int(self.nb_contraintes_entry.get())
        self.clear_widgets()

        for i in range(nb_contraintes):
            tk.Label(self, text=f"Contrainte {i+1}").pack()
            contrainte_var_entries = []
            for var in self.variables:
                tk.Label(self, text=f"Constante {var}:").pack()
                entry = tk.Entry(self)
                entry.pack()
                contrainte_var_entries.append(entry)
            self.contrainte_entries.append(contrainte_var_entries)

            tk.Label(self, text="Disponible:").pack()
            disponible_entry = tk.Entry(self)
            disponible_entry.pack()
            self.disponible_entries.append(disponible_entry)

            tk.Label(self, text="Inégalité:").pack()
            combobox = ttk.Combobox(self, values=[">=", "<=", ">", "<","="])
            combobox.pack()
            self.inegalite_comboboxes.append(combobox)

        tk.Button(self, text="Soumettre", command=self.afficher_contraintes).pack()

    def afficher_contraintes(self):
        contraintes = []
        for i in range(len(self.contrainte_entries)):
            constantes = []
            for j in range(len(self.contrainte_entries[i])):
                constantes.append(int(self.contrainte_entries[i][j].get()))
            contrainte = Contrainte.Contrainte(self.variables,constantes,self.inegalite_comboboxes,self.disponible_entries[i])
            contraintes.append(contrainte)
        prob = getSolution(self.variables,self.constantesFonctionObj,contraintes)
        print("Status de la résolution après :",LpStatus[prob.status])
        print("Valeur optimale de la fonction objective :",prob.objective.value())
        print("x : ", prob.variables()[0].value())
        print("y : ", prob.variables()[1].value())
        window = Result.Result(prob,self.variables)
            
        # for i, contrainte in enumerate(self.contrainte_entries):
        #     contrainte_values = [entry.get() for entry in contrainte]
        #     disponible = self.disponible_entries[i].get()
        #     inegalite = self.inegalite_comboboxes[i].get()
        #     print(f"Contrainte {i+1}: {contrainte_values}, Disponible: {disponible}, Inégalité: {inegalite}")

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

# def main():
#     variables = ["x", "y"] 
#     app = FormulaireContrainte(variables)
#     app.mainloop()

# if __name__ == "__main__":
#     main()
