# 私有属性:在类的内部通过两个下划线开头`__`定义的属性 `__name`;注意点:只能在类的内部定义和调用

# 需求: 去工商银行存钱,银行的名称是一个公有属性,存钱的金额私有属性

# 定义工商银行类
class ICBC(object):
    # 定义属性 init方法
    def __init__(self):
        # 定义银行名称的公有属性
        self.name='工商银行'
        # 定义存钱的私有属性
        self.__money=100000

    # 获取私有属性,可以定义一个公有的方法,里面实现获取私有属性的值
    def get_money(self):
        print(f'银行卡的余额为{self.__money}')

# 创建对象
icbc=ICBC()
print(icbc.name)
# print(icbc.__money)  # 发生报错,私有属性不能在类的外部调用
# 调用get_money方法
icbc.get_money()

# 类的外部定义一个__type,此时属性是一个公有属性
icbc.__type='银行'
print(icbc.__type)