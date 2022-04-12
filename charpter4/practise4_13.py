# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 8:41
# @Author : 齐物逍遥游
# @File : python4_13.py
# @Software : PyCharm

#4-13  图书馆  有一家图书馆，可提供五本书的免费阅读。想出五本书，并将其存储在一个元组中

books = ('庄子','苏轼词','鲁迅杂文集','西方哲学史','悲剧的诞生')

#使用一个for循环将该图书馆提供免费阅读的五本书打印出来
for book in books:
    print(book)

#尝试修改其中的一个元素，核实Python会拒绝
#books[-1] = '查拉图斯特拉如是说'   #TypeError: 'tuple' object does not support item assignment

#图书馆修改了免费阅读的树木，替换了其中两本书籍。请给元组变量赋值，并用for 循环 将新元组的每个元素打印出来
print("-"*30)

books = ('庄子','鲁迅杂文集','西方哲学史','大问题','资本论')
for book in books:
    print(book)