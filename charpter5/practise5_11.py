# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 10:48
# @Author : 齐物逍遥游
# @File : practise5_11.py
# @Software : PyCharm

#5-11 序数 序数表示位置 如1st 2nd，序数大多以th结尾，只有1,2,3例外

#在一个列表中存储数字1~9
numbers = list(range(1,10))
print(numbers)

#遍历这个列表
for number in numbers:
    print(number)

# 在循环中使用if-elif-else结构，打印每个数字对应的序数，每个序数独占一行
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print("3rd")
    else:
        print(f'{number}th')