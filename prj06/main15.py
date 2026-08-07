#설문 응답 집계
from enum import unique

import numpy as np

# 1=별로 2=보통 3=좋음
answers = np.array([1, 3, 2, 1, 1, 2, 3, 3, 3, 2])

# 1. 등장한 고유 응답값
x= np.unique(answers)

print(x)


# 2. 각 응답이 몇 번 나왔는지
print(np.sum(answers == 1))
print(np.sum(answers == 2))
print(np.sum(answers == 3))


# count=np.bincount(answers)
# print(count[1:])


# 3. 가장 많이 나온 응답
count=np.bincount(answers)
print(np.argmax(count))


# 4. (도전) 응답별 비율(%)

count=np.bincount(answers)[1:]
rate = count / len(answers) * 100
print(np.round(rate,1))

'''
코드	의미
np.unique()	중복 제거
np.bincount()	숫자별 개수
np.argmax()	가장 큰 값의 위치
len()	데이터 개수
개수 / 전체 * 100	비율
'''


