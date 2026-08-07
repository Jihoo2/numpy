#백터연산
import numpy as np
a = np.array([3, 4])
b = np.array([1, 2])

# 1. a와 b의 내적 (dot)
print(np.dot(a,b))
# 2. a의 크기(길이, norm)
print(np.linalg.norm(a))
# 3. a와 b 사이의 유클리드 거리
print(np.linalg.norm(a-b))

# 4. (도전) a 방향의 단위벡터
unit=a/np.linalg.norm(a)
print(unit)


'''
코드	의미
np.dot(a,b)	두 벡터의 내적                             a₁b₁ + a₂b₂ + ...
np.linalg.norm(a)	벡터의 크기(길이)                  √(x²+y²+...)
a-b	두 벡터의 차이
np.linalg.norm(a-b)	두 벡터 사이 거리
a / np.linalg.norm(a)	단위벡터 변환                  벡터 / 벡터크기
np.linalg	선형대수 관련 기능

'''