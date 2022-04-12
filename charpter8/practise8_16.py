# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 15:47
# @Author : 齐物逍遥游
# @File : practise8_16.py
# @Software : PyCharm

#8-16 导入 选择一个你编写的且只包含一个函数的程序，将该函数放在另一个文件中。在主程序文件中，使用各种方法导入这个函数再调用它

# #1.
# import book
# book.favorite_book('庄子')

# #2.
# from book import favorite_book
# favorite_book('悲剧的诞生')
#
# 3.
# from book import favorite_book as fn
# fn('鲁迅杂文集')
#
# #4.
# import book as mn
# mn.favorite_book('大问题')

#5.
from book import *
favorite_book('西方哲学史')