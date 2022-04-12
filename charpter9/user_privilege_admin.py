# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 8:00
# @Author : 齐物逍遥游
# @File : user_privilege_admin.py
# @Software : PyCharm

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

class Privileges():
    def __init__(self):
        self.privileges = ['增','删','改','查']

#  将方法show_privileges()移到这个类中。
    def show_privileges(self):
        print(f'以下是管理员admin的权限：')
        for privilege in self.privileges:
            print(f'-{privilege}')

#  在Adimin类中，将一个privileges实例用作属性。
class Admin(User):
    def __init__(self, first_name, last_name, country, tag, work):
        super().__init__(first_name, last_name, country, tag, work)
        self.privileges = Privileges()
