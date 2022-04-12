# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 16:30
# @Author : 齐物逍遥游
# @File : practise7_2.py
# @Software : PyCharm

#7-2 餐馆订位  编写一个程序，询问用户有多少人，如果超过8位，就表示没有空桌，否则指出有空桌
person_number = input('请问你们有多少人用餐：')
number = int(person_number)
if number > 8:
    print('不好意思，没有空桌了')
else:
    print('欢迎光临，请里面坐')