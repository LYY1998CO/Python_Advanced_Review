# 需求:统计通过狗类创建出来的对象的个数,打印 对象时输出创建了几个对象

"""
需求分析:
①定义类
②+1, 初始的统计值 num = 0(没有创建对象) num+=1
③每次创建对象 执行 num+=1, init魔法方法(创建对象时自行执行)
④定义str魔法方法 return后跟 创建了几个对象
"""


# 定义类
class Dog(object):
    # 定义初始统计类属性 num = 0
    num = 0

    # 定义init初始方法
    def __init__(self):
        Dog.num += 1

    # 定义str魔法方法
    def __str__(self):
        return f'创建了{Dog.num}个对象'


# 创建第一个对象
erha = Dog()
print(erha)
# 创建第二个对象
xtq = Dog()
print(xtq)
# 创建第三个对象
zangao = Dog()
print(zangao)
