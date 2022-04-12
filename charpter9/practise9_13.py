# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 8:14
# @Author : 齐物逍遥游
# @File : practise9_13.py
# @Software : PyCharm

from random import randint

#9-13 骰子 创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。
class Die:
    def __init__(self,sides=6):
        self.sides = sides

#编写一个名为roll_die()的方法，它打印位于1和骰子面熟之间的随机数。
    def roll_die(self):
        ranom_number = randint(1,self.sides)
        print(f"这个{self.sides}面骰子这次甩出来的数字是{ranom_number}")

#创建一个6面的骰子再掷10次
six_dice = Die()
for number in range(10):
    six_dice.roll_die()
print('*'*30)

#创建一个10面的骰子和一个20面的骰子，再分别掷10次
ten_dice = Die(10)
for number in range(10):
    ten_dice.roll_die()
print('*' * 30)

ten_dice = Die(20)
for number in range(10):
    ten_dice.roll_die()