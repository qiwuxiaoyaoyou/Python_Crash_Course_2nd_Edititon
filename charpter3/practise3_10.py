# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 22:07
# @Author : 齐物逍遥游
# @File : practise3_10.py
# @Software : PyCharm

#3-10 尝试使用各个函数 想想可存储到列表中的东西，任何喜欢的东西。编写一个程序，在其中创建一个包含这些元素的列表，
#       使用每个本章介绍的每个函数，至少使用一次来处理这个列表

likes = ["sea","book","panda","python","dog","beautiful_girl"]

#1.使用sorted的函数对列表进行临时排序
print(sorted(likes))

#2.使用sorted函数对列表进行倒序临时排序
print(sorted(likes,reverse=True))

#3.使用len()函数得到列表的长度，即元素的个数
print(len(likes))