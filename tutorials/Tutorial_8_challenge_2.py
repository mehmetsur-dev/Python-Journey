# Tutorial 8 - challenges
# Mehmet - Day 19



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'Mehmet', 'age': 21}

student_info(*courses, **info)


print('---------------------------------------------')

def square(n):
    return n * n

def apply(func, value):    
    return func(value)

print(apply(square, 5))    

print('---------------------------------------------')

def circle_area(radius):
    return 3.14159 * radius ** 2

result = circle_area(5)
print(result)

print('---------------------------------------------')

def double(n):
    return n * 2     

def apply_twice(func, value):
    first = func(value)
    second = func(first)
    return second

result = apply_twice(double, 3)
print(result)         