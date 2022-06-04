# 定义类
class Student(object):
    # 定义__init__方法
    def __init__(self, name, age, *args, gender='男', **kwargs):
        # 初始化对象的属性值
        self.name = name
        self.age = age
        self.gender = gender
        self.classes = args[0]
        print(args)
        print(kwargs)


# 创建对象
# 如果类中有init方法,并且方法中有形参,此时创建对象时,需要在括号中传入对应的实参
xm = Student('小明', 18, 1, 2, 3)
print(xm.name, xm.age, xm.gender)

# 创建小红对象
xh = Student('小红', 16, 1, 2, 3, gender='女', a=1, b=2)
print(xh.name, xh.age, xh.gender)
print(xh.classes)

# 函数参数传递
# ①位置传参 ②关键字传参 ③默认值传参(缺省参数) ④不定长传参
