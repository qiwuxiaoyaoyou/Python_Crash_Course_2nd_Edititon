# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 18:10
# @Author : 齐物逍遥游
# @File : practise2_3.py
# @Software : PyCharm

#2-3个性化消息 用变量表示一个人的名字，并向其显示一条消息
name = "张三"
message_1 = f"你好，{name}！你今天做核酸了吗？"      #python3.6及以后的版本可使用
message_2 = "你好，{}！你今天做核酸了吗？".format(name)      #python3.5及以前的版本使用
print(message_1)
print(message_2)