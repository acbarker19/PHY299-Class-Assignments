# Midterm part 1
# Alec Barker

import math
import numpy as np
import matplotlib.pyplot as plt

# problem 1-1
print("Problem 1-1: {:.6}".format(float(math.log(4 - 0.5 * (0.15**3)))))

# problem 1-2
A = 1.5
w = 0.35
k = 0.05

tvals = np.linspace(0, 100, 1000)
xtvals = []
for t in tvals:
    xtvals.append(A * math.cos(w * t) * (math.e**(-1 * k * t)))

print("Problem 1-2:")
plt.figure(dpi = 200)
plt.plot(tvals, xtvals, c = 'g')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()

# problem 1-3
E = 0
x = 0
while E <= 2:
    x += 0.01
    E = 100 * abs((math.sin(x) - x) / math.sin(x))
print("Problem 1-3:   x = {} radians, x = {:.6} degrees".format(
        x, math.degrees(x)))

# problem 1-4
def f(value):
    return value[::-1]

print("\r\nProblem 1-4:")
val = "Nuclear physics is rad!"
print("Original:", val)
val = f(val)
print("Reversed:", val)
val = f(val)
print("Reversed Again:", val)