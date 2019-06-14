# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:01:38 2019

@author: Explorer
"""

#上机考试题1

ch=input('ch:')
Str=[]
Str=input('请输入字符串：')
Str=Str.split()
Str2=[]


#删除
for i in Str:
    if i!='@':
        Length=len(i)
        for j in range(Length):
            if j<len(i) and i[j]==ch:
                i=i[:j]+i[j+1:]
        Str2.append(i)

Str2.sort()
print(Str2[::-1])

        


