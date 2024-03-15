from scipy.optimize import linprog
import numpy as np
import random

# Task 2
# Compute the best strategy to schedule the use of the appliances
off_peak_hours = range(0-16) and range(21-24)
peak_hours = range(17-20)
lighting_hours = range(10-20) # switch appliance?

# Non-shiftable appliances
lighting = 1.5
refrigerator = 2
tv = 0.6
electric_stove = 3.9

# Shiftable appliances
dishwasher = 1.44
laundry_machine = 1.94
cloth_dryer = 2.50
electric_vehicle = 9.9

# using a random function to generate the pricing curve in a day
def generate_pricing_curve():
    random.seed(6)
    price_curve = []
    for i in range(24):
        if i in peak_hours:
            # higher price in the peak hours
            price_curve.append(random.uniform(1, 1.5))
        else:
            # lower price in the off-peak hours
            price_curve.append(random.uniform(0.5, 1))
    return price_curve

pricing_curve = generate_pricing_curve()
print(pricing_curve)


# write a program in order to minimize energy cost
# linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None)
