# 多继承:子类继承多个父类

# 需求:一个徒弟有多个师傅,继承师傅的方法以及独家秘方

# 第一个父类 Master
class Master(object):
    # 定义init方法,初始化属性
    def __init__(self):
        self.kongfu_master = ['麻辣']

    # 定义制作煎饼的方法
    def cook_cake_master(self):
        print('hello')
        print(f'使用了{self.kongfu_master}技术制作煎饼')

# 第二个父类 School
class School(object):
    # 定义init方法,初始化属性
    def __init__(self):
        self.kongfu_school = ['番茄']

    # 定义制作煎饼的方法
    def cook_cake_school(self):
        print(f'使用了{self.kongfu_school}技术制作煎饼')


# 定义子类
# 多继承中如果父类出现同名方法或者属性,默认继承子类括号中第一个父类
class Prentice(School,Master):
    pass

# 创建子类对象
tudi=Prentice()
# 获取属性
# print(tudi.kongfu_master)   # 发生报错,init方法同名,只能初始化第一个父类中init方法的属性
print(tudi.kongfu_school)
# 调用方法
tudi.cook_cake_school()
tudi.cook_cake_master() # 发生报错,调用了此方法,但是此方法中没有kongfu_master属性


