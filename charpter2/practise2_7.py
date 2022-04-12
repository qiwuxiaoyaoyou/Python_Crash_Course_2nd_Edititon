# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 18:40
# @Author : 齐物逍遥游
# @File : practise2_7.py
# @Software : PyCharm

#2-7 剔除人名中的空白  用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次
        #打印这个人名，显示其开头和末尾的空白，然后分别使用剔除函数lstrip()、rstrip()和strip()对人名进行处理，并打印

"""
\t是制表符，\n是换行符，经常使用\n\t，来进行换行缩进？
"""
name = "  本杰明·\t富\n兰克林  "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

name_1 = '张\t三'
name_2 = "张\n三"
name_3 = "张\n\t三"
name_4 = "张\t\n三"
print(name_1)
print(name_2)
print(name_3)
print(name_4)



