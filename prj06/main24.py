import numpy as np

from main01 import result

# 카페 5개 지점의 3개월(6,7,8월) 음료 판매량
branches = np.array(["강남점", "홍대점", "신촌점", "잠실점", "건대점"])
sales = np.array([[320, 350, 410],
                  [280, 260, 300],
                  [150, 200, 180],
                  [400, 420, 460],
                  [220, 210, 195]])

# 1. 지점별 3개월 총 판매량
total = np.sum(sales, axis=1)
print(total)

# 2. 판매량이 가장 많은 지점 이름
print(branches[np.argmax(total)])
# 3. 월별(6/7/8월) 평균 판매량
month_avg = np.mean(sales,axis=0)
print(month_avg)
# 4. 총 판매량이 900개 이상인 지점 이름
print(branches[total>=900])
# 5. 매달 판매량이 계속 증가한 지점 이름
sales[:,1]>sales[:,0]
sales[:,2]>sales[:,1]
result=(sales[:,1]>sales[:,0]) & (sales[:,2]>sales[:,1])
print(branches[result])
'''
코드	의미
np.sum(sales, axis=1)	각 행의 합
np.mean(sales, axis=0)	각 열의 평균
np.argmax(total)	최댓값의 위치
branches[조건]	조건에 맞는 지점 선택
sales[:,1] > sales[:,0]	7월 > 6월
(조건1) & (조건2)	두 조건 모두 만족
'''