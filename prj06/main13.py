#주가변동
import numpy as np


price = np.array([100, 105, 103, 110, 108, 115])

# 1. 전일 대비 변동액 (diff)
diff=np.diff(price)
print(diff)
# 2. 가장 많이 오른 날의 변동액
print(np.max(diff))


# 3. 오른 날의 수 (변동 > 0)
print(np.sum(diff>0))


# 4. (도전) 전일 대비 변동률(%) — 소수 첫째자리

rate = (diff/price[:-1])*100
print(np.round(rate,1))

#변동률 = 변동액 / 전날 가격 × 100    즉 (오늘가격-어제가격/어제가격)*100

'''
코드	의미
np.diff()	앞뒤 차이 계산
np.max()	최대값
np.sum(조건)	조건 개수
price[:-1]	마지막 값 제외
np.round(값, 자리수)	반올림

코드	의미	결과
price[-1]	마지막 값 하나	115
price[:-1]	처음부터 마지막 전까지	[100,105,103,110,108]
price[::-1]	전체 역순	[115,108,110,103,105,100]


'''