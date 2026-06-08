# =============================================================================
# OOP TUTORIAL 4 - INHERITANCE: CREATING SUBCLASSES
# Challenge 1: Vehicle / Car / ElectricCar
# Day 25 | Topics: class Sub(Parent), super().__init__(), class variable override
# =============================================================================


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f'{self.year} {self.make} {self.model}')

    
class Car(Vehicle):
    fuel_type = "Gasoline"

    def __init__(self, make, model, year, num_doors=4):
        super().__init__(make, model, year)
        self.num_doors = num_doors

class ElectricCar(Vehicle):
    fuel_type = "Electric"

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

car1 = Car("Toyota", "GXR", 2025, 4)
car2 = ElectricCar("Tesla", "Model 3", 2023)

car1.description()
print(Car.fuel_type)
print(ElectricCar.fuel_type)
print(car1.num_doors)