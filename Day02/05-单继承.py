# 单继承:子类继承了一个父类

# 需求: 做煎饼果子,有一个师傅会做煎饼果子,收了一个徒弟,把做煎饼果子的方法传给了弟子

# 定义父类
class Master(object):
    # 添加父类的属性值
    def __init__(self):
        self.kongfu=['麻辣','番茄']

    # 定义做煎饼的方法
    def cook_cake(self):
        print(f'使用{self.kongfu}技术做了煎饼')


# 定义子类
# 单继承就是子类括号中只有一个父类
class Prentice(Master):
    pass


# 定义对象
tudi=Prentice()
tudi.cook_cake()