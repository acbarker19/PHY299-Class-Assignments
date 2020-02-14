# HW 7-1
# Alec Barker

import numpy as np
import math
import matplotlib.pyplot as plt

# P3.1.1

xvals = np.linspace(-20, 20, 1000)
yvals1 = []
yvals2 = []

for x in xvals:
    y = math.log(1 / math.cos(x)**2)
    yvals1.append(y)
    
    y = math.log(1 / math.sin(x)**2)
    yvals2.append(y)

fig = plt.figure(dpi = 300)
plt.axhline(y = 0, c = "k", lw = 2)
plt.axvline(x = 0, c = "k", lw = 2)
plt.plot(xvals, yvals1, c = "b", label = "ln(1 / cos^2x)")
plt.plot(xvals, yvals2, c = "r", label = "ln(1 / sin^2x)")
plt.legend(loc = "best")
plt.show()

"""
At ln(1 / cos^2x), the values should be at y = 0 at every multiple of pi,
while ln(1 / sin^2x) should be at y = 0 at every multiple of pi + pi/2
(for example pi/2, 3pi/2, 5pi/2, etc).

The graph reflects this properly.
"""