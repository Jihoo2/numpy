#전처리
import pandas as pd

df= pd.read_csv("data/people.csv")
#결측치 처리
# df=df.dropna() #결측치 삭제

df["나이"] = df["나이"].fillna(df["나이"].mean())
df["도시"] = df["도시"].fillna("ff")
df["연봉"] = df["연봉"].fillna(3000)

# print(df.info())
# 중복제거
print(df.duplicated())
df=df.drop_duplicates()

#결측치 확인
# print(df.isna().sum())

print(df.head(10))