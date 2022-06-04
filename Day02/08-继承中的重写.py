# 重写：在子类中定义了和父类同名的方法或者属性，再通过子类对象调用此方法或者属性时，调用的就是子类自己的属性或者方法

# 需求：一个动物类，里面动物名称为“动物”，还有叫的方法， 还有一个狗类，继承动物类，狗类的名称是 二哈，叫的方法汪汪汪

# 定义动物类
class Animal(object):
    # 定义init方法
    def __init__(self):
        self.name = '动物类'

    # 定义call方法
    def call(self):
        print('动物在叫...')


# 定义狗类，继承动物类
class Dog(Animal):
    # 定义init方法
    def __init__(self):
        self.name = '二哈'

    # 定义call方法
    def call(self):
        print('汪汪汪....')


# 创建狗类对象
erha = Dog()
print(erha.name)
erha.call()
