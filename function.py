import numpy as np


def integral(to_integrate: np.ndarray) -> np.ndarray:
    n, m = to_integrate.shape
    integrated = np.copy(to_integrate)

    for i in range(n):
        for j in range(m):
            if i > 0:
                integrated[i, j] += integrated[i - 1, j]
            if j > 0:
                integrated[i, j] += integrated[i, j - 1]
            if i > 0 and j > 0:
                integrated[i, j] -= integrated[i - 1, j - 1]

    return integrated
