# tutorial_09_imports.py
# Topic: Importing Modules
# Day 20 - Mehmet's Python Journey

# ============================================
# SECTION 1: Import a built-in module (math)
# ============================================
# use at least 3 things from math (sqrt, pi, floor or ceil)

import math

print(math.sin(83))
print(math.sqrt(25))
print(math.ceil(3.3))

# ============================================
# SECTION 2: from ... import
# ============================================
# - show the difference (no need to write math.something)

from math import cos

print(cos(60))

# ============================================
# SECTION 3: import as (alias/nickname)
# ============================================
# - give a module or function a short nickname
# - use it

from math import floor as f

print(f(3.88909))

# ============================================
# SECTION 4: import your OWN file
# ============================================
# - create a second file called my_module.py
# - write 2 simple functions in it (you choose what they do)
# - import and use them in this main script

# import my_module

# courses = ['History', 'Math', 'Art', 'Python']

# index = my_module.find_index(courses, 'Python')
# print(index)

# greet = my_module.greet('Mehmet')
# print(greet)

# ============================================
# SECTION 5: import random (fun one!)
# ============================================
# - generate a random number between 1 and 100
# - pick a random item from a list

import random

random_number = random.randint(1, 100)

print(f"The random number is: {random_number}")