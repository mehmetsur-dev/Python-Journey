# Challenge 1 - Append New Employees
# Day 32 - File I/O Append Mode

# Create base file
with open("employees.txt", "w") as f:
    f.write("Ali Veli - Python Developer\n")
    f.write("Mehmet Sur - Junior Developer\n")
    f.write("Ayse Kaya - Data Analyst\n")

# Append new employees
with open("employees.txt", "a") as af:
    af.write("Yahya Sur - Java Dev\n")
    af.write("Lana Clay - Python Dev\n")
    af.write("Cloude - Ai engine\n")

# Read and verify
with open("employees.txt", "r") as rf:
    print(rf.read())