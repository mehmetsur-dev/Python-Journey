# ============================================================
# OOP - Property Decorators: Challenge 3
# Topic   : @property, setter, validation, isinstance(),
#           any(), max(), min(), raise, __repr__
# Day     : 27
# ============================================================


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    @property
    def grades(self):
        return self._grades
    
    @grades.setter
    def grades(self, value):
        if not isinstance(value, list):
            raise ValueError("Grades must be a list")
        elif any(g < 0 or g > 100 for g in value):
            raise ValueError("All grades must be between 0 and 100")
        self._grades = value

    @property
    def gpa(self):
        return round(sum(self.grades) / len(self._grades), 2)
    
    @property
    def highest(self):
        return max(self.grades)

    @property
    def lowest(self):
        return min(self.grades)
    
    def __repr__(self):
        return f"Student(name='{self.name}', gpa={self.gpa})"
    
s = Student('Mehmet', [90, 85, 92, 78, 88])
print(s.gpa)        # 86.6
print(s.highest)    # 92
print(s.lowest)     # 78
print(s)            # Student(name='Mehmet', gpa=86.6)

s.grades = [100, 95, 98]
print(s.gpa)        # 97.67

try:
    s.grades = "not a list"
except ValueError as e:
    print(e)        # Grades must be a list

try:
    s.grades = [50, 110, 80]
except ValueError as e:
    print(e)        # All grades must be between 0 and 100