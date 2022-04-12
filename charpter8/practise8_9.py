# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 9:48
# @Author : 齐物逍遥游
# @File : practise8_9.py
# @Software : PyCharm

#8-9 消息 创建一个列表，其中包含一系列简短的文本消息。将该列表传递给一个名为show_message()的函数，函数将打印每条消息
def show_messages(messages):
    for message in messages:
        print(message)

messages = ['逍遥游','齐物论','养生主','人间世','德充符','大宗师','应帝王']
show_messages(messages)

