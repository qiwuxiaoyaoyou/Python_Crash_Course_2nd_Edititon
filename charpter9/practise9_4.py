# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 16:45
# @Author : 齐物逍遥游
# @File : practise9_4.py
# @Software : PyCharm

#9-4 就餐人数  在完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0
class Restaurant():

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 22

    def describe_restaurant(self):
        print(f'欢迎光临{self.restaurant_name},我们主打{self.cuisine_type}')

    def open_restaurant(self):
        print('本餐厅正在营业')

#根据这个类 创建一个名为restaurant的实例，打印有多少人在这家餐厅就餐过，然后修改这个值并再次打印它。
# restaurant = Restaurant('宜宾燃面','川菜')
# print(f'有{restaurant.number_served}人曾莅临本店就餐')

#添加一个名为set_number_served()的方法，让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值
    def set_number_served(self,number_served):
        self.number_served = number_served

# restaurant = Restaurant('宜宾燃面','川菜')
# restaurant.set_number_served(100)
# #此处传入方法set_number_served()的实参100之后，使得number_served的值变为100，
# # 然后还是要通过init中的number_served获得该值
# print(f'本店当前就餐人数为{restaurant.number_served}')

#添加一个名为 increment_number_served()的方法，让你能够将就餐人数递增。
    def increment_number_served(self,number_served):
        self.number_served += number_served

# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
restaurant = Restaurant('宜宾燃面','川菜')

restaurant.set_number_served(100)
print(f'本店当前就餐人数为{restaurant.number_served}')

restaurant.increment_number_served(200)
print(f'本店每天可能接待的人数为{restaurant.number_served}')

'''
本练习总结：通过方法可以覆盖或者改变属性中默认定义的值
'''