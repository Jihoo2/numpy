#인덱싱,연산
import numpy as np
#데이터 준비
a1= np.array([10,20,30,40,50])
a2= np.array(
    [[1,2,3],
    [4,5,6],
    [7,8,9]
 ])

#데이터 확인
# print(a[2,0]) #a[x][y],a[x,y] 둘다가능
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.size)
# print(a.dtype)
#
# #1차원 슬라이싱
# print(a1[1:4]) #[20 30 40]1이상 4미만
# print(a1[:3]) #[10 20 30]처음 3미만
# print(a1[3:]) #[40 50]3이상 ~끝가지
# print(a1[::2])#처음~끝까지2칸씩 건너뜀

#2차원 슬라이싱
# print(a2[1,0])
# print(a2[1,1])
# print(a2[2,0])
# print(a2[2,1])
# print(a2[1:3,0:2])
print(a2[: , 1:2])
print(a2[2:,:])