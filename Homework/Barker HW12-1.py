# HW 12-1
# Alec Barker

# Q8.2.2

from scipy import integrate
import numpy as np

# part b
def b(x):
    return x**3 / (np.exp(x) - 1)

value, error = integrate.quad(b,0,np.inf)

print("Part B. quad() indicates the value is {0:.2e} with absolute error no greater than {1:.2e}".format(value,error))



# part c
def c(x):
    return x**(-x)

value, error = integrate.quad(c,0,1)

print("Part C. quad() indicates the value is {0:.2e} with absolute error no greater than {1:.2e}".format(value,error))