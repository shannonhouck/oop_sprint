"""
A module for handling school students related information
"""


class Student(object):
    """Basic student class"""

    def __init__(self, name, ID, GPA, status):
        self.name = name
        self._GPA = GPA     # single underscore == protected
        self.__ID = ID      # double underscore == private
        self.status = status

    def get_GPA(self):
        return self._GPA

    def set_GPA(self, GPA):
        self._GPA = GPA

    def __str__(self):
        return "Student Name " + self.name


class GradStudent(Student):
    """A graduate student which inherits stuff from the student class"""

    def __init__(self, name, ID, GPA):
        super().__init__(name, ID, GPA, 'Grad')

    def is_pass(self):
        return self.get_GPA() >= 3.0

    def set_advisor(self, advisor):
        self._advisor = advisor

    def get_advisor(self):
        return self._advisor


class UndergradStudent(Student):
    """An undergraduate student which inherits stuff from the student class"""

    def __init__(self, name, ID, GPA):
        super().__init__(name, ID, GPA, 'Undergrad')

    def is_pass(self):
        return self.get_GPA() >= 2.0
