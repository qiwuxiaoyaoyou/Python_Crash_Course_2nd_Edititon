# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 17:14
# @Author : 齐物逍遥游
# @File : practise9_5.py
# @Software : PyCharm

#9-5 尝试登陆次数  在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。
class User():

    def __init__(self,first_name,last_name,country,tag,work):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.tag = tag
        self.work = work
        self.login_attempts = 0  #本练习中增加的属性，默认为0

# 在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
    def describe_user(self):
        print(f'{self.first_name}{self.last_name}是'
              f'{self.country}的著名{self.tag},他的代表作品是《{self.work}》')

# 再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
    def greet_user(self):
        print('欢迎来到21世纪的网络时代！\n')

#  编写一个名为 increment_login_attempts()的方法，将属性login_attempts的值加1。
    def increment_login_attempts(self):
        self.login_attempts += 1

# 再编写一个名为reset_login_attempts()的方法，将属性login_attempts 的值重置为0。
    def reset_login_attempts(self):
        self.login_attempts = 0

#根据User类创建一个实例，再调用方法increment_login_attempts()多次，打印属性login_attempts的值，确认它被正确地递增
zhuangzi = User('庄',"周",'战国时期','思想家','庄子')
print(f'尝试登陆{zhuangzi.login_attempts}次')

zhuangzi.increment_login_attempts()
print(f'尝试登陆{zhuangzi.login_attempts}次')

zhuangzi.increment_login_attempts()
print(f'尝试登陆{zhuangzi.login_attempts}次')

zhuangzi.increment_login_attempts()
print(f'尝试登陆{zhuangzi.login_attempts}次')

zhuangzi.increment_login_attempts()
print(f'尝试登陆{zhuangzi.login_attempts}次')

zhuangzi.increment_login_attempts()
print(f'尝试登陆{zhuangzi.login_attempts}次')

zhuangzi.reset_login_attempts()
print(f'尝试登陆{zhuangzi.login_attempts}次')
