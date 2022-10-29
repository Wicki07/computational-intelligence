import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters.plotters import plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Mesher
import matplotlib.pyplot as plt
from pyswarms.utils.plotters.formatters import Designer

# Run optimizer
options = {'c1':0.5, 'c2':0.3, 'w':0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
optimizer.optimize(fx.ackley, iters=50)
# tworzenie animacji
m = Mesher(func=fx.ackley)
# animation = plot_contour(pos_history=optimizer.pos_history,
#  mesher=m,
# mark=(0, 0))
d = Designer(limits=[(-1,1), (-1,1), (-0.1,1)], label=['x-axis', 'y-axis', 'z-axis'])
pos_history_3d = m.compute_history_3d(optimizer.pos_history)
animation3d = plot_surface(pos_history=pos_history_3d, # Use the cost_history we computed
                           mesher=m, designer=d,       # Customizations
                           mark=(0,0,0))

for i in range(len(optimizer.pos_history)):
    plt.pause(0.1)
plt.show()

# animation.save('plot0.gif', writer='imagemagick', fps=10)
