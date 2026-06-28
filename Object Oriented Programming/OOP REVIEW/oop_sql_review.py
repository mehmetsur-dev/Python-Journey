# Day 53 - OOP + SQL Combined Review
# Student Registry Challenge
# Topics: classes, @property, @classmethod, __str__, class variables


class Student:
    total_students = 0

    def __init__(self, name, age, grade=0):
        self.name = name
        self.age = age
        self.grade = grade
        Student.total_students += 1

    @classmethod
    def set_string(cls, string):
        name, age, grade = string.split(",")
        return cls(name, int(age), int(grade))
     
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        if value < 0:
            raise ValueError("Not Valid")
        elif value > 100:
            raise ValueError("Not Valid")
        self._grade = value
        
    def __str__(self):
        return f"{self.name} (age {self.age}) - Grade: {self.grade}"

        
    
