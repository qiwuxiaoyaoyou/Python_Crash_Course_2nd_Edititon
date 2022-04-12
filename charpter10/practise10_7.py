# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 14:08
# @Author : 齐物逍遥游
# @File : practise10_7.py
# @Software : PyCharm

#10-7 加法计算器  将10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数）后能够继续输入数
while True:
    print('\n请按照提示输入两个整数，将告诉您他们的和（任意时刻quit退出）')
    try:
        number_one = input('请输入第一个整数:')
        if number_one == 'quit':
            break
        number_one = int(number_one)

        number_two = input('请输入第二个整数:')
        if number_two == 'quit':
            break
        number_two = int(number_two)

        result = int(number_one) + int(number_two)
    except ValueError:
        print('\n您未按要求输入两个整数，请确保输入的是整数！')
    else:
        print(f'您输入的两个整数之和为{result}')
