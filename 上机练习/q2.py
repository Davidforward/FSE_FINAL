# -*- coding: utf-8 -*-

#练习题2-长整数加法

#i为负数
def minusA(i):
    if abs(i)>Length_A:
        return 0
    else:
        return A[i]
    

def minusB(i):
    if abs(i)>Length_B:
        return 0
    else:
        return B[i]

A=input('A:')
B=input('B:')
Length_A=len(A)
Length_B=len(B)
Sum=''

Surplus=0
for i in range(1,max(Length_A,Length_B)+1):
    Tem=int(minusA(-i))+int(minusB(-i))
    if Tem>=10:
        Tem-=10
        Sum=str(Tem+Surplus)+Sum
        Surplus=1
    else:
        Sum=str(Tem+Surplus)+Sum
        Surplus=0

print('A+B='+Sum)
