# HW1
# Alec Barker

import math

"""
Q2.2.1 Expected Results
   
a. 2.7 / 2 = 1.35
b. 2 / 4 - 1 = -0.5
c. 2 // 4 - 1 = -1
d. (2 + 5) % 3 = 1
e. 2 + 5 % 3 = 4
f. 3 * 4 // 6 = 2
g. 3 * (4 // 6) = 0
h. 3 * 2 ** 2 = 12
i. 3 ** 2 * 2 = 18
"""
print("Q2.2.1 Executed Results")
print("a. 2.7 / 2 = " + str(2.7 / 2))
print("b. 2 / 4 - 1 = " + str(2 / 4 - 1))
print("c. 2 // 4 - 1 = " + str(2 // 4 - 1))
print("d. (2 + 5) % 3 = " + str((2 + 5) % 3))
print("e. 2 + 5 % 3 = " + str(2 + 5 % 3))
print("f. 3 * 4 // 6 = " + str(3 * 4 // 6))
print("g. 3 * (4 // 6) = " + str(3 * (4 // 6)))
print("h. 3 * 2 ** 2 = " + str(3 * 2 ** 2))
print("i. 3 ** 2 * 2 = " + str(3 ** 2 * 2))



"""
Q2.2.5

The e variable that is set by the user is being overwritten during the import
statement by the mathematical constant e, which is equal to 2.71828.
"""



"""
Q2.2.9 Expected Results

a. True
b. False
c. True
d. True
e. False
f. 2
g. 0
h. 1
i. False
"""
print("\n\rQ2.2.9 Executed Results")
print("a. " + str(not 1 < 2 or 4 > 2))
print("b. " + str(not (1 < 2 or 4 > 2)))
print("c. " + str(1 < 2 or 4 > 2))
print("d. " + str(4 > 2 or 10/0 == 0))
print("e. " + str(not 0 < 1))
print("f. " + str(1 and 2))
print("g. " + str(0 and 1))
print("h. " + str(1 or 0))
print("i. " + str(type(complex(2, 3).real) is int))



print("\r\nP2.2.4")

a = 6378137.0
c = 6356752.314245
e2 = 1 - ((c**2)/(a**2))
e = math.sqrt(e2)
s = 2 * math.pi * (a**2) * (1 + ((1 - e2) / e) * math.atanh(e))
print("Oblate Spheroid Surface Area: " + str(s) + " m")

r = 6371 * 1000
s = 4 * math.pi * r**2
print("Perfect Sphere Surface Area: " + str(s) + " m")