#불리언 인덱싱
import pandas as pd

df= pd.read_csv("data/people.csv")


# print(df[ (df["나이"] >= 40) & (df["연봉"] >= 5000) ])

# print(df[(df["도시"] == "서울") | (df["도시"]=="부산")])

# print(df[df["도시"].isin(["서울","부산"])])

# mask01=df["나이"] >= 30
# mask02=df["나이"] <40
#
# mask= mask01 & mask02
#
# print(df[mask])



# print(df[(df["나이"] >= 30)  &  (df["나이"] <40)])



mask =df["나이"].between(30, 39)
print(df[mask])


