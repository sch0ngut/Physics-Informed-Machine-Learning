from burgers_numerical.FTCS import FTCS
from util.generate_plots import *

ftcs = FTCS(n_spatial=161, n_temporal=10**4+1)
ftcs.time_integrate()
print(ftcs.get_l2_error())
# generate_snapshots_plot(u=ftcs.u, t_vec=np.array([0, 0.35, 0.4, 0.85]), savefig_path='plots/FTCS_oscillations.jpg')
generate_snapshots_plot(u=ftcs.u, t_vec=np.array([0, 0.35, 0.4, 0.85]))
