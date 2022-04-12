# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 15:11
# @Author : 齐物逍遥游
# @File : practise8_12.py
# @Software : PyCharm

#8-12 菜品 编写一个函数，它接受顾客要在某道菜中添加的一系列食材或调料。这个函数只有一个形参，打印一条信息
#  调用这个函数三次，每次都提供不同数量的实参

def dishes(*dishes):
    print('\n我们将为您添加以下食材或调料：')
    for dish in dishes:
        print(dish)

dishes('蒜泥')
dishes('花生米','醋')
dishes('酱油','香菜','八角')