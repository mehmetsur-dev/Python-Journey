# Day 48 — OOP Review Topic 2: Class Variables vs Instance Variables


# The core idea:
# pythonclass Dog:
#     species = "Canis familiaris"  # class variable — shared by ALL instances

#     def __init__(self, name):
#         self.name = name          # instance variable — unique to each instance

# species lives on the class — every dog shares it
# name lives on the instance — each dog has its own


# The tricky part — what happens when you reassign:
# pythond1 = Dog("Rex")
# d2 = Dog("Max")

# Dog.species = "Wolf"   # changes for ALL instances
# d1.species = "Wolf"    # creates a new instance variable on d1 ONLY — doesn't touch the class
# That second one is where most people get confused.