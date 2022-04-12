# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 8:42
# @Author : 齐物逍遥游
# @File : practise8_8.py
# @Software : PyCharm

def make_film(actor,film,year=None):
    film_info = {'actor':actor,'film':film}
    #下面这两行条件测试的代码，必须要添加，否则调用函数时，无法将year的实参传入
    if year:
        film_info['year'] = year
    return film_info

#8-8 用户的电影  在练习8-7编写的程序中，编写一个while循环，让用户输入电影的主演和名称。
actor_prompt = '请输入您喜欢演员名字（输入quit可随时退出）：'
film_prompt = '请输入该演员主演的一部电影（输入quit可随时退出）：'

while True:
    actor = input(actor_prompt)
    if actor == 'quit':
        break

    film = input(film_prompt)
    if film == 'quit':
        break

# 获取这些信息后，使用它们来调用函数make_film()，并将创建的字典打印出来。
    film_info = make_film(actor, film)
    print(film_info)
#while循环务必提供正确的退出路径

'''
本练习的while循环可以考虑是否还有其他写法
'''
