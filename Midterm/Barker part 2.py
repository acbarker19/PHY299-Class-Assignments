# Midterm part 2
# Alec Barker

import math
import random as r
import matplotlib.pyplot as plt

# problem 2-2
p1 = (0, 0)
p2 = (1, 0)
p3 = (0.5, math.sqrt(3) / 2)

vxvals = [0, 1, 0.5, 0]
vyvals = [0, 0, math.sqrt(3) / 2, 0]

xvals = []
yvals = []

p = [r.random(), r.random()]
xvals.append(p[0])
yvals.append(p[1])
    
print("Problem 2-2:   p = {}".format(p))

pmid = [0, 0]
    
for i in range(10000): 
    vertex = r.randint(1, 3)
    if vertex == 1:
        vertex = p1
    elif vertex == 2:
        vertex = p2
    else:
        vertex = p3
    
    if p[0] > vertex[0]:
        half_len = (p[0] - vertex[0]) / 2
        pmid[0] = p[0] - half_len
    else:
        half_len = (vertex[0] - p[0]) / 2
        pmid[0] = p[0] + half_len
        
    if p[1] > vertex[1]:
        half_len = (p[1] - vertex[1]) / 2
        pmid[1] = p[1] - half_len
    else:
        half_len = (vertex[1] - p[1]) / 2
        pmid[1] = p[1] + half_len
        
    p = pmid
    xvals.append(p[0])
    yvals.append(p[1])

plt.figure(dpi = 200)
plt.scatter(xvals, yvals, s = 1)
plt.plot(vxvals, vyvals, c = 'g')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()