# 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象
#
# 使用init方法给对象添加属性
#
# 定义方法playing()，打印“xxx出演了yyy，非常好看”
class star(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def playing(self):
        print(f'打印{self.name}出演了{self.movie}，非常好看')


zhou_xing_chi = star('周星驰', '功夫')
zhou_xing_chi.playing()
