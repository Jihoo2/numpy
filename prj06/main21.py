import numpy as np

temps = np.array([12, 15, 18, 14, 20, 22, 17])  # 월~일 기온(℃)

# --------------------------------------------------
# [문제] 아래 조건에 맞는 코드를 작성해보세요.
# --------------------------------------------------

# 1. 일주일간의 평균 기온 구하기 (np.mean)
week_avg= np.mean(temps)
print(week_avg)


# 2. 가장 더운 날과 가장 추운 날의 기온을 튜플 형태로 한 번에 출력하기 (np.max, np.min)
print((np.max(temps)),(np.min(temps)))

# 3. 기온의 표준편차를 구하고 소수점 둘째 자리까지 출력하기 (np.std)
std = np.std(temps)
print(round(std,2))

# 4. 기온의 중앙값(Median) 구하기 (np.median)
md=np.mean(temps)
print(md)

# 5. (도전) 일주일 중 '평균 기온보다 더 따뜻했던 날'은 총 며칠이었는지 구하기 (np.sum 활용)
avg=np.mean(temps)
print(np.sum(avg<temps))
'''
코드	의미
np.mean()	평균
np.max()	최댓값
np.min()	최솟값
np.std()	표준편차
np.median()	중앙값
np.sum(조건)	조건을 만족하는 개수
np.round(값, 2)	소수점 둘째 자리까지 반올림
(값1, 값2)	튜플
'''