# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 20:04
# @Author : 齐物逍遥游
# @File : practise7_8.py
# @Software : PyCharm

#7-8 饭店 创建一个名为dish_orders的列表，在其中包含各种菜的名称，再创建一个名为finished_dishes的空列表。
# 遍历列表dish_orders，对于其中的每种菜品，都打印一条消息，并将其移到列表finished_dishes中，
# 所有菜品都制作好后，打印一条消息，将这些菜品列出来。
dish_orders = ['爆炒花甲','宜宾燃面','三合一','酸辣土豆丝','诸葛烤鱼','夫妻肺片']
finished_dishes = []

for dish_order in dish_orders:
    print(f'我在做这道{dish_order}')
    finished_dishes.append(dish_order)

print('\n所有的菜都做好了！\n')

for finished_dish in finished_dishes:
    print(finished_dish)

print('-'*30)

#以下用while写法
dish_orders = ['爆炒花甲','宜宾燃面','三合一','酸辣土豆丝','诸葛烤鱼','夫妻肺片']
finished_dishes = []

while dish_orders:  #当dish_orders存在元素时，执行while循环
    current_dish = dish_orders.pop()
    print(f'我在做这道{current_dish}')
    finished_dishes.append(current_dish)

print('\n所有的菜都做好了！\n')

for finished_dish in finished_dishes:
    print(finished_dish)