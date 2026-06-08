# ============================================================
# OOP - Property Decorators: Challenge 1
# Topic   : @property, setter, validation
# Day     : 27
# ============================================================


class Ractangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

r = Ractangle(4, 5)
print(r.area)
print(r.perimeter)

r.width = 10
print(r.area)         

r.width = -3       # raises ValueError: Width must be positive