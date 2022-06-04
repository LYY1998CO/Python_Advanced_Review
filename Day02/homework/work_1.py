# 1. 创建一个Animal（动物）基类,其中有一个run方法,输出`跑起来....`
# 2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
#    1. run方法输出 `跑起来....`
#    2. eat 方法输出 `吃东西...`
class Animal(object):
    def run(self):
        print('跑起来...')


class Horse(Animal):
    def eat(self):
        print('吃东西....')


if __name__ == '__main__':
    h1 = Horse()
    h1.run()
    h1.eat()
