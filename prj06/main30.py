import numpy as np

fruits = np.array(["사과", "바나나", "포도", "딸기", "수박"])

# 5개 과일 × 3개 지표 [월간 판매량(개), 당도(10점 만점), 보유 품종 수]
data = np.array([
    [5000, 9.2, 12],
    [4800, 8.8, 10],
    [5200, 9.0, 15],
    [3100, 7.9, 8],
    [4100, 8.5, 9]
])

# 1. 월간 판매량(1열)의 총합
print(np.sum(data[:,0]))
# 2. 당도(2열)가 가장 높은 과일의 이름
max_sweet=np.argmax(data[:,1])
print(fruits[max_sweet])
# 3. 보유 품종 수(3열)가 10개 이상인 과일들의 이름
print(fruits[data[:,2]>=10])
# 4. 월간 판매량이 4000개 이상인 과일의 수
sales= np.sum(data[:,0]>=4000)
print(sales)
# 5. 월간 판매량과 당도를 곱한 값이 가장 큰 과일의 이름
score = data[:,0] * data[:,1]

idx = np.argmax(score)

print(fruits[idx])

'''
코드	의미
data[:,0]	판매량 열
data[:,1]	당도 열
data[:,2]	품종 수 열
fruits[조건]	조건에 맞는 이름 가져오기
np.sum(조건)	조건 개수 세기
np.argmax(값)	가장 큰 값의 위
'''