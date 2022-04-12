# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 8:11
# @Author : 齐物逍遥游
# @File : practise9_12.py
# @Software : PyCharm

#9-12 多个模块  将User类存储在一个模块中，并将privileges类和Admin类存储在另一个模块中。
# 再创建一个文件，在其中创建一个Admin实例并对其调用方法show_privileges(),确认能运行。

from privileges_admin import Admin
zhuangzi = Admin('庄',"周",'战国时期','思想家','庄子')
zhuangzi.privileges.show_privileges()