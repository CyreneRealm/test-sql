import numpy as np
import matplotlib.pyplot as plt

# tạo trục thời gian
t = np.linspace(0, 10, 100)

# tín hiệu gốc
signal = np.sin(t)

plt.plot(t, signal)
plt.title("Original Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

