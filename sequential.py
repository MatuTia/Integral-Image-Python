import numpy as np
import time

from image_loader import image_loader
from function import integral

if __name__ == '__main__':

    path = './images/'

    start = time.time()

    list_matrix = image_loader(path)

    print(time.time() - start)

    result = [integral(list_matrix[i]) for i in range(len(list_matrix))]

    print(time.time() - start)

    control = [np.sum(np.sum(list_matrix[i], axis=0)) for i in range(len(list_matrix))]

    for i in range(len(result)):
        assert control[i] == result[i][-1, -1]
