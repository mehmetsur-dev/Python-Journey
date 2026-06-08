# Day 29 - OOP Review Drill
# Car + ElectricCar + Garage
# Topics: classes, inheritance, properties, validation, dunder methods,
#         classmethods, staticmethods, list comprehension
# Completed: 01.06.2026


class Car:
    total_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        Car.total_cars += 1

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if value < 0 or value > 200:
            raise ValueError("Must be bettwen 0-200")
        self._speed = value

    def accelerate(self, amount):
        self.speed = min(self.speed + amount, 200)

    def brake(self, amount):
        self.speed = max(self.speed - amount, 0)
    
    def __repr__(self):
        return f"{self.make}, {self.model}, {self.year}"
    
    def __str__(self):
        return f"Brand= {self.make} - Model= {self.model} - Year= {self.year}"
    
    def __eq__(self, value):
        return self.make == value.make and self.model == value.model and self.year == value.year


    @classmethod
    def get_total(cls):
        return cls.total_cars
    

    @staticmethod
    def is_vintage(year):
        return year <= 2026 - 25


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def __str__(self):
        return f"Brand= {self.make}, Model= {self.model}, Year= {self.year}, Battery Size= {self.battery_size}kWh"

    
    @classmethod
    def from_string(cls, emp_string):
        make, model, year, battery_size = emp_string.split(",")
        return cls(make, model, int(year), int(battery_size))
    

class Garage:
    def __init__(self, cars=None):
        self.cars = cars if cars is not None else []

    def add_car(self, car):
        return self.cars.append(car)
    
    def remove_car(self, car):
        return self.cars.remove(car)
    
    def __len__(self):
        return len(self.cars)
    
    def __repr__(self):
        return f"Car List= {self.cars}"
    
    def find_vintage(self):
        return [car for car in self.cars if Car.is_vintage(car.year)]
    
#--------------------
#       Test
#--------------------

if __name__ == "__main__":

    car1 = Car("Toyota", "F-150", 2020)
    car2 = Car("BMW", "X7", 2023)
    car3 = Car("Toyota", "Crown", 1982)
    ec1 = ElectricCar.from_string("Tesla,Model3,2022,100")
    my_garage = Garage([car1, car2, car3, ec1])

    print(Car.total_cars)
    ec1.accelerate(190)
    print(ec1.speed)
    print(len(my_garage))
    vintage = my_garage.find_vintage()
    print(vintage)