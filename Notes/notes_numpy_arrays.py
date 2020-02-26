import numpy as np
import matplotlib.pyplot as plt
import random

print("Numpy Arrays")

# 1d array with 4 zeros
print("np.zeros(4, float) =", np.zeros(4, float))
# 2d array of zeros with 3 rows and 4 columns
print("np.zeros([3, 4], float) =", np.zeros([3, 4], float))
# same as above but with ones
print("np.ones([3, 4], float) =", np.ones([3, 4], float))
# an empty array
print("np.empty([3, 4], float) =", np.empty([3, 4], float))
# create an array with a list or list of lists
r = [[1.0, 2, 3], [5.5, 4.4, 9]]
print("r =", r)
print("np.array(r, int) =", np.array(r, int))

def f(i, j):
    return 2*i*j
print("np.fromfunction(f, (4, 3)) =", np.fromfunction(f, (4, 3)))

def f(i, j):
    return i*j**2
a = np.fromfunction(f, (100, 100))
fig = plt.figure(dpi = 300)
plt.imshow(a)
plt.show()



print("\r\nSave and Load from Text File")
a = np.array([[1, 2, 3], [4, 5, 6]], float)
np.savetxt("Data Files/demo_array.txt", a)
b = np.loadtxt('Data Files/demo_array.txt')
print("loadtxt():", b)



print("\r\n1D and 2D Arrays")
a = np.array([1, 2, 3], float)
a[0] = 5.5
print("Printing from 1D array:", a)

a = np.zeros([2, 2], int)
a[0, 1] = 1
a[1, 0] = -1
print("Printing from 2D array:", a)

a = np.array([[1, 2, 3], [4, 5, 6]], float)
print("\r\nAll values:", a)
print("0th row, columns 1 onwards:", a[0, 1:])
print("All rows, 0th column:", a[:, 0])
print("2x2 sub-block starting at 0, 1:", a[0:2, 1:3])

a = np.array([[1, 2, 3], [4, 5, 6]], float)
b = np.array([7, 8, 9], float)
print("\r\nA:", a)
print("B:", b)
a = np.vstack((a, b))
print("Stacked Values:", a)

# a 3x3x4 array
# reshape sets 3 rows, 4 columns, and 4 of the other axis
a = np.linspace(1, 48, 48).reshape(3, 4, 4)
print("\r\nAll values:", a)
print("a[1][0][3] =", a[1][0][3])
print("a[0][2] =", a[0][2])
print("a[2] =", a[2])
print("a[:, 1, 0:2] =", a[:, 1, 0:2])

a1 = np.array([1, 2, 3], float)
a2 = np.array([4, 5, 6], float)
print("\r\na1 =", a1)
print("a2 =", a2)
print("a1 + a2 =", a1 + a2)
print("a2 - a1 =", a2 - a1)
print("a1 * a2 =", a1 * a2)
print("a1 / 4 =", a1 / 4)

a = np.array([1, 2], float)
b = np.array([3, 4], float)
print("\r\nA =", a)
print("B =", b)
print("Dot Product Between A and B =", np.dot(a, b))
print("Cross Product Between A and B =", np.cross(a, b))

a = np.array([[1, 2], [0, 1]], float)
b = np.array([[1, 2], [3, 4]], float)
print("\r\nA =", a)
print("B =", b)
print("Dot Product Between A and B =", np.dot(a, b))



print("\r\nLinear Algebra")
a1 = np.array([[1, 2], [3, 4]], float)
# this is 1 * 4 - 2 * 3 = -2
print("A1 =", a1)
print("Determinant of A1 =", np.linalg.det(a1))
a2 = np.array([[5, 8, 10, 16],
               [-6, -4, 3, 10],
               [0.25, 4.2, 3.9, 0],
               [4, 5, 6, 7.5]])
print("A2 =", a2)
print("Determinant of A1 =", np.linalg.det(a2))

vals, vects = np.linalg.eig(a2)
print("\r\nA2 =", a2)
print("Values =", vals)
print("Vectors =", vects)

M = np.array([[3, -2, 0], [-2, 1, -3], [4, 6, 1]])
b = np.array([8, -20, 7])
solution = np.linalg.solve(M, b)
print(solution)
print("\r\nx = {}, y = {}, z = {}".format(*solution))

print("\r\nTransisters")
M = np.array([[1, -1, -1], [6, 3, 0], [6, 0, 2]])
b = np.array([0, 18, 45])
solution = np.linalg.solve(M, b)
print(solution)
print("I1 = {}, I2 = {}, I3 = {}".format(*solution))

print("\r\nPolynomials")
# shortcut to library
Polynomial = np.polynomial.Polynomial
p = Polynomial([6, 3, 1])
# 1000 values from -5 to 5
xvals = np.linspace(-5, 5, 1000)
# plugs x values into polynomial
yvals = p(xvals)
plt.figure(dpi = 200)
plt.plot(xvals, yvals)
plt.show()

print("\r\nPolynomial Algebra")
p = Polynomial([6, 3, 1])
q = Polynomial([0, 2, 1, 1])
print(p + q)
print(p * q)

p = Polynomial([-4, 0, 1])
print(p.roots())

print("\r\nExample E6.10")
R = 1.5
F = 2e-4
V0 = 4/3 * np.pi * R**3
T = V0 / F   # total time for the tank to empty
c2, c3 = np.pi * R, -np.pi / 3   # contant coefficients, c1 = 0
# how many time steps?
N = 100
time = np.linspace(0, T, N)
# an emptycontainer for the corresponding heights
h = np.empty(N)
#determine c0 at every step and find the roots
for i, t in enumerate(time):
    c0 = F * t - V0
    p = Polynomial([c0, 0, c2, c3])
    roots = p.roots()
    # the physically viable solution has h inside the tank
    roots = [r for r in roots if r >= 0 and r <= 2 * R]
    h[i] = roots[0]
# make a plot
plt.figure(dpi = 200)
plt.scatter(time, h, color = "k", s = 5)
plt.xlabel("Time")
plt.ylabel("Height")
plt.show()



print("\r\nCalculus")
# 6 - 5x + x^2
p = Polynomial([6, -5, 1])
print("Polynomial([6, -5, 1]) =", p)
# derivatives
p2 = p.deriv()
p3 = p.deriv(2)
# indefinite integrals
p4 = p3.integ()
p5 = p3.integ(m = 2)
# definite integrals
q = Polynomial([5])
q2 = q.integ(lbnd = 1, k = 2)
print("Polynomial([5]).integ(lbnd = 1, k = 2) =", q2)
# evaluate integral for an upper bound
print("Upper bound q2(5) =", q2(5))

print("\r\nFitting to Data")
# get noisy data of x^2
xvals = np.linspace(-10, 10, 100)
yvals = [(x + .1 * x * random.random())**2 for x in xvals]
# fit to a polynomial of degree 2
p, stats = Polynomial.fit(xvals, yvals, 2, full = True)
# determine the yvals for this polynomial
y_fit = p(xvals)
# make a plot
plt.figure(dpi = 200)
plt.scatter(xvals, yvals, s = 5, c = "k")
plt.plot(xvals, y_fit, "g-")
plt.show()
# stats[0] is the residual/sum of the error terms
print("Residual =", stats[0])
print("Coefficients =", p)