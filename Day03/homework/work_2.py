# 定义一个 Bank 类， 有属性， name 和 money，name 是共有属性，money是私有属性，
# 根据 Bank 类，创建一个 ICBC 对象，
# 完成三次 存钱操作， 第一次 存入 100  第二次 存入 1000 第三次 存入 10000
# 存完之后，最终输出 总共当前 的 ICBC 中 有多少钱。
class Bank(object):
    def __init__(self, name):
        self.name = name
        self.__money = 0

    def save_money(self, money):
        self.__money += money
        print('存钱成功...')

    def print_money(self):
        print(f'当前的{self.name}的总余额为：{self.__money}')


ICBC = Bank('工商银行')
ICBC.save_money(100)
ICBC.print_money()
ICBC.save_money(1000)
ICBC.print_money()
ICBC.save_money(10000)
ICBC.print_money()
