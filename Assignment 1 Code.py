# -*- coding: utf-8 -*-
"""Notebook 1 DO NOT SUBMIT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MJzV7ulo0TH6ORzod75q1k9YLK15ahJo
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

#Minimization Problem
prob = LpProblem("Minimize_Z", LpMinimize)

#Decision Variables
#yogurt
x1 = LpVariable('x1', lowBound=0)
#spinach
x2 = LpVariable('x2', lowBound=0)
#chickpea patties
x3 = LpVariable('x3', lowBound=0)
#Nature Valley bar
x4 = LpVariable('x4', lowBound=0)
#Sausage patties
x5 = LpVariable('x5', lowBound=0)

#test

#Objective function
prob += 1.18 * x1 + 0.9 * x2 + 1.15 * x3 + 1.1 * x4 + 1.66 * x5, "Z"

#Constraints (in MG)
prob += 420 * x1 + 455 * x2 + 2660 * x3 + 1120 * x4 + 3220 * x5 <= 35000, "Sodium"
prob += 840 * x1 + 140 * x2 + 1190 * x3 + 1330 * x4 + 120 * x5 >= 14000, "Energy/Calories"
prob += 0.105 * x1 + 0.014 * x2 + 0.063 * x3 + 0.028 * x4 + 0.126 * x5 >= 0.350, "Protein"
prob += 0 * x1 + 0 * x2 + 0 * x3 + 0 * x4 + 0 * x5 >= 140, "VitaminD"
prob += 1260 * x1 + 560 * x2 + 140 * x3 + 0 * x4 + 420 * x5 >= 9100, "Calcium"
prob += 1.4 * x1 + 18.9 * x2 + 8.4 * x3 + 5.6 * x4 + 12.6 * x5 >= 112, "Iron"
prob += 1680 * x1 + 0 * x2 + 1820 * x3 + 700 * x4 + 1540 * x5 >= 32900, "Potassium"


prob.solve()

if prob.status == 1:  # 1 means "Optimal"
    print("Optimal Weekly Servings (lacking Vitamin D):")
    print(f"x1/Yogurt = ", round(value(x1)))
    print(f"x2/Spinach = ",  round(value(x2)))
    print(f"x3/Chickpea Patties = ",  round(value(x3)))
    print(f"x4/Nature Valley Bar = ",  round(value(x4)))
    print(f"x5/Sausage Patties = ",  round(value(x5)))
    print(f"Optimal Z (cost) =  $", round(value(prob.objective), 2))
else:
    print("No optimal solution found.")

#Removing Vitamin D
#Minimization Problem
prob = LpProblem("Minimize_D", LpMinimize)

#Decision Variables
#yogurt
x1 = LpVariable('x1', lowBound=0)
#spinach
x2 = LpVariable('x2', lowBound=0)
#chickpea patties
x3 = LpVariable('x3', lowBound=0)
#Nature Valley bar
x4 = LpVariable('x4', lowBound=0)
#Sausage patties
x5 = LpVariable('x5', lowBound=0)

#Objective function
prob += 1.18 * x1 + 0.9 * x2 + 1.15 * x3 + 1.1 * x4 + 1.66 * x5, "Z"

#Constraints
prob += 420 * x1 + 455 * x2 + 2660 * x3 + 1120 * x4 + 3220 * x5 <= 35000, "Sodium"
prob += 840 * x1 + 140 * x2 + 1190 * x3 + 1330 * x4 + 120 * x5 >= 14000, "Energy/Calories"
prob += 0.105 * x1 + 0.014 * x2 + 0.063 * x3 + 0.028 * x4 + 0.126 * x5 >= 0.350, "Protein"
#prob += 0 * x1 + 0 * x2 + 0 * x3 + 0 * x4 + 0 * x5 >= 140, "VitaminD"
prob += 1260 * x1 + 560 * x2 + 140 * x3 + 0 * x4 + 420 * x5 >= 9100, "Calcium"
prob += 1.4 * x1 + 18.9 * x2 + 8.4 * x3 + 5.6 * x4 + 12.6 * x5 >= 112, "Iron"
prob += 1680 * x1 + 0 * x2 + 1820 * x3 + 700 * x4 + 1540 * x5 >= 32900, "Potassium"


prob.solve()

if prob.status == 1:  # 1 means "Optimal"
    print("Optimal Weekly Servings (lacking Vitamin D):")
    print(f"x1/Yogurt = ", round(value(x1)))
    print(f"x2/Spinach = ",  round(value(x2)))
    print(f"x3/Chickpea Patties = ",  round(value(x3)))
    print(f"x4/Nature Valley Bar = ",  round(value(x4)))
    print(f"x5/Sausage Patties = ",  round(value(x5)))
    print(f"Optimal Z (cost) =  $", round(value(prob.objective), 2))
else:
    print("No optimal solution found.")

#Removing Vitamin D, need at least 1 serving of each food
#Minimization Problem
prob = LpProblem("Minimize_D", LpMinimize)

#Decision Variables
#yogurt
x1 = LpVariable('x1', lowBound=0)
#spinach
x2 = LpVariable('x2', lowBound=0)
#chickpea patties
x3 = LpVariable('x3', lowBound=0)
#Nature Valley bar
x4 = LpVariable('x4', lowBound=0)
#Sausage patties
x5 = LpVariable('x5', lowBound=0)

#Objective function
prob += 1.18 * x1 + 0.9 * x2 + 1.15 * x3 + 1.1 * x4 + 1.66 * x5, "Z"

#Serving constraints
prob += x1 >= 1
prob += x2 >= 1
prob += x3 >= 1
prob += x4 >= 1
prob += x5 >= 1

#Constraints
prob += 420 * x1 + 455 * x2 + 2660 * x3 + 1120 * x4 + 3220 * x5 <= 35000, "Sodium"
prob += 840 * x1 + 140 * x2 + 1190 * x3 + 1330 * x4 + 120 * x5 >= 14000, "Energy/Calories"
prob += 0.105 * x1 + 0.014 * x2 + 0.063 * x3 + 0.028 * x4 + 0.126 * x5 >= 0.350, "Protein"
#prob += 0 * x1 + 0 * x2 + 0 * x3 + 0 * x4 + 0 * x5 >= 140, "VitaminD"
prob += 1260 * x1 + 560 * x2 + 140 * x3 + 0 * x4 + 420 * x5 >= 9100, "Calcium"
prob += 1.4 * x1 + 18.9 * x2 + 8.4 * x3 + 5.6 * x4 + 12.6 * x5 >= 112, "Iron"
prob += 1680 * x1 + 0 * x2 + 1820 * x3 + 700 * x4 + 1540 * x5 >= 32900, "Potassium"



prob.solve()

if prob.status == 1:  # 1 means "Optimal"
    print("Optimal Weekly Servings (lacking Vitamin D and including Spinach):")
    print(f"x1/Yogurt = ", round(value(x1)))
    print(f"x2/Spinach = ",  round(value(x2)))
    print(f"x3/Chickpea Patties = ",  round(value(x3)))
    print(f"x4/Nature Valley Bar = ",  round(value(x4)))
    print(f"x5/Sausage Patties = ",  round(value(x5)))
    print(f"Optimal Z (cost) =  $", round(value(prob.objective), 2))
else:
    print("No optimal solution found.")
