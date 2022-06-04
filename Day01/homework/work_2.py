# 定义一个`Star`类(明星类)， 通过明星类创建一个zhou_xing_chi对象
# 给对象添加属性
# 明星姓名= “周星驰”
# 明星的电影 = “功夫”
class Star(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie
zhou_xing_chi=Star('周星驰','功夫')
print(zhou_xing_chi.name)
print(zhou_xing_chi.movie)
