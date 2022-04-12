# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 9:54
# @Author : 齐物逍遥游
# @File : practise8_10.py
# @Software : PyCharm

#8-10 发送消息  在8-9编写的程序中，编写一个名为send_messages()的函数，
def show_messages(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
        sent_messages.sort(reverse=True)     #pop弹出的元素时从后往前的，这里可以用sort方法进行列表反转，变成原顺序

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




