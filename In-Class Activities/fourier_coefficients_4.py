import matplotlib.pyplot as plt
import numpy as np

fft = np.fft

y = np.loadtxt("Data Files\dow.txt", float)

c = fft.rfft(y)

maxval = max(c)
for i in range(len(c)):
    if abs(c[i]) < .005 * maxval:
        c[i] = 0

y2 = fft.irfft(c)

plt.figure(dpi = 250)

# raw data
plt.subplot(311)
plt.plot(y)
plt.xlabel("Time")
plt.ylabel("Signal")

# filtered dft
plt.subplot(312)
plt.semilogy(abs(c))
plt.xlabel("Fourier Coefficients (freq)")
plt.ylabel("Magnitude")

# cleaned up data via inverse dft
plt.subplot(313)
plt.plot(y2.real)
plt.xlabel("Time")
plt.ylabel("Signal")
plt.subplots_adjust(hspace=0.6)
plt.show()