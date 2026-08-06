
import numpy as np

missions = np.array([
    "화성탐사",
    "달탐사",
    "목성탐사",
    "금성탐사",
    "토성탐사"
])

# [속도, 연료효율, 탐사기간]
data = np.array([
    [90, 80, 300],
    [70, 95, 120],
    [150, 60, 500],
    [100, 75, 250],
    [130, 85, 450]
])

#문제

#1탐사선별 총 점수 구하기
#2총 점수가 가장 높은 탐사선 이름
#3속도가 평균 이상인 탐사선 찾기
#4탐사기간이 300일 이상인 탐사선 개수


















total=np.sum(data,axis=1)
print("탐사선별 총점수:",total)

idx = np.argmax(total)
print("총 점수가 가장높은 탐사선",missions[idx])

speed=data[:,0]
# print(speed)
avg=np.mean(speed)
a= avg <= speed
print("속도가 평균이상인 탐사선 찾기",missions[a])

period=data[:,2]
# print(period)
result= period>=300
print("탐사 기간이 300일 이상인 탐사선 갯수"np.sum(result))