# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 10:11
# @Author : 齐物逍遥游
# @File : test.py
# @Software : PyCharm
messages = ['逍遥游','齐物论','养生主','人间世','德充符','大宗师','应帝王']
sent_messages = []
for message in messages:
    print(messages)
    print(message)

    current_message = messages.remove(message)
    print(current_message)
    sent_messages.append(current_message)
    print(sent_messages,'\n')

# print(messages)
# print(sent_messages)
#
# messages = ['逍遥游','齐物论','养生主','人间世','德充符','大宗师','应帝王']
# sent_messages = []
# while messages:
#     current_message = messages.pop()
#     sent_messages.append(current_message)
#
# print(messages)
# print(sent_messages)
