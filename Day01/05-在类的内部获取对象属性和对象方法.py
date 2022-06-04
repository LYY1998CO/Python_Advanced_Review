# 在类的内部获取对象方法和对象属性,需要用到self参数

# 定义类
class Student(object):
    # 定义方法
    # 此时在对象方法中获取对象属性,通过 self.name
    def study(self):
        print(f'{self.name}好好学习,月薪过万....')

    def play(self):
        # 需求:玩的前提是要先学习完,调用study方法
        # 语法:self.方法名()
        self.study()
        print('学习完了，可以玩耍了')


# 创建对象
xm = Student()
# 添加对象属性
xm.name = '小明'
print(xm.name)
xm.study()

# 调用play方法
# 在调用play方法时,先执行7行代码,在类的内部调用对象方法
xm.play()
