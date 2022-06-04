# __repr__(self): 执行 print([对象名1,对象名2,...]) 代码时,打印此魔法方法中返回的字符串内容,否则打印的就是对象的内存地址
# 作用:答应对象列表时,列表中输出对象的一些信息
# 注意点: 必须要有返回值,返回值的类型必须是字符串类型

# 定义类
class Student(object):
    # 定义init方法
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f'我叫{self.name}'
    def __repr__(self):
        # pass  # 一定要有返回值
        # return 13.23  # 返回值类型必须是字符串类型
        return f'我叫{self.name}'


# 创建对象
xm = Student('小明')
xh = Student('小红')

# 定义一个空列表
list1 = []
list1.append(xm)
list1.append(xh)
print(list1)  # 如果没有定义__repr__魔法方法,输出的结果就是对象内存地址的列表

# 当定义了__str__魔法方法时,不再定义__repr__魔法方法,执行以下两行代码,此时输出的对象的信息
# for i in list1:
#     print(i)
