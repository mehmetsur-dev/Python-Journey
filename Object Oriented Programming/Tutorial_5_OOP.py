# ============================================================
# MAGIC / DUNDER METHODS - Complete Walkthrough
# Corey Schafer OOP Tutorial 5
# ============================================================

# Dunder = "Double UNDERscore" → __like_this__
# These methods are called automatically by Python in certain situations.
# You don't call them directly — Python calls them for you behind the scenes.


# ── 1. THE PROBLEM WITHOUT DUNDER METHODS ───────────────────

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

emp1 = Employee("Mehmet", "Yilmaz", 50000)

print(emp1)
# Output: <__main__.Employee object at 0x...>   ← useless!
# Python doesn't know HOW to display your object, so it shows the memory address.


# ── 2. __repr__ — "Official" String Representation ──────────
# Goal: unambiguous, meant for DEVELOPERS / debugging
# Rule of thumb: should look like code you could paste to recreate the object
# Python calls this automatically when you type the object in the REPL,
# or when there is no __str__ defined.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    def __repr__(self):
        # Looks like valid Python code → developer-friendly
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

emp1 = Employee("Mehmet", "Yilmaz", 50000)
print(repr(emp1))   # Employee('Mehmet', 'Yilmaz', 50000)
print(emp1)         # Also uses __repr__ because __str__ is not defined yet


# ── 3. __str__ — "Informal" String Representation ───────────
# Goal: readable, meant for END USERS
# Python calls this automatically with print() and str()
# If __str__ is missing → Python falls back to __repr__

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.first} {self.last} — Salary: {self.pay} €"

emp1 = Employee("Mehmet", "Yilmaz", 50000)

print(str(emp1))    # Mehmet Yilmaz — Salary: 50000 €   ← __str__
print(repr(emp1))   # Employee('Mehmet', 'Yilmaz', 50000) ← __repr__
print(emp1)         # Mehmet Yilmaz — Salary: 50000 €   ← print() uses __str__

# RULE: Always define __repr__. Add __str__ when you want a nicer user message.


# ── 4. __add__ — Arithmetic Operators ───────────────────────
# When Python sees  a + b  it calls  a.__add__(b)
# You can define what "+" means for YOUR class.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __add__(self, other):
        # "Adding" two employees = combining their salaries
        return self.pay + other.pay

emp1 = Employee("Mehmet", "Yilmaz", 50000)
emp2 = Employee("Anna",   "Schmidt", 60000)

print(emp1 + emp2)   # 110000  ← Python called emp1.__add__(emp2)

# This is exactly how Python's built-in types work:
print(1 + 2)          # int.__add__(1, 2)    → 3
print("hi " + "bye")  # str.__add__(...)     → "hi bye"


# ── 5. __len__ — The len() Function ─────────────────────────
# When Python sees  len(x)  it calls  x.__len__()

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __len__(self):
        # Define "length" as the number of characters in the full name
        return len(self.first) + len(self.last)

emp1 = Employee("Mehmet", "Yilmaz", 50000)
print(len(emp1))   # 12  (6 + 6)


# ── 6. FULL CLASS — All Methods Together ────────────────────

class Employee:
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    # --- Dunder methods ---
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.first} {self.last} — Salary: {self.pay} €"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.first) + len(self.last)

    # --- Regular methods ---
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("Mehmet", "Yilmaz",  50000)
emp2 = Employee("Anna",   "Schmidt", 60000)

print(emp1)           # Mehmet Yilmaz — Salary: 50000 €
print(repr(emp1))     # Employee('Mehmet', 'Yilmaz', 50000)
print(emp1 + emp2)    # 110000
print(len(emp1))      # 12


# ── 7. QUICK REFERENCE — Common Dunder Methods ──────────────
#
#  __init__      →  called on  MyClass()
#  __repr__      →  called on  repr(obj)  /  fallback for print()
#  __str__       →  called on  str(obj)   /  print(obj)
#  __add__       →  called on  obj + other
#  __sub__       →  called on  obj - other
#  __mul__       →  called on  obj * other
#  __len__       →  called on  len(obj)
#  __eq__        →  called on  obj == other
#  __lt__        →  called on  obj < other
#  __gt__        →  called on  obj > other
#  __contains__  →  called on  x in obj
#  __getitem__   →  called on  obj[key]