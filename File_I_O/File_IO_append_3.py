# Challenge 3 - Smart Append (No Duplicates)
# Day 32 - File I/O Append Mode


# with open("names.txt", "w") as f:
#     f.write("Ali\n")
#     f.write("Ayse\n")
#     f.write("Mehmet\n")

with open("names.txt", "r") as rf:
    content = rf.read()

if "Lana" in content:
    print("Name already exists!")
else:
    with open("names.txt", "a") as af:
        af.write("Lana\n")