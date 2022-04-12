# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 11:29
# @Author : 齐物逍遥游
# @File : practise6_3.py
# @Software : PyCharm

#6-3 词汇表  Python字典可以用于模拟现实生活中的字典，可称为“词汇表”

#想出你学过的5个编程术语，将其用作词汇表中的键，并将它们的含义作为值存储在词汇表中
glossary = {
    'python':'一种计算机语言，以简洁著称',
    '列表':'由一系列按特定顺序排列的元素组成，符号为[]',
    'remove()':'python中的一种方法，可以将列表中某个元素移除',
    'for循环':'python中一种循环方式，可以遍历序列元素',
    'if循环':'判断语句，可以对条件进行判断对错',
    }

#6-4 词汇表2 用遍历字典的方式 输出6-3练习中的键和值
for key,value in glossary.items():
    print(f'{key}:{value}')