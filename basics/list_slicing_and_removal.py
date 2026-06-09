# slicing - removal

squad = ["Muhammed", "Ahmed", "Ali", "Haydar"]

print(f"The leader is: {squad[0]}")

squad. append("Yahya")

squad. remove("Ahmed")

# [1:] means "Start at index 1 and go all the way to the end" skip 0
for name in squad[1:]:
    print(name)
