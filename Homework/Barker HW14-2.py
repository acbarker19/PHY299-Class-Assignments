# 14-2
# Alec Barker

import numpy as np
from scipy import optimize

def P(n):
    return (n - 1)*K1 + (n - 1)*K2 + ((n - 1)**2)*K1*K2*d

d = 0.5
K1 = 2.8
K2 = 5

nvals = np.linspace(0, 1, 100)
Pvals = [P(n) for n in nvals]

min_index = Pvals.index(min(Pvals))
min_n = nvals[min_index]
print("(Try 1) Numerical value for n:", min_n)

data = optimize.minimize(P, 0.45)
print("(Try 2) Numerical value for n:", data['x'])



# dP/dn = K2 + K1*(1 - 2*d*K2 + 2*d*K2*n) = 0

n = (-K2/K1 + 2*d*K2 - 1)/(2*d*K2)
print("\nAnalytical value for n:", n)