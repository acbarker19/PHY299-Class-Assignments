# HW 7-2
# Alec Barker

import math
import numpy as np
import matplotlib.pyplot as plt

# P3.3.1

a = 0
b = 2

angles = np.linspace(0, 8 * math.pi, 1000)
radiuses = []

for angle in angles:
    r = a + b * angle
    radiuses.append(r)
    
fig = plt.figure(dpi = 300)
plt.polar(angles, radiuses, c = "r")
plt.title("Archimedean Spiral", size = "x-large")
plt.show()
  
a = 0.8
radiuses = []

for angle in angles:
    r = a**angle
    radiuses.append(r)
    
fig = plt.figure(dpi = 300)
plt.polar(angles, radiuses, c = "b")
plt.title("Logarithmic Spiral", size = "x-large")
plt.show()