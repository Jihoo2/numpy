#문제 5 주사위 시뮬레이션

import numpy as np

rng = np.random.default_rng(seed=42)

# 1. 주사위(1~6)를 100번 굴린 배열 만들기
dice= rng.integers(1,7,size=100)
print(dice)


# 2. 각 눈(1~6)이 몇 번씩 나왔는지 세기
count= np.bincount(dice)
print(count[1:])
# 3. 나온 값들의 평균
avg=np.mean(dice)
print(avg)
# 4. (도전) 6이 나온 횟수
count6=np.sum(dice==6)
print(count6)

'''
rng.integers()	랜덤 정수 생성
np.bincount()	숫자별 개수 세기
np.mean()	평균
np.sum()	합계
조건식	True/False 만들기

'''