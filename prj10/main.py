from os import dup
from statistics import mean
from unittest import result

import pandas as pd

df=pd.read_csv('data/emp.csv')

# print(df.shape)
# print(df.describe())
# print(df.info())
# print(df.size)
# print(df.isna().sum())
# print(df.duplicated().sum())

# 전 직원 평균 급여
# result=df["급여"].mean()
# # 부서별 평균 급여
# result = df.groupby("부서")["급여"].mean()
#
# #부서별 인원수
# result= df.groupby("부서").size()

#부서별 여러 통계 한번에// 급여에 대한 최대,최소, 평균
# result=df.groupby("부서")["급여"].agg(["max","min","mean"])

#칼럼으로 묶기 (부서+직급)
# result=df.groupby(["부서","직급"])["급여"].max()

# 칼럼마다 다른 집계//급여 평균,나이 최대, 평가점수 최소
# result = df.agg({"급여":"mean","나이":"max","평가점수":"min"})
result =df.groupby("부서").agg({"급여":"mean","나이":"max","평가점수":"min"})
# 결과 확인

# def f01(x):
    # if pd.isna(x): return None

#     if x >= 90 :
#         return "A"
#     elif x >= 80:
#         return "B"
#     elif x >= 70:
#         return "C"
#     else:
#         return "D"
# #map

# result = df["평가등급"] = df["평가점수"].map(f01) #기존의 평가점수를 기반으로 만들어준 등급
#맵은 시리즈만 대상
# df["평가점수등급"] = df["평가점수"].apply(f01)
def calc_score(r):
    return  ["근속연수"] * r["평가점수"]


# sr = df.apply (calc_score, axis=1)
#어플라이는 시리즈 df다가능
df["종합점수"]=df.apply (lambda r : r["근속연수"] * r["평가점수"], axis=1)
print(df)