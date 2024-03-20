from pulp import LpProblem,LpVariable,LpStatus,LpMaximize,LpMinimize

prob = LpProblem("Exemple",LpMaximize)

x = LpVariable("x", cat="Integer")
y = LpVariable("y", cat="Integer")

prob += 2*x + 3*y , "FonctionObjectif"

prob += x + 2*y >= 4, "Contrainte_1"
prob += 3*x - y <= 6, "Contrainte_2"
prob += x >= 0, "Contrainte_3"
# prob += y >= 0, "Contrainte_4"

prob.solve()

print("Status de la résolution après :",LpStatus[prob.status])
print("Valeur optimale de la fonction objective :",prob.objective.value())
print("x : ", x.value())
print("y : ", y.value())