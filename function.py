import numpy as np


def integral(to_integrate: np.ndarray, i: int, j: int) -> None:
    if i > 0:
        to_integrate[i, j] += to_integrate[i - 1, j]
    if j > 0:
        to_integrate[i, j] += to_integrate[i, j - 1]
    if i > 0 and j > 0:
        to_integrate[i, j] -= to_integrate[i - 1, j - 1]
