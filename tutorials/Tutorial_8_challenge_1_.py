# Tutorial 8 - challenges
# Mehmet - Day 18


# Challenge 1
def greet_user(name):
    print(f"Welcome, {name}")

greet_user(name="Mehmet")
print('---------------------------------------------')

# Challenge 2 
def square(a):
    return a * a 

result = square(5)
print(result)
print('---------------------------------------------')

# Challenge 3 
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(7))  
print(even_or_odd(10))
print('---------------------------------------------')

# Challenge 4
def total(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(total([1, 2, 3, 4, 5]))
print('---------------------------------------------')


# Challenge 5
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
scores = [95, 82, 67, 55, 73]

for score in scores:
    print(f"Score {score} is {get_grade(score)}")
