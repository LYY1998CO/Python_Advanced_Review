# 类属性和对象属性重名时,只能通过 类名.属性名 方式进行调用
# 定义类
class Dog(object):
    # 定义类属性
    type = '狗类'

    # 定义对象(实例)属性
    def __init__(self):
        self.type = '二哈'


# 创建对象
erha = Dog()
# 获取类属性
print(Dog.type)
# 获取对象属性
print(erha.type)
