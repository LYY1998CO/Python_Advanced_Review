# 类属性:类的属性,在类的内部方法之外定义的属性(类属性名=值)
# 获取类属性: ①类名.类属性名 ②对象名.类属性名
# 通过当前类创建出来的多个对象的类属性值相同

# 需求:有一个狗类,可以通过狗类创建出两个对象(二哈,哮天犬),两个对象的type都是狗类

# 定义狗类
class Dog(object):
    # 定义类属性 type
    type = '狗类'

    # 定义对象属性
    def __init__(self, name):
        self.name = name


# 创建对象
erha = Dog('哈士奇')
xtq = Dog('哮天犬')
# 获取类属性
print(Dog.type)
# 获取对象中的类属性值
print(erha.type)
print(xtq.type)

# 如何修改类属性? 只能通过 类名.类属性名 = 新值
Dog.type = '修改了类属性'
print(Dog.type)
erha.type = '再次修改类属性'
print(Dog.type)
# 获取二哈对象的type属性
print(erha.type)
# 获取哮天犬对象的type属性
print(xtq.type)
