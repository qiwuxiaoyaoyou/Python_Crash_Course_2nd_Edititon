# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 7:21
# @Author : 齐物逍遥游
# @File : pracitse4_1.py
# @Software : PyCharm

#4-1 书籍 想出至少三本你喜欢的书籍，并将其名称存储在一个列表中国，再使用for循环打印
books = ["庄子","大问题","西方哲学史","资本论","苏轼词","鲁迅杂文集"]
for book in books:
    print(book)

#修改这个for循环，使其打印包含书名的句子，每本书显示一行
print('-'*30)
for book in books:
    print("我很喜欢这本《{}》".format(book))

#在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢看书。
print("我很喜欢阅读！")


