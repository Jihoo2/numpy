#인덱싱
import numpy as np

matrix=np.linspace(1,12,24).reshape(3.4).astype(int)
print(matrix.shape)
print(matrix.size)
print(matrix.ndim)
print(matrix.dtype)
print(matrix)
print(matrix[1:-1])
print(matrix[1:3,1:3])