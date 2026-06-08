# Tutorial 1 
# OOP
# 5/25/2026



# 1. The Class — the Blueprint
class employee:

# 3. __init__ — The Constructor
# This runs automatically the moment you create an instance.
# It's where you give the object its data.
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        self.email = name.lower().replace(" ", ".") + "@company.com"
        
    def introduce(self):
        print(f"Hi, I'm {self.name} and i earn {self.pay}$ per Year.")
        print(f"Contact me at {self.email}")


# 4. self — What Is It?
# self means "this specific instance". When you write self.name,
#  you're saying "this employee's name" — not all employees, just this one.
# When you call:

emp1 = employee("Mehmet Sur", 50000)
emp2 = employee("John Gate", 45000)

# 2. The Instance — the Real Thing
emp1.introduce()
emp2.introduce() 