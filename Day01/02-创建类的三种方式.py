# 方式一: class 类名:
# 定义类
# class Student:
#     def study(self):
#         print('好好学习...')
#  # 创建对象
# xm=Student()
# xm.study()
# Student().study()

# 方式二:class类名():
# class Student():
#     def study(self):
#         print('好好学习')
# xm=Student()
# xm.study()

# 方式三:class 类名(object):
class Student(object):
    def study(self):
        print('哈哈')


xm = Student()
xm.study()
