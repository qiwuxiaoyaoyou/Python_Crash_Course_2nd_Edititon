# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 18:44
# @Author : 齐物逍遥游
# @File : practise9_6.py
# @Software : PyCharm

#9-6 冰淇淋小店  冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承9-1或9-4练习编写的Restaurant类
class Restaurant():

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 22

    def describe_restaurant(self):
        print(f'欢迎光临{self.restaurant_name},我们主打{self.cuisine_type}')

    def open_restaurant(self):
        print('本餐厅正在营业')

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,number_served):
        self.number_served += number_served

class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)

#添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。
        self.flavors = []

#编写一个显示这些冰淇淋的方法。
    def show_flavors(self):
        print('我们有以下冰淇淋出售：')
        for flavor in self.flavors:
            print(f'-{flavor}')

#创建一个IceCreamStand实例，并调用这个方法。
heluxue = IceCreamStand('和路雪','冰淇淋')
heluxue.flavors = ['巧克力','奶油','草莓','菠萝']

heluxue.describe_restaurant()
heluxue.show_flavors()