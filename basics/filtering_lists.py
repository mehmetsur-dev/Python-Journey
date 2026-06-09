# filtering - lists 

materials = ["Mulberry", "Silk", "Wood", "Water", "Iron"]
workshop_list = [] # We start with an empty list

for item in materials:
    if item.startswith("W"):
        workshop_list.append(item) # We only add it if it starts with W

print(workshop_list)
