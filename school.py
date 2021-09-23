#add studesnt and teacher
#all student teacher return

from Models.Teacher import Teacher
from Models.Student import Student

class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def addTeacher(self, teachars:Teacher):
        self.teachers.append(teachars)

    def addStudents(self, students:Student):
        self.students.append(students)

    def allTeachers(self):
        return self.teachers

    def allStudents(self):
        return self.students


