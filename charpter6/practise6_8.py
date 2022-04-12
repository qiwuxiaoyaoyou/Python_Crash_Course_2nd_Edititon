# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 15:38
# @Author : 齐物逍遥游
# @File : practise6_8.py
# @Software : PyCharm

#6-8 宠物 创建多个表示宠物的字典，每个字典包含都包含宠物的类型等信息，再存入列表pets,再遍历列表，将所有信息打出来
dog = {'class':'dog','name':'eight','country':'Japan',}
cat = {'class':'cat','name':'beibei','country':'China',}
panda = {'class':'panda','name':'gungun','country':'China',}
lion = {'class':'lion','name':'xinba','country':'America',}

pets = [dog,cat,panda,lion]

for pet in pets:
    kind = pet['class']
    name = pet['name']
    country = pet['country']
    print(f'有一只名叫{name}的{kind}，它生活在{country}')