# OOP Review Topic 3: @classmethod and @staticmethod
# @classmethod
# A classmethod receives the class itself as the first argument, by convention named cls instead of self.
# pythonclass Dog:
#     species = "Canis familiaris"

#     @classmethod
#     def get_species(cls):
#         return cls.species

# You call it on the class: Dog.get_species()
# Common use case: alternative constructors — creating instances from different input formats

# pythonclass Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, dog_string):
#         name, age = dog_string.split("-")
#         return cls(name, int(age))

# rex = Dog.from_string("Rex-5")

# @staticmethod
# A staticmethod receives neither self nor cls. It's just a regular function that lives inside the class for organizational reasons.
# pythonclass Dog:
#     @staticmethod
#     def is_adult(age):
#         return age >= 2

# You call it on the class: Dog.is_adult(3)
# No access to instance or class data
# Use it when the logic belongs to the class conceptually but doesn't need class or instance state


# Key distinction
# First argHas access toRegular methodselfinstance + class@classmethodclsclass only@staticmethodnothingneither