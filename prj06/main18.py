#이동평균
import numpy as np

sales = np.array([10, 20, 30, 40, 50, 60])

# 1. 전체 평균
avg=np.mean(sales)
print(avg)

# 2. (도전) 3일 이동평균 (연속 3개씩 평균)


result=[]
for i in range(len(sales)-2):
    result.append(np.mean(sales[i:i+3]))
print(result)


#    → 결과 길이는 4

'''
np.mean()	평균 계산
배열[i:i+3]	연속 3개 선택
len(배열)	배열 개수
range(len(data)-2)	이동 가능한 횟수
append()	리스트에 값 추가

핵심 공식:

이동평균 = 연속된 N개의 합 / N

예:

3일 이동평균 = (오늘 + 어제 + 그 전날) / 3



sales[i:i+3]	i번째부터 3개 선택
range(len(data)-2)	이동평균 가능한 횟수
np.mean()	선택한 값들의 평균
이동평균 개수	전체개수 - 묶음크기 + 1
'''