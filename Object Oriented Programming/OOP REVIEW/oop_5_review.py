# OOP Review Topic 5 — Dunder/Magic Methods
# Dunder = Double underscore. Methods __init__, __str__, __repr__, __len__, __add__ etc.
# Python calls them automatically in certain situations.

# The key ones:
# __init__ When you create an object
# __str__ When you print(obj) or str(obj)
# __repr__ When you inspect obj in the console / repr(obj)
# __len__ When you call len(obj)
# __add__ When you use obj1 + obj2
# __eq__ When you use obj1 == obj2

# Quick example:
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    def __len__(self):
        return self.pages

b = Book("Clean Code", 431)
print(b)       # 'Clean Code' (431 pages)
print(len(b))  # 431
# Without __str__, print(b) would give something like <__main__.Book object at 0x...>.