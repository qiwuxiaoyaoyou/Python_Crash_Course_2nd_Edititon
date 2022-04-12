# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 14:27
# @Author : 齐物逍遥游
# @File : practise10_8.py
# @Software : PyCharm

#10-8 猫和狗 创建文件cats.txt和dogs.txt ，在第一个文件中至少存储三只猫的名字，第二个文件至少存储三条狗的名字。
#  编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个 try-except代码块中，以便在文件不存在时捕获FileNotFound错误，并显示一条友好的消息。
#  将任意一个文件移到另一个地方，并确认except代码块中的代码将正确执行
filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    try:
        with open(filename,encoding='utf-8') as file:
            print(f'\n文件{filename}的内容如下：')
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f'{filename}文件找不到')

