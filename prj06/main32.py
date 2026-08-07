import numpy as np

# 1분 동안 측정한 세트별 줄넘기 횟수 (회)
rope_jumps = np.array([120, 450, 110, 130, 850, 140, 125, 95])

# 1. 평균 줄넘기 횟수와 중앙값
avg_rope = np.mean(rope_jumps)
median=np.median(rope_jumps)
print(avg_rope, median)
# 2. 가장 많이 뛴 횟수(최댓값)와 가장 적게 뛴 횟수(최솟값)
r_max=np.max(rope_jumps)
r_min=np.min(rope_jumps)
print(r_max, r_min)
# 3. 줄넘기 횟수의 표준편차
print(np.std(rope_jumps))
# 4. 목표 기준치인 200회를 초과한 세트 수
print(np.sum(rope_jumps>200))