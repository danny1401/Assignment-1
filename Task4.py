import numpy as np
from scipy.optimize import linprog

# Coefficient matrix of the equality constraints
A_eq = []
for i in range(4):
    row = [1 if i * 24 <= j < i * 24 + 24 else 0 for j in range(96)]
    A_eq.append(row)

# Right-hand side of the equality constraints
b_eq = [1.44, 1.94, 2.5, 9.9]

# Coefficient matrix of the inequality constraints
A_ub = []  
identity_matrix = np.eye(24)
for i in range(24):
    row = np.tile(identity_matrix[i], 4)
    A_ub.append(row.tolist())

# Right-hand side of the inequality constraints
hour_power_cap_vector = np.full(24, 7)  # in kWh
k = np.array([0.77 for _ in range(24)])  # hourly power usage for all non-shiftable appliances
b_ub = hour_power_cap_vector - k  

# Bounds for each decision variable
bounds = [(0, None) for _ in range(96)]  # Non-negative bounds for all variables

# Objective function coefficients
c = [00.8966700418808315, 0.9109770211598633, 0.7425173139654726, 0.630810741472329, 0.5002258574425356, 0.8314092814418839, 0.7351271285322225, 0.8798653175489466, 0.6865801860369207, 0.8850699179689951, 0.6363490428359854, 0.9009577415813018, 0.864912416311008, 0.7070032205826517, 0.7691526097776384, 0.8410258706443392, 0.5964924378820438, 0.7768075827491421, 0.9025620249244866, 0.632760527219251, 0.9016826548056567, 0.8428449410502205, 0.9221411623980824, 0.6677910089129071] * 4

# Solve the linear programming problem
result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Check if the optimization was successful
if result.success:
    optimal_solution = result.x
    optimal_value = result.fun
    print("Optimal Solution:", optimal_solution)
    print("Optimal Value of Objective Function:", optimal_value)
else:
    print("Optimization failed. Message:", result.message)
