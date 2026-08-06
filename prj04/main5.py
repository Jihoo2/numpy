import numpy as np


a=np.array([1,2,3])
b=np.array([4,5,6])

np.vstack([a,b])                  #vertical stack horizontal stack
result=np.hstack([a,b])
print(result)
