class User:
    def show_name(self):
        raise NotImplementedError('write own implementation "show_name" method')


class Teacher(User):
    pass


teacher_1 = Teacher()
teacher_1.show_name()

