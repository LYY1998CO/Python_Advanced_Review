# 添加属性: 对象名.属性名 = 值
# 获取属性: 对象名.属性名

# 定义类
class Student(object):
    # 定义方法
    def study(self):
        print('好好学习')


# 创建对象
xm = Student()
# 添加对象属性
xm.name = '小明'
xm.age = 18
# 获取对象属性
print(xm.name)

# 创建xh对象
xh = Student()
xh.name = '小红'
print(xh.name)
xh.study()
