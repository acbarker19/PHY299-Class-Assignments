# HW 9-1
# Alec Barker

import numpy as np
import matplotlib.pyplot as plt

"""
N = 1000
xy_vals = np.linspace(-2, 2, N)
z_vals = np.zeros([N, N], float)

for y in range(N):
    y_val = xy_vals[y]
    
    for x in range(N):
        x_val = xy_vals[x]
        
        c = complex(x_val, y_val)
        count = 0
        z = 0
        
        while count < 100:
            count += 1
            z = z**2 + c
            if abs(z) > 2.0:
                break
        
        z_vals[x, y] = count
        
np.savetxt("Data Files\mandelbrot_data.txt", z_vals)
"""

z_vals = np.loadtxt("Data Files\mandelbrot_data.txt")

fig = plt.figure(dpi = 300)
plt.imshow(z_vals, cmap = "CMRmap")
plt.show()