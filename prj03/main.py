import numpy as np

# bool 인덱싱
#
# scores = np.array([100,50,70,30])
# print(scores)
#
# # for s in scores:
# #     if s> 60:
# #         print(s)
# # x=scores<60
# # scores[x] = 0
# # print(scores)
#
# #
# # scores[scores>60] = 0
# # print(scores)
#
#
# x=(scores>=50) & (scores<80)              #넘파이에서는 and 가 아니라 &로 사용한다
# print(scores[x])                              #&사용시 곱하기 처럼 우선순위가 더세서 괄호를 씌워줘야한다



scores = np.array([100,50,70,30])

x = scores