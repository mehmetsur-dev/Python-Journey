# @property — The Core Idea
# Without @property, if you want to protect an attribute, you might use a getter/setter method. Property decorators let you do that while still accessing it like a normal attribute.

# The Three Decorators
# pythonclass Circle:
#     def __init__(self, radius):
#         self._radius = radius  # single underscore = "private by convention"

#     @property
#     def radius(self):          # GETTER — accessed like circle.radius
#         return self._radius

#     @radius.setter
#     def radius(self, value):   # SETTER — triggered by circle.radius = 5
#         if value < 0:
#             raise ValueError("Radius can't be negative")
#         self._radius = value

#     @radius.deleter
#     def radius(self):          # DELETER — triggered by del circle.radius
#         del self._radius
# Usage:
# pythonc = Circle(5)
# print(c.radius)   # 5 — calls getter
# c.radius = 10     # calls setter
# del c.radius      # calls deleter
# No parentheses. It looks like a plain attribute from the outside.

# Why bother?

# Add validation without breaking existing code
# Create read-only attributes (define getter only, no setter)
# Compute values on the fly instead of storing them