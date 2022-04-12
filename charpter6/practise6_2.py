# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 11:09
# @Author : 齐物逍遥游
# @File : practise6_2.py
# @Software : PyCharm

#6-2 喜欢的数 使用一个字典来存储一些人喜欢的数，想出5个人的名字，对应一个数
name_numbers = {
    'zhaoyi':1,
    'qianer':2,
    'sunsan':3,
    'lisi':4,
    'zhouwu':5,
    }
for key,value in name_numbers.items():
    print(f"{key}的数字是{value}")
