# HW 7-3
# Alec Barker

import math
import matplotlib.pyplot as plt

# P2.7.5 Graphed

g = 9.81

angles = range(91)
range_vals = []
height_vals = []

def get_range_and_height(a, v):
    range_val = ((v**2) * math.sin(math.radians(2 * a))) / g
    height = ((v**2) * (math.sin(math.radians(a)))**2) / (2 * g)
    return round(range_val, 4), round(height, 4)
 
for a in angles:
    range_val, height = get_range_and_height(a, 10)
    range_vals.append(range_val)
    height_vals.append(height)

fig = plt.figure(dpi = 200)
plt.axhline(y = 0, c = "k", lw = 2)
plt.axvline(x = 0, c = "k", lw = 2)
plt.plot(angles, range_vals, c = "r", label = "Ranges")
plt.plot(angles, height_vals, c = "b", label = "Heights")
plt.legend(loc = "best")
plt.xlabel("Angle α")
plt.ylabel("Distance (m)")
plt.title("Range and Height of a Projectile at Various Angles", size = "large")
plt.show()

range_val, height = get_range_and_height(45, 10)
print(range_val, " ", height)