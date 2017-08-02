"""
A module for handling school students related information
"""


class Student(object):
    """Basic student class"""

    def __init__(self, name, ID, GPA):
        self.name = name
        self._GPA = GPA     # protected
        self.__ID = ID      # private

    def get_GPA(self):
        return self._GPA

    def set_GPA(self, GPA):
        self._GPA = GPA

    def __str__(self):
        return "Student Name " + self.name
