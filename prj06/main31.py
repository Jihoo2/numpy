#오버워치 딜킬금
import numpy as np

heroes = np.array(["겐지", "트레이서", "리퍼", "솔저76", "한조"])

elim = np.array([28, 35, 22, 31, 26])  # 처치 수
death = np.array([8, 10, 6, 7, 9])  # 죽은 횟수
damage = np.array([12000, 15000, 18000, 16500, 14000])  # 가한 피해량

# 1. 팀의 평균 처치 수를 구하시오.
avg=np.mean(elim)
print(avg)

# 2. 가장 많은 처치를 한 영웅의 이름과 처치 수를 출력하시오.
high_hero= np.max(elim)
print(heroes[np.argmax(elim)], high_hero)
# 3. 평균 피해량보다 높은 피해를 준 영웅을 모두 출력하시오.
avg_damage = np.mean(damage)

print(heroes[damage > avg_damage])

# 4. 죽은 횟수가 8 이하인 영웅은 몇 명인지 구하시오.
print(np.sum(death <= 8))

# 5. 피해량이 높은 순서대로 영웅 이름을 출력하시오.
idx = np.argsort(damage)[::-1]
print(heroes[idx])
# 6. 가장 높은 피해량과 가장 낮은 피해량의 차이를 구하시오.
gap = np.max(damage) - np.min(damage)
print(gap)