# =============================================================================
# OOP TUTORIAL 4 - INHERITANCE: CREATING SUBCLASSES
# Corey Schafer Series | Reference Script by Mehmet
# Day 24 → Day 25 | Topic: Inheritance
# =============================================================================
# WHAT IS INHERITANCE?
# Inheritance lets a new class (subclass/child) take on all the attributes
# and methods of an existing class (superclass/parent).
# This allows you to reuse code and add/override only what's different.
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
# 1. THE BASE (PARENT) CLASS
# ─────────────────────────────────────────────────────────────────────────────

class Employee:
    """The parent class. All subclasses will inherit from this."""

    raise_amount = 1.04  # 4% raise — class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"


# ─────────────────────────────────────────────────────────────────────────────
# 2. CREATING A SUBCLASS (Basic Inheritance)
# ─────────────────────────────────────────────────────────────────────────────

class Developer(Employee):
    """
    Developer inherits EVERYTHING from Employee.
    The (Employee) in the class definition means: "inherit from Employee".
    Even with an empty body, Developer already has __init__, fullname, apply_raise, etc.
    """
    pass


dev1 = Developer("Ali", "Veli", 50000)
dev2 = Developer("Mehmet", "Yilmaz", 60000)

print("─── Basic Inheritance ───")
print(dev1.email)       # inherited from Employee
print(dev1.fullname())  # inherited from Employee
print(dev1)             # inherited __repr__ from Employee


# ─────────────────────────────────────────────────────────────────────────────
# 3. METHOD RESOLUTION ORDER (MRO)
# ─────────────────────────────────────────────────────────────────────────────
# Python uses MRO to decide which class to look in first.
# Order: Developer → Employee → object (built-in base of all classes)
# Use help() to see the full MRO and inherited methods.

print("\n─── MRO (Method Resolution Order) ───")
print(Developer.__mro__)
# OR: help(Developer)  # ← shows full breakdown


# ─────────────────────────────────────────────────────────────────────────────
# 4. OVERRIDING A CLASS VARIABLE IN THE SUBCLASS
# ─────────────────────────────────────────────────────────────────────────────
# We can override raise_amount just for Developer without touching Employee.

class Developer(Employee):
    raise_amount = 1.10  # Developers get a 10% raise instead of 4%

dev1 = Developer("Ali", "Veli", 50000)
emp1 = Employee("Anna", "Smith", 50000)

print("\n─── Overriding Class Variable ───")
print(f"Developer raise amount : {Developer.raise_amount}")   # 1.10
print(f"Employee  raise amount : {Employee.raise_amount}")    # 1.04  (unchanged)

dev1.apply_raise()
print(f"Dev1 pay after raise   : {dev1.pay}")   # 55000 (10%)

emp1.apply_raise()
print(f"Emp1 pay after raise   : {emp1.pay}")   # 52000 (4%)


# ─────────────────────────────────────────────────────────────────────────────
# 5. ADDING NEW ATTRIBUTES TO THE SUBCLASS WITH __init__ + super()
# ─────────────────────────────────────────────────────────────────────────────
# When Developer needs extra attributes (like prog_lang), we write our own
# __init__. But we DON'T want to copy-paste Employee's __init__ logic.
# → Use super().__init__() to let the parent handle the shared part.

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)   # Employee handles: first, last, pay, email
        self.prog_lang = prog_lang           # Developer adds: prog_lang

dev1 = Developer("Ali", "Veli", 50000, "Python")
dev2 = Developer("Mehmet", "Yilmaz", 60000, "JavaScript")

print("\n─── super().__init__() ───")
print(dev1.email)       # still works — set by Employee.__init__ via super()
print(dev1.prog_lang)   # new attribute — set by Developer.__init__
print(dev2.prog_lang)


# ─────────────────────────────────────────────────────────────────────────────
# 6. A SECOND SUBCLASS — Manager
# ─────────────────────────────────────────────────────────────────────────────
# Manager also inherits from Employee and adds its own attribute: employees list.

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Never use a mutable object (like a list) as a default parameter!
        # Use None and handle it inside the method instead.
        self.employees = employees if employees is not None else []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"  → {emp.fullname()}")


dev1 = Developer("Ali", "Veli", 50000, "Python")
dev2 = Developer("Mehmet", "Yilmaz", 60000, "JavaScript")

mgr1 = Manager("Sarah", "Connor", 90000, [dev1])

print("\n─── Manager Subclass ───")
print(mgr1.fullname())    # inherited
print(mgr1.email)         # inherited

print("Manager's team:")
mgr1.print_emps()

mgr1.add_emp(dev2)
print("After adding dev2:")
mgr1.print_emps()

mgr1.remove_emp(dev1)
print("After removing dev1:")
mgr1.print_emps()


# ─────────────────────────────────────────────────────────────────────────────
# 7. isinstance() and issubclass()
# ─────────────────────────────────────────────────────────────────────────────
# isinstance(obj, Class)   → Is this object an instance of Class (or its subclasses)?
# issubclass(Sub, Parent)  → Is Sub a subclass of Parent?

print("\n─── isinstance() and issubclass() ───")

print(isinstance(mgr1, Manager))    # True  — mgr1 is a Manager
print(isinstance(mgr1, Employee))   # True  — Manager inherits from Employee
print(isinstance(mgr1, Developer))  # False — Manager is NOT a Developer

print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Employee))    # True
print(issubclass(Manager, Developer))   # False


# ─────────────────────────────────────────────────────────────────────────────
# 8. OVERRIDING A METHOD IN THE SUBCLASS
# ─────────────────────────────────────────────────────────────────────────────
# You can completely override a parent method, or extend it with super().

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        # Extending the parent's __repr__ concept but adding prog_lang
        return f"Developer('{self.first}', '{self.last}', {self.pay}, '{self.prog_lang}')"


dev1 = Developer("Ali", "Veli", 50000, "Python")
emp1 = Employee("Anna", "Smith", 50000)

print("\n─── Overriding __repr__ ───")
print(dev1)   # Developer('Ali', 'Veli', 50000, 'Python')
print(emp1)   # Employee('Anna', 'Smith', 50000)


# =============================================================================
# SUMMARY — KEY CONCEPTS FROM TUTORIAL 4
# =============================================================================
# ┌─────────────────────────────────────────────────────────────────────────┐
# │  CONCEPT                  SYNTAX / RULE                                 │
# ├─────────────────────────────────────────────────────────────────────────┤
# │  Define subclass          class Sub(Parent):                            │
# │  Inherit everything       just use (Parent) — even empty body works     │
# │  MRO                      Sub → Parent → object  (use help() to check)  │
# │  Override class var       redefine it in the subclass                   │
# │  Add new attributes       write __init__ in subclass + super().__init__ │
# │  super()                  delegates to the parent class automatically   │
# │  Mutable default param    use None, assign [] inside __init__           │
# │  Override a method        redefine the method in the subclass           │
# │  isinstance(obj, Class)   checks if obj is instance of Class or child   │
# │  issubclass(Sub, Parent)  checks if Sub inherits from Parent            │
# └─────────────────────────────────────────────────────────────────────────┘
# =============================================================================