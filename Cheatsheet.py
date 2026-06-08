# ============================================================
# cheatsheet.py
# Mehmet Sur — Python Learning Journey
# Update this file manually whenever you learn something new
# ============================================================


# ============================================================
# STRINGS
# ============================================================

name = "mehmet"
print(name.upper())           # MEHMET
print(name.capitalize())      # Mehmet
print(name[0:3])              # meh  (slicing)
print(len(name))              # 6
print(f"Hello {name}")        # f-string
print("Hello " + name)        # concatenation


# ============================================================
# MATH OPERATORS
# ============================================================

print(10 + 3)    # 13  addition
print(10 - 3)    # 7   subtraction
print(10 * 3)    # 30  multiplication
print(10 / 3)    # 3.3 division
print(10 // 3)   # 3   floor division
print(10 % 3)    # 1   modulus (remainder)
print(10 ** 3)   # 1000 exponent


# ============================================================
# LISTS
# ============================================================

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")        # add to end
fruits.remove("banana")       # remove by value
fruits.pop()                  # remove last item
print(fruits[0])              # apple  (indexing)
print(fruits[-1])             # last item
print(fruits[0:2])            # slice


# ============================================================
# TUPLES
# ============================================================

coords = (10, 20)             # immutable
x, y = coords                 # unpacking
print(x, y)                   # 10 20


# ============================================================
# SETS
# ============================================================

my_set = {1, 2, 3, 3}        # duplicates removed automatically
my_set.add(4)
my_set.discard(1)
print(2 in my_set)            # True


# ============================================================
# DICTIONARIES
# ============================================================

person = {"name": "Mehmet", "age": 27}
print(person["name"])         # Mehmet
person["city"] = "Kirkuk"     # add new key
person.get("job", "unknown")  # safe get with default

for key, value in person.items():
    print(key, value)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)


# ============================================================
# CONDITIONALS & BOOLEANS
# ============================================================

x = 10
if x > 5:
    print("big")
elif x == 5:
    print("equal")
else:
    print("small")

print(True and False)   # False
print(True or False)    # True
print(not True)         # False


# ============================================================
# FOR LOOPS
# ============================================================

for i in range(5):
    print(i)                  # 0 1 2 3 4

for fruit in fruits:
    print(fruit)

# list comprehension
evens = [x for x in range(10) if x % 2 == 0]
squares = [x**2 for x in range(5)]


# ============================================================
# WHILE LOOPS
# ============================================================

count = 0
while count < 5:
    print(count)
    count += 1

# break and continue
for i in range(10):
    if i == 3:
        continue              # skip 3
    if i == 7:
        break                 # stop at 7
    print(i)


# ============================================================
# FUNCTIONS
# ============================================================

def greet(name, greeting="Hello"):       # default parameter
    return f"{greeting}, {name}!"

print(greet("Mehmet"))                   # Hello, Mehmet!
print(greet("Mehmet", greeting="Merhaba"))  # keyword argument

def add(a, b):
    return a + b


# ============================================================
# IMPORTS
# ============================================================

import math
print(math.sqrt(16))          # 4.0
print(math.pi)                # 3.14159...

from math import sqrt, pi     # from...import
print(sqrt(25))

import random as rnd           # alias
print(rnd.randint(1, 10))

import math as m               # alias
print(m.floor(3.9))           # 3

# own module (if you have mymodule.py)
# import mymodule
# from mymodule import my_function


# ============================================================
# OOP — CLASSES & __init__
# ============================================================

class Employee:
    def __init__(self, name, pay):
        self.name = name       # instance variable
        self.pay = pay

    def greet(self):
        return f"Hi, I am {self.name}"

emp1 = Employee("Mehmet", 5000)
print(emp1.greet())
print(emp1.name)


# ============================================================
# OOP — CLASS VARIABLES
# ============================================================

class Employee:
    raise_amount = 1.04        # class variable — shared by all
    num_of_emps = 0

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        Employee.num_of_emps += 1    # increment on every new instance

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee("Mehmet", 5000)
emp2 = Employee("Ali", 4000)

print(Employee.num_of_emps)   # 2
Employee.raise_amount = 1.05  # changes for all instances
emp1.raise_amount = 1.10      # override only for emp1

print(emp1.__dict__)          # instance namespace
print(Employee.__dict__)      # class namespace


# ============================================================
# OOP — @classmethod & @staticmethod
# ============================================================

class Employee:
    raise_amount = 1.04

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @classmethod
    def set_raise_amount(cls, amount):    # cls = the class itself
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):        # alternative constructor
        name, pay = emp_str.split('-')
        return cls(name, int(pay))

    @staticmethod
    def is_workday(day):                  # no cls or self — pure utility
        return day.weekday() < 5

Employee.set_raise_amount(1.06)
emp1 = Employee.from_string("Mehmet-5000")


# ============================================================
# OOP — INHERITANCE
# ============================================================

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):                        # Dog inherits Animal
    def __init__(self, name, breed):
        super().__init__(name)            # call parent __init__
        self.breed = breed

    def speak(self):                      # method override
        return "Woof!"

dog = Dog("Rex", "Labrador")
print(isinstance(dog, Dog))              # True
print(isinstance(dog, Animal))           # True
print(issubclass(Dog, Animal))           # True

# None -> [] mutable default pattern
class Team:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members if members is not None else []


# ============================================================
# OOP — DUNDER / MAGIC METHODS
# ============================================================

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):                   # for developers, always define this
        return f"Book('{self.title}', {self.pages})"

    def __str__(self):                    # for users / print()
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):                    # len(book)
        return self.pages

    def __eq__(self, other):             # book1 == book2
        return self.title == other.title

    def __lt__(self, other):             # book1 < book2
        return self.pages < other.pages

    def __add__(self, other):            # book1 + book2
        return self.pages + other.pages

b1 = Book("Dune", 412)
b2 = Book("Hobbit", 310)
print(b1)                                # calls __str__
print(repr(b1))                          # calls __repr__
print(len(b1))                           # calls __len__
print(b1 == b2)                          # calls __eq__
print(b1 < b2)                           # calls __lt__
print(b1 + b2)                           # calls __add__


# ============================================================
# OOP — @property DECORATORS
# ============================================================

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):                  # getter — access like attribute
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, value):           # setter — runs on assignment
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Must be a non-empty string")
        first, last = value.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):                  # deleter — runs on del
        print("Deleting fullname...")
        self.first = None
        self.last = None

    # _private naming convention
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value

p = Person("Mehmet", "Sur")
print(p.fullname)                        # Mehmet Sur  (no parentheses!)
p.fullname = "Ali Veli"                  # triggers setter
del p.fullname                           # triggers deleter


# ============================================================
# ADD NEW THINGS BELOW AS YOU LEARN THEM
# ============================================================