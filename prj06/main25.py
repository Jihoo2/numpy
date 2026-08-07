import numpy as np

branches = np.array(["강남점", "홍대점", "잠실점", "신촌점"])
menus = np.array(["아메리카노", "라떼", "콜드브루", "티", "에이드"])

# 4개 지점 x 5개 메뉴, 한 달 판매량
sales = np.array([
    [320, 210, 150, 80, 140],  # 강남점
    [280, 190, 260, 100, 175],  # 홍대점
    [410, 230, 180, 60, 120],  # 잠실점
    [150, 260, 200, 130, 300],  # 신촌점
])

# 1. 지점별 한 달 총 판매량.
total = np.sum(sales, axis=1)
print(np.sum(sales, axis=1))
# 2. 판매량 1위 지점 이름.
idx= np.argmax(total)
print(branches[idx])
# 3. 메뉴별 평균 판매량. (5개 메뉴 각각이 지점 평균 몇 잔씩 팔렸는지)
avg = np.mean(sales,axis=0)
print(avg)
# 4. 200잔 이상 팔린 메뉴만 골라내기. (지점 메뉴 포함)
rows,cols=np.where(sales>=200)

for r, c in zip(rows, cols):
    print(branches[r], menus[c], sales[r, c])

# 5. 각 지점에서 가장 많이 팔린 메뉴 이름. (지점 포함)
idx = np.argmax(sales, axis=1)

print(menus[idx])

for i in range(len(branches)):
    print(branches[i], menus[idx[i]])
'''
np.sum(sales, axis=1)	지점별 합계
np.mean(sales, axis=0)	메뉴별 평균
np.argmax(total)	전체에서 최댓값의 위치
np.argmax(sales, axis=1)	각 지점에서 최댓값의 위치
branches[idx]	인덱스로 지점 이름 선택
menus[idx]	인덱스로 메뉴 이름 선택
sales >= 200	200 이상인지 조건 확인
np.where(조건)	조건을 만족하는 위치 찾기
'''