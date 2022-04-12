# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 8:37
# @Author : 齐物逍遥游
# @File : practise4_12.py
# @Software : PyCharm

#4-12 使用多个循环  请选择书中一个foods.py版本，在其中编写两个for循环 ，将各个食品列表打印出来
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

for my_food in my_foods:
    print(my_food)

print('-'*30)

for friend_food in friend_foods:
    print(friend_food)