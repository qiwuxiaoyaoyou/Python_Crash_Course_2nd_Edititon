# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 10:14
# @Author : 齐物逍遥游
# @File : practise10_1.py
# @Software : PyCharm

#10-1 python学习笔记  在文本编辑器中新建一个文件，写几句话来总结一下关于python的知识。
# 将这个文件命名为learning_python.txt，并存储到为完成本章练习而编写的程序所在的目录中。
#编写一个程序，读取这个文件，并将你所写的内容打印三次：
with open('learning_python.txt',encoding='utf-8') as file:  #含中文文档的需要解码encoding

#第一次打印时读取整个文件；
    contents = file.read()
    print(contents)

print('*'*30)

#第二次打印遍历文件对象；
with open('learning_python.txt',encoding='utf-8') as file:
    for line in file:
        print(line.rstrip())  #因为文件中每行有换行符，所以遍历时会出现空行，用rstrip()方法消除这些空行

print('*'*30)

#第三次打印时将各行存储在一个列表中，再在with代码块外打印
with open('learning_python.txt',encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)

for line in lines:
    print(line.rstrip())