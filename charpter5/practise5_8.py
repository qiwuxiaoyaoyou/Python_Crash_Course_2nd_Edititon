# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 9:57
# @Author : 齐物逍遥游
# @File : practise5_8.py
# @Software : PyCharm

#5-8 以特殊方式跟管理员打招呼   创建一个至少包含5个用户名的列表，其中一个名为'admin'。
# 遍历用户列表，并向每位用户打印一条问候信息，其中admin收到的信息比较特殊
users = ['张三','李四','王五','赵六','孙七','admin']
for user in users:
    if user == 'admin':
        print(f'你好{user},请使用管理员权限')
    else:
        print(f'你好{user},欢迎访问')