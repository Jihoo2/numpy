#온라인 주문데이터
import numpy as np


#  열 = [주문ID, 금액, 수량]
orders = np.array([
    [1, 25000, 2],
    [2, 13000, 1],
    [3, 48000, 3],
    [4,  9000, 1],
    [5, 30000, 1],
])

# 1. 전체 매출(금액 합)
total= np.sum(orders[:,1])
print(total)
# 2. 평균 주문 금액
print(np.mean(orders[:,1]))
# 3. 3만원 이상 주문의 주문ID
print(orders[orders[:,1] >= 30000, 0])
# 4. 가장 비싼 주문의 ID
idx = np.argmax(orders[:,1])
print(orders[idx,0])
# 5. (도전) 단가(금액/수량)가 가장 높은 주문의 ID

unit = orders[:,1] / orders[:,2]
idx = np.argmax(unit)
print(orders[idx,0])
'''
배열[:,열번호]	특정 열 전체 선택
orders[:,1]	금액 열 선택
orders[:,2]	수량 열 선택
배열[조건, 열번호]	조건에 맞는 행의 특정 열 선택
np.sum()	합계
np.mean()	평균
np.argmax()	최댓값 위치
금액 / 수량	단가 계산
'''