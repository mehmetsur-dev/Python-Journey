# =============================================================
# OOP TUTORIAL 3 — classmethods & staticmethods
# Mehmet's Python Journey | Day 24
# Reference file: read this whenever you forget how these work
# =============================================================

# ─────────────────────────────────────────────────────────────
# QUICK REMINDER: 3 types of methods in a class
# ─────────────────────────────────────────────────────────────
#
#  Method type      | First param | Has access to
# ─────────────────────────────────────────────────────────────
#  Instance method  |  self       | instance variables + class variables
#  Class method     |  cls        | class variables only (NOT instance vars)
#  Static method    |  (nothing)  | neither — just a normal function inside the class
# ─────────────────────────────────────────────────────────────


import datetime  # We need this for the static method example below


# ─────────────────────────────────────────────────────────────
# THE EMPLOYEE CLASS — used in all examples below
# ─────────────────────────────────────────────────────────────

class Employee:

    # Class variable (shared by all employees)
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Instance variables (unique to each employee)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # ─────────────────────────────────────────────────────────
    # 1) INSTANCE METHOD  (you already know this from Tutorial 1)
    # ─────────────────────────────────────────────────────────
    # - Has "self" as first parameter
    # - Can access instance variables (self.first, self.pay, etc.)
    # - Can also access class variables (self.raise_amount)

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # ─────────────────────────────────────────────────────────
    # 2) CLASS METHOD  ← NEW in Tutorial 3
    # ─────────────────────────────────────────────────────────
    # - Use the @classmethod decorator above the def
    # - Has "cls" as first parameter (cls = the class itself, like Employee)
    # - Can only access class variables, NOT instance variables
    #
    # MOST COMMON USE CASE: alternative constructor
    #   → a second way to create an Employee object
    #   → instead of always doing Employee("Mehmet", "Yilmaz", 5000)
    #     you can parse a string like "Mehmet-Yilmaz-5000" directly

    @classmethod
    def set_raise_amount(cls, amount):
        # This changes the raise_amount for ALL employees at once
        # cls.raise_amount is the same as Employee.raise_amount
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # ALTERNATIVE CONSTRUCTOR — creates an Employee from a string
        # emp_str looks like: "Mehmet-Yilmaz-5000"
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))  # cls(...) = Employee(...)
        # Why "cls" instead of "Employee"?
        # Because if someone creates a subclass (child class) of Employee,
        # cls will refer to THAT subclass automatically. More flexible!

    # ─────────────────────────────────────────────────────────
    # 3) STATIC METHOD  ← NEW in Tutorial 3
    # ─────────────────────────────────────────────────────────
    # - Use the @staticmethod decorator above the def
    # - NO "self" or "cls" — it receives NO automatic first argument
    # - It's basically a regular function that lives inside the class
    # - Put it in the class because it's LOGICALLY RELATED to it,
    #   but it doesn't actually need any instance or class data to work
    #
    # EXAMPLE: checking if a date is a workday
    # This is related to Employee work schedules,
    # but it doesn't need to know anything about a specific employee

    @staticmethod
    def is_workday(day):
        # day.weekday() returns:
        #   0 = Monday, 1 = Tuesday, ..., 4 = Friday, 5 = Saturday, 6 = Sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False  # It's a weekend
        return True  # It's a workday


# =============================================================
# RUNNING THE EXAMPLES
# =============================================================

# ── Create employees the normal way ──
emp_1 = Employee('Mehmet', 'Yilmaz', 5000)
emp_2 = Employee('Ali', 'Demir', 6000)

print("=== Regular instance method ===")
print(emp_1.fullname())      # Mehmet Yilmaz
print(emp_2.fullname())      # Ali Demir

# ── classmethod: change raise for ALL employees ──
print("\n=== classmethod: set_raise_amount ===")
print(f"Before: {Employee.raise_amount}")   # 1.04
Employee.set_raise_amount(1.10)             # Call on the CLASS (not instance)
print(f"After:  {Employee.raise_amount}")   # 1.10 — changed for everyone
print(f"emp_1 also sees: {emp_1.raise_amount}")  # 1.10 — yes, same!

# You can also call it on an instance, but convention is to use the class name:
# emp_1.set_raise_amount(1.10)  ← works but looks weird

# ── classmethod: from_string — alternative constructor ──
print("\n=== classmethod: from_string (alternative constructor) ===")
emp_str_1 = 'Fatima-Ozturk-7000'
emp_str_2 = 'Kemal-Arslan-8500'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)

print(emp_3.fullname())   # Fatima Ozturk
print(emp_3.pay)          # 7000
print(emp_4.email)        # Kemal.Arslan@company.com

# ── staticmethod: is_workday ──
print("\n=== staticmethod: is_workday ===")
my_date = datetime.date(2026, 5, 25)   # Monday
print(f"{my_date} → workday? {Employee.is_workday(my_date)}")   # True

my_date2 = datetime.date(2026, 5, 24)  # Sunday
print(f"{my_date2} → workday? {Employee.is_workday(my_date2)}")  # False

# You can also call static methods on an instance (but using the class name is cleaner):
# emp_1.is_workday(my_date)  ← works, but Employee.is_workday(my_date) is better style


# =============================================================
# KEY QUESTION TO ASK YOURSELF (always remember this!)
# =============================================================
#
#  Do I need a specific employee's data (name, pay)?
#      → instance method  (use self)
#
#  Do I need something about ALL employees or the class itself?
#      → classmethod  (use cls)
#      → most common example: alternative constructor
#
#  Is this function just logically related to Employee,
#  but doesn't actually need any employee data?
#      → staticmethod  (no self, no cls)
#
# =============================================================
# DECORATORS — quick note
# =============================================================
# @classmethod and @staticmethod are called DECORATORS.
# A decorator is a special word starting with @ that you put
# directly above a function to change how it behaves.
# You will learn much more about decorators later in the course.
# For now, just remember:
#   @classmethod   → method works on the CLASS
#   @staticmethod  → method is a regular function inside the class
# =============================================================

print("\n=== All done! OOP Tutorial 3 complete ===")