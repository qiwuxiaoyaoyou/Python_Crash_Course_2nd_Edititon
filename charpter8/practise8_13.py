# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 15:16
# @Author : 齐物逍遥游
# @File : practise8_13.py
# @Software : PyCharm

#8-13 用户简介  复制本章节的程序user_profile.py，在其中调用build_profile()来创建有关某个人的简介。
# 调用这个函数时，指定这个人的名和姓，以及三个描述这个人的键值对
def build_profile(first,last,**user_info):
    '''创建一个字典，其中包含我们知道的有关用户的一切'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# user_profile = build_profile('albert','einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)

#这里在传入键值对的时候，键可以是中文
zhuangzi = build_profile('庄','周',
                         学派='道家',
                         思想='逍遥',
                         国家='宋国蒙')
print(zhuangzi)