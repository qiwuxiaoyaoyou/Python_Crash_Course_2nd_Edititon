# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 18:28
# @Author : 齐物逍遥游
# @File : practise2_5.py
# @Software : PyCharm

#2-5 名言 找一句你钦佩的名人说的名言，将其姓名和名言打印出来。
famous_person = "庄子"
famous_saying = "吾以天地为棺椁，以日月为连璧，星辰为珠玑，万物为送賷。吾葬具岂不备邪？"
print(f'{famous_person}说过："{famous_saying}"')       #3.5之前写法
print('{}说过："{}"'.format(famous_person,famous_saying))  #3.6以后写法
