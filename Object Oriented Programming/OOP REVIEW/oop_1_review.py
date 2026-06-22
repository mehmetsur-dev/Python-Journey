# 1. Class vs Instance — closer analogy:
# A class is a blueprint. An instance is the actual object built from that blueprint.
# pythonclass Car:          # blueprint — defines what a Car looks like
#     ...

# car1 = Car(...)     # instance — one real Car built from that blueprint
# car2 = Car(...)     # another real Car — separate object, same blueprint
# car1 and car2 are both Cars, but they have their own data. The blueprint doesn't hold data — the instances do.

# 2. self is not just an argument — it's the instance itself.
# When you write car1 = Car("BMW", 200), Python secretly does this:
# pythonCar.__init__(car1, "BMW", 200)
# So self inside __init__ literally is car1 — that specific object being created. It's how the object refers to itself.

# 3. self.brand vs brand:
# pythondef __init__(self, brand):
#     self.brand = brand   # stores "BMW" ON the object — survives after __init__ ends
#     brand                # just a local variable — disappears after __init__ ends
# self.brand becomes a permanent attribute of the instance. Plain brand is just a temporary parameter.