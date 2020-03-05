import matplotlib.pyplot as plt
import numpy as np
import random as r
import math

x = 0.73
y = .053
z = 2.219

print("{:.2e}".format(-1*(x**y)/z))



N = 148
val = 0
for i in range(2, N + 1):
    if i % 2 == 0:
        val += i
print(val)



tol = 1E-3
i = 1
ans = math.log(2)
val = 1
while abs(ans - val) > tol:
    i += 1
    if i % 2 == 0:
        val -= i**(-1)
    else:
        val += i**(-1)
print(i)



xvals = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
yvals = []
for i in xvals:
    yvals.append((math.sin(i)**3)/(2 + math.cos(i)))
plt.figure(dpi = 100)
plt.plot(xvals, yvals)
plt.show()



xvals = [0]
yvals = [0]
N = 1e5
while len(xvals) < 10000:
    rand = r.random()
    if rand < 0.01:
        xvals.append(0)
        yvals.append(0.16 * yvals[-1])
    elif rand < 0.86:
        xvals.append(0.85 * xvals[-1] + 0.04 * yvals[-1])
        yvals.append(-0.04 * xvals[-1] + 0.85 * yvals[-1] + 1.6)
    elif rand < 0.93:
        xvals.append(0.2 * xvals[-1] - 0.26 * yvals[-1])
        yvals.append(0.23 * xvals[-1] + 0.23 * yvals[-1] + 1.6)
    else:
        xvals.append(-0.15 * xvals[-1] + 0.28 * yvals[-1])
        yvals.append(0.26 * xvals[-1] + 0.24 * yvals[-1] + 0.44)
plt.figure(dpi = 100)
plt.scatter(xvals, yvals, c="g", s=1)
plt.show()



L = 10
Lvals = [10]
Llimit = 50
N = 100
averages = []
counts = []
while L < Llimit:
    for i in range(N):
        w1 = r.randint(1, L)
        while True:
            w2 = r.randint(0, L)
            if w1 != w2:
                break
        count = 0
        while True:
            w1m = r.randint(1, 2)
            w2m = r.randint(1, 2)
            if w1m == 1:
                if w1 - 1 > 1:
                    w1 -= 1
            else:
                if w1 + 1 < L:
                    w1 += 1
            if w2m == 1:
                if w2 - 1 > 1:
                    w2 -= 1
            else:
                if w2 + 1 < L:
                    w2 += 1
            count += 1
            if w1 == w2:
                counts.append(count)
                break
    averages.append(np.mean(counts))
    L += 5
    if L < Llimit:
        Lvals.append(L)
plt.figure(dpi=100)
plt.scatter(Lvals, averages)
plt.show()



def displacement(a, t):
    return .5 * a * t**2
print("{:.2e} m".format(displacement(8.17, 5.2)))



x = 0.25
y = 106.88
z = 13.67
print("{:.2e}".format(math.log10(x)**(y * -1) * math.sqrt(z)))



p = [1, 2, 3, 4, 5, 6]
c = []
for i in range(6):
    while True:
        rand = r.randint(1, 31)
        if rand not in c:
            c.append(rand)
            break
c.sort()
print(p == r)



x = np.linspace(0, 10, 1000)
y = []
for i in x:
    y.append(math.tanh(i) * math.e**(-1 * math.sin(i)))
plt.figure(dpi = 100)
plt.plot(x, y)
plt.show()