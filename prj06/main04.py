import numpy as np
exam = np.array([95, 82, 60, 45, 88, 73, 100])

# 1. 60점 이상 "합격", 미만 "불합격"
exam>=60
test=np.where(exam>=60,"합격","불합격")
print(test)
# 2. 90점 이상이면 True, 아니면 False
result=exam>=90
print(result)
# 3. 합격자 수
pass_test=exam>=60
count=np.sum(pass_test)
print(count,"명")
# 4. (도전) 90↑ "A", 70~89 "B", 그 외 "C"
grade = np.where(exam >= 90, "A",
         np.where(exam >= 70, "B", "C"))

print(grade)