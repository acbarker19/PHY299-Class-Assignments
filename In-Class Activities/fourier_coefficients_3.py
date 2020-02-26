from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

sample_rate, wav = wavfile.read("Data Files\WilhelmScream.wav")

s1 = wav[:, 0] # left channel
s2 = wav[:, 1] # right channel

s1_fft = np.fft.rfft(s1)
s2_fft = np.fft.rfft(s2)

plt.figure(dpi = 250)

plt.subplot(221)
plt.plot(wav[:, 0], "g-")
plt.ylabel("Left Channel")

plt.subplot(223)
plt.plot(wav[:, 1], "r-")
plt.ylabel("Right Channel")
plt.xlabel("Sound")

plt.subplot(222)
plt.plot(abs(s1_fft), "g-")

plt.subplot(224)
plt.plot(abs(s2_fft), "r-")
plt.xlabel("FFT")

plt.show()