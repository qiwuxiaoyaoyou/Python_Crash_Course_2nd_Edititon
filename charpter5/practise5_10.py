# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 10:22
# @Author : 齐物逍遥游
# @File : practise5_10.py
# @Software : PyCharm

#5-10 检查用户名  按下面的说明编写一个程序，模拟网站如何确保每位用户的用户名都独一无二

#1、创建一个至少包含5个用户名的列表，将其命名为current_users
current_users = ['Zhaoyi','qianer','sunsan','lisi','Zhouwu','wuliu','zhengqi','wangBa']

#2、再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在current_users中
new_users = ['jiayi','yier','zhouwu','wangba','bingsan']

#3、遍历列表new_users，对于其中的每个用户名，都检查他是否已被使用，并分别输出一条消息。
for user in new_users:
    if user in current_users:
        print(f'用户名{user}已被占用')
    else:
        print(f'用户名{user}你可以使用')

print('-'*30)
#4、确保比较时不区分大小写，如john已被使用，那么JOHN 也无法使用
#可以先创建current_users的副本
current_users_copy = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_copy :
        print(f'用户名{user}已被占用')
    else:
        print(f'用户名{user}你可以使用')