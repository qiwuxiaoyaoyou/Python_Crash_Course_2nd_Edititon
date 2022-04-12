# -*-codeing = utf-8 -*-
# @Time : 2022-04-09 8:51
# @Author : 齐物逍遥游
# @File : practise5_1.py
# @Software : PyCharm

#5-1 条件测试  编写至少10个测试，其中结果为True 和 False 的测试至少都有5个
#1
book = '庄子'
print('book == "庄子" 正确吗？ 我认为是正确的')
print(book == "庄子")

#2
book = 'zhuangzi'
print("\nbook == 'Zhuangzi' 正确吗？ 我认为是错误的")
print(book == 'Zhuangzi')

#3
book = None
print("\nbook == None 正确吗？ 我认为是正确的" )
print(book == None)

#4
number_one = 5
number_two = 10
print("\nnumber_1 > 10 and number_two > 5 正确吗？ 我认为是错误的")
print(number_one > 10 and number_two > 5)

#5
number_one = 5
number_two = 10
print("\nnumber_1 > 1 and number_two > 5 正确吗？ 我认为是正确的")
print(number_one > 1 and number_two > 5)

#6
books = []
print("\nbooks = None 正确吗？ 我认为是错误的")
print(books == None)

#7
world = False
print("\nworld == False 正确吗？我认为是正确的" )
print(world == False)

#8
number = 10
print('\nnumber > 10 or number <= 10 正确吗？我认为是正确的')
print(number > 10 or number <= 10)

#9
life = True
print('\nlife 正确吗？我认为是正确的')
print(life)

#10
books = ['庄子','老子']
print('\n"庄子" not in books 正确吗？我认为是错误的')
print("庄子" not in books)

#11
books = ['庄子','老子']
print("\nbooks != ['庄子','老子'] 正确吗？我认为是错误的'")
print(books != ['庄子','老子'])

'''
总结：print中可以放入一个条件句，输出的是True 或者 False
'''