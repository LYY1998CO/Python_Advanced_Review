# a.定义一个Star类(明星类)，包含初始化init方法：
# 成员属性：明星姓名 明星的电影
# 成员方法：playing()
# 打印：“xxx出演了yyy，非常好看”
# 打印对象时显示“xxx是我的偶像，我非常喜欢他的电影yyy”
# 程序运行结束时提示“xxx我不再喜欢了”
# xxx为明星姓名，yyy是电影的名字
# b.键盘循环输入五个Star对象的姓名和电影名。
# c.分别调用输入Star对象的playing方法和打印对象
class star(object):
    def __init__(self,name,movie):
        self.name=name
        self.movie=movie
        pass
    def playing(self):
        print(f'{self.name}出演了{self.movie}，非常好看')
        pass
    def __str__(self):
        return f'{self.name}是我的偶像，我非常喜欢他的电影{self.movie}'
        pass
    def __del__(self):
        print(f'{self.name}我不再喜欢了')

list1=[]
for i in range(5):
    name=input('请输入明星的姓名:')
    movie=input('请输入明星出演的电影名称:')
    s1=star(name,movie)
    list1.append(s1)
for i in  list1:
    i.playing()
    print(i)
