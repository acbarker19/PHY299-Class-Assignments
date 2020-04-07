# HW 13-1
# Alec Barker

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

L = 100
d = 2

N = 10000

def analyze(method, var, loc=0, scale=1):
    """
    loc and scale have different meanings based on the method.
    In general, 'loc' shifts the center of the distribution,
    while 'scale' shifts the spread.
    """
    
    values = method.rvs(size=N, loc = loc, scale = scale)
    
    if var == "x":
        for i in values:
            i *= d
    elif var == "theta":
        for i in values:
            i *= 2 * np.pi
    
    return values

def count_lines_crossed(xvals, thetavals):
    crossedvals = []
    
    for i in range(N):
        x = xvals[i]
        theta = thetavals[i]
        
        # length from needle midpoint to its edge (horizontal length only)
        half_length = L/2 * np.sin(theta)
        
        left_side_crossed = int((half_length + x) / d)
        right_side_crossed = int((half_length + d - x) / d)
        
        crossedvals.append(left_side_crossed + right_side_crossed)
    
    return crossedvals

plt.figure(dpi=200)

plt.subplot(211)

xvals = analyze(stats.uniform, "x")
thetavals = analyze(stats.uniform, "theta")
crossedvals = count_lines_crossed(xvals, thetavals)

uniform_count = np.zeros(max(crossedvals) + 1) 
for i in crossedvals:
    uniform_count[i] += 1
average = round(sum(uniform_count)/len(uniform_count), 2)
    
plt.axhline(average, label="Average = {}".format(average))
plt.hist(crossedvals, bins=max(crossedvals) + 1, alpha=0.2)
plt.legend(loc="best")
plt.ylabel("Number of Occurances")
plt.title("Uniform Distribution", size="x-large")

plt.subplot(212)
xvals = analyze(stats.uniform, "x")
thetavals = analyze(stats.norm, "theta", scale=0.3)
crossedvals = count_lines_crossed(xvals, thetavals)
width = max(crossedvals) + abs(min(crossedvals))
plt.hist(crossedvals, bins=width + 1, alpha=0.2)
plt.xlabel("Number of Lines Crossed")
plt.ylabel("Number of Occurances")
plt.title("Normal Distribution", size="x-large")

plt.tight_layout()
plt.show()