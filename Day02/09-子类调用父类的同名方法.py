# 父类名.方法名(self):如果修改了父类的名称,子类中同时需要修改父类名
# super(子类名,self).方法名() 或者 super().方法名(): 避免修改了父类名,再浪费时间修改子类中的父类名

# 需求:一个动物类父类, 添加动物属性name, 定义动物的call方法; 定义狗类子类,定义call方法,在输出自己的方法之前,调用父类的call方法

# 定义动物类父类
class Animal(object):
    # 定义init方法
    def __init__(self):
        self.name = '动物类'

    # 定义call方法
    def call(self):
        print('动物在叫...')


# 定义狗类子类
class Dog(Animal):
    def __init__(self):
        self.name = '二哈'

    # 定义call方法
    def call(self):
        # 调用父类的call方法
        # ① 父类名.方法名(self)
        # Animal.call(self)
        # ② super(子类名,self).方法名()
        # super(Dog, self).call()
        # ③ super().方法名()
        super().call()
        print('汪汪汪....')


# 创建狗类对象
erha = Dog()
erha.call()
