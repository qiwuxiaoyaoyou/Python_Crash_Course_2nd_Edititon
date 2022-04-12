# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 10:58
# @Author : 齐物逍遥游
# @File : practise10_3.py
# @Software : PyCharm

#10-3 访客  编写一个程序，提示用户输入名字。用户做出响应后，将其名字写入文件guest.txt中
prompt = '请输入您的名字（输入quit可随时退出）：'
file_name = 'guest.txt'
name = ''

while name != 'quit':
    name = input(prompt)
    if name != 'quit':
        with open(file_name,'w') as file:
            file.write(name)


