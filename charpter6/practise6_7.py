# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 15:22
# @Author : 齐物逍遥游
# @File : practise6_7.py
# @Software : PyCharm

#6-1 人 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市，将存储在字典中的每项信息打印出来
zhuangzi = {'first_name':'庄','last_name':'周','age':369-286,"city":'商丘'}

#6-7  在练习6-1中，再创建两个表示人的字典，将这三个字典都存储在一个名为peple的列表中，遍历这个列表，打印每个人的所有信息
sushi = {'first_name':'苏','last_name':'轼','age':1101-1037,"city":'眉山'}
luxun = {'first_name':'周','last_name':'树人','age':1936-1881,"city":'绍兴'}

people = [zhuangzi,sushi,luxun]

for persons in people:
    first_name = persons['first_name']
    last_name = persons['last_name']
    age = persons['age']
    city = persons['city']
    print(f'{first_name}{last_name}姓{first_name}名{last_name}，终年{age}岁，祖籍{city}。')
