# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 8:28
# @Author : 齐物逍遥游
# @File : practise8_7.py
# @Software : PyCharm

#8-7 电影 编写一个名为make_film()的函数，创建一个描述电影的字典。该函数应接受主演的名字和电影名，并返回包含上述信息的字典。
# def make_film(actor,film):
#     film_info = {'actor':actor,'film':film}
#     return film_info
#
# # 使用这个函数创建三个表示不同电影的字典，并打印每个返回的值，核实是否正确。
# gump = make_film('汤姆·汉克斯','阿甘正传')
# longmao = make_film('龙猫','龙猫')
# bullet_fly = make_film('姜文','让子弹飞')
# print(gump,longmao,bullet_fly)

#给函数make_film()添加一个默认值None为可选形参，以便存储电影包含的年份。如果调用这个函数时制定了年份，就添加至该字典中
#调用这个函数，并至少在一次调用中制定电影包含的年份
def make_film(actor,film,year=None):
    film_info = {'actor':actor,'film':film}
    #下面这两行条件测试的代码，必须要添加，否则调用函数时，无法将year的实参传入
    if year:
        film_info['year'] = year
    return film_info

gump = make_film('汤姆·汉克斯','阿甘正传')
longmao = make_film('龙猫','龙猫',year=1988)
bullet_fly = make_film('姜文','让子弹飞')
print(gump,longmao,bullet_fly)