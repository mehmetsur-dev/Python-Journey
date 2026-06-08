# ============================================================
# OOP Class Variables — Challenge 1
# Topic: Class variables, instance variables, methods
# Day 23 — Corey Schafer OOP Tutorial 2
# Author: Mehmet Sur
# Date: 26.05.2026
# ============================================================

class student:
    school_name = "Parlak"
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        student.total_students += 1

    def show_info(self):
        print(f"{self.name} - Grade: {self.grade}, School: {self.school_name}")

    def apply_bonus(self, bonus):
        self.grade = self.grade + bonus

stu1 = student("Mehmet Sur", 85)
stu2 = student("Will Stones", 90)

print(f"Total Student: {student.total_students}")

stu1.show_info()
stu2.show_info()

print(stu1.grade)     # Before bonus
stu1.apply_bonus(15)  # After bonus
print(stu1.grade)