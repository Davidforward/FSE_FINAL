# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:19:35 2019

@author: Explorer
"""
N=int(input('n:'))
a=input('请输入数据：').split()

#
A=[]
B=[]
C=[]
D=[]
for i in range(N*4):
    if (i%4)==0:
        A.append(int(a[i]))
    elif (i%4)==1:
        B.append(int(a[i]))
    elif (i%4)==2:
        C.append(int(a[i]))
    else:
        D.append(int(a[i]))


count=0;
for i in A:
    for j in B:
        for k in C:
            for r in D:
                if(i+j+k+r==0):
                    count+=1
print(count)
