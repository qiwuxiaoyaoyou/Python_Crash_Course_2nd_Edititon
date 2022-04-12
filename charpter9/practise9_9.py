# -*-codeing = utf-8 -*-
# @Time : 2022-04-11 7:08
# @Author : 齐物逍遥游
# @File : practise9_9.py
# @Software : PyCharm

#9-9  在本节最后一个 electric_car.py版本中，给 Battery类添加一个名为 upgrade_battery()的方法。
#该方法检查电瓶容量，如果它不是100，就将它设置为 100 。
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,milege):
        if milege >= self.odometer_reading:
            self.odometer_reading = milege
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"This car doesn't need a gas tank!")

class Battery:

    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}--kwh battery.')

    def get_range(self):
        '''打印一条消息，支出点评的续航里程。'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = '?'
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        '''检查电瓶容量，如果它不是100，就将它设置为 100'''
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()  #此处可以向Battery传递实参，从而修改Battery类中的属性battery_size的值

# 创建一辆电瓶容量为默认值的电动汽车，调用方法 get_range()，
my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 然后对电瓶进行升级，并再次调用 get_range()。你将看到这辆汽车的续航里程增加了
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()