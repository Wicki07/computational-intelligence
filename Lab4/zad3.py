import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
import math


def endurance(x, y, z, u, v, w):
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

x_max = 10 * np.ones(2)
x_min = -1 * x_max
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

# Set-up hyperparameters

# Call instance of GlobalBestPSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6,
                                    options=options, bounds=bounds)

# Perform optimization
stats = optimizer.optimize(endurance, 100,)
print(stats)
cost_history = optimizer.cost_history

# Plot!
plot_cost_history(cost_history)
plt.show()
