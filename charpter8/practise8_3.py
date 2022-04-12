# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 21:00
# @Author : 齐物逍遥游
# @File : practise8_3.py
# @Software : PyCharm

#8-3 T恤 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子，概要地说明T恤的尺码和字样
def make_shirt(size,text):
    print(f'这件T恤的尺码是{size},上面写着"{text}"')
#使用位置实参调该函数来制作一件T恤，再使用关键字实参来调用这个函数

make_shirt(165,'shit')  # 位置实参调用函数
make_shirt(text='人生苦短，我要学python',size='xl')     #关键字实参调用函数