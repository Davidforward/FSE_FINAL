# -*- coding: utf-8 -*-
#习题一：字符串变换

Str1=input('请输入字符串：')
length=len(Str1)
Str_new=''

Tem=Str1[0]
Count=1
for i in range(1,length):
    #print(i)
    if Str1[i]==Tem:
        Count+=1
    else:
        if Count==1:
            Str_new+=Tem
        else:
            Str_new+=str(Count)+Tem
        Tem=Str1[i]
        Count=1

if Count==1:
    Str_new+=Tem
else:
    Str_new+=str(Count)+Tem

print(Str_new)

        
        