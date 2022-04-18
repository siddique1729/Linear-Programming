"""
Solving Using Pulp
Author: Jawwad Shadman Siddique

"""

# Importing functions

from pulp import LpProblem
from pulp import LpMinimize
from pulp import LpVariable
import pulp
from pulp import LpStatus


#
prob = LpProblem("xvariables", LpMinimize)

# Defining bound constraints for variables

x1 = LpVariable("x11", 0.0, None)
x2 = LpVariable("x22", 0.0, 5.0)
x3 = LpVariable("x33", None, 0.5)
x4 = LpVariable("x44", -3.0, None)

# Writing the Objective Function to be Minimized

prob += -29*x1 - 45*x2 + 0*x3 + 0*x4, "Minimize varr"

# Adding the Constraints

prob += x1 - x2 - 3*x3 + 0*x4 <= 5.0, "x1prb"
prob += 2*x1 - 3*x2 - 7*x3 + 3*x4 >= 10.0, "x2prob"
prob += 2*x1 + 8*x2 + x3 + 0*x4 == 60.0, "x3prob"
prob += 4*x1 + 4*x2 + 0*x3 + x4 == 60.0, "x4prob"


# Solving Using Pulp
prob.writeLP("varout.lp")
prob.solve()

print("Status:", LpStatus[prob.status])

# Printing the values

for v in prob.variables():
    print(v.name, "=", v.varValue)