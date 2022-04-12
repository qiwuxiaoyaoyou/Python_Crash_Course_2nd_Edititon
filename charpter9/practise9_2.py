# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 16:12
# @Author : 齐物逍遥游
# @File : practise9_2.py
# @Software : PyCharm

#9-2 三家餐馆，根据9-1的练习而编写的程序，创建三个实例，并对每个实例调用方法describe_restaurant()
class Restaurant():

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(f'欢迎光临{self.restaurant_name},我们主打{self.cuisine_type}')

    def open_restaurant(self):
        print('本餐厅正在营业')

weiji = Restaurant('魏记','淮扬菜')
weiji.describe_restaurant()

grandma = Restaurant('外婆家','杭帮菜')
grandma.describe_restaurant()

kfc = Restaurant('肯德基','快餐')
kfc.describe_restaurant()
