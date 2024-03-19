from pulp import LpProblem,LpVariable,LpStatus,LpMaximize,LpMinimize

prob = LpProblem("Exemple",LpMaximize)

x = LpVariable("x", cat="Integer")
y = LpVariable("y", cat="Integer")

prob += 2*x + 3*y , "FonctionObjectif"

prob += x + 2*y >= 4, "Contrainte_1"
prob += 3*x - y <= 6, "Contrainte_2"
prob += x >= 0, "Contrainte_3"
prob += y >= 0, "Contrainte_4"

prob.solve()

print("Status de la résolution après :",LpStatus[prob.status])
print("Valeur optimale de la fonction objective :",prob.objective.value())
print("x : ", x.value())
print("y : ", y.value())

# from scipy . optimize import minimize

# def fun (x) :
#     return (x -2) **2

# def fun2Variable ( x):
#     return ( x [0] -2) **2 + (x [1] -2) **2
# # fonction fun à partir de x2
# x0 = 0
# result = minimize ( fun , x0 )
# print ( result )

# #le resultat se trouve dans
# print ( result .x )

# # pour la fonction à deux variables
# x0 = [0 ,0]
# result = minimize ( fun2Variable , x0 )
# print ( "result ",result )

# def objective (x):
#     return ( x [0] -3) **2 + (x [1]+1) **2
# # fonction pour la contrainte
# def contrainte_fonction (x) :
#     return x [0]+ x [1] -5
# def contrainte_positivite_x (x) :
#     return x [0]
# def contrainte_positivite_y (x) :
#     return x [1]

# bound = [(0 ,5) ,(0 ,5) ]
# # construction de la contrainte avec son type
# contrainte = [
#     {'type': 'eq', 'fun': contrainte_fonction},
#     {'type': 'ineq', 'fun': contrainte_positivite_x},
#     {'type': 'ineq', 'fun': contrainte_positivite_y}
# ]
# # point de dé part
# x0 = [0 ,0]
# result = minimize ( objective , x0 , constraints = contrainte , bounds = bound )
# print ( result )