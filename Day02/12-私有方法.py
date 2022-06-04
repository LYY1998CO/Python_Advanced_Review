# 私有方法: 定义方法时以两个下划线开头`__方法名(self)`,注意点:只能在类的内部调用

# 需求: 有一个ICBC类,初始化属性,银行的名字公有属性,存款的金额私有属性,定义一个私有方法,用来更新存款的金额,打印最新银行卡余额

# 定义ICBC类
class ICBC(object):
    # 定义init方法,初始化属性值
    def __init__(self):
        self.name = '工商银行'
        self.__money = 10000  # 私有属性

    # 定义存钱的私有方法,更新存款
    def __set_money(self, money):
        self.__money += money

    # 定义一个公有方法,里面调用私有方法
    def set_money(self, money):
        self.__set_money(money)

    # 获取私有属性的值
    def get_money(self):
        print(f'银行卡的最新余额为{self.__money}')


# 创建对象
icbc = ICBC()
# icbc.__set_money()  # 私有方法只能在类的内部调用
# 存钱
icbc.set_money(10000)
# 打印银行卡余额
icbc.get_money()
icbc.set_money(1000000000)
icbc.get_money()
