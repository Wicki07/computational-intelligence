import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
from pyswarms.backend.topology import Star
from pyswarms.backend.topology import Ring
from pyswarms.backend.topology import Pyramid

# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

# Call instance of GlobalBestPSO
optimizerStar = ps.single.GeneralOptimizerPSO(n_particles=10, dimensions=2,
                                    options=options, topology=Star())

statsStar = optimizerStar.optimize(fx.sphere, iters=100)
cost_historyStar = optimizerStar.cost_history

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9, 'k': 5, 'p': 1}
optimizerRing = ps.single.GeneralOptimizerPSO(n_particles=10, dimensions=2,
                                    options=options, topology=Ring())

statsRing = optimizerRing.optimize(fx.sphere, iters=100)
cost_historyRing = optimizerRing.cost_history

optimizerPyramid = ps.single.GeneralOptimizerPSO(n_particles=10, dimensions=2,
                                    options=options, topology=Pyramid())

statsPyramid = optimizerPyramid.optimize(fx.sphere, iters=100)
cost_historyPyramid = optimizerPyramid.cost_history

# Plot!
print(cost_historyStar)
print(cost_historyRing)
print(cost_historyPyramid)
plt.show()
plot_cost_history(cost_historyStar)
plt.show()
plot_cost_history(cost_historyRing)
plt.show()
plot_cost_history(cost_historyPyramid)
plt.show()
