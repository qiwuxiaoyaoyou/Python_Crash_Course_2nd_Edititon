# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 11:09
# @Author : 齐物逍遥游
# @File : practise6_2.py
# @Software : PyCharm

#6-2 喜欢的数 使用一个字典来存储一些人喜欢的数，想出5个人的名字，对应一个数
# name_numbers = {
#     'zhaoyi':1,
#     'qianer':2,
#     'sunsan':3,
#     'lisi':4,
#     'zhouwu':5,
#     }
# for key,value in name_numbers.items():
#     print(f"{key}的数字是{value}")

#6-10 喜欢的数字2 修改6-2编写的程序，让每个人都可以有多个喜欢的数，然后将每个人的名字及喜欢的数打印出来

name_numbers = {
    'zhaoyi':[1,2,3],
    'qianer':[2,4,6],
    'sunsan':[3,6,9],
    'lisi':[4,8,12],
    'zhouwu':[5,10,15,20,25]
    }

for name,numbers in name_numbers.items():  #这里的numbers取出来的是一个列表
    print(f'\n{name}最喜欢的数字分别是：')
    for number in numbers:
        print(number)

