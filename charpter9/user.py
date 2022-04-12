# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 8:06
# @Author : 齐物逍遥游
# @File : user.py
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