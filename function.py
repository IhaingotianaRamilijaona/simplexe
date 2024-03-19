from pulp import LpProblem,LpVariable,LpStatus,LpMaximize,LpMinimize
from typing import List
import Contrainte

def getSolution(variables: LpVariable,constantes: List[int],contraintes: List[Contrainte]):    
    prob = LpProblem("Exemple",LpMaximize)
    fonctionObjectifValue = 0
    for i in range(len(variables)):
        fonctionObjectifValue += constantes[i]*variables[i] 

    prob += fonctionObjectifValue , "FonctionObjectif"

    for i in range(len(contraintes)):
        prob += contraintes[i].getContrainte(),"contrainte_"+str(i)

    prob.solve()
    return prob

variables = [
    LpVariable("x", cat="Integer"),
    LpVariable("y", cat="Integer")
]
constantes = [2,3]
constantesContraintes = [
    [1,2],
    [3,-1],
    [0,1],
    [1,0]
]
contraintes = [
    Contrainte.Contrainte(variables,constantesContraintes[0],">=",4),
    Contrainte.Contrainte(variables,constantesContraintes[1],"<=",6),
    Contrainte.Contrainte(variables,constantesContraintes[2],">=",0),
    Contrainte.Contrainte(variables,constantesContraintes[3],">=",0),
]
# prob = getSolution(variables,constantes,contraintes)
# print("Status de la résolution après :",LpStatus[prob.status])
# print("Valeur optimale de la fonction objective :",prob.objective.value())
# print("x : ", prob.variables()[0].value())
# print("y : ", prob.variables()[1].value())