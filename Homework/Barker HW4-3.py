# HW 4-3
# Alec Barker

# P2.5.10

import random
import math

N = 1000000
count = 0

for i in range(N):
    x = random.random()
    y = random.random()
    
    if y < math.sqrt(1 - x**2):
        count += 1

print("{0} out of {1} points found below the function curve y = (1 - x^2)^0.5".format(count, N))
print("Estimated value of pi/4: ", count / N)
print("Actual value of pi/4: ", math.pi / 4)