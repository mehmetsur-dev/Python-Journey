# ─────────────────────────────────────────────────────────────
# Challenge 1 — Static method
# OOP Tutorial 3 — Challenge 1: Static method
# Date: 27.05.2026
# ─────────────────────────────────────────────────────────────

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @staticmethod
    def is_passing(grade):
        if grade >= 50:
            return True
        return False


stu1 = Student("Alex", 60)
stu2 = Student("Mehmet", 45)

print(stu1.is_passing(60))
print(stu2.is_passing(45))
