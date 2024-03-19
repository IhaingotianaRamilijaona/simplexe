from pulp import LpProblem,LpVariable,LpStatus,LpMaximize,LpMinimize,LpConstraint

class Contrainte:
    def __init__(self,variables,constantes,egalite,disponible):
        self.variables = variables
        self.constantes = constantes
        self.egalite = egalite
        self.disponible = disponible

    def getContrainte(self):
        contrainteValue = 0
        for i in range(len(self.variables)):
            contrainteValue += (self.constantes[i]*self.variables[i]) 
            # print(str(self.constantes[i])+""+str(self.variables[i].name))

        if self.egalite == ">=":
            return contrainteValue >= self.disponible
        elif self.egalite == "<=":
            return contrainteValue <= self.disponible
        elif self.egalite == "=":
            return contrainteValue == self.disponible
        elif self.egalite == ">":
            return contrainteValue > self.disponible
        elif self.egalite == "<":
            return contrainteValue < self.disponible
        else:
            raise ValueError("Signe invalide")






        #      def afficher_contraintes(self):
        # contraintes = []
        # for i in range(len(self.contrainte_entries)):
        #     constantes = []
        #     for j in range(len(self.contrainte_entries[i])):
        #         constantes.append(int(self.contrainte_entries[i].get()))
        #     contrainte = Contrainte.Contrainte(self.variables,constantes,self.inegalite_comboboxes,self.disponible_entries[i])
        #     contraintes.append(contrainte)