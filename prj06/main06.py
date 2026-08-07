#6.행렬 연산
import numpy as np

A = np.array([[2, 1],
              [1, 3]])
B = np.array([[1, 0],
              [2, 1]])

# 1. 요소별 곱  A * B
result =A*B
print(result)

# 2. 행렬곱    A @ B
result1=A@B
print(result1)
# 3. A의 역행렬
A_inv = np.linalg.inv(A)
print(A_inv)
# 4. (도전) 연립방정식 풀기
#    2x + y = 5
#     x + 3y = 10

answer = np.linalg.solve(A, B)

print(answer)

'''
A * B                 # 요소별 곱
A @ B                 # 행렬곱
np.linalg.inv(A)      # 역행렬
np.linalg.solve(A, b) # 연립방정식 풀이

'''