# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 20:29
# @Author : 齐物逍遥游
# @File : practise7_10.py
# @Software : PyCharm

#7-10 梦想的度假胜地  编写一个程序，调查用户梦想的独家胜地。
responses = {}
#设置一个标志，指出调查是否继续
active = True

while active:
    #提示输入被调查者的名字和回答？
    name = input('\n怎么称呼您？')
    place = input('你最想去哪里度假呢？')
    #将回答存储在字典responses中，其中name为键，place为值
    responses[name] = place
    #是否愿意介绍给别人参与调查
    repeat = input('你愿意介绍给他人参与我们的调查吗？（yes/no）')
    if repeat == 'no':
        active = False

print('\n以下为调查结果：\n')
for name,place in responses.items():
    print(f'{name}最想要去的度假胜地是{place}')
