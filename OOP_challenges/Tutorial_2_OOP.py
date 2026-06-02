# Class Variables vs Instance Variables
# There are two kinds of variables in a class:
# Instance variables → belong to each object individually
# Class variables → belong to the class itself, shared by all objects


class Employee:
    # CLASS VARIABLE — shared by all employees
    company_name = "TechCorp"
    raise_amount = 1.04  # 4% raise
    employee_count = 0

    def __init__(self, name, salary):
        # INSTANCE VARIABLES — unique to each employee
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

emp1 = Employee("Mehmet", 50000)
emp2 = Employee("Ali", 60000)

print(Employee.company_name)    # TechCorp
print(emp1.company_name)        # TechCorp

print(Employee.employee_count)  # 2

print(emp1.salary)   # 50000  — before raise
emp1.apply_raise()
print(emp1.salary)   # 52000  — after raise ✅