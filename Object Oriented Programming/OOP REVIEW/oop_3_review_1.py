# Day 49 - OOP Review Topic 3: @classmethod and @staticmethod
# Concepts: class methods with cls, static methods, alternative raise logic
# Challenge: Employee class with set_raise classmethod and is_valid_salary staticmethod


class Employee:
    raise_percentage = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        return self.salary * self.raise_percentage
    
    @classmethod
    def set_raise(cls, amount):
        cls.raise_percentage = amount

    @staticmethod
    def is_valid_salary(salary):
        if salary > 0:
            return True
        return False
        

emp1 = Employee("John", 300000)
emp2 = Employee("Clara", 200000)

print(emp1.salary)
print(emp2.salary)

print(emp1.is_valid_salary(100000))
print(emp2.is_valid_salary(0))

Employee.set_raise(1.10)

new_salary = emp1.apply_raise()
print(new_salary)