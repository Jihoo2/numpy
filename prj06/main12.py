#통장 잔액 흐름
import numpy as np

# 입출금 내역 (양수=입금, 음수=출금)
trans = np.array([100, -30, 50, -80, 200, -60])

# 1. 거래별 누적 잔액 (시작 잔액 0)
total= np.cumsum(trans)
print(total)
# 2. 최종 잔액
print(np.sum(total))
# 3. 잔액이 가장 많았던 시점의 잔액
print(np.max(trans))
# 4. (도전) 잔액이 마이너스가 된 적이 있는가?
total< 0
print(np.any(total<0))



'''
np.sum()      # 전체 합
np.cumsum()   # 누적 합
np.max()      # 최댓값
np.any()      # 하나라도 True인지 확인
'''