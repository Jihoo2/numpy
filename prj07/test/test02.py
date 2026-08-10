# n차원 배열


import numpy as np

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

result = np.array([matrix, matrix,matrix,matrix])

print(result.shape)
print(result.ndim)
