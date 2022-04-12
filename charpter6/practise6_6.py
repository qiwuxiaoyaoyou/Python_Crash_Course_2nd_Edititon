# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 15:14
# @Author : 齐物逍遥游
# @File : practise6_6.py
# @Software : PyCharm

#6-6 调整 在6.3.1节编写的程序 favorite_languages.py中执行以下操作
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#创建一个应该会接受调查的人员名单，有些已包含在字典中，其他人未包含
persons = ['jen','sarah','zhangsan','lisi','wangwu']

#遍历这个人员名单。对已参加的，表示感谢，未参加的，邀请参加。
for person in persons:
    if person in favorite_languages.keys():
        print(f'{person},谢谢您参与我们的调查！')
    else:
        print(f'{person},我们希望能邀请您参与我们的调查')