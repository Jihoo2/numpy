import pandas as pd

from main13 import result

# 직원 데이터
emp = pd.DataFrame({
    "이름": ["가영", "나은", "다희", "라온", "마루", "바다", "사랑"],
    "부서코드": ["D01", "D02", "D01", "D03", "D02", "D05", "D01"]
})

# 부서 데이터
dept = pd.DataFrame({
    "부서코드": ["D01", "D02", "D03", "D04"],
    "부서명": ["개발팀", "영업팀", "인사팀", "총무팀"]
})



result = pd.merge(emp,dept, on="부서코드",how="right") #온을 붙여야 매칭이댐 left right 적는거에따라 매칭안되는것들 버리는것을 살려준다
print(result)                                               # a + b left 시 a쪽사라진걸 살림 right b  outer 모두살림