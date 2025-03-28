import numpy as np

R = 8.314

def vanderWaals(T):
    V = np.linspace(0.34, 5, 100)
    P = []
    for v in V:
        P.append(((8 * T) / (3 * v - 1)) - (3 / v ** 2))
    return T, V, P

def critical(a, b):
    Tc = (8 * a) / (27 * R * b)
    Pc = a / (27 * b**2)
    return Tc, Pc

T1, V1, P1 = vanderWaals(1)
T2, V2, P2 = vanderWaals(0.9)
T3, V3, P3 = vanderWaals(1.1)

plt.figure(dpi = 200)
plt.plot(V1, P1, c = "b", label = "T = 1")
plt.plot(V2, P2, c = "g", label = "T = 0.9")
plt.plot(V3, P3, c = "r", label = "T = 1.1")
plt.ylim(0, 2)
plt.legend(loc = "best")
plt.show()

a = 4.28E-1
b = 3.71E-5
Tc, Pc = critical(a, b)
print("Critical Temperature of Ammonia = {:.2g} K, " \
      "Critical Pressure of Ammonia = {:.2g} Pa".format(Tc, Pc))

T, p = 298, 1.01325e5
poly = Polynomial([-a * b, a, -(p * b + R * T), p])
roots = poly.roots()
print("For STP: ")