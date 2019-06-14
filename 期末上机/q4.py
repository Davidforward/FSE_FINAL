# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:16:35 2019

@author: Explorer
"""
#第四题，旅行商问题
N=int(input('N:'))
M=int(input('M:'))
Edge_in=input('请输入路线数据：').split()
A=[]
for i in range(M-1):
    A.append([int(Edge_in[i*3+0]),int(Edge_in[i*3+1]),int(Edge_in[i*3+2])])

Edge=A

'''
Edge=[[1,2,3],
[1,3,2],
[2,4,1],
[3,4,3]]
'''

Node=[]
for i in Edge:
    if i[0] in Node:
       pass;
    else:
        Node.append(i[0])
    if i[1] in Node:
       pass;
    else:
        Node.append(i[1])
sorted(Node)

location=Node[0]
target=Node[-1]
cost=0
routine=[]
for i in Edge:
    if i[0]==location and i[1]>location:
        location=i[1]
        cost+=i[2]
    if location==target:
        break
print(cost)
        
