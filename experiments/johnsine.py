import matplotlib.pyplot as plt
import numpy as np

a = 80
b = 5
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * a * x / b)
temp = plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()
