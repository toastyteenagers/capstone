import matplotlib.pyplot as plt
import numpy as np

array1 = []
with open('test_hrm.txt') as f:
    for line in f:
            array1.append(int(line))

x = np.arange(0, len(array1))
y = np.asarray(array1)

print(y)

plt.title("Raw Data")
plt.xlabel("Time (ticks)")
plt.ylabel("Transmittance (1)")
plt.plot(x, y, color="red")
plt.plot(0, 400, 20)
plt.show()

