# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 20:40
# @Author : 齐物逍遥游
# @File : practise3_1.py
# @Software : PyCharm

#3-2 问候语 继续使用3-1的列表，但是改为为没人打印一条消息，消息包含相同的问候语
names = ["庄子","苏东坡","鲁迅","梁启超","尼采","康德","本杰明·富兰克林","马克思"]
for name in names:
    message = f'{name}，看你的书真是一种享受'
    print(message)

for name in names:
    message = '{}，看你的书真是一种享受'.format(name)
    print(message)



