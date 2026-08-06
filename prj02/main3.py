import numpy as np

x=np.array([
    [1.1,2.2,3,4],
    [5,6,7,8.5],
], dtype=int)
print(x)
# y=np.array([
#     [1.1,2.2,3.4,5.6],
# ]
print("x.shape:",x.shape)
print("x.ndim:",x.ndim)
print("x.size:",x.size)  #요소들의 갯수
print("x.dtype:",x.dtype)

result= x.astype(int)
print(result)