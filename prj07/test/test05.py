import numpy as np

from test.test02 import result

#shape 변환

x=np.linspace(1,24,24)
x=x.astype(int)
x=x.reshape(2,3,4)
print(x)
print(x.shape)
print(x.ndim)
print(x.size)
print(x.dtype)
