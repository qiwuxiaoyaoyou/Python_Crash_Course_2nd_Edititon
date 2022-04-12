# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 7:55
# @Author : 齐物逍遥游
# @File : restaurant.py
# @Software : PyCharm

class Restaurant():

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 22

    def describe_restaurant(self):
        print(f'欢迎光临{self.restaurant_name},我们主打{self.cuisine_type}')

    def open_restaurant(self):
        print('本餐厅正在营业')

#添加一个名为set_number_served()的方法，让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值
    def set_number_served(self,number_served):
        self.number_served = number_served

#添加一个名为 increment_number_served()的方法，让你能够将就餐人数递增。
    def increment_number_served(self,number_served):
        self.number_served += number_served