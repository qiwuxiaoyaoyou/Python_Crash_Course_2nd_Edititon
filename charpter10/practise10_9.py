# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 14:49
# @Author : 齐物逍遥游
# @File : practise10_9.py
# @Software : PyCharm

#10-9 静默的猫和够 修改练习10-8中编写的except代码块，让程序在任意文件不存在时静默失败
filenames = ['cats.txt','dogs.txt']

for filename in filenames:

    try:
        with open(filename,encoding='utf-8') as file:
            print(f'\n文件{filename}的内容如下：')
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        pass