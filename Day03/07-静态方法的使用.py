# 静态方法:通过 @staticmethod 装饰器装饰的方法,并且方法中没有默认参数,但是可以有其他的参数
# 静态方法调用: 通过类或者对象来调用

# 需求: 小明学习很努力,培训完之后,找到了月薪两万的工作, 通过静态方法打印小明的工资

# 定义类
class Student(object):
    # 定义init方法
    def __init__(self, name):
        self.name = name

    # 定义静态方法,打印小明工资
    @staticmethod
    def salary(money):
        print(f'小明的工资是{money}')

# 创建对象
xm = Student('小明')
# 调用静态方法
# ①类名.方法名
Student.salary(1000)
# ②对象名.方法名
xm.salary(10000)
