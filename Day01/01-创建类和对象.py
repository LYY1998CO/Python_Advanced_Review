"""
创建类通过 class 关键字进行创建
创建类语法: class 类名(object):
在类中可以创建属性和方法
类名要遵从标识符命名规则
"""


# 定义类
class Student():
    # 定义方法(行为)
    def study(self):
        print('好好学习，天天向上...')

    def play(self):
        print('学习完了，可以玩耍了....')


# 创建对象 对象名 = 类名()
xm = Student()
# 调用对象中的方法 对象名.方法名()
xm.study()
xm.play()
print(xm)
# 一个类中可以创建多个对象
xh = Student()
xh.study()
print(xh)  # 打印对象的内存地址(十六进制的)
print(id(xh))  # 转换成十进制的内存地址
