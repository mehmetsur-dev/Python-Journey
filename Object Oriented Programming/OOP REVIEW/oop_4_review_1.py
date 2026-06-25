# Day 50 - OOP Review Topic 4: Inheritance
# Concepts: child classes, super(), method overriding, add_reports


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    
class Developer(Employee):
    def __init__(self, name, salary, language='Python'):
        super().__init__(name, salary)
        self.language = language


class Manager(Employee):
    def __init__(self, name, salary, reports=None):
        super().__init__(name, salary)

        if reports is None:
            self.reports = []

        else:
            self.reports = reports

    def add_reports(self, report):
        self.reports.append(report)


emp1 = Manager('Cat', 10000000)
emp2 = Employee('Dog', 10000)

emp1.add_reports(emp2)
print(emp1.reports)