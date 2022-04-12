# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 7:28
# @Author : 齐物逍遥游
# @File : practise4_2.py
# @Software : PyCharm

#4-2 想出至少三种有共同特征的动物，存入列表，再用for循环打印
animals = ["大熊猫","金丝猴","丹顶鹤","中华豚","东北虎","藏羚羊"]
for animal in animals:
    print(animal)

#修改程序，对于每一种动物打印一个句子
print('-'*30)
for animal in animals:
    print(f'{animal}是国宝级动物')

#在程序末尾添加一行代码，指出这些动物的共同点
print("\n这些动物都是国宝级动物！")