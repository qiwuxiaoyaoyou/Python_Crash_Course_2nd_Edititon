# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 15:42
# @Author : 齐物逍遥游
# @File : practise10_11.py
# @Software : PyCharm

import  json
#10-11 喜欢的数  编写一个程序，提示用户输入喜欢的数，并使用json.dump()将这个数据存储到文件中。
#  再编写一个程序，从文件中读取这个值，打印一段消息
favorite_number = input('你最喜欢的数是什么：')
file_name = 'favorite_number.json'

with open(file_name,'w',encoding='utf-8') as file:
    json.dump(favorite_number,file)

with open(file_name,encoding='utf-8') as file:
    number = json.load(file)
    print(f'我知道你最喜欢的数字是{number}')
