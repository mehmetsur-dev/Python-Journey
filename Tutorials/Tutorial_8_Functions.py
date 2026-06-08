# 

def greet():
    print("Hello!")

greet()  # calling the function
greet()  # calling it again

print('---------------------------------------------')

# # 1. Parameters vs Arguments

def greet(name):              # 'name' is a PARAMETER (the placeholder)
    print(f"Hello, {name}")

greet("Mehmet")               # "Mehmet" is the ARGUMENT (the real value)

print('---------------------------------------------')

# # 2. Return Values

def add(a, b):
    return a + b             # sends the result BACK to whoever called it

result = add(3, 5)
print(result)                # 8

print('---------------------------------------------')

# # 3. Default Parameters

def greet(name, language="English"):
    if language == "German":
        print(f"Hallo, {name}")
    else:
        print(f"Hello, {name}")

greet("Mehmet")               # uses default → Hello, Mehmet!
greet("Mehmet", "German")     # → Hallo, Mehmet!

print('---------------------------------------------')

# # 4. Keyword Arguments

def user_info(name, age, city):
    print(f"{name}, {age}, from {city}")

user_info(age=21, city="kirkuk", name="Mehmet")  # order doesn't matter!

print('---------------------------------------------')

# # 5. Multiple Return Values

def min_max(numbers):
    return min(numbers), max(numbers)   # returns a TUPLE

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)                        # 1  9