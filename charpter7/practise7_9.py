# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 20:19
# @Author : 齐物逍遥游
# @File : practise7_9.py
# @Software : PyCharm

#7-9  夫妻肺片卖完了   使用7-8练习而创建的列表dish_orders,并确保‘夫妻肺片’在其中至少出现了三次。
# 在程序开头附近添加这样一段代码：打印一条消息，指出饭店的‘夫妻肺片’卖完了
#再使用一个while循环将列表dish_orders 中的‘夫妻肺片’删除。
#确认最终的列表finished_dishes 未包含‘夫妻肺片’

dish_orders = ['爆炒花甲','宜宾燃面','夫妻肺片','三合一','酸辣土豆丝','夫妻肺片','诸葛烤鱼','夫妻肺片']
finished_dishes = []

print('夫妻肺片卖完了！\n')

while '夫妻肺片' in dish_orders:
    dish_orders.remove('夫妻肺片')

while dish_orders:
    current_dish = dish_orders.pop()
    finished_dishes.append(current_dish)

print(finished_dishes)