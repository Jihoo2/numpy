from unittest import result

import pandas as pd


df=pd.read_csv("data/emp.csv")

#Q4-1. 연봉을 12로 나눈 월급 열 생성
# df["월급"] = df["급여"] / 12

#Q4-2. 급여를 내림차순으로 정렬해서 상위 3명의 이름·급여 보기
# df=df.sort_values("급여",ascending=False).head(3)

#Q4-3. 부서코드별 평균 연봉 → 네 데이터에서는 부서별 평균 급여

# result=df.groupby("부서")["급여"].mean()
# print(result)

#Q4-4. 부서별 인원 수와 평균 나이를 한 번에 구하기
# result=df.groupby("부서").agg(인원수=("이름","count"),평균나이=("나이","mean"))
# print(result)