"""
案例需求:将小于房子面积的家具放到房子中,打印房子对象时输出房子的地理位置,总面积,剩余面积以及家具列表信息
案例分析步骤:
- 定义家具类
- 添加家具的初始属性值(定义`__init__`方法)
  - 家具的名称
  - 家具的占地面积
- 定义房子类
- 添加房子的初始属性值(定义`__init__`方法)
  - 房子的地理位置
  - 房子的总面积
  - 房子的初始剩余面积(等于房子的总面积)
  - 房子中添加的家具列表(初始值为空列表)
- 定义添加家具方法
  - 传入家具对象,获取家具的名称和占地面积
  - 房子剩余面积和占地面积做比较,判断是否能将此家具放到房子中
  - 更新房子剩余面积
- 定义`__str__`方法,实现打印房子对象输出房子的基本信息
"""
# 定义家具类
class Furniture(object):
    # 定义init方法,添加家具的属性
    def __init__(self,name,area):
        # 添加家具名称
        self.name=name
        # 添加家具占地面积
        self.area=area
    def __repr__(self):
        return f"{self.name}"

# 定义房子类
class House(object):
    # 定义init方法,添加房子的属性
    def __init__(self,address,area):
        """
               初始化房子的属性
               :param address: 房子位置
               :param area: 房子总面积
               """
        # 添加房子总面积
        self.total_area=area
        # 添加房子的位置属性
        self.address=address
        # 添加房子的家具列表
        self.furnitures=[]
        # 添加房子的初始剩余面积,初始的剩余面积等于总面积
        self.free_area=area

    # 定义添加家具的方法(获取家具的名称,占地面积)
    # 传入对象名参数,实际上就等同于函数中传入函数名参数
    def add_furniture(self,ft):
        #通过房子剩余面积和家具的占地面积进行判断
        # 房子剩余面积大于等于家具占地面积,添加家具,更新房子剩余面积
        # ft.area 实际上就是在类的外部获取对象的属性 对象名.属性名
        if self.free_area>=ft.area:
            # self.furnitures.append(ft.name)
            self.furnitures.append(ft)
            # 更新房子剩余面积 = 房子剩余面积 - 家具的占地面积
            self.free_area-=ft.area
        # 房子剩余面积小于家具占地面积,提示用户房子太小,换房
        else:
            print('房子太小了，可以考虑换一个大点的房子了...')

    # 定义str方法,输出房子的基本信息
    def __str__(self):
        return f'房子的地理位置{self.address},房子的总面积为{self.total_area},' \
               f'房子的剩余面积为{self.free_area},房子中的家具有{self.furnitures}'

# 定义房子对象
house=House('宝安区',120)
# 定义家具对象
bed=Furniture('双人床',4)
# 添加家具
# 调用房子的添加家具方法
house.add_furniture(bed)
print(house)
sofa=Furniture('沙发',8)
house.add_furniture(sofa)
print(house)