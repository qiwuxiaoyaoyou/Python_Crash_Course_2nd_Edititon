# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 13:45
# @Author : 齐物逍遥游
# @File : practise10_6.py
# @Software : PyCharm

#10-6 加法运算  提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。
#  在此情况下，当你尝试将输入转换为整数时，将引发ValueError异常。
# 编写一个程序，提示用户输入两个数，再将其相加并打印结果。
# 在用户输入的任何一个值不是数时都捕获ValueError异常，并打印一条友好的错误信息。
# 对你编写的程序进行测试：先输入两个数，再输入一些文本而不是数。

number_one = input('\n按照提示输入两个整数，将告诉您它们的和\n请输入第一个整数:')
number_two = input('请输入第二个整数:')

try:
    result = int(number_one) + int(number_two)
except ValueError:
    print('您没有输入整数！请输入一个整数！')
else:
    print(f'您输入的两个整数之和为{result}')

