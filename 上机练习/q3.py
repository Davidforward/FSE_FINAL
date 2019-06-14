# -*- coding: utf-8 -*-
#练习题3-股票交易
Stock_info=eval(input('输入：'))
Sum=0
for i in range(1,len(Stock_info)):
    if Stock_info[i]-Stock_info[i-1]>0:
        Sum+=Stock_info[i]-Stock_info[i-1]
print(Sum)
