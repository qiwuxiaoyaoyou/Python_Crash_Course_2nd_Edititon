# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 15:29
# @Author : 齐物逍遥游
# @File : practise8_14.py
# @Software : PyCharm

#8-14 书籍  编写一个函数，将一本书的信息存储在字典中。这个函数总是接受作者名字及其国家（朝代），另外接受任意数量的关键字实参。
def read_book(author,country,**book_info):
    book_info['作者'] = author
    book_info['国家（朝代）'] = country
    return book_info
#调用函数时，提供必不可少的信息，以及两个名称值对。
zhuangzi = read_book('庄周',"战国",著名篇目='逍遥游',领域='美学')
#打印返回的字典，确认正确处理了所有信息
print(zhuangzi)