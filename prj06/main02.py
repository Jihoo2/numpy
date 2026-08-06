import numpy as np


stores = np.array(["강남", "홍대", "잠실"])
# 4일 × 3지점 매출(만원)
sales = np.array([[120, 90, 100],
                  [130, 95, 110],
                  [100, 80,  90],
                  [140, 100, 120]])


#1. 지점별 총매출 (열별 합계)
a = np.sum(sales,axis=0)
print(a)

#2. 일별 총매출 (행별 합계)
b=np.sum(sales,axis=1)
print(b)
#3. 전체 평균매출
c=np.mean(sales)
print(c)
#4. 매출이 가장 높은 지점이름
total=np.sum(sales,axis=0)
idx=np.argmax(total)
print(stores[idx])
