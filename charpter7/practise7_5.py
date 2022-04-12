# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 17:11
# @Author : 齐物逍遥游
# @File : practise7_5.py
# @Software : PyCharm

#7-5 电影票  不到3岁的观众免费，3-12岁10元，超过12岁收15元。编写一个循环，询问用户年龄，并指出其票价

#写法一:常规写法
prompt = '\n写法一：请问您今年几岁（输入quit退出）:'
age = ''
while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            print('你的电影票免费')
        elif age <12:
            print('你需要支付10元')
        else:
            print('你需要支付15美元')

#写法二：使用标志active
prompt = '\n写法二：请问您今年几岁（输入quit退出）:'
active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print('你的电影票免费')
        elif age <12:
            print('你需要支付10元')
        else:
            print('你需要支付15美元')

#写法三：使用break退出循环
prompt = '\n写法三：请问您今年几岁（输入quit退出）:'

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print('你的电影票免费')
        elif age < 12:
            print('你需要支付10元')
        else:
            print('你需要支付15美元')

'''
书本7-6的要求已包含于此
'''