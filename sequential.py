import numpy as np
import time

from function import integral

if __name__ == '__main__':
    np.random.seed(42)

    matrix = np.random.randint(10, size=(1920, 1080))

    control = np.sum(np.sum(matrix, axis=0))

    n, m = matrix.shape

    start = time.time()

    for i in range(n):
        for j in range(m):
            integral(matrix, i, j)

    print(time.time() - start)

    assert control == matrix[-1, -1]
