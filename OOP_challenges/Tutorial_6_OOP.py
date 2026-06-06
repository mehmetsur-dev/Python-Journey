# ============================================================
# OOP - Property Decorators: Getters, Setters, and Deleters
# Corey Schafer Tutorial - Day 27 Reference
# ============================================================


# ------------------------------------------------------------
# STEP 1: THE PROBLEM (without @property)
# ------------------------------------------------------------
# If email is set in __init__, it never updates when first/last changes.

class Employee_NoProp:
    def __init__(self, first, last):
        self.first = first
        self.last  = last
        self.email = first + '.' + last + '@company.com'  # set once, never updates

emp = Employee_NoProp('John', 'Smith')
print(emp.email)   # john.smith@company.com  ✓

emp.first = 'Jim'
print(emp.email)   # john.smith@company.com  ✗  BUG: still old email!


# ------------------------------------------------------------
# STEP 2: @property  (GETTER)
# ------------------------------------------------------------
# @property turns a method into an attribute.
# Now email is computed fresh every time you access it.

class Employee_Getter:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    @property
    def email(self):              # getter - called when you READ emp.email
        return f'{self.first}.{self.last}@company.com'

emp = Employee_Getter('John', 'Smith')
print(emp.email)   # john.smith@company.com  ✓

emp.first = 'Jim'
print(emp.email)   # jim.smith@company.com   ✓  auto-updated!

# Note: you access it like an attribute, NOT like a method:
#   emp.email    ← correct
#   emp.email()  ← wrong, will raise TypeError


# ------------------------------------------------------------
# STEP 3: SECOND @property (fullname getter)
# ------------------------------------------------------------
# You can have as many @property methods as you want.

class Employee_TwoGetters:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):           # second getter
        return f'{self.first} {self.last}'

emp = Employee_TwoGetters('John', 'Smith')
print(emp.fullname)  # John Smith
print(emp.email)     # john.smith@company.com

emp.first = 'Jim'
print(emp.fullname)  # Jim Smith             ← auto-updated
print(emp.email)     # jim.smith@company.com ← auto-updated


# ------------------------------------------------------------
# STEP 4: @name.setter  (SETTER)
# ------------------------------------------------------------
# Without a setter, trying to SET a property raises AttributeError.
# The setter lets you control what happens when someone assigns a value.
# The setter method name MUST match the property name.

class Employee_Setter:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter              # decorator name = property name + .setter
    def fullname(self, name):     # method name must also match
        first, last = name.split(' ')
        self.first = first
        self.last  = last

emp = Employee_Setter('John', 'Smith')

# Without setter this line would raise: AttributeError: can't set attribute
emp.fullname = 'Jim Brown'        # calls the setter
print(emp.first)    # Jim
print(emp.last)     # Brown
print(emp.fullname) # Jim Brown


# ------------------------------------------------------------
# STEP 5: @name.deleter  (DELETER)
# ------------------------------------------------------------
# The deleter runs when you use del on the property.
# Lets you control cleanup logic instead of just deleting one attribute.
# The deleter method name MUST also match the property name.

class Employee_Deleter:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last  = last

    @fullname.deleter             # decorator name = property name + .deleter
    def fullname(self):           # no extra parameter, just self
        print('Deleting name!')
        self.first = None
        self.last  = None

emp = Employee_Deleter('John', 'Smith')
del emp.fullname                  # calls the deleter
print(emp.first)    # None
print(emp.last)     # None


# ------------------------------------------------------------
# STEP 6: COMPLETE CLASS - all three together
# (This is the final version from Corey's tutorial)
# ------------------------------------------------------------

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last  = last

    @fullname.deleter
    def fullname(self):
        print('Deleting name!')
        self.first = None
        self.last  = None


emp1 = Employee('John', 'Smith')

print(emp1.fullname)              # John Smith
print(emp1.email)                 # john.smith@company.com

emp1.fullname = 'Jim Brown'       # setter fires
print(emp1.fullname)              # Jim Brown
print(emp1.email)                 # jim.brown@company.com

del emp1.fullname                 # deleter fires -> prints 'Deleting name!'
print(emp1.first)                 # None
print(emp1.last)                  # None


# ------------------------------------------------------------
# QUICK RULES TO REMEMBER
# ------------------------------------------------------------
# 1. @property          → getter   → called when you READ  the attribute
# 2. @name.setter       → setter   → called when you SET   the attribute
# 3. @name.deleter      → deleter  → called when you DEL   the attribute
# 4. All three method names must match the property name exactly
# 5. Access like an attribute (emp.email), NOT like a method (emp.email())
# 6. Getter must exist before you can add a setter or deleter