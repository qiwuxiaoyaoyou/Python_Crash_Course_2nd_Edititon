# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 8:21
# @Author : 齐物逍遥游
# @File : practise4_11.py
# @Software : PyCharm

#4-11 你的书，我的书  在完成4-1练习的程序中，创建书籍列表的副本，并将其赋给变量friend_books，完成如下任务
books = ["庄子","大问题","西方哲学史","资本论","苏轼词","鲁迅杂文集"]
friend_books = books[:]  #使用完整切片来创建列表副本
print(friend_books)

#在原来的书籍列表中添加一本书
books.append("乡土中国")

#在书籍列表副本中添加一本书
friend_books.append("居民膳食指南")

#通过for循环核实有两个不同的列表
print("\n我最喜欢的书是：")
for book in books:
    print(book)

print("\n朋友最喜欢的书是：")
for friend_book in friend_books:
    print(friend_book)