# 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象
# 使用init方法给对象添加name 和 movie属性
class star(object):
    def __init__(self,name,movie):
        self.name=name
        self.movie=movie
zhou_xing_chi=star('周星驰','功夫')
print(zhou_xing_chi.name)
print(zhou_xing_chi.movie)