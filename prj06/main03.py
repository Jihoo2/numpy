import numpy as np

players = np.array(["A", "B", "C", "D", "E"])
score   = np.array([320, 150, 480, 275, 390])

# 1. 점수를 오름차순 정렬
result=np.sort(score)
# 2. 높은 점수 순으로 플레이어 이름 나열
idx= np.argsort(score)
# print(idx)
idx=np.argsort(score)[::-1]
print(players[idx])
# 3. 상위 3명
top3= players[idx][:3]
print(top3)
# 4. 1등과 꼴찌 이름
print(players[idx[0]])
print(players[idx[-1]])