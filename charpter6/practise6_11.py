# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 16:09
# @Author : 齐物逍遥游
# @File : practise6_11.py
# @Software : PyCharm

#6-11 城市 创建一个名为cities的字典，将三个城市名用作键。没做城市都创建一个字典，包含如国家、人口等信息，并打印出来
cities = {
    'nanking':{
        'country':'China',
        'provience':'jiangsu',
        'centre':'qinhuai',
        },
    'shanghai':{
        'country':'China',
        'provience':'shanghai',
        'centre':'jingan',
        },
    'nantong':{
        'country':'China',
        'provience':'jiangsu',
        'centre':'chongchuan',
        },
    }

for name,facts in cities.items():
    print(f'\n这座城市的名字是{name}')
    country = facts['country']
    provience = facts['provience']
    centre = facts['centre']
    print(f'它属于{country} {provience},它的中心是{centre}')
