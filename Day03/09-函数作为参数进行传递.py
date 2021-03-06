# 函数:可以实现特定功能的一段代码,并且是被定义的
# 函数参数:定义函数传参时,可以将函数名(内存地址)作为参数传递
# print(函数名) ===> 内存地址
# 函数名() ===> 执行内存地址中保存的代码

# 需求:定义两个函数,第二个函数实现调用第一个函数的功能

# 定义第一个函数
def func01():
    print('func01...')


# 定义第二个函数
def func02(func):
    print('func02...')
    # 调用第一个函数
    func()


# print(func01)# <function func01 at 0x0000027EC1A65948>
#  调用函数时,传入实参
# func02(func01)
print(func01())
