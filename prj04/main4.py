import numpy as np
#데이터준비
m= np.arange(12)

#차원추가
m=m[np.newaxis,:]
np.newaxis
print(m)
print(m.shape)
print("-----")
m2=m[:,np.newaxis]
print(m2)
print(m2.shape)