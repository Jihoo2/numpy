#배열 생성 및 속성
import numpy as np

from test.test02 import result

# result=np.zeros(100,100)
# result=np.full((100,100),255)
# print(result)
# print(result.shape)
# print(result.ndim)


shape=(100,100)
v=123
result=np.zeros(shape)    #전부 0으로채움
result=np.ones(shape)     #전부 1로 채움
result=np.full(shape,v)    #전부 v로채움
result=np.eye(2)            #단위행렬(n*x)(대각선 요소들이 전부 1)
print(result)
print(result.shape)
print(result.ndim)