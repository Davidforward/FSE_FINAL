# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:00:05 2019

@author: Explorer
"""
#第5题：二次函数问题
n=2
k=9
a=[[1,0,0],[1,2,0]]
b=[]
for i in a:
    b.append(round(-i[1]/(i[0]+i[0])))

Storage=[]
for j in range(len(a)):
        Storage.append(a[j][0]*(b[j])*a[j][0]*(b[j])+a[j][1]*(b[j])+a[j][2])


for i in range(1,k):
    for j in range(len(a)):
        Storage.append(a[j][0]*(b[j]+i)*a[j][0]*(b[j]+i)+a[j][1]*(b[j]+i)+a[j][2])
        Storage.append(a[j][0]*(b[j]-i)*a[j][0]*(b[j]-i)+a[j][1]*(b[j]-i)+a[j][2])

Storage.sort()
print(Storage[0:k])


