from statistics import mean, median

import pandas as pd
from pandas.core.dtypes import astype

df = pd.read_csv('data/emp.csv')

# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.size)
# print(df.describe())


# 결측치확인 isna()
# print("##### 전처리전 #####")
# print(df.isna().sum())


# 결측치 삭제
# print(df.dropna())

# 결측치 채우기
# x=df["나이"].median()
# print("x:",x)
df["나이"] = df["나이"].fillna(df["나이"].median())

# 결측치 연봉 해당 행 없애기
df = df.dropna(subset=["연봉", "이름"])
# print(df)

# 결측치 도시 최빈값으로 채우기
# x=df["도시"].mode()
# print("x: ", x,sep="")
# print("x: ",type(x))
x = df["도시"].mode()[0]
# print("x:",x)
sr = df["도시"].fillna(x)
df["도시"] = sr

df["도시"] = df["도시"].fillna(x)

# df["도시"]=df["도시"].fillna(df["도시"].mode())


# 중복 제거
df.drop_duplicates(inplace=True)

# 칼럼 이름 변경
df.rename(columns={"도시": "지역"}, inplace=True)

# 칼럼 삭제
df.drop(columns=["이름"], inplace=True)
# 나이 칼럼의 타입 int 로 변경
df["나이"] = df["나이"].astype("int")
df["연봉"] = df["연봉"].astype("int")
# 값 치환
df["지역"] = df["지역"].replace("서울", "한양")


#칼럼 추가
df["월급"]=(df["연봉"]/12).astype(int)

#정렬 값기준
# df.sort_values("월급", ascending=False,inplace=True)
#정렬 인덱스 기준
# df=df.sort_index()


# 결측치 확인
# print("\n\n##### 전처리후 #####")
# print(df.isna().sum())
print(df.head())
