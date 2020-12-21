from termcolor import cprint
import scipy.io
import numpy as np
import sys


def data_loader(n_spatial: int, n_temporal: int) -> np.ndarray:
    """
    Tries to load the exact solution of the specified granularity

    :param n_spatial: number of spatial discretisation points
    :param n_temporal: number of temporal discretisation points
    :return: The exact solution as a numpy array
    """
    try:
        data = scipy.io.loadmat(
            f'burgers_exact/solutions/burgers_exact_K={n_temporal-1}_H={n_spatial-1}.mat')
        return np.real(data['x']), np.real(data['t']), np.real(data['u'])
    except FileNotFoundError as e:
        cprint(e, "red")
        cprint("Please make sure that the exact solution for the desired granularity exists. Check out "
               "burgers_exact/README.md", "red")
        sys.exit(0)
