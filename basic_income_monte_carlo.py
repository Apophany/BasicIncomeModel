import matplotlib.pyplot as plt
import numpy as np
from basic_income_model import *

TRIALS = 1024*12
bi = np.zeros(shape=(TRIALS,), dtype=float)

for k in range(TRIALS):
    bi[k] = basic_income_cost_benefit()

plt.subplot(211)
width = 4e12
height = 50 * TRIALS / 1024

plt.title("Basic Income")
plt.hist(bi, bins=50)
plt.axis([0, width, 0, height])

plt.show()
