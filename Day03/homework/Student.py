class Student(object):
    # id 是主键,按照主键来区分每个学生的个人信息
    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender

    def __str__(self):
        return f'id:{self.id},name:{self.name},gender:{self.gender}'
