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

#3-7 缩减名单 你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。

#1.以完成练习3-6的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
print("\n不好意思朋友们，由于特殊情况，只能邀请两位共进晚餐\n")

#2.使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印出一条消息表示抱歉
while len(friends) > 2:
    last_friend = friends.pop()
    print(f"{last_friend},实在抱歉，今晚无法邀请您了")

print("-"*30)

#3.对于余下两位嘉宾中的每一位，打印一条消息，指出他依然在受邀人之列
for friend in friends:
    invitation = f"{friend},您依然在受邀之列！"
    print(invitation)

#4.使用del将最后两位嘉宾从名单中删除，让名单边变成空，打印改名单，何时
del friends[0]     #del也可以只删除其中的某个元素,如果直接删除列表名称，将报错：该列表未被定义
del friends[0]
print(friends)



