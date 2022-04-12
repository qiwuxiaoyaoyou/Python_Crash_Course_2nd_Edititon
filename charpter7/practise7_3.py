# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 16:38
# @Author : 齐物逍遥游
# @File : practise7_3.py
# @Software : PyCharm

#7-3 10的整数倍  让用户输入一个数，并指出该数是否为10的整数倍
number = input('请输入一个数,我将告诉你它是不是10的整数倍：')
number = int(number)
if number % 10 == 0:
    print('这个数是10的整数倍')
else:
    print('这个数不是10的整数倍')