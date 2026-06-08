# Challenge 2 - File I/O: Read & Search
# Read a file, take user input, check if name exists in file


with open('employees.txt', 'r') as rf:
    content = rf.read()

    name = input("Enter a name: ")

    if name in content:
        print("Found")
    else:
        print("Not Found")