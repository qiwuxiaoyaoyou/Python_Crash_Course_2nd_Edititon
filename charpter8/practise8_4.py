# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 21:09
# @Author : 齐物逍遥游
# @File : practise8_4.py
# @Software : PyCharm

#8-4 大号T恤  修改函数make_shirt(),使其默认状态下制作一件印有'I love Python'字样的大号T恤。
# 调用这个函数来制作：一件默认字样的大号T恤，一件印有默认字样的中号T恤，一件印有其他字样的T恤（尺码无所谓）

def make_shirt(size='xxl',text="I love Python"):
    print(f'这件衬衫的规则为{size},上面印着"{text}"')

#一件默认字样的大号T恤
make_shirt()

#一件印有默认字样的中号T恤
make_shirt(size='xl')

#一件印有其他字样的T恤（尺码无所谓）
make_shirt(size='l',text='shit')
