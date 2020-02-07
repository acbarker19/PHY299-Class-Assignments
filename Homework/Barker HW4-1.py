# HW 4-1
# Alec Barker

import math

# Q2.5.2

a = 1
b = math.sqrt(2)

while a != b:
    stored_a = a
    stored_b = b
    
    a = 0.5 * (stored_a + stored_b)
    b = math.sqrt(stored_a * stored_b)
    
    print(a, b)

G = 1 / a
print("Gauss's Constant: ", a)