"""
return:在函数可以使用return(一般情况函数都是有return)
作用:
① 可以返回函数的返回值给函数调用处, 函数名() = 返回值的内容
② 函数遇到return就停止运行
注意点:
①有return,并且return后边有值, 函数名() = return后边的值
②没有return或者return后边没有任何内容, 函数名() = None
"""
def func01():
    print('func01...')
    return 120
# func01()
# print(func01())
# func01()
print(func01())