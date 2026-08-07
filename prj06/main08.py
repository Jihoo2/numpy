#데이터 정규화
import numpy as np

data = np.array([10, 20, 30, 40, 50])

# 1. min-max 정규화 → 0~1 범위로
minmax= (data-np.max(data))/(np.max(data)-np.min(data))
print(minmax)

# 2. z-score 표준화 → 평균0, 표준편차1
z=(data-np.mean(data))/np.std(data)
print(z)
# 3. (도전) 아래 2D를 '열별'로 min-max 정규화
features = np.array([[1, 100],
                     [2, 200],
                     [3, 300]])


minmax = (features - np.min(features, axis=0)) / (np.max(features, axis=0) - np.min(features, axis=0))

print(minmax)

'''

종류	공식	목적
Min-Max 정규화	(x-최소)/(최대-최소)	0~1 범위로 변경
Z-score 표준화	(x-평균)/표준편차	평균 0, 표준편차 1


np.max(heat)             # 전체 최대값
np.argmax(heat)          # 최대값 위치(index)
np.unravel_index()       # 2차원 좌표로 변환

np.max(heat, axis=1)     # 행별 최대값
np.max(heat, axis=0)     # 열별 최대값

np.argmax(heat, axis=0)  # 열별 최대값의 행 번호
'''