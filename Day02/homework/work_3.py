# 1. 创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来...`
# 2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
#    1. run方法输出 `跑起来....`
#    2. eat 方法输出 `吃东西...`
# 3. 创建一个 SwiftHorse（千里马）类继承Horse类，初始化init方法name属性为千里马
class Animal(object):
    def run(self):
        print('跑起来...')

    pass


class Horse(Animal):
    def eat(self):
        print('吃东西...')


class SwiftHorse(Horse):
    def __init__(self):
        self.name = '千里马'


if __name__ == '__main__':
    S = SwiftHorse()
    S.run()
    S.eat()
    print(S.name)
    pass
