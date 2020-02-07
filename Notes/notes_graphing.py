import matplotlib.pyplot as plt
import numpy as np
import math

print("Graphing Data")

print("\r\nSimple Scatter Plot")
xvals = list(range(10))
yvals = list(range(10))

fig = plt.figure(dpi = 300)   # dpi = 300 so the resolution is increased
plt.scatter(xvals, yvals)
plt.show()

print("\r\nChanging Look")
fig = plt.figure(dpi = 300)
plt.scatter(xvals, yvals, s = [10 * x for x in xvals], c = "b", edgecolors = "k")
plt.show()

print("\r\nAdding Labels")
fig = plt.figure(dpi = 300)
plt.scatter(xvals, yvals)
plt.xlabel("Doritos available")
plt.ylabel("Doritos eaten")
plt.show()

print("\r\nLabel Settings")
fig = plt.figure(dpi = 300)
plt.scatter(xvals, yvals)
# fontsize can be xx-small, x-small, small, medium, large, x-large, xx-large
# fontsize can also be a number value
plt.xlabel("Doritos available", fontname = "serif", fontsize = "large")
plt.ylabel("Doritos eaten", fontname = "Times New Roman", fontsize = 30)
plt.show()

print("\r\nTick Mark Settings")
fig = plt.figure(dpi = 300)
plt.scatter(xvals, yvals)
plt.xlabel("Doritos available")
plt.ylabel("Doritos eaten")
# set a custom window size
plt.xlim(left = -0.5)
plt.ylim(-0.5, 10.5)
# change the tick mark font
plt.xticks(fontname = "times new roman")
# change the values of the tick marks to text, rotate text 45 degrees,
# and align test to the top of the tick mark
plt.yticks([2, 4, 6, 8, 10],
           ["not enough", "still not enough", "just right", "too many", "I'm sick"],
           rotation = 45, va = "top")
plt.show()

print("\r\nTitles and Legends")
fig = plt.figure(dpi = 300)
# add label to scatter plot
plt.scatter(xvals, yvals, label = "data label")
plt.xlabel("Doritos available")
plt.ylabel("Doritos eaten")
# adds title of the graph
plt.title("Graph of tastiness", size = "x-large")
# adds a legend in the best position to not overlap data
plt.legend(loc = "best")
plt.show()



"""
Types of Graphs:

scatter(xvals, yvals) = scatter plot
plot(xvals, yvals) = line plot
hist(list of data) = histogram with automatic bins
boxplot(list of lists of data) = box-and-whisker plot
pie(list of relative sizes) = a pie chart
"""



print("\r\nUsing Numpy to get Large Amounts of Data")
# creates a list of 1000 values between 0 and 6
xvals = np.linspace(0, 6, 1000)
# np.sin() can take an array and return the sin() of each
# math.sin() returns an error if the same thing is tried
yvals = np.sin(xvals)
fig = plt.figure(dpi = 300)
plt.plot(xvals, yvals)
plt.xlabel("x", size = "x-large")
plt.ylabel("sin(x)", size = "x-large")
plt.show()

print("\r\nLine Settings")
fig = plt.figure(dpi = 300)
plt.plot(xvals, yvals, color = "green", linestyle = "dashed")
plt.xlabel("x", size = "x-large")
plt.ylabel("sin(x)", size = "x-large")
plt.show()

print("\r\nLine Settings Shortcut")
fig = plt.figure(dpi = 300)
# can use shortcut to change line settings. g means green and -- means dashed
plt.plot(xvals, yvals, "g--")
plt.xlabel("x", size = "x-large")
plt.ylabel("sin(x)", size = "x-large")
plt.show()

print("\r\nHistograms and Multiple Data Sets on One Graph")
# loc is set mean and size is number of data points
# normal is a normal bell curve
data = np.random.normal(loc = 10, size = 10000)
fig = plt.figure(dpi = 300)
plt.hist(data, bins = 30, density = True, color = "r", alpha = 0.5)
plt.hist(data, bins = 30, density = True, cumulative = True, color = "b", alpha = 0.2)
plt.xlabel("x", size = "x-large")
plt.ylabel("relative count", size = "x-large")
plt.ylim(top = 1.1)
plt.show()

print("\r\nShowing Multiple Subplots")
data1 = np.random.normal(loc = 10, size = 10000)
data2 = np.random.normal(loc = 10, size = 10000)
fig = plt.figure(dpi = 300)
# 2 rows, 2 columns, first panel. If more than 9 for any value, add commas
ax1 = plt.subplot(221)
plt.scatter(data1, data2, c = "k", marker = "d", alpha = 0.01)
# 2 rows, 2 columns, fourth panel
ax1 = plt.subplot(224)
plt.scatter(data1, data2)
plt.hist2d(data1, data2)
plt.show()



print("\r\nExample Problem")
val = 1
series = [1]
for i in range(1, 20):
    val += ((-1)**i) * (1 / ((i * 2 + 1) * (3**i)))
    series.append(val)
series = [math.sqrt(12) * i for i in series]
print("pi -= {0:.4g}".format(series[-1]))

fig = plt.figure(dpi = 300)
plt.plot(list(range(20)), series, "g", marker = "s")
plt.xlabel("# terms")
plt.ylabel("pi", size = "x-large")
plt.show()