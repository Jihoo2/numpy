import numpy as np

books = np.array(["파이썬 입문", "데이터 분석", "머신러닝", "알고리즘", "웹개발"])
rental = np.array([12, 25, 8, 30, 15])  # 누적 대출 횟수
stock = np.array([3, 0, 5, 1, 7])  # 현재 재고

# 1. 대출 횟수를 내림차순 정렬
print(np.sort(rental)[::-1])

# 2. 대출 많은 순으로 책 제목 나열
idx=np.argsort(rental)[::-1]
print(books[idx])

# 3. 재고가 0권인 책 이름
print(books[stock == 0])
# 4. 대출 횟수 상위 3권의 평균 대출 횟수
top3 = np.sort(rental)[::-1][:3]
print(top3)

# 5. 재고 5권 미만이면서 대출 횟수 20회 이상인 '인기 소진' 책 이름
print(books[(stock < 5) & (rental >= 20)])
'''
코드	의미
np.sort()	오름차순 정렬
[::-1]	역순
np.argsort()	정렬된 순서의 인덱스
배열[인덱스]	인덱스 순서대로 재배열
[:3]	앞에서 3개 선택
배열[조건]	조건에 맞는 값 선택
(조건1) & (조건2)	두 조건을 모두 만족
'''