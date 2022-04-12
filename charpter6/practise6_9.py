# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 15:51
# @Author : 齐物逍遥游
# @File : practise6_9.py
# @Software : PyCharm

#6-9 喜欢的地方  创建一个字典，其中用三个人的名字用作键，并存储每个人喜欢的1~3个地方
favorite_places = {
    '庄子': ['宇宙'],
    '苏轼': ['黄州','杭州','儋州'],
    '文豪': ['南京','南通'],
    }

for name,places in favorite_places.items():
    print(f'\n{name}最喜欢的地方是:')
    for place in places:
        print(f'{place}')