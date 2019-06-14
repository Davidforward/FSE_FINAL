# -*- coding: utf-8 -*-

#练习题4-穿墙而过


Brick=eval(input('输入：'))
#print(len(Brick))
Brick_add=Brick
Tem_sum=0
for Brick_item in Brick_add:
    Sum_item=0
    for i in range(len(Brick_item)):
        Sum_item+=Brick_item[i]
        Brick_item[i]=Sum_item
        Tem_sum=Sum_item

Brick_list=[]
for Brick_item in Brick_add:
    for i in Brick_item:
        if i!=Tem_sum:
            Brick_list.append(i)


Minus=max(Brick_list.count(x) for x in set(Brick_list))
print(Tem_sum-Minus)
