# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 14:05
# @Author : 齐物逍遥游
# @File : test.py
# @Software : PyCharm
file_name = 'Alice in Wonderland.txt'

with open(file_name,encoding='utf-8') as file:
    contents = file.read()
    # print(contents)
    print(contents.count('the'))
    print(contents.lower().count('the'))
    print(contents.lower().count('the '))

