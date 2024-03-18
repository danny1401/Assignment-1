from scipy.optimize import linprog
import numpy as np
import random
# Define RTP scheme
peak_hours = range(17, 20)
off_peak_hours = range(0-16) and range(21-24)
peak_hours = range(17-20)
lighting_hours = range(10-20) # switch appliance?


# Define appliance information
appliances = {
    # Non-shiftable appliances
    "lightning": {"power": 1.5, "hours": range(10, 21)},
    "refrigerator": {"power": 2, "hours": range(0, 24)},
    "TV": {"power": 0.6, "hours": range(0, 24)},
    "electric_stove": {"power": 3.9, "hours": range(0, 24)},
    # Shiftable appliances
    "dishwasher": {"power": 1.44, "hours": range(24)},
    "laundry_machine": {"power": 1.94, "hours": range(24)},
    "cloth_dryer": {"power": 2.50, "hours": range(24)},
    "electric_vehicle": {"power": 9.9, "hours": range(24)}
}

# Define pricing curve generation function
def generate_pricing_curve(peak_hours):
    random.seed(6)
    pricing_curve = []
    for hour in range(24):
        if hour in peak_hours:
            pricing_curve.append(random.uniform(1, 1.5))  # Peak hours pricing
        else:
            pricing_curve.append(random.uniform(0.5, 1))  # Off-peak hours pricing
    return pricing_curve

pricing_curve = generate_pricing_curve(peak_hours)

# Define objective function coefficients (cost per kWh)
c = np.array(pricing_curve)

# Define coefficients for the constraints (power requirements)
A_eq = []
b_eq = []

for appliance in appliances.values():
    power_usage = [appliance["power"] if hour in appliance["hours"] else 0 for hour in range(24)]
    A_eq.append(power_usage)
    b_eq.append(sum(power_usage))

# Define bounds for each variable (x_i)
# Non-negativity constraints

bounds = [(0, None)] * 24  
# Solve the linear programming problem
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
if result.success:
    # Round the optimal energy consumption schedule
    optimal_schedule = np.round(result.x, decimals=7)
    total_cost = np.dot(pricing_curve, optimal_schedule)
    
    # Print the result
    print("Optimal energy consumption schedule:")
    print(optimal_schedule )
    print("Total cost:", round(result.fun, 10))
else:
    print("No solution found.")