import pandas as pd
import numpy as np

# #파이썬 순수 리스트
# x = [10,20,30]
#
# #numpy 리스트
# y = np.array(x)
#
# z = pd.Series(x)


# a=pd.Series([10,20,30],index=["math","kor","eng"])
# print(a)
# b=pd.Series([40,50,60],index=["kor","math","abc"])
# print(a["math"])
# print(b.iloc[0])
# print(a+b)
# sr01 = pd.Series(["가영", "나영", "다영"], index=["첫번째학생","두번째학생","세번째학생"])
# sr02 = pd.Series([100, 90, 80],index=["첫번째학생","두번째학생","세번째학생"])
#
# sr03 = pd.Series([ "홍길동","김철수"],index=["네번째학생","다섯번째학생"])
# sr04 = pd.Series([ 50,60 ],index=["네번째학생","열번째학생"])
#
# sr_names = pd.concat([sr01,sr03])
# sr_scores = pd.concat([sr02,sr04])
#
# df = pd.DataFrame({
#     "이름":sr_names,
#     "성적":sr_scores,
# })
#
# print(df.loc["첫번째학생"])

df = pd.read_csv("data/people.csv")
# print(df.info())
# print(df.describe())
# print(df.isna().sum())
# print(df.sample(5))

# sr = df["나이"]
# print(sr.max())
# print(sr.min())
# print(sr.mean())
# x =df["나이"].value_counts()
# print(x.max())
# print(type(x))

# pd.to.csv("data/people.csv",index=False)
# df.to_csv("data/result.csv",index=False,encoding="utf-8-sig")
# print(df[["이름","연봉"]])
# print(df.loc[0:3,"이름"])
# print(df.iloc[0:3,0:3])




df=df.drop_duplicates()    #중복제거
df=df.rename(columns={"나이":"레벨"})
#결측치 확인
# print(df.isna())
# print(df.duplicated())
df.dropna(inplace=True)
print(df.head())