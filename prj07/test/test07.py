#bool 타입 언덱싱
import numpy as np

from test.test02 import result

m= np.linspace(1,5,).astype(int)
# mask= [False, True, True, False,False]
mask = m > 3
print(m.shape)
print(m.ndim)
print(m.dtype)
# print(m[mask])
print(mask)