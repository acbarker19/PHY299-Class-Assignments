# HW 6-2
# Alec Barker

import math

# P2.7.5

g = 9.81

def get_range_and_height(a, v):
    range_val = ((v**2) * math.sin(math.radians(2 * a))) / g
    height = ((v**2) * (math.sin(math.radians(a)))**2) / (2 * g)
    return round(range_val, 4), round(height, 4)
    
range_val, height = get_range_and_height(30, 10)
print("Range = {} m, Height = {} m".format(range_val, height))