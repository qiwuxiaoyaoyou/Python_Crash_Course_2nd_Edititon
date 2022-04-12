# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 9:43
# @Author : 齐物逍遥游
# @File : practise5_6.py
# @Software : PyCharm

#5-6 人生的不同阶段  设置变量age的值，再编写一个if-elif-else结构，根据age的值判断一个人处于人生的哪个阶段
age = 100
if age < 2:
    print('这是一个婴儿')
elif age < 4:
    print('这是一个幼儿')
elif age < 13:
    print('这是一个儿童')
elif age < 20:
    print('这是一个青少年')
elif age < 65:
    print('这是一个成年人')
else:
    print('这是一个老年人')