# 多层继承:类A=>类B=>类C=>类D,有一个继承顺序链,最底层的类可以继承前边所有类的公有属性和方法

# 需求: 第一个类动物类,属性和方法; 第二个狗类,继承第一个类;第三个二哈类,继承第二个类

# 定义动物类
class Animal(object):
    def __init__(self):
        self.name='动物类'
    def sleep(self):
        print('动物在睡觉...')

# 定义狗类
class Dog(Animal):
    def __init__(self):
        self.name='狗类'
    def eat(self):
        print('啃骨头...')

# 定义二哈类
class ErHa(Dog):
    def __init__(self):
        self.name='二哈'
    def call(self):
        print('汪汪汪...')


# 创建二哈类对象
erha=ErHa()
print(erha.name)
erha.eat()
erha.sleep()
erha.call()


# 创建狗类对象
dog=Dog()
dog.sleep()


# 打印继承顺序链 类名.__mro__
print(ErHa.__mro__)
