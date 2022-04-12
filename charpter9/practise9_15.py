# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 8:45
# @Author : 齐物逍遥游
# @File : practise9_15.py
# @Software : PyCharm

from random import choice
#9-15 彩票分析  可以使用一个循环来明白9-14中的彩票大奖有多难中奖。
def lottery(number_letters):
    '''抽奖函数'''

    winner_ticket = []
    while len(winner_ticket) < 4:
        number_letter = choice(number_letters)
        if number_letter not in winner_ticket:
            winner_ticket.append(number_letter)
    return winner_ticket

def check_ticket(my_ticket,winner_ticket):
    '''核对我的彩票是否中奖'''
    if my_ticket == winner_ticket:
        return True
    else:
        return False

number_letters = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
winner_ticket = lottery(number_letters)

#创建一个名为my_ticket的列表或元组，再编写一个循环，不断地随机选择数或字母，直到中大奖为止。
my_ticket = [1,2,3,4]

plays = 0
won = False

while not won:
    check_ticket(my_ticket, winner_ticket)
    plays += 1
    if plays > 100000:
        break

if won:
    print(f'中奖号码是{winner_ticket},我抽了{plays}次')
else:
    print(f'我没有中奖，但是我已经抽了{plays}次')


#打印一条消息，报告执行循环多少次才中了大奖。

