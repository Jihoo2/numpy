
import numpy as np
a=[
    [1,2],
    [3,4],
]
b=[
    [5,6],
    [7,8],
]
a=np.array(a)
b=np.array(b)
x = np.array([100,50,80,30])

# #통계함수
# # result=np.sum(x)
# # result=np.max(x)
# # result=np.min(x)
# #result=np.mean(x)
# # result=np.median(x)
# result=np.std(x)#표준편차
#




#집계,axis

#정렬
# result=np.sort(x)
# result=np.argsort(x)
# result= np.argmax(x)
#where
# result=np.where(x>60,"합격", "불합격") #if문처럼

# random
# g=np.random.default_rng(42)
# result=g.random(3)
#result=g.integers(1,7,size=3)
# result=g.normal(140,220,size=10)

#행렬 곱
# result=a*b #*은 묶인것끼리 곱하고 @는 행렬곱하듯이한다


#역행렬
#result=np.linalg.inv(a)
#결과출력

np.save("data.npy",x)
result=np.load("data.npy")
print(result)