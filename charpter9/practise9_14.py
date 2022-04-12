# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 8:30
# @Author : 齐物逍遥游
# @File : practise9_14.py
# @Software : PyCharm

from random import choice

#9-14 彩票  创建一个列表或元组，其中包含10个数和5个字母。
#  从这个列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4个数或字母，就中大奖。
number_letters = (1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e')
winners = []

while len(winners) < 4:
    number_letter = choice(number_letters)
    if number_letter not in winners:
        winners.append(number_letter)

print(f'大奖号码为{winners}')
