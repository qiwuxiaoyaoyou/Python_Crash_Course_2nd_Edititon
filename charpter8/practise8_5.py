#8-5  城市 编写一个名为 describe_city()的函数，接受一座城市的名字，以及该城市所属的国家。
#  这个函数应打印一个简单的句子。 给用于存储国家的形参指定默认值
def describe_city(name,country='中国'):
    print(f'{name}属于{country}')

#为三座不同的城市调用这个函数，其中至少有一座城市不属于默认国家

describe_city('南京')
describe_city('上海')
describe_city('温哥华',country='加拿大')