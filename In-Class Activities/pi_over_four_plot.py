import random
import math
import numpy
import matplotlib.pyplot as plt

N = 1000
count = 0

x_vals = []
y_vals = []

pi_x_vals = numpy.linspace(0, 1, N)
pi_y_vals = []

colors = []

for i in range(N):
    x = random.random()
    y = random.random()
    
    if y < math.sqrt(1 - x**2):
        count += 1
        colors.append("b")
    else:
        colors.append("r")
    
    x_vals.append(x)
    y_vals.append(y)
    
    pi_y_vals.append(math.sqrt(1 - pi_x_vals[i]**2))

print("{0} out of {1} points found below the function curve y = (1 - x^2)^0.5".format(count, N))
print("Estimated value of pi/4: ", count / N)
print("Actual value of pi/4: ", math.pi / 4)

fig = plt.figure(dpi = 200)

plt.plot(pi_x_vals, pi_y_vals, c = "k")

plt.scatter(x_vals, y_vals, c = colors, s = 10, alpha = 0.3)

plt.axhline(y = 0, c = "k", lw = 2)
plt.axvline(x = 0, c = "k", lw = 2)
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal')

plt.show()