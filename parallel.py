import numpy as np
import time

from function import integral
from joblib import Parallel, delayed

if __name__ == '__main__':
    np.random.seed(42)

    matrix = np.random.randint(10, size=(1920, 1080))

    control = np.sum(np.sum(matrix, axis=0))

    n, m = matrix.shape

    start = time.time()

    for diag_sum in range(n + m - 1):

        Parallel(n_jobs=-2, require='sharedmem')(delayed(integral)(matrix, i, diag_sum - i)
                                                 for i in range(diag_sum + 1)
                                                 if i < n and diag_sum - i < m)

    print(time.time() - start)

    assert control == matrix[-1, -1]
