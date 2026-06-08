# ============================================================
# OOP Class Variables — Challenge 2
# Topic: Class variables, instance variables, methods
# Day 23 — Corey Schafer OOP Tutorial 2
# Author: Mehmet Sur
# Date: 26.05.2026
# ============================================================


class Car:
    manufacturer = "AutoCorp"
    total_cars = 0
    depreciation_rate = 0.90
    

    def __init__(self, model, price):
        self.model = model
        self.price = price
        Car.total_cars +=1


    def show_info(self):
        print(f"Model: {self.model} - Price: {self.price} - Manufacturer: {self.manufacturer}")
 
    def apply_depreciation(self):
        self.price = int(self.price * self.depreciation_rate)

    def update_manufacturer(self, new_name):
        Car.manufacturer = new_name

        

car1 = Car("Tesla", 45000)
car2 = Car("BMW", 60000)
car3 = Car("Rolls Royes", 230000)

print(Car.total_cars)

car1.show_info()
car2.show_info()
car3.show_info()

print(car1.price)
car1.apply_depreciation()
print(car1.price)

car1.update_manufacturer("EloCorp")

print(car1.manufacturer)
print(car2.manufacturer)
print(car3.manufacturer)