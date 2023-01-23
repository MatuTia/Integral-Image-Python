import numpy as np
import time

from image_loader import parallel_image_loader
from function import integral
from joblib import Parallel, delayed
from asyncio import run

if __name__ == '__main__':

    path = './images/'

    start = time.time()

    list_matrix = run(parallel_image_loader(path))

    print(time.time() - start)

    result = Parallel(n_jobs=236)(delayed(integral)(matrix) for matrix in list_matrix)

    print(time.time() - start)

    control = [np.sum(np.sum(list_matrix[i], axis=0)) for i in range(len(list_matrix))]

    for i in range(len(result)):
        assert control[i] == result[i][-1, -1]
