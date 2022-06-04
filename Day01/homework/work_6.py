# 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象
#
# 使用init方法给对象添加属性
#
# 删除创建的对象，打印“我不喜欢xxx了”
class star(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print(f'我不喜欢{self.name}了')

zhou_xing_chi=star('周星驰')
del zhou_xing_chi