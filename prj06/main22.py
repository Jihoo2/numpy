import numpy as np

my_loc = np.array([0, 0])
target = np.array([3, 4])
cafes = np.array([
    [1, 1],
    [5, 5],
    [-1, 2]
])

# 1. 내 위치와 목적지 사이의 유클리드 거리 (norm 함수 사용)
loc=np.linalg.norm(target-my_loc)
print(loc)
# 2. 유클리드 거리 공식을 직접 작성하여 구하기 (np.sqrt 등 사용)
distance=np.sqrt(np.sum((target-my_loc)**2))
print(distance)
# 3. 내 위치에서 각 카페들까지의 모든 거리 구하기
distance=np.linalg.norm(cafes-my_loc,axis=1)
print(distance)
# 4. 가장 가까운 카페의 인덱스 번호 찾기
idx=np.argmin(distance)
print(idx)
'''
target - my_loc	두 좌표의 차이
np.linalg.norm()	벡터의 크기/거리
np.sqrt()	제곱근
** 2	제곱
axis=1	각 행별로 계산
np.argmin()	가장 작은 값의 위치

'''