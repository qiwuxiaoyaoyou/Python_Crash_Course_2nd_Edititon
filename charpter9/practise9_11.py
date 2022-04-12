# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 7:57
# @Author : 齐物逍遥游
# @File : practise9-11.py
# @Software : PyCharm

#9-11  导入Admin类  以为完成练习9-8而做的工作为基础。将User类、Privileges类和Admin类存储在一个模块中。
# 再创建一个文件，在其中创建一个Admin实例并对其调用方法show_privileges()，以确认一切都能正确运行。
from user_privilege_admin import Admin

zhuangzi = Admin('庄',"周",'战国时期','思想家','庄子')
zhuangzi.privileges.show_privileges()