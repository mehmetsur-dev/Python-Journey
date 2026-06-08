# Tutorial_2: Strings

greeting = "Hello"
name = "Ali"


# .format() this will make our script look clean, 
# {} this braket is used to add words inside it when we print
message = "{}, {}. Welcome!". format(name, greeting)
print(message)

# f STRING  this is another way to do it and its more clean
# we also have to use {} this bracket with f String
# f String shoul be always outside (f"") this we can add it inside () tho
message = f"{greeting}, {name}. Welcome!"
print(message)

