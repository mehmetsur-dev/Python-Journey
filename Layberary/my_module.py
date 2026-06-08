# find index function

def find_index(to_search, target):
    '''find the index of a value in a sequance'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1
#============================================
# greeting function

def greet(name):
    return f"Hello, {name} Welcome back!"