from Student import Student


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def add_student(self):
        id = int(input('请输入新增学生的ID:'))
        name = input('请输入新增学生的姓名:')
        gender = input('请输入新增学生的性别:')
        stu = Student(id, name, gender)
        self.student_list.append(stu)
        print('执行新增操作成功...')
        pass

    def del_student(self):
        del_id = int(input('请输入待删除学生的ID:'))
        for i in self.student_list:
            if i.id == del_id:
                self.student_list.remove(i)
                print(f'执行删除操作成功,且删除的学生的信息为:{i}')
                break
        else:
            print('没有在本系统中查询到您所输入的学生的ID，无法执行此操作，请谅解..')
        pass

    def mod_student(self):
        mod_id = int(input('请输入待更新学生的ID:'))
        for i in self.student_list:
            if i.id == mod_id:
                i.id = int(input('请输入更新后学生的ID:'))
                i.name = input('请输入更新后学生的姓名:')
                i.gender = input('请输入更新后学生的性别:')
                print(f'执行更新操作操作成功')
                break
        else:
            print('没有在本系统中查询到您所输入的学生的ID，无法执行此操作，请谅解..')
        pass

    def sel_student(self):
        sel_id = int(input('请输入待查询学生的ID:'))
        for i in self.student_list:
            if i.id == sel_id:
                print(f'执行查询操作成功,且查询到的学生的信息为:{i}')
                break
        else:
            print('没有在本系统中查询到您所输入的学生的ID，无法执行此操作，请谅解..')
        pass

    def save_student(self):
        with open('./student.txt','w',encoding='utf-8') as f:
            new_list=[i.__dict__ for i in self.student_list]
            f.write(str(new_list))
        print('保存数据成功...')
        pass

    def tra_student(self):
        for i in self.student_list:
            print(i)
        pass

    def load_data(self):
        try:
            f=open('student.txt','r',encoding='utf-8')
        except:
            f=open('student.txt','w',encoding='utf-8')
        else:
            content=f.read()
            if not content:
                return
            data=eval(content)
            self.student_list=[Student(i['id'],i['name'],i['gender']) for i in data]
        finally:
            print('加载数据成功...')
            f.close()
        pass
    @staticmethod
    def show_menu():
        print('' * 40)
        print('1.添加学生信息')
        print('2.删除学生信息')
        print('3.修改学生信息')
        print('4.查询学生信息')
        print('5.遍历学生信息')
        print('6.保存学生信息')
        print('7.退出学生信息管理系统')
        print('' * 40)
        pass

    def sys_run(self):
        print('欢迎使用本学生信息管理系统   V2.0')
        self.load_data()
        while True:
            self.show_menu()
            fun_number = int(input('请输入您要选择的功能选项:'))
            if fun_number == 1:
                self.add_student()
            elif fun_number == 2:
                self.del_student()
            elif fun_number == 3:
                self.mod_student()
            elif fun_number == 4:
                self.sel_student()
            elif fun_number == 5:
                self.tra_student()
            elif fun_number == 6:
                self.save_student()
            elif fun_number == 7:
                print('感谢您使用本学生信息管理系统....')
                break
            else:
                print('您所输入的功能选项不合法，请您重新输入！')
        pass

    pass
