# 继承:子类继承父类的所有公有方法和属性
# 继承作用:提高代码的复用率,减少重复代码的书写
# 继承的语法: class 类A(类B):
# 类A是子类,类B是父类

# 需求: 有一个动物类,动物类中动物属性值,跑的方法,还有狗类,狗类继承父类的方法

# 定义动物类
class Animal(object):
    # 定义init方法添加属性
    def __init__(self):
        self.name='动物类'

    # 定义run方法
    def run(self):
        print('动物在跑...')
# 定义狗类,继承动物类
class Dog(Animal):
    pass
# 创建狗类对象
erha=Dog()
# 调用run方法
erha.run()
# 打印属性
print(erha.name)

try:
    print(1)
    pass
except Exception as e:
    print(e)
    pass