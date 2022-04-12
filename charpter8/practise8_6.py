# -*-codeing = utf-8 -*-
# @Time : 2022-04-10 8:19
# @Author : 齐物逍遥游
# @File : practise8_6.py
# @Software : PyCharm

#8-6 城市名 编写一个名为city_country()的函数，它接受城市的名称及所属的国家。
def city_country(name,country):
    city = f'"{name},{country}"'
    return city

nanjing = city_country('南京','中国')
wengehua = city_country('温哥华','加拿大')
london = city_country('伦敦','英国')
print(nanjing,wengehua,london)

