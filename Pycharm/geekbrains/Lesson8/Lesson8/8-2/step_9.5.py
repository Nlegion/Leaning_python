class StudentLayoffError(Exception):
    pass


class User:
    def __init__(self, name, age, gender=None, inn=None):
        self._name = name
        self._age = age
        self._gender = gender
        self._inn = inn

    def __str__(self):
        return f'{self._name}'


class Student(User):
    def __init__(self, name, age, gender=None, inn=None,
                 student_id=None):
        super().__init__(name, age, gender, inn)
        self._student_id = student_id
        self._group = None
        self._level = None
        # self._attrs = {'имя': name, 'возраст': age}  # bad

    def __str__(self):
        return f'студент {self._name} (группа {self._group._name})'

    def _get_student_id(self):
        return self._student_id

    def _set_student_id(self, val):
        # validator
        self._student_id = val

    def _delete_student_id(self):
        del self._student_id

    student_id = property(_get_student_id, _set_student_id, _delete_student_id)

    # @property
    # def student_id(self):
    #     return self._student_id
    #
    # @student_id.setter
    # def student_id(self, val):
    #     # validator
    #     self._student_id = val
    #
    # @student_id.deleter
    # def student_id(self):
    #     del self._student_id

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, val):
        # validator
        self._group = val


class Teacher(User):
    def __init__(self, name, age, gender=None, inn=None,
                 subject=None, salary=None):
        super().__init__(name, age, gender, inn)
        self._subject = subject
        self._salary = salary


class StudentGroup:
    student_type = Student

    def __init__(self, name, faculty=None):
        self._name = name
        self._faculty = faculty
        self._students = {}
        self.__idx = 0
        self.__series = None

    @classmethod
    def _student_type_validator(cls, student):
        if not isinstance(student, cls.student_type):
            raise TypeError(f'wrong student type: {type(student)}')

    def enroll(self, student):
        # if isinstance(student, Student):
        # if not isinstance(student, self.student_type):
        #     raise TypeError(f'wrong student type: {type(student)}')
        self._student_type_validator(student)
        self._students[student.student_id] = student
        student.group = self

    def layoff(self, student):
        try:
            del self._students[student.student_id]
            student.group = None
        except Exception as e:
            raise StudentLayoffError(f'student layoff failed: {e}')

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self, value):
        # validate
        self._faculty = value

    def __str__(self):
        return f'{self._name}, обучается {len(self._students)} студентов'

    # def __getitem__(self, student):
    #     self._student_type_validator(student)
    #     return self._students.get(student.student_id)

    def __getitem__(self, student_id):
        return self._students.get(student_id)  # O(1)

    def __iter__(self):
        self.__idx = 0
        self.__series = list(self._students.values())
        return self
        # return iter(self._students.values())

    def __next__(self):
        if self.__idx < len(self._students):
            self.__idx += 1
            return self.__series[self.__idx - 1]
        raise StopIteration


def user_code():
    student_1 = Student('Иванов Иван', age=18, student_id=123789)
    student_2 = Student('Петров Петр', age=19, student_id=789123)
    student_3 = Student('Сергеев Сергей', age=18, student_id=456789)
    student_4 = Student('Данилов Данил', age=18, student_id=456321)
    teacher_1 = Teacher('Романов Роман', age=30, subject='Физика', salary=19000)
    student_group_1 = StudentGroup('ФМ-205', faculty='Физмат')
    student_group_2 = StudentGroup('М-208', faculty='Физмат')
    student_group_1.enroll(student_1)
    student_group_1.enroll(student_2)
    student_group_2.enroll(student_3)
    student_group_1.enroll(student_4)

    print(student_group_1)
    print(student_group_2)

    for student in student_group_1:
        print(student)
    #
    # for student in student_group_2:
    #     print(student)

    # for student in student_group_1._students.values():  # bad -> property .students
    #     print(student)


if __name__ == '__main__':
    try:
        user_code()
    except Exception as e:
        print(e)
