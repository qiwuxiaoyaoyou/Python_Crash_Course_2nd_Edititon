# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 15:07
# @Author : 齐物逍遥游
# @File : practise10_10.py
# @Software : PyCharm

#练习10-10 常见单词  下载一本古登堡计划的txt电子书，并对其分析
#例如 利用count()方法 来确定特定的单词或短语在字符串中出现了多少次？
#编写一个程序，它读取你在古登堡计划中获取的文件，并计算单词'the' 在每个文件中分别出现了多少次
#再尝试计算'the '（包含空格）出现的次数，看看结果相差多少？
def words_count(file_name):
    try:
        with open(file_name,encoding='utf-8') as file:
            contents = file.read()
            # print(contents)
            the_count = contents.count('the')
            the_count_lower = contents.lower().count('the')
            the_count_lower_space = contents.lower().count('the ')
            print(f'包含"the"的单词数量是{the_count}个（不加空格，区分大小写）')
            print(f'包含"the"的单词数量是{the_count_lower}个（不加空格，不区分大小写）')
            print(f'包含"the"的单词数量是{the_count_lower_space}个（加空格，不区分大小写）')
    except FileNotFoundError:
        print('该文件不存在')

file_name = 'Alice in Wonderland.txt'
words_count(file_name)