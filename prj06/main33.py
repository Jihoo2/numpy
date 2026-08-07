#유클리드 거리구하기
import numpy as np

my_loc = np.array([0, 0])
target = np.array([3, 4])
cafes = np.array([
    [1, 1],
    [5, 5],
    [-1, 2]
])

# 1. 내 위치와 목적지 사이의 유클리드 거리 (norm 함수 사용)
my_dis=np.linalg.norm(target-my_loc)
print(my_dis)
# 2. 유클리드 거리 공식을 직접 작성하여 구하기 (np.sqrt 등 사용)
distance= np.sqrt(np.sum((target-my_loc)**2))

# 3. 내 위치에서 각 카페들까지의 모든 거리 구하기
cafe_distance=np.linalg.norm(cafes-my_loc,axis=1)
print(cafe_distance)
# 4. 가장 가까운 카페의 인덱스 번호 찾기
near_cafe= np.argmin(cafe_distance)
print(near_cafe)

'''
np.linalg.norm(값)
거리(벡터의 크기) 계산

np.sqrt(값)
제곱근 계산

np.sum(값)
값의 합

np.argmin(값)
가장 작은 값의 위치(index)

axis=1
행 방향으로 계산
'''