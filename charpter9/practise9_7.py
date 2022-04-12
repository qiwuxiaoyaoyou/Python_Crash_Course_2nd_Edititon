# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 22:48
# @Author : 齐物逍遥游
# @File : practise9_7.py
# @Software : PyCharm

#9-7 管理员  管理员是一种特殊的用户。编写一个名为Admin的类，让它继承练习9-3或9-5而编写的User类。
class User():

    def __init__(self,first_name,last_name,country,tag,work):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.tag = tag
        self.work = work
        self.login_attempts = 0  #本练习中增加的属性，默认为0

    def describe_user(self):
        print(f'{self.first_name}{self.last_name}是'
              f'{self.country}的著名{self.tag},他的代表作品是《{self.work}》')

    def greet_user(self):
        print('欢迎来到21世纪的网络时代！\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name,country,tag,work):
        super().__init__(first_name,last_name,country,tag,work)

#添加一个名为privileges的属性，用于存储一个由字符串（各种特殊权限）组成的列表。
        self.privileges = []

#编写一个名为show_privileges()的方法，显示管理员的权限。
    def show_privileges(self):
        print(f'以下是{self.first_name}{self.last_name}的权限：')
        for privilege in self.privileges:
            print(f'-{privilege}')

#创建一个Admin的实例，并调用这个方法。
zhuangzi = Admin('庄',"周",'战国时期','思想家','庄子')
zhuangzi.privileges = ['增','删','改','查']
zhuangzi.describe_user()
zhuangzi.show_privileges()

