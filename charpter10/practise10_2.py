# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 10:42
# @Author : 齐物逍遥游
# @File : practise10_2.py
# @Software : PyCharm

#10-2 C语言学习笔记  可使用方法replace()将字符串中的特点单词都替换为另一个单词。
# 读取你刚创建的文件learning_python.txt中的每一行，将其中的python都替换成另一门语言的名称，比如C。
with open('learning_python.txt',encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    new_line = line.replace('python','C语言')  #replace仅仅是临时保存替换后的字符串，效力跟sorted函数类似
#将修改后的各行都打印到屏幕上
    print(new_line.rstrip())

print('-'*30)
#另外一种写法：
with open('learning_python.txt',encoding='utf-8') as file:
    contents = file.read()
    print(contents.replace('python','C语言'))