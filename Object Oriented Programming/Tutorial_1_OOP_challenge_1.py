
import random

# ==========================================
# Day 22 - OOP Challenge 1
# Topic: Classes, __init__, instance methods
# Date: 25/05/2026
# ==========================================

class student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.id = random.randint(1000000, 2000000)

    def intro(self):
        print(f"Hi, I'm {self.name}, {self.age} Years old")
        print(f"My course is, {self.course}")
        print(f"ID: <{self.id}>")
        

stu1 = student("Mehmet Sur", 21, "Python")

stu2 = student("Alex Axe", 25, "Math")


stu1.intro()
stu2.intro()