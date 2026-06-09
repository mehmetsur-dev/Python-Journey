import random

# ==========================================
# Day 22 - OOP Challenge 2
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
        print(f"Hi, I'm {self.name}, {self.age} years old")
        print(f"My course is {self.course}")
        print(f"ID: <{self.id}>")

    def study(self, subject):
        print(f"{self.name} is studying {subject} today.")

    def graduate(self):
        print(f"Congratulations {self.name}! You have graduated from {self.course}.")


stu1 = student("Mehmet Sur", 21, "Python")
stu2 = student("Alex Axe", 25, "Math")

stu1.intro()
stu2.intro()

stu1.study("Algorithms")
stu2.study("Calculus")

stu1.graduate()
stu2.graduate()