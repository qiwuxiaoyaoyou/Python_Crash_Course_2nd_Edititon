# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 7:48
# @Author : 齐物逍遥游
# @File : practise9_10.py
# @Software : PyCharm

#9-10  导入Restaurant类  将最新的Restaurant类存储在一个模块中。在另一个文件中，导入Restaurant类
from restaurant import  Restaurant

# 创建一个Restaurant实例，并调用Restaurant中的一个方法，确认import语句正确无误
restaurant = Restaurant('回味鸭血粉丝','金陵菜')
restaurant.describe_restaurant()
