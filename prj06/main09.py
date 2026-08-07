#히트맵 최댓값의 위치
import numpy as np

heat = np.array([[3, 8, 2],
                 [9, 1, 5],
                 [4, 7, 6]])

# 1. 전체 최댓값
print(np.max(heat))

# 2. 최댓값의 (행, 열) 위치
idx=np.argmax(heat)
row = idx//heat.shape[1]
col = idx%heat.shape[1]
print(row, col)
# 3. 각 행의 최댓값
print(np.max(heat,axis=1))

# 4. 각 열에서 최댓값이 있는 행 번호
print(np.argmax(heat, axis=0))
'''
axis=0 → 열 방향 계산 (행을 따라 내려감)
axis=1 → 행 방향 계산 (열을 따라 옆으로 감)
shape[0] → 행 개수
shape[1] → 열 개수
'''