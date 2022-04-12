# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 7:50
# @Author : 齐物逍遥游
# @File : practise4_8.py
# @Software : PyCharm

#4-8 立方  创建一个列表，其中包含整数1~10的立方，再使用for循环将这些立方数打印出来

numbers = []
for number in range(1,11):
    numbers.append(number**3)
print(numbers)

for number in numbers:
    print(number)