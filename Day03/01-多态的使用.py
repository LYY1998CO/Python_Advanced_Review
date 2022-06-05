# 多态:同一个行为具有多种不同的表现形式
# 多态的条件: ① 继承关系 ② 重写父类方法 ③ 定义一个公共的方法,传入不同类的对象

# 举例:有一个动物父类,里面有一个叫的方法;定义两个子类 狗类和猫类,同样需要定义叫的方法

# 定义动物类
class Animal(object):
    # 定义call方法
    def call(self):
        print('动物在叫...')


# 定义狗类
class Dog(Animal):
    # 定义call方法
    def call(self):
        print('汪汪汪...')


# 定义猫类
class Cat(Animal):
    # 定义call方法
    def call(self):
        print('喵喵喵...')


# 定义公共的方法,传入不同的对象
def get_call(obj):
    obj.call()


# 创建动物对象
animal = Animal()
# 创建狗类对象
erha = Dog()
# 创建猫类对象
lanbai = Cat()
# 传入对象到公共方法中,就可以实现多态
get_call(animal)
get_call(erha)
get_call(lanbai)

animal.call()
erha.call()
lanbai.call()

get_call(Animal())
