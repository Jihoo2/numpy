#점수 보정
import numpy as np
raw = np.array([95, 120, -10, 80, 105, 60])

# 1. 0~100 범위로 잘라내기 (0미만→0, 100초과→100)
fixed= np.clip(raw, 0, 100)
print(fixed)

'''
클립을 모른다면
fixed = raw.copy()

fixed[fixed < 0] = 0
fixed[fixed > 100] = 100

print(fixed)

# 2
print(np.mean(fixed))

# 3
print(np.sum(fixed != raw))
'''

# 2. 보정 후 평균

avg=np.mean(fixed)
print(avg)




# 3. (도전) 보정된 값이 원래와 다른 항목 수

x = fixed != raw
print(x)

print(np.sum(fixed != raw))



'''
코드	의미
np.clip()	값 범위 제한
np.mean()	평균
!=	서로 다른지 비교
np.sum(조건)	조건이 True인 개수
'''






