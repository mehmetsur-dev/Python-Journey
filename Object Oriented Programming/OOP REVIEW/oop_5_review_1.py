# OOP Review - Topic 5: Dunder/Magic Methods
# __str__, __len__, __add__ | Cart class challenge
# Day 51

class Cart:
    def __init__(self, owner, items=None):
        self.owner = owner

        if items is None:
            self.items = []
        else:
            self.items = items

    def add_item(self, item, price):
        self.items.append((item, price))

    def __str__(self):
        return f"Cart(owner={self.owner}, items={len(self.items)})"
    
    def __len__(self):
        return len(self.items)
    
    def __add__(self, other):
        return Cart(self.owner, self.items + other.items)
    
cart1 = Cart('Alex')
cart2 = Cart('Sera')

cart1.add_item("1kg Meat", 20)
cart2.add_item("Wood Plank", 8)

print(cart1)
print(len(cart1))

merged = cart1 + cart2
print(merged)