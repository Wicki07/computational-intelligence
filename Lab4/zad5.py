import numpy as np
import pyswarms as ps
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_cost_history

S = [1, 2, 3, 6, 10, 17, 25, 29, 30, 41, 51, 60, 70, 79, 80]


def fitness_func(solution):
     sum1 = np.sum(solution * S)
     solution_invert = 1 - solution
     sum2 = np.sum(solution_invert * S)
     fitness = np.abs(sum1-sum2)
     #lub: fitness = 1.0 / (1.0 + numpy.abs(sum1-sum2))
     return fitness




def f(positions):
    n_particles = positions.shape[0]
    j = [fitness_func(positions[i]) for i in range(n_particles)]
    return np.array(j)


# Perform optimization
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9, 'k':2, 'p':1}
optimizer = ps.discrete.BinaryPSO(n_particles=10, dimensions=15,
options=options)
stats = optimizer.optimize(f, iters=30, verbose=True)
cost_history = optimizer.cost_history
posistions = stats[1]
s1 = []
s2 = []

print(stats)
for i in range(len(posistions)):
    if (posistions[i]):
        s1.append(S[i])
    else:
        s2.append(S[i])

print(s1)
print(s2)
plot_cost_history(cost_history)
plt.show()
