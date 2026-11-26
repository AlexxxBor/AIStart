import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return x ** 4 - 10 * x + 3

x_values = [x for x in np.arange(-5, 5, 0.1)]
f_values = [f(x) for x in np.arange(-5, 5, 0.1)]

plt.figure(figsize=(10, 10))
plt.axvline(x=0, c='black')
plt.axhline(y=0, c='black')

plt.plot(x_values, f_values)