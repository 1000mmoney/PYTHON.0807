# import matplotlib.pyplot as plt
# import numpy as np
#
# np.random.seed(0)
#
# n = 50
# x = np.random.rand(n)
# y = np.random.rand(n)
# area = (30 * np.random.rand(n))**2
# colors = np.random.rand(n)
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
# plt.colorbar()
# plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [random.uniform(0,100) for _ in range(1000)]
y = [random.uniform(0,100) for _ in range(1000)]

plt.clf()
plt.scatter(x, y, label="Random Data Points", color='green', marker='*', s=30, alpha=0.5)
plt.title('Scatter Plot Example')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.savefig("./scatter.png")
plt.show()
