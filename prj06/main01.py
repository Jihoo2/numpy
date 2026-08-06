#일주일 기온 통계
import numpy as np
from numpy.ma.extras import median

temps = np.array([12, 15, 18, 14, 20, 22, 17])  # 월~일 기온(℃)

# 1. 평균 기온
# 2. 가장 더운 날과 추운 날의 기온
# 3. 기온의 표준편차
# 4. 중앙값
# 5. 평균보다 더운 날은 몇번 있었나?

result=np.mean(temps, axis=0)
a=np.max(temps)
b=np.min(temps)
c=np.std(temps)
d=np.median(temps)
count=len(temps[temps>result])


print(a,b,c,d)
print("평균보다 더운날",count,"일")