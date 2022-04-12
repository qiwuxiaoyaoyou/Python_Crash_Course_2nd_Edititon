# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 20:58
# @Author : 齐物逍遥游
# @File : practise3_3.py
# @Software : PyCharm

#3-3 自己的列表 创建一个包含多种通勤方式的列表，并创建一系列有关这些通勤方式的宣言。

commuter_ways = ["自行车","步行","地铁","出租车","自驾","高铁"]
for commuter_way in commuter_ways:
    announcement = f"我比较喜欢的通勤方式是{commuter_way}"
    print(announcement)