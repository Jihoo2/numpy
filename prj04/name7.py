import numpy as np

a=np.arange(6)
m=np.array([
    [1,2,3],
    [4,5,6],
    [3,8,1]
])
#????
a=a.reshape(2,3)
# result =np.sum(m,axis=0)
result= np.min(m,axis=0)
print(a)
print(result)




