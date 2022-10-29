import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import math
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_cost_history
import numpy as np

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

x_max = np.ones(6)
x_min = np.zeros(6)
print(x_min)
print(x_max)
bounds = (x_min, x_max)

optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=bounds)
optimizer.optimize(fx.sphere, iters=1000)


def endurance(props):
    return math.exp(-2 * (props[0] - math.sin(props[1])) ** 2) + math.sin(props[2] * props[3]) + math.cos(props[4] * props[5])


def f(x):
    n_particles = x.shape[0]
    j = [-endurance(x[i]) for i in range(n_particles)]
    return np.array(j)


# Perform optimization
stats = optimizer.optimize(f, 100)
cost_history = optimizer.cost_history

# Plot!
plot_cost_history(cost_history)
plt.show()
