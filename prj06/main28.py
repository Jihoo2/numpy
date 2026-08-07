import numpy as np

member = np.array(["김감자", "이호박", "박키위", "최사과", "양양파"])
# 배열 왼쪽부터 "김감자", "이호박", "박키위", "최사과", "양양파" 1은 출석 0은 결석
attend_reco = np.array([
    [1, 1, 1, 1, 1],  # 월요일
    [0, 0, 1, 1, 1],  # 화요일
    [1, 0, 1, 0, 1],  # 수요일
    [0, 0, 1, 0, 1],  # 목요일
    [1, 0, 1, 1, 1],  # 금요일
    [1, 0, 1, 0, 0],  # 토요일
    [1, 1, 1, 1, 0]  # 일요일
])

# 1. 인물별 출석 횟수를 출력
count=np.sum(attend_reco,axis=0)
print(count)
# 2. 평일과 주말에 각각 출석률이 가장 낮은 사람(member)을 출력
weekday=attend_reco[:5]
weekend=attend_reco[5:]
day_rate=np.mean(weekday,axis=0)
weekend_rate=np.mean(weekend,axis=0)
print(member[np.argmin(day_rate)])
print(member[np.argmin(weekend_rate)])
# 3. 가장 많이 출석한 사람과 낮은 사람의 출석률(%)을 출력
rate=np.mean(attend_reco,axis=0)*100
max_idx=np.argmax(rate)
print(member[max_idx],rate[max_idx])
# 4. 평균 출석률보다 낮은 사람 목록하고 출석률이 가장 높은 사람 이름을 출력
avg_rate=np.mean(rate)
print(member[rate<avg_rate])
max_idx=np.argmax(rate)
print(member[max_idx])
'''
np.sum(attend_reco, axis=0)	사람별 출석 횟수
np.mean(attend_reco, axis=0)	사람별 출석률
attend_reco[:5]	월~금
attend_reco[5:]	토~일
np.argmin()	가장 작은 값의 위치
np.argmax()	가장 큰 값의 위치
member[조건]	조건에 맞는 사람 선택
'''