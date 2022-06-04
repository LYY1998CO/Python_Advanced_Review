# 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象
#
# 使用init方法给对象添加属性
#
# print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"
#
# xxx为明星姓名，yyy是电影的名字
class star(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def __str__(self):
        return f'{self.name}是我的偶像，我非常喜欢他的电影{self.movie}'


zhou_xing_chi = star('周星驰', '功夫')
print(zhou_xing_chi)
