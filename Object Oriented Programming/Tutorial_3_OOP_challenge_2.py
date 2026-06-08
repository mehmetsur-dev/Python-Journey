# ─────────────────────────────────────────────────────────────
# Challenge 2 — Static method
# OOP Tutorial 3 — Challenge 2: Static method & Class method
# Date: 27.05.2026
# ─────────────────────────────────────────────────────────────


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def from_string(cls, stu_string):
        name, grade = stu_string.split("-")
        return cls(name, int(grade))

    @staticmethod
    def is_passing(grade):
        if grade >= 50:
            return True
        return False


stu1 = Student("Mehmet", 85)
stu2 = Student("John", 40)

new_stu1_str = "Alex-99"
new_stu2_str = "Rose-100"
new_stu1 = Student.from_string(new_stu1_str)
new_stu2 = Student.from_string(new_stu2_str)

print(new_stu1.name, new_stu1.grade)
print(new_stu2.name, new_stu2.grade)

print(Student.is_passing(85))
print(Student.is_passing(40))
print(Student.is_passing(99))
print(Student.is_passing(100))