class Dog(object):
    # 定义类属性
    type = '狗类'

    # 定义类方法
    @classmethod
    def show_type(cls):
        print(f'type的值为{Dog.type}')
        print(f'type的值为{cls.type}')


# 创建对象
erha = Dog()
# 调用类方法
# ① 对象名.类方法名()
erha.show_type()
# ② 类名.类方法名()
Dog.show_type()
