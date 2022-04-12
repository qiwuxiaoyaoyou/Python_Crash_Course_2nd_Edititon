# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 16:17
# @Author : 齐物逍遥游
# @File : practise9_3.py
# @Software : PyCharm

#9-3 用户 创建一个名为User的类，其中包含属性first_name 和 last_name，以及用户简介通常会存储的其他几个属性。
class User():

    def __init__(self,first_name,last_name,country,tag,work):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.tag = tag
        self.work = work

# 在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
    def describe_user(self):
        print(f'{self.first_name}{self.last_name}是'
              f'{self.country}的著名{self.tag},他的代表作品是《{self.work}》')

# 再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
    def greet_user(self):
        print('欢迎来到21世纪的网络时代！\n')

#创建多个表示不同用户的实例，并对每个实例调用上述两个方法
zhuangzi = User('庄',"周",'战国时期','思想家','庄子')
zhuangzi.describe_user()
zhuangzi.greet_user()

luxun = User('鲁',"迅",'民国时期','作家','呐喊')
luxun.describe_user()
luxun.greet_user()