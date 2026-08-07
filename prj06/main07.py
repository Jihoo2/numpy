#상품필터링
import numpy as np

from main01 import result

products = np.array(["사과", "바나나", "포도", "딸기", "수박"])
price = np.array([3000, 1500, 8000, 6000, 12000])
stock = np.array([50, 120, 20, 35, 8])

# 1. 5000원 이상인 상품 이름
print(products[price>=5000])
# 2. 재고 30개 미만인 상품 이름
print(products[stock<30])
# 3. 5000원 이상 상품들의 평균 가격
high=price[price>=5000]
avg=np.mean(high)
print(avg)
# 4. (도전) 5000원 이상 '그리고' 재고 30개 미만인 상품
print(products[(price>=5000) & (stock<30)])




'''
| : 또는(OR)
& : 그리고(AND)
~ : 반대(NOT)
'''