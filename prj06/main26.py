# 아이스크림 인기 평가

import numpy as np

icecream = np.array([
    [95, 90, 88],  # 민트초코
    [90, 85, 92],  # 바닐라
    [85, 80, 89],  # 딸기
    [88, 95, 84],  # 초당옥수수
    [70, 60, 75]  # 마라
])

menu = np.array([
    "민트초코",
    "바닐라",
    "딸기",
    "초당옥수수",
    "마라"
])

evaluation = np.array([
    "맛", "향", "식감",
])

# 문제 1: 각 아이스크림의 총점을 구하세요.(힌트 : axis=1, np.sum())
total=np.sum(icecream, axis=1)
print(total)
# 문제 2: 각 아이스크림의 평균 점수를 구하세요. (힌트 : axis=1, np.mean())
evg=np.mean(icecream, axis=1)
print(evg)
# 문제 3: 각 평가 항목(맛, 향, 식감)의 평균 점수를 구하세요. (힌트 : axis=0)
print(np.mean(icecream, axis=0))

# 문제 4: 평균 점수가 85점 이상인 아이스크림 이름만 출력하세요. (힌트 : 불리언 인덱싱)
print(menu[evg >= 85])
# 문제 5: 다음을 구하세요.
## 가장 높은 점수 (np.max)
print(np.max(icecream))
## 가장 낮은 점수 (np.min)
print(np.min(icecream))
## 전체 점수의 표준편차 (np.std)
print(np.std(icecream))
## 전체 점수의 중앙값 (np.median)
print(np.median(icecream))

# 보너스 문제 (조금 어려움)-평균 점수가 가장 높은 아이스크림이 무엇인지 출력하세요.
## 힌트) evg = np.mean(icecream, axis=1)
idx = np.argmax(evg)
print(menu[idx])

'''
axis=1  → 각 아이스크림별 계산
axis=0  → 각 평가항목별 계산
즉 행마다 계산 → axis=1, **열마다 계산 → axis=0**
'''
