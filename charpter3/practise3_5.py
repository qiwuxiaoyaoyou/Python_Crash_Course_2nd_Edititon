# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 21:03
# @Author : 齐物逍遥游
# @File : practise3_4.py
# @Software : PyCharm

#3-5 修改嘉宾名单 得知有位嘉宾无法赴约，因此需要另外邀请以为嘉宾

#1.以3-4练习为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约
friends = ["庄子","苏东坡","鲁迅","梁启超","尼采","康德","本杰明·富兰克林","马克思"]
# for friend in friends:
#     invitation = '{},和我一起共进晚餐可好？'.format(friend)
#     print(invitation)
print("大佬{}将无法赴约".format(friends[-1]))

#2.将无法赴约的嘉宾姓名更改为新邀请的嘉宾姓名
friends[-1] = "恩格斯"

#3.再次打印一系列消息，向名单中的每位嘉宾发出邀请
for friend in friends:
    invitation = '{},和我一起共进晚餐可好？'.format(friend)
    print(invitation)