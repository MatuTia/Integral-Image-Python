import numpy as np
import time

from function import integral
from joblib import Parallel, delayed

if __name__ == '__main__':
    np.random.seed(42)

    list_matrix = [np.random.randint(10, size=(1920, 1080)) for _ in range(10)]

    control = [np.sum(np.sum(list_matrix[i], axis=0)) for i in range(len(list_matrix))]

    start = time.time()

    Parallel(n_jobs=-2, require='sharedmem')(delayed(integral)(matrix) for matrix in list_matrix)

    print(time.time() - start)

    for i in range(len(list_matrix)):
        assert control[i] == list_matrix[i][-1, -1]
