import numpy as np

category = ["한식", "양식", "중식", "일식"]
meal = ["점심", "저녁", "야식"]
food = [
    ["김치찌개", "제육볶음", "육개장"],
    ["피자", "햄버거", "파스타"],
    ["짜장면", "마라탕", "깐쇼새우"],
    ["초밥", "텐동", "라멘"]
]
price = [
    [6000, 8000, 10000],
    [12000, 5000, 9000],
    [7000, 8000, 13000],
    [10500, 11000, 8000]
]

# 모든 음식의 평균 가격
print(np.mean(price))
# 점심,저녁, 야식 별 총 가격(열)
print(np.sum(price, axis=0))
# 카테고리 별 평균 가격(행)
print(np.mean(price, axis=1))
# 가장 비싼 음식, 가장 저렴한 음식
max_idx = np.argmax(price)
min_idx = np.argmin(price)

row_max = max_idx // len(price[0])
col_max = max_idx % len(price[0])

row_min = min_idx // len(price[0])
col_min = min_idx % len(price[0])

print(food[row_max][col_max])
print(food[row_min][col_min])

# 카테고리 별 음식 오름차순으로 정렬해서 출력

for i in range(len(category)):
    idx = np.argsort(price[i])

    print(category[i])
    print(np.array(food[i])[idx])
'''
np.mean(price)	리스트 전체 평균도 가능
np.sum(price, axis=0)	열 기준 계산
np.mean(price, axis=1)	행 기준 계산
np.argmax(price)	가장 큰 값 위치
np.argmin(price)	가장 작은 값 위치
len(price[0])	리스트의 열 개수
np.argsort()	정렬 순서(index) 반환
np.array(food[i])[idx]	해당 순서대로 음식 재배열
'''