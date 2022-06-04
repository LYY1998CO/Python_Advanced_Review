# 多继承:子类继承多个父类

# 需求:一个徒弟有多个师傅,继承师傅的方法以及独家秘方

# 第一个父类 Master
class Master(object):
    # 定义init方法,初始化属性
    def __init__(self):
        self.kongfu = ['麻辣']

    # 定义制作煎饼的方法
    def cook_cake(self):
        print(f'使用了{self.kongfu}技术制作煎饼')

    def cook_potato_master(self):
        print('烤地瓜master')


# 第二个父类 School
class School(object):
    # 定义init方法,初始化属性
    def __init__(self):
        self.kongfu = ['番茄']

    # 定义制作煎饼的方法
    def cook_cake(self):
        print(f'使用了{self.kongfu}技术制作煎饼')

    def cook_potato_school(self):
        print('烤地瓜school')


# 定义子类
# 多继承中如果父类出现同名方法或者属性,默认继承子类括号中第一个父类
class Prentice(School, Master):
    pass


# 创建子类对象
tudi = Prentice()
# 获取属性
print(tudi.kongfu)
# 调用方法
tudi.cook_cake()
tudi.cook_potato_school()
tudi.cook_potato_master()
