# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 12:26
# @Author : 齐物逍遥游
# @File : practise10_4.py
# @Software : PyCharm

#10-4 访客名单 编写一个while循环，提示用户输名字，用户输入名字后，在屏幕上打印依据问候语，
prompt = '\n来者可留姓名？（输入quit随时退出）：'
file_name = 'guest_book.txt'
name = ''

while name != 'quit':
    name = input(prompt)
    if name != 'quit':
        print(f'{name}，欢迎到此！')
# 并将一条到访记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
        with open(file_name,'a',encoding='utf-8') as file:
            file.write(f'在下{name}到此一游！\n')

