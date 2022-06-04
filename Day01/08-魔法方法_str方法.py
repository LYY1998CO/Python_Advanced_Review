"""
__str__(self): 打印对象名 print(对象名),如果定义了str魔法方法,输出方法中返回(return)的字符串内容(返回值的类型str),
否则输出对象的内存地址;
执行 print(str(对象名)) 代码时,也是会调用此魔方方法,输出方法中返回的字符串内容,否则就是普通的类型转换
作用:在打印对象名,输出对象的一些默认信息
注意点:魔法方法中必须要有返回值(return),返回值的类型必须是字符串类型
"""


# 定义类
class Student(object):
    # 定义init方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义str魔法方法
    def __str__(self):
        print('hello world')
        # pass # 没有返回值是发生报错  TypeError: __str__ returned non-string (type NoneType)
        # return 11  # 返回值必须是字符串类型 TypeError: __str__ returned non-string (type int)
        return f'我的名字叫{self.name},今年{self.age}岁'

# 创建对象
xm = Student('小明', 18)
print(xm) # 定义了str魔法方法,此时打印的结果就是返回值的内容

xh = Student('小红', 20)
print(xh)
print(type(xh))

# 调用str()方法,类型转换方法,如果定义了__str__魔法方法,此时打印的就是此方法中的返回值内容,
# 否则就是普通的字符串类型转换
print(str(xh))
print('-' * 40)
print(type(str(xh)))
