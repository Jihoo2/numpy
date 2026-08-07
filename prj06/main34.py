import numpy as np

# 7량 열차, 각 칸의 이름
subway_room = np.array(["1칸", "2칸", "3칸", "4칸", "5칸", "6칸", "7칸"])
# 각 칸의 인원 (순서대로)
people = np.array([32, 72, 58, 54, 93, 42, 12])

# 1. 가장 붐비는 칸 순서대로 어느 칸인지를 나열하라
idx= np.argsort(people)[::-1]
print(subway_room[idx])
# 2. 환승에 유리한 칸이 정차역 순서대로 3, 5, 1 칸이라면, 각각 몇명으로 붐빌지 계산하라
transfer_people = people[[2, 4, 0]]
print(transfer_people)
# 3. 가장 붐비는 칸과 가장 여유로운 칸을 numpy array를 이용하여 계산하여라

max_room = subway_room[np.argmax(people)]
min_room = subway_room[np.argmin(people)]

print(max_room)
print(min_room)