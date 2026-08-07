import numpy as np

# 1. 0~11 정수 배열을 만들어 3×4 행렬로
arr = np.arange(12)
matrix = arr.reshape(3, 4)
print(matrix)
# 2. 그 행렬의 shape과 차원 수(ndim)
print(matrix.shape)
print(matrix.ndim)
# 3. 0부터 1까지 균등하게 5개 나누기
x = np.linspace(0,1,5)
print(x)
# 4. (도전) 위 3×4 행렬을 다시 1차원으로
one=matrix.reshape(-1)
print(one)


'''
np.arange()     # 일정한 정수 배열 생성
reshape()       # 배열 모양 변경
shape           # 크기 확인
ndim            # 차원 확인
np.linspace()   # 일정 간격 숫자 생성

'''