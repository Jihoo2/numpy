import numpy as np

# 관람객 만족도 (1=불만족, 2=보통, 3=만족)
satisfaction = np.array([3, 2, 3, 1, 3, 2, 1, 3, 3, 2])

# 일자별 매출 (양수=매출 , 음수=지출)
daily_sales = np.array([500000, -120000, 300000, -50000, 800000, -200000])

# 스낵바 메뉴, 가격, 재고
snacks = np.array(["팝콘", "나초", "오징어", "콜라", "츄러스"])
snack_price = np.array([6000, 5000, 4500, 3000, 4000])
snack_stock = np.array([40, 15, 25, 100, 8])

# 직원별 이번달 점수
staffs = np.array(["김사원", "이과장", "박대리", "최주임", "정사원"])
incentive = np.array([85, 92, 78, 95, 88])

# 1. 만족도 평균은 몇점인가요? :
avg = np.mean(satisfaction)
print(avg)
# 2. 총 매출 금액은 얼마인가요? :
total = np.sum(daily_sales)
print(total)
# 3. 총 재고 가치는 얼마인가요? :
stock_value = np.sum(snack_price * snack_stock)
print(stock_value)

#   - 최고가 메뉴 :
max_idx = np.argmax(snack_price)
print(snacks[max_idx])
#   - 최저 수량 재고메뉴 :
min_idx = np.argmin(snack_stock)
print(snacks[min_idx])
# 4. 직원들 점수 평균 점수는 몇점인가요? :
avg_incentive = np.mean(incentive)
print(avg_incentive)
#   - 가장 높은 점수의 직원은 누구인가요? :
max_idx=np.argmax(incentive)
print(staffs[max_idx])