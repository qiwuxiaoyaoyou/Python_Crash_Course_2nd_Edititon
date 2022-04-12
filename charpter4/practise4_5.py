# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 7:37
# @Author : 齐物逍遥游
# @File : practise4_5.py
# @Software : PyCharm
import time


#4-5 一百万求和  创建一个包含1~1000000的列表，再使用min()和max()函数何时该列表。另外对这个列表调用sum()函数,
#               看看python将100万个数相加需要多长时间。
numbers = list(range(1,1000001))
print(min(numbers))

print(max(numbers))

time_start=time.time()
print(sum(numbers))
time_end=time.time()
print('totally cost',time_end-time_start)