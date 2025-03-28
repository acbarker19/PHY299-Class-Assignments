import matplotlib.pyplot as plt
from scipy import optimize

file = open("Data Files/Hubble.txt", "rt")

name = []
distance = []
velocity = []

for line in file:
  if line.startswith("#"):
      pass
  else:
      n, d, v = line.split(",")
      name.append(n)
      distance.append(d)
      velocity.append(v)

popt, pcov = optimize.curve_fit(lambda x, m : m * x, distance, velocity, 0.002)
print(popt, pcov)

plt.figure(dpi=200)
plt.scatter(distance, velocity)
plt.xlabel("Distance (MPc)")
plt.ylabel("Velocity (km/s)")
plt.show()