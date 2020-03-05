# HW 10-1
# Alec Barker

import math
import numpy as np
import matplotlib.pyplot as plt

a = 0.75
l = 1

xvals = np.linspace(-2, 2, 1000)

def f(N):
    yvals = []
    for x in xvals:
        sum_value = 0
        for n in range(1, N + 1):
            An = (2/(math.pi * n)) * math.sin((math.pi * a * n)/l)
            kn = (2 * math.pi * n)/l
            sum_value += An * math.cos(kn * x)
        yvals.append(sum_value)
    return yvals

f1 = f(2)
f2 = f(10)
f3 = f(100)

plt.figure(dpi = 200)
plt.plot(xvals, f1, label = "N = 2")
plt.plot(xvals, f2, label = "N = 10")
plt.plot(xvals, f3, label = "N = 100")
plt.legend(loc = "best")
plt.show()