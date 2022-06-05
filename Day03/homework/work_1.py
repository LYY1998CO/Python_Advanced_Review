# 定义一个 Animal 类，类中有方法，eat 和 run
# eat 方法中输出  正在吃饭
# run 方法中输出  正在奔跑
# 定义一个类 Dog 类，继承自 Animal。并实现自己的 eat 方法，在自己的eat 方法中输出 啃骨头，
# 但是在啃骨头之前，要再去调用父类中的方法 eat 方法， 在使用 Dog 对象 去调用 eat 方法的时候，输出结果如下
# 正在吃饭
# 啃骨头
class Animal(object):
    def run(self):
        print('正在奔跑')
    def eat(self):
        print('正在吃饭')
class Dog(Animal):
    def eat(self):
        super().eat()
        # super(Dog, self).eat()
        print('啃骨头')

dog=Dog()
dog.eat()