# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 10:32
# @Author : 齐物逍遥游
# @File : practise8_11.py
# @Software : PyCharm

#8-11 消息归档  修改8-10而编写的程序，在调用函数send_messages(),向它传递消息列表的副本。
#  调用函数send_messages()后，将两个列表都打印出来，确认保留了原始列表的消息

#8-10 发送消息  在8-9编写的程序中，编写一个名为send_messages()的函数，
def show_messages(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    for message in messages:
        sent_messages.append(message)

# 将show_messages()中的每条信息打印出来并移到一个叫sent_messages的列表中。
messages = ['逍遥游','齐物论','养生主','人间世','德充符','大宗师','应帝王']
show_messages(messages)

# 调用send_messages(),
sent_messages = []
send_messages(messages,sent_messages)

# 再将两个列表都打印出来，确认正确地移动了消息。
print('\n确认两个列表的情况：')
print(messages)
print(sent_messages)

'''
本练习书本参考的答案的方式是：在8-10的基础上，直接给函数send_messages（）传递列表messages的副本[:]
我采用的方法是用for循环的方式取出messages里的各个字符串，再依次附加给空列表sent_messages
'''