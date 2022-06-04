"""
案例需求:
根据地瓜被烤的时间确定地瓜当前的状态,同时还可以给地瓜添加调料,最后打印地瓜对象输出地瓜烤的时间,当前状态以及添加的调料信息
0-3分钟：生的
3-5分钟：半生不熟
5-8分钟：熟的
超过8分钟：烤糊了

步骤分析:
- 定义地瓜类
- 添加地瓜的初始属性值(定义`__init__`魔法方法)
  - 被烤的初始时间为0
  - 地瓜的初始状态为生的
  - 初始添加的调料为空列表
- 定义烤地瓜的方法
  - 输入烤地瓜的时间,更新当前的地瓜被烤的总时间
  - 根据总时间进行判断,修改地瓜的当前状态
- 定义添加调料的方法
  - 输入要使用的调料,将调料添加到调料列表中
- 定义`__str__`魔法方法,打印地瓜对象时输出地瓜的基本信息
"""
# 定义地瓜类
class Potato(object):
    # 添加地瓜属性值,定义init魔法方法,在创建对象时才会执行
    def __init__(self):
        self.total_time=0 # 地瓜烤的总时间,初始为0
        self.status='生的' # 地瓜的初始状态,生的
        self.condiments=[] # 保存添加的调料

    # 定义烤地瓜的方法
    def cook(self,time):
        # 更新烤地瓜的总时间
        self.total_time+=time
        # 根据总时间判断地瓜的烤的状态
        if 0<=self.total_time<3:
            self.status='生的'
        elif 3<=self.total_time<5:
            self.status='半生不熟的'
        elif 5<=self.total_time<8:
            self.status='熟的'
        else:
            self.status='烤糊了'

    # 定义添加调料的方法
    def add_condiment(self,condiment):
        # 将调料保存到调料列表中
        self.condiments.append(condiment)

    # 定义str魔法方法
    def __str__(self):
        return f'地瓜烤了{self.total_time}分钟，当前的状态为{self.status},添加的调料为{self.condiments}'

# 创建对象
digua=Potato()
# 烤地瓜
digua.cook(2)
# 添加调料
digua.add_condiment('糖')
print(digua)

# 继续烤地瓜
digua.cook(5)
digua.add_condiment('番茄酱')
print(digua)