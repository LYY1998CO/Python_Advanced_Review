# 定义一个`Person` 类,包含初始化 init 方法:
# 实例属性: 名字, name  年龄, age
# 1. 记录由该类创建的对象的个数,创建一个对象,计数+1, 删除一个对象,计数减一
# 2. 定义一个方法,可以打印当前对象的个数
# 3. 定义一个方法`show_info`, 输出以下信息
# 这是一个 Person 类,谢谢查看!
# 4. 打印对象的时候,可以输出打印自己的名字和年龄
# 我的名字是 xxx, 年龄是 xxx
# 5. 定义一个方法 `study`, 输出以下信息
# 我叫 xxx, 我要好好学习
# 6. 操作步骤
# 1. 调用`show_info `方法
# 2. 创建两个对象, 打印当前对象,并打印当前的对象个数
# 3. 分别使用两个对象调用`study`方法
# 4. 删除一个对象,打印输出当前的对象个数
class Person(object):
    obj_count = 0

    def __init__(self, name, age):
        Person.obj_count += 1
        self.name = name
        self.age = age
        print(f'当前创建的对象个数为{self.obj_count}个')

    @classmethod
    def show_info(self):
        print('这是一个 Person 类,谢谢查看!')

    def __str__(self):
        return f'我的名字是 {self.name}, 年龄是 {self.age}岁'

    def study(self):
        print(f'我叫 {self.name}, 我要好好学习')

    def __del__(self):
        Person.obj_count -= 1
        print(f'当前创建的对象个数为:{self.obj_count}个')


Person.show_info()
ming = Person('小明', 23)
print(ming)
# print(f'当前的对象个数为{ming.obj_count}个')
ming.study()
wang = Person('小王', 24)
print(wang)
# print(f'当前的对象个数为{wang.obj_count}个')
wang.study()
del ming
# print(f'当前的对象个数为{Person.obj_count}个')
del wang
# print(f'当前的对象个数为{Person.obj_count}个')
