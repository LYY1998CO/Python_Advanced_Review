# 继承中的私有权限:子类只能继承父类的公有属性和方法,不能继承私有的属性和方法

# 需求: 一个动物的父类,里面有两个属性,一个name公有属性,一个type私有属性, 两个方法, 一个eat公有方法,一个sleep方法
# 再创建一个狗类的子类,继承父类中的方法和属性

# 定义动物类
class Animal(object):
    # 定义属性
    def __init__(self):
        self.name = '动物类'
        self.__type = '私有属性'

    # 定义eat方法
    def eat(self):
        print('动物在吃东西')

    # 定义sleep私有方法
    def __sleep(self):
        print('动物在睡觉...')

    # 定义一个公有的方法,获取私有属性和调用私有方法
    def get_type_sleep(self):
        print(f'获取了父类中的私有属性:{self.__type}')
        self.__sleep()


# 定义狗类
class Dog(Animal):
    pass


# 创建狗类对象
erha = Dog()
print(erha.name)
# print(erha.__type)    # 发生报错,不能继承父类的私有属性
erha.eat()
# erha.__sleep()    # 发生报错,不能继承父类的私有方法
erha.get_type_sleep()
