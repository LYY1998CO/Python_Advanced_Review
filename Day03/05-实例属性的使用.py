# 定义狗类
class Dog(object):
    # 定义类属性
    type = '狗类'

    # 在类的内部定义对象属性
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # 在类的内部获取对象属性
    def get_name(self):
        print(self.name)


# 创建对象
erha = Dog('哈士奇', '白色')
# 类的外部获取实例(对象)属性
print(erha.name, erha.color)
# 类的外部添加对象属性
erha.gender = 'male'
print(erha.gender)
erha.get_name()
