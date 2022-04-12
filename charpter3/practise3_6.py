# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 21:22
# @Author : 齐物逍遥游
# @File : practise3_6.py
# @Software : PyCharm

#3-6 添加嘉宾 你找到更大的餐桌，可容纳更多的嘉宾。你还想邀请哪三位嘉宾。

#1.以练习3-4时编写的程序为基础，在程序末尾添加一条print语句，支出你找到了一个更大餐桌
friends = ["庄子","苏东坡","鲁迅","梁启超","尼采","康德","本杰明·富兰克林","马克思"]
# for friend in friends:
#     invitation = '{},和我一起共进晚餐可好？'.format(friend)
#     print(invitation)
print("我找到了一张更大的餐桌")

#2.使用insert()将以为新嘉宾添加到名单开头
friends.insert(0,"查拉图斯特拉")
# print(friends)
friends.insert(5,"伊拉斯谟")
# print(friends)
friends.append("加缪")
for friend in friends:
    invitation = '{},和我一起共进晚餐可好？'.format(friend)
    print(invitation)