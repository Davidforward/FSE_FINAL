# -*- coding: utf-8 -*-
#扩展题*：股票交易升级版
Stock_info=eval(input('输入：'))
K=int(input('请输入k：'))
Trade=[]
Time=0
Sum_highest=0
for i in range(1,len(Stock_info)):
    if Stock_info[i]-Stock_info[i-1]>0:
        Sum_highest+=Stock_info[i]-Stock_info[i-1]
        Trade.append((i-1,i))
        Time+=1

Tailor=Time-K
while Tailor>0:
    Minus=99999999 #寻找最小收益损失
    i_target=0
    for i in range(1,len(Trade)):
        if Minus>Stock_info[Trade[i][1]]-Stock_info[Trade[i-1][0]]:
            Minus=Stock_info[Trade[i][1]]-Stock_info[Trade[i-1][0]]
            i_target=i
    Trade[i_target-1]=(Trade[i_target-1][0],Trade[i_target][1])
    Trade.remove(Trade[i_target])
    Sum_highest-=Minus
    Tailor-=1

print(Sum_highest)
    
