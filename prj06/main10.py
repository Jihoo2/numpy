#직원 실적 분석

import numpy as np
names = np.array(["김철수", "이영희", "박민수", "최지우", "정해인"])
depts = np.array(["개발", "영업", "개발", "디자인", "영업"])
# 5명 × 3분기 실적
sales = np.array([[100, 120, 130],
                  [ 90,  95, 100],
                  [110, 105, 120],
                  [ 80,  85,  90],
                  [130, 140, 135]])

# 1. 직원별 연간 총실적
total= np.sum(sales, axis=1)
print(total)
# 2. 실적 1등 직원 이름
idx= np.argmax(total)
print(names[idx])

# 3. 분기별 평균 실적
avg=np.mean(total,axis=0)
print(avg)




# 4. 연간 총실적 300 이상인 우수 직원 이름
print(total>=300)
print(names[total>=300])

# 5. (도전) 매 분기 상승한(3분기>2분기>1분기) 직원 이름
#3분기>2분기
sales[:,2]>sales[:,1]

#2분기>1분기
sales[:,2]>sales[:,0]

result=((sales[:,2] > sales[:,1]) & (sales[:,2] > sales[:,0]))
print(names[result])

'''
np.sum(sales, axis=1)     # 직원별 합계
np.argmax(total)          # 최대 위치
np.mean(sales, axis=0)    # 분기별 평균
names[조건]               # 조건에 맞는 이름 추출
(s조건) & (조건)          # AND 조건
'''
