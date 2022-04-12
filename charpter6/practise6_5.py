# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 15:06
# @Author : 齐物逍遥游
# @File : practise6_5.py
# @Software : PyCharm

#6-5 河流 创建一个字典，在其中存储三条重要河流及其流经的国家。
rivers = {
    '巴西':'亚马逊河',
    '埃及':'尼罗河',
    '中国':'长江',
    }

#使用循环为每条河流打印一条消息
for county,river in rivers.items():
    print(f'{river}流经{county}')

print('-'*30)
#使用循环将该字典中每条河流的名字打印出来
for river in rivers.values():
    print(river)

print('-'*30)
#使用循环将该字典包含的每个国家的名字打印出来
for county in rivers.keys():
    print(county)