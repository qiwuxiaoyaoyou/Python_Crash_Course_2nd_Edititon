# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 8:06
# @Author : 齐物逍遥游
# @File : privileges.py
# @Software : PyCharm

from user import User #如果使用import user导入整个模块，子类继承父类时，用 模块名.类名 的方式继承

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