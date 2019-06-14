# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:37:47 2019

@author: Explorer
"""

N=int(input('输入n:'))
Edge_in=input('请输入数据：').split()    #输入节点连通，是否枯萎等数据
A=[]
for i in range(N-1):
    A.append([int(Edge_in[i*3+0]),int(Edge_in[i*3+1]),int(Edge_in[i*3+2])])

Edge=A
'''
N=5
Edge=[
      [1,2,2],
      [1,3,2],
      [1,4,2],
      [1,5,2],
     ]
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

drug=0;
drug_list=[];
for i in Edge[::-1]:
    if i[2]==2:
        drug+=1;
        drug_list.append(i[1])
        for j in range(len(Edge)):
            if (Edge[j]!=i and Edge[j][1]==i[1]):
                if Edge[j][1]==2:
                    Edge[j][1]==1
drug_list.sort()
print(drug,drug_list)
    