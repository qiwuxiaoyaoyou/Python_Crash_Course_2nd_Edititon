# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 15:56
# @Author : 齐物逍遥游
# @File : practise9_1.py
# @Software : PyCharm

#9-1 餐馆  创建一个名为Restaurant的类，为其方法__init__()设置属性 restaurant_name 和 cuisine_type。
class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法。
#前者打印两条信息，后者表示餐馆正在营业
    def describe_restaurant(self):
        print(f'欢迎光临{self.restaurant_name},我们主打{self.cuisine_type}')

    def open_restaurant(self):
        print('本餐厅正在营业')

#根据这个类创建一个名为restaurant的实例，
restaurant = Restaurant('宜宾燃面','川菜')

# 分别打印其两个属性，
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# 再调用两个方法
restaurant.describe_restaurant()
restaurant.open_restaurant()