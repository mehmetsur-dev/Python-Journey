# =============================================================================
# OOP TUTORIAL 4 - INHERITANCE: CREATING SUBCLASSES
# Challenge 2: Animal / Dog / Cat
# Day 25 | Topics: method override, isinstance(), object lists
# =============================================================================


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Hiss")


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):        
        print("Woof!")


class Cat(Animal):
    def __init__(self, name, species, indoor):
        super().__init__(name, species)
        self.indoor = indoor

    def make_sound(self):        
        print("Meow!")


dog1 = Dog("Rex", "Canine", "Labrador")
cat1 = Cat("Mimi", "Feline", True)
cat2 = Cat("Luna", "Feline", False)
dog2 = Dog("Buddy", "Canine", "Poodle")


animal_list = [dog1, cat1, cat2, dog2]

for animal in animal_list:
    if isinstance(animal, Dog):
        animal.make_sound()
        print(f"Breed: {animal.breed}")

    elif isinstance(animal, Cat):
        animal.make_sound()
        print(f"Indoor: {animal.indoor}")