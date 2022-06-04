# 定义类
class Student(object):
    # 定义对象方法
    def study(self):
        print(f'self的值是{self}')
        print('好好学习，月薪过万')


# 创建对象
xm = Student()
xm.study()
print(xm)

xh = Student()
xh.study()
print(xh)
