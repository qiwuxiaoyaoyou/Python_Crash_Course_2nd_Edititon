# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 16:46
# @Author : 齐物逍遥游
# @File : practise7_4.py
# @Software : PyCharm

#7-4 编写一个循环，提示用户输入一系列书名，并在用户输入'quit'时结束循环，每当用户输入一本书名时，打印一条信息
book_name = '\n请告诉我们你想要借的书（输入quit退出):'
book = ''
while book != 'quit':
    book = input(book_name)
    if book != 'quit':
        print(f'我会给你找到真本《{book}》')