import pandas as pd

df=pd.read_csv("data/orders.csv")
#Q4-5. orders 정제 → 매출 → 카테고리별 총 매출
# 1. 중복 제거
df = df.drop_duplicates()

# 2. 카테고리 통일
df["카테고리"] = df["카테고리"].replace("food", "식품")

# 3. 단가 결측치를 중앙값으로 채우기
df["단가"] = df["단가"].fillna(df["단가"].median())

# 4. 매출 계산
df["매출"] = df["수량"] * df["단가"]

# 5. 카테고리별 총 매출
result = df.groupby("카테고리")["매출"].sum()

print(result)