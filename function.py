import numpy as np


def integral(to_integrate: np.ndarray) -> None:
    n, m = to_integrate.shape

    for i in range(n):
        for j in range(m):
            if i > 0:
                to_integrate[i, j] += to_integrate[i - 1, j]
            if j > 0:
                to_integrate[i, j] += to_integrate[i, j - 1]
            if i > 0 and j > 0:
                to_integrate[i, j] -= to_integrate[i - 1, j - 1]
