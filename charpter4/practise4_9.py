# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 7:57
# @Author : 齐物逍遥游
# @File : practise4_9.py
# @Software : PyCharm

#4-9  立方解析 使用列表解析生成一个列表，其中包含前10个整数的立方

numbers = [number**3 for number in range(1,11)]
print(numbers)