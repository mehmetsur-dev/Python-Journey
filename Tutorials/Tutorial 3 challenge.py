# challenge 1

user = "1049002"

# correctly converts the string to an integer.
user = int(user)

# correctly calculates how many full $20 bills fit into that giant number.
print(user // 20)

# correctly finds the leftover amount (the "modulus").
print(user % 20)

# checks if the total starting amount was zero.
leftover = user % 20
print(leftover == 0)