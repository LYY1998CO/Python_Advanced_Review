# __init__():在创建对象时,会自动的执行此方法中的代码,可以给对象初始化的属性值
# 注意点:__init__()魔法方法可以传参

# 定义类
class Student(object):
    # 定义魔法方法 __init__
    def __init__(self):
        print('我是init魔法方法，我被执行了...')
        # 添加对象的属性,初始化对象属性
        self.name = '小明'
        self.age = 18
        self.gender = '男'


# 创建对象
xm = Student()
print(xm.name, xm.age)

# 创建xh对象
xh = Student()
print(xh.name)
print(xh.age)
