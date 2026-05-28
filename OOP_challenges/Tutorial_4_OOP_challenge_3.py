


class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.first} {self.last}")


class Student(Person):
    def __init__(self, first, last, age, student_id, grades=None):
        super().__init__(first, last, age)
        self.student_id = student_id

        if grades is None:
            self.grades = []
        else:
            self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    def __init__(self, first, last, age, subject, students=None):
        super().__init__(first, last, age)
        self.subject = subject

        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        self.students.append(student)

    def print_roster(self):
        print(f"Teacher: {self.first} {self.last} | Subject: {self.subject}")
        for student in self.students:
            print(f"  - {student.first} {student.last} | Avg: {student.average_grade()}")


st1 = Student("Ali", "Veli", 20, "S001")
st1.add_grade(90)
st1.add_grade(85)

st2 = Student("Mehmet", "Sur", 21, "S002")
st2.add_grade(99)
st2.add_grade(80)

st3 = Student("John", "Smith", 23, "S003")
st3.add_grade(40)
st3.add_grade(50)

teacher1 = Teacher("Sarah", "Connor", 35, "Python")
teacher1.add_student(st1)
teacher2 = Teacher("Lara", "Golds", 33, "Java")
teacher2.add_student(st2)
teacher3 = Teacher("Alex", "Buns", 40, "C++")
teacher3.add_student(st3)
print("----------------------------------------")
teacher1.print_roster()
print("----------------------------------------")
teacher2.print_roster()
print("----------------------------------------")
teacher3.print_roster()
print("----------------------------------------")