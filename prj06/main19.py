#결측치 처리
import numpy as np
data = np.array([10, np.nan, 30, np.nan, 50])

# 1. 결측치(NaN) 위치 찾기
print(np.isnan(data))
print(data[np.isnan(data)])
# 2. 결측치 개수
print(np.sum(np.isnan(data)))
# 3. NaN 무시하고 평균 (nanmean)
print(np.nanmean(data))
# 4. (도전) NaN을 0으로 채우기
data[np.isnan(data)] = 0
print(data)

'''
np.nan	결측치(값 없음)
np.isnan()	NaN 여부 확인
np.sum(조건)	조건 만족 개수
np.nanmean()	NaN 제외 평균
배열[조건] = 값	조건 위치 값 변경
np.mean()	평균 (NaN 있으면 NaN 반환)
np.isnan(data)	NaN 위치 찾기
'''