# 需求:将学生管理系统修改为面向对象版本
# 1. 定义学生类,初始化学生的基本信息
# 2. 定义管理系统类,实现学生的增删改查操作
# 3. 提示:面向过程版本保存学生信息是:
# `[{学生1字典},{学生2字典},{学生3字典},...]`,面向对象版保存学生信息`{学生1学号:学生1对象,学生2学号:学生2对象}`
from StudentManager import StudentManager

if __name__ == '__main__':
    studentmanager = StudentManager()
    studentmanager.sys_run()
    pass
