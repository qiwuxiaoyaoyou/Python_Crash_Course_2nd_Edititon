# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 13:21
# @Author : 齐物逍遥游
# @File : practise10_5.py
# @Software : PyCharm

#10-5 调查  编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所以原因的文件中
file_name = 'program_survey.txt'
results = []

while True:
    answer_one = input('\n你为什么喜欢编程呢：')
    results.append(answer_one)

    answer_two = input('你愿意帮我们邀请其他人参与本调查吗（yes/no):')
    if answer_two == 'no':
        break


with open(file_name,'a',encoding='utf-8') as file:
    for result in results:
        file.write(f'{result}\n')
