# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 21:03
# @Author : 齐物逍遥游
# @File : practise3_4.py
# @Software : PyCharm

#3-4 嘉宾名单 如果你可以邀请任何人一起共进晚餐，你会邀请哪些人？请创建一个列表，其中包含至少三个你想邀请的人，然后邀请这些人
friends = ["庄子","苏东坡","鲁迅","梁启超","尼采","康德","本杰明·富兰克林","马克思"]
for friend in friends:
    invitation = '{},和我一起共进晚餐可好？'.format(friend)
    print(invitation)