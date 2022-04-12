# -*-codeing = utf-8 -*-
# @Time : 2022-04-08 21:47
# @Author : 齐物逍遥游
# @File : practise3_8.py
# @Software : PyCharm

#3-8 放眼世界 想出至少5个你渴望去旅游的地方。

#1.将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
cities = ['sanya','xiamen','dalian','liugongdao','canada','europe']

#2.按原始排列顺序打印该列表
print(cities)

#3.使用sorted()按字母顺序打印这个列表，同时不要修改它。
print(sorted(cities))  #sorted只是临时改变列表的顺序

#4.再次打印该表，确定顺序没有变化
print(cities)

#5.使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它
print(sorted(cities,reverse=True))

#6.再次打印该表，确定顺序没有变化
print(cities)

#7.使用reverse()修改列表元素的排列顺序。打印核实
cities.reverse()  #不能直接对这个进行打印
print(cities)

#8.使用reverse()再次修改列表元素的排列顺序。打印核实
cities.reverse()
print(cities)

#9.使用sort()修改该列表，使其元素按字母顺序排列，打印核实
cities.sort()
print(cities)

#10.使用sort()修改该列表，使其元素按字母相反顺序排列，打印核实
cities.sort(reverse=True)
print(cities)


"""
总结：
sorted()是函数，用于列表后返回的是列表；
sort是方法，采用列表.sort()的形式调用
"""